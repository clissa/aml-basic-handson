""""Example of a more complex script from: https://github.com/clissa/github-user-dashboard
"""

import os

import altair as alt
import datapane as dp
import numpy as np
import pandas as pd
from dotenv import load_dotenv
from github import Github, UnknownObjectException

# get token
load_dotenv()
token = os.environ.get("GITHUB_API_TOKEN")
dp_token = os.environ.get("DATAPANE_TOKEN")

# get user profile data
username = 'clissa'
gh = Github(token)
user = gh.get_user(username)

# initialize empty dataframe for repos data
colnames = ['languages', 'topics', 'description', 'commits', 'collaborators', 'forks', 
            'stargazers', 'open_issues', 'visibility', 'license']
repos_df = pd.DataFrame(data={}, columns=colnames)
repos_df.index.name = 'repository'

# loop through repos to get infos
for repo in user.get_repos():
    try:
        license = repo.get_license().raw_data['license']['name']
    except UnknownObjectException:  # github.GithubException.UnknownObjectException:
        license = None
    repos_df.loc[repo.name] = [
        repo.get_languages(), repo.get_topics(), repo.description, repo.get_commits().totalCount,
        repo.get_collaborators().totalCount, repo.forks, repo.stargazers_count,
        repo.open_issues_count, 'Private' if repo.private else 'Public', license
        ]

# highlights tab
received_stars = repos_df.stargazers.sum()
PREV_FOLLOWS = 4

# languages tab
def get_languages_pct(repo_languages: dict) -> dict:
    total = sum(repo_languages.values())
    return {k: v / total for k, v in repo_languages.items()}


def get_languages_total(user_languages: pd.Series) -> dict:
    languages_dict = {}
    for repo_languages in user_languages:
        for k, v in repo_languages.items():
            languages_dict[k] = languages_dict.get(k, 0) + v
    return languages_dict


user_languages = get_languages_total(repos_df.languages)
user_languages_pct = get_languages_pct(user_languages)

source_bar = pd.DataFrame(
    {'language': user_languages.keys(), 'code lines': [np.log(x) for x in user_languages.values()]})
# source_bar.sort_values('code lines', ascending=False, inplace=True)
bar_chart = alt.Chart(source_bar).mark_bar().encode(
    x='code lines:Q',
    # x=alt.X(field='code lines:Q', scale=alt.Scale(domainMax=source_bar[source_bar.language=='Python']['code lines'].values[0])),
    y=alt.Y('language:O', sort='-x'),
    tooltip=['language', 'code lines'],
).interactive()

source_donut = pd.DataFrame({'language': user_languages_pct.keys(), 'pct': user_languages_pct.values()})
source_donut.sort_values('pct', ascending=False, inplace=True)
donut_chart = alt.Chart(source_donut).mark_arc(innerRadius=45).encode(
    theta=alt.Theta(field='pct', type='quantitative'),
    color=alt.Color(field='language', type='nominal'),
    tooltip=['language', 'pct'],
).interactive()

python_idx = np.where(source_donut.language == 'Python')[0][0]
python_code_lines = np.exp(source_bar[source_bar.language == 'Python']['code lines'].values[0])


# repos
def get_repo_insights(name: str, gh: Github = gh) -> (pd.DataFrame, pd.DataFrame):
    repo = gh.get_repo(name)

    repo_languages_pct = get_languages_pct(repo.get_languages())
    repo_languages_pct = pd.DataFrame({'language': repo_languages_pct.keys(), 'pct': repo_languages_pct.values()})

    # ctrbs = repo.get_contributors()
    # contributors = [user.login for i in range(ctrbs.totalCount) for user in ctrbs.get_page(i)]
    contributions_df = pd.DataFrame({}, columns=['author', 'total', 'week', 'commits'])
    for stats in repo.get_stats_contributors():
        for activity in stats.weeks:
            contributions_df.loc[contributions_df.shape[0]] = [stats.author.login, stats.total, activity.w, activity.c]
    return repo_languages_pct, contributions_df

# user-defined collaborative projects
#TODO: change from hard-coded to interactive (e.g. CLI args?)
repo_names = ['robomorelli/cell_counting_yellow', 'operationalintelligence/opint-framework']

# intitialize dictionary with plots for each collaborative project section
repo_sections = {}
time_periods = {
    'robomorelli/cell_counting_yellow': pd.to_datetime(['2020-11-01', '2021-12-31']).astype(int) / 10 ** 6,
    'operationalintelligence/opint-framework': pd.to_datetime(['2019-07-01', '2020-06-30']).astype(int) / 10 ** 6,
}

# populate each section with 3 plots
for name in repo_names:
    source_languages, source_contributors = get_repo_insights(name, gh)

    donut_repo_languages = alt.Chart(source_languages).mark_arc(innerRadius=45).encode(
        theta=alt.Theta(field='pct', type='quantitative'),
        color=alt.Color(field='language', type='nominal'),
        tooltip=['language', 'pct'],
    ).interactive()

    base = alt.Chart(source_contributors.groupby('author').first().reset_index()).encode(
        theta=alt.Theta("total:Q", stack=True),
        radius=alt.Radius("total", scale=alt.Scale(type="sqrt", zero=True, rangeMin=0)),
        color="author:N", tooltip=['total', 'author'],
    )
    donut_contributors = base.mark_arc(innerRadius=20, stroke="#fff")
    donut_contributors = donut_contributors + base.mark_text(radiusOffset=10).encode(text="total:Q")
    donut_contributors.interactive()

    commits_chart = alt.Chart(source_contributors).mark_line().encode(
        # x="week:T",
        x=alt.X('week:T', scale=alt.Scale(domain=list(time_periods[name]))),
        y="commits:Q",
        color="author:N", tooltip=['week', 'commits', 'total', 'author'],
    ).interactive()

    repo_sections[name] = [donut_repo_languages, commits_chart, donut_contributors]

# report
report = dp.Report(
    blocks=[
        dp.Page(
            blocks=[
                dp.Text("# User data"),
                dp.Text("This tab contains some highlights of the user's data and activity."),
                dp.Text(
                    f"""The GitHub account **{user.login}** has a total of *{user.public_repos + user.total_private_repos} repositories*, 
                    *{user.public_repos}* of which are *public*. In terms of engagement, the user received *{received_stars} stars* 
                    and currently has *{user.followers} followers*. Also, the account follows *{user.following} other people* 
                    and participates in *{user.get_orgs().totalCount} public organizations*."""),
                dp.Group(
                    dp.Group(
                        dp.Group(
                            dp.BigNumber(
                                heading='Name',
                                value=user.name
                            ),
                            dp.BigNumber(
                                heading='Login',
                                value=user.login,
                                # value=f"[{user.login}](https://github.com/{user.login})"
                                # value=f"<a href='https://github.com/{user.login}'>{user.login}</a>",
                            ),
                            # dp.Text(f"user login: **{user.login}**"),
                            columns=2
                        ),
                        dp.Text(f"![]({user.avatar_url})"),
                        columns=1,
                    ),
                    dp.Group(
                        blocks=[
                            dp.Text(f"**bio**: {user.bio}"),
                            # dp.Text(f"<span style='color:blue'>bio: {user.bio}</span>"),
                            dp.Text(f"**company**: {user.company}"),
                            dp.Text(f"**blog**: {user.blog}"),
                            dp.Divider(),
                            dp.Group(
                                dp.Group(
                                    blocks=[
                                        dp.Text('### Repos'),
                                        dp.BigNumber(
                                            heading="Public",
                                            value=user.public_repos
                                        ),
                                        dp.BigNumber(
                                            heading="Private",
                                            value=user.total_private_repos
                                        )
                                    ]
                                ),
                                dp.Group(
                                    blocks=[
                                        dp.Text('### Engagement'),
                                        dp.BigNumber(
                                            heading="Followers",
                                            value=user.followers,
                                            prev_value=PREV_FOLLOWS,
                                            change=f"{(user.followers - PREV_FOLLOWS) / PREV_FOLLOWS * 100:4.1f}%",
                                            is_upward_change=True,
                                            label='Last week'
                                        ),
                                        dp.BigNumber(
                                            heading="Stars",
                                            value=received_stars,
                                        )
                                    ],
                                ),
                                columns=2)
                        ],
                    ),
                    columns=2),
                dp.Divider(),
                # dp.Text(url=user.get_repo(user.login).get_contents("README.md").download_url),
            ],
            title="Highlights"
        ),
        dp.Page(
            blocks=[
                dp.Text("# Programming languages"),
                dp.Text(f"""Here is a summary of the languages involved in **{user.login}**'s repositories. On the left,
                        the (log) number of lines for each programming language. On the right, their percentages over
                        the total amount of code present in user's repositories."""),
                dp.Group(
                    blocks=[
                        dp.Plot(bar_chart),
                        dp.Plot(donut_chart),
                    ], columns=2, ),
                dp.Text("## Top 3"),
                dp.Text(
                    f"""The most present language is *{source_donut.iloc[0].language}*, followed by 
                    *{source_donut.iloc[1].language}* and *{source_donut.iloc[2].language}*. 
                    However, GitHub also tracks automatically generated code (not written by the user).
                    Python comes {python_idx}-th with {round(python_code_lines)} lines of code, 
                    followed by {source_donut.iloc[python_idx + 1].language}. 
                    """),
                dp.Group(
                    blocks=[
                        dp.BigNumber(
                            heading=source_donut.iloc[0].language,
                            value=f"{source_donut.iloc[0].pct:.2}%"
                        ),
                        dp.BigNumber(
                            heading=source_donut.iloc[1].language,
                            value=f"{source_donut.iloc[1].pct:.2}%"
                        ),
                        dp.BigNumber(
                            heading=source_donut.iloc[2].language,
                            value=f"{source_donut.iloc[2].pct:.2}%"
                        ),
                    ], columns=3,
                ),
            ],
            title="Languages"
        ),
        # dp.Page(
        #     dp.Text("Sample content"),
        #     title="Following/Followers"
        # ),
        # dp.Page(
        #     dp.Text("Sample content"),
        #     title="Starred"
        # ),
        # dp.Page(
        #     dp.Text("Sample content"),
        #     title="Organizations"
        # ),
        dp.Page(
            blocks=[
                dp.Text("# Collaborative contributions"),
                dp.Text("""The top section reports user specified contributions to collaborative projects 
                (see drop-down menu for options), with a donut chart for the programming languages adopted, 
                plus line and radial plots illustrating the contributions in terms of commits for each collaborator.
                """),
                dp.Select(
                    blocks=[dp.Group(blocks=repo_sections[name], columns=3, label=name) for name in repo_names],
                    type=dp.SelectType.DROPDOWN
                ),
                dp.Divider(),
                dp.Text("# Most starred"),
                dp.Text("""Dataframe of most starred user's repositories."""),
                dp.DataTable(repos_df.sort_values('stargazers', ascending=False), caption="User repositories"),
            ],
            title="Repositories"
        ),
    ]
)
report.save(path='report.html',
            open=True)  # , formatting=dp.ReportFormatting(bg_color='#B1BEBA', accent_color='#297373'))

# upload report
dp.login(token=dp_token)
report.upload(name="GitHub user dashboard", #project='github_dashboard',
              description='Mock-up dashboard of GitHub profile data and activity.', publicly_visible=True)
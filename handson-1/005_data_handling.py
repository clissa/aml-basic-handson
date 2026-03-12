from pathlib import Path
outpath = Path().resolve() / "data" / "005"
outpath.mkdir(parents=True, exist_ok=True)

# Writing to a file
file = open(outpath / "attendance.txt", "w")
file.write("Name,Surname,Date,Status\n")
file.write("Alice,Smith,2024-03-10,Present\n")
file.write("Bob,Johnson,2024-03-10,Absent\n")
file.close()

# Reading from the file
file = open(outpath / "attendance.txt", "r")
content = file.read()
file.close()

print(content)

### same but with context manager
# Writing using "with" (automatically closes file)
with open(outpath / "attendance.txt", "w") as file:
    file.write("Name,Surname,Date,Status\n")
    file.write("Alice,Smith,2024-03-10,Present\n")
    file.write("Bob,Johnson,2024-03-10,Absent\n")

# Reading using "with"
with open(outpath / "attendance.txt", "r") as file:
    content = file.read()

print(content)

### same with pandas
import pandas as pd

# Creating a DataFrame
data = {
    "Name": ["Alice", "Bob"],
    "Surname": ["Smith", "Johnson"],
    "Date": ["2024-03-10", "2024-03-10"],
    "Status": ["Present", "Absent"]
}

df = pd.DataFrame(data)
df.head()

# Writing to CSV
df.to_csv(outpath / "attendance.csv", index=False)

# Reading the file back
df_read = pd.read_csv(outpath / "attendance.csv")
print(df_read)


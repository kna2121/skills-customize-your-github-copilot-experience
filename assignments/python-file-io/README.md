# 📘 Assignment: Python File I/O and Data Persistence

## 🎯 Objective

Learn how to read, write, and update files in Python so your programs can persist data between runs.

## 📝 Tasks

### 🛠️ Read data from files

#### Description
Load data from a JSON file and a CSV file, then display the contents and summary information.

#### Requirements
Completed program should:

- Open and read a JSON file using the `json` module
- Open and read a CSV file using the `csv` module
- Print the loaded records and the total number of entries
- Handle missing files with a clear message

### 🛠️ Write data to files

#### Description
Save a list of data records to both JSON and CSV files so they can be reused later.

#### Requirements
Completed program should:

- Write a Python list of dictionaries to a JSON file
- Write the same records to a CSV file with field headers
- Confirm that both files were saved successfully

### 🛠️ Update persisted data

#### Description
Read the saved file data, modify it, and write the updated contents back to disk.

#### Requirements
Completed program should:

- Load data from the saved JSON or CSV file
- Add or update a record in the dataset
- Save the updated dataset back to disk
- Preserve the file format and structure after saving

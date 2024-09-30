# COMP3613 Assignment 1
* Student Name: Teal Trim
* Student ID: 816024202
* Course: Software Engineering II (COMP3613)
* Assignment: COMP3613 Assignment 1
* Date: 30/09/2024


# Dependencies
* Python3/pip3
* Packages listed in requirements.txt

# Installing Dependencies
```bash
$ pip install -r requirements.txt
```

# Supported Commands:
* Initializing the Database
```bash
flask init
```
* Create Competition
```bash
flask competition create 'competition_id' 'competition_name'
```
* Import competition results from file
```bash
flask competition import 'file_name'
```
* View competitions list
```bash
flask competition list
```
* View competition results
```bash
flask competition results 'competition_id'
```
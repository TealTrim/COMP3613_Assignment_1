# Software Engineering II (COMP3613) Assignment 1
#### Student Information:
* Student Name: Teal Trim
* Student ID: 816024202
* Course Name: Software Engineering II
* Course Code: COMP 3613
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
flask competition result 'competition_id'
```

# General Notes
* Upon initialization the database will have 10 competitions, the first 5 of which will have results.

* The file results.txt contains results for the next 5 competitions, and the import command can easily be used to get these.

* The format for importing a file of results for a given competition is as follows:

Key: 'value: data_Type'

```bash
'result_ID: int', 'competition_ID: int', 'winner_Name: string', 'number_Of_Participants'
```

* Commands allow for the creation of competitions.

* Results for these competitions can be added and asociated with pre-exisiting competitions by importing them from a file.

* Commands allow for the listing of all competitions in the database and the viewing of results for any competition in the database.

* This project was developed using GitHub Codespaces as Repl and Gitpod gave time limit and sign-up issues respectively.
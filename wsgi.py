#-------------------------------------------
#Student Information:
#-------------------------------------------
#Student Name: Teal Trim
#Student ID: 816024202
#Course: Software Engineering II (COMP3613)
#Assignment: COMP3613 Assignment 1
#Date: 30/09/2024
#-------------------------------------------

import click
#import pytest, sys
from flask import Flask
from flask.cli import with_appcontext, AppGroup

from App.database import db, get_migrate
#from App.models import User
from App.models import Competition
from App.models import Result
from App.main import create_app
#from App.controllers import (create_user, get_all_users_json, get_all_users, initialize, get_all_competitions, create_competition, get_competition, create_result)
from App.controllers import (initialize, get_all_competitions, create_competition, get_competition, create_result)

# This commands file allow you to create convenient CLI commands for testing controllers

app = create_app()
migrate = get_migrate(app)

#This command creates and initializes the database
@app.cli.command("init", help="Creates and initializes the database")
def init():
    initialize()
    print('database intialized')

#'''
#User Commands
#'''

# Commands can be organized using groups

# create a group, it would be the first argument of the comand
# eg : flask user <command>
#user_cli = AppGroup('user', help='User object commands') 

# Then define the command and any parameters and annotate it with the group (@)
#@user_cli.command("create", help="Creates a user")
#@click.argument("username", default="rob")
#@click.argument("password", default="robpass")
#def create_user_command(username, password):
#    create_user(username, password)
#    print(f'{username} created!')

# this command will be : flask user create bob bobpass

#@user_cli.command("list", help="Lists users in the database")
#@click.argument("format", default="string")
#def list_user_command(format):
#    if format == 'string':
#        print(get_all_users())
#    else:
#        print(get_all_users_json())

#app.cli.add_command(user_cli) # add the group to the cli

#'''
#Test Commands
#'''

#test = AppGroup('test', help='Testing commands') 

#@test.command("user", help="Run User tests")
#@click.argument("type", default="all")
#def user_tests_command(type):
#    if type == "unit":
#        sys.exit(pytest.main(["-k", "UserUnitTests"]))
#    elif type == "int":
#        sys.exit(pytest.main(["-k", "UserIntegrationTests"]))
#    else:
#        sys.exit(pytest.main(["-k", "App"]))
#    
#app.cli.add_command(test)

#MY WORK:
competition_cli = AppGroup('competition', help='Competition object commands') 

@competition_cli.command("create", help="Creates a competition. [Usage: flask competition create <competition_id> <competition_name>]")
@click.argument("competition_id")
@click.argument("competition_name")
def create_competition_command(competition_id, competition_name):
    try:
        print("---")
        create_competition(competition_id, competition_name)
        print(f'A competition named: {competition_name}, with an ID of {competition_id} has been created and added to database.')
        print("---")
    except ValueError as e:
        print("---")
        print(f"Error: {e}")
        print("---")

@competition_cli.command("list", help="Lists competitions in the database. [Usage: flask competition list]")
def list_competition_command():
    print("---")
    print("Competition List:")
    print(get_all_competitions())
    print("---")

@competition_cli.command("result", help="Shows the results for a given competition in the database. [Usage: flask competition result <competition_id>]")
@click.argument("competition_id")
def display_results_command(competition_id):
    comp = Result.query.filter_by(competition_ID=competition_id).first()
    if not comp:
        print("---")
        print("No results found for that competition")
        print("---")
        return
    print("---")
    print(f'Results for {get_competition(competition_id).competitionName}:')
    print(comp)
    print("---")
   
@competition_cli.command("import", help="Imports results from a given text file into the database. [Usage: flask competition import <file_name>]")
@click.argument("file_name")
def read_results_command(file_name):
    print("---")
    with open(file_name, 'r') as file:
        for line in file:
            data = line.strip().split(',')
            if len(data) == 4:
                resultID = int(data[0])
                competition_ID = int(data[1])
                winnerName = data[2].strip()
                numberOfParticipants = int(data[3])
                create_result(resultID, competition_ID, winnerName, numberOfParticipants)
    print(f'Results imported from {file_name}.')
    print("---")
app.cli.add_command(competition_cli)

from App.models import Competition
from App.database import db

def create_competition(competitionID, competitionName):
    newcompetition = Competition(competitionID=competitionID, competitionName=competitionName)
    db.session.add(newcompetition)
    db.session.commit()
    return newcompetition

def get_competition(competitionID):
    return Competition.query.get(competitionID)

def get_all_competitions():
    return Competition.query.all()

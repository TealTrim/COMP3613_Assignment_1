from App.models import Result
from App.database import db

def create_result(resultID, competition_ID, winnerName, numberOfParticipants):
    newresult = Result(resultID=resultID, competition_ID=resultID, winnerName=resultID, numberOfParticipants=resultID)
    db.session.add(newresult)
    db.session.commit()
    return newresult

def get_resultID (self, resultID):
    return Result.query.get(resultID)
    
def get_competition_ID (self, competition_ID):
    return Result.query.get(competition_ID)
    
def get_winnerName (self, winnerName):
    return Result.query.get(winnerName)
    
def get_numberOfParticipants (self, numberOfParticipants):
    return Result.query.get(numberOfParticipants)

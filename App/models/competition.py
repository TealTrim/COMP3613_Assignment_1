from App.database import db

class Competition(db.Model):
    competitionID = db.Column(db.Integer, primary_key=True)
    competitionName = db.Column(db.String(120), nullable=False)

    def __init__(self, competitionID, competitionName):
        self.set_competitionID(competitionID)
        self.set_competitionName(competitionName)
    
    def set_competitionID (self, competitionID):
        self.competitionID = competitionID
    
    def set_competitionName (self, competitionName):
        self.competitionName = competitionName

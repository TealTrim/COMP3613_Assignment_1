from App.database import db

class Result(db.Model):
    resultID = db.Column(db.Integer, primary_key=True)
    competition_ID = db.Column(db.Integer, db.ForeignKey('competition.competitionID'), nullable=False)
    winnerName = db.Column(db.String(120), nullable=False)
    numberOfParticipants = db.Column(db.Integer)

    def __init__(self, resultID, competition_ID, winnerName, numberOfParticipants):
        self.set_resultID(resultID)
        self.set_competition_ID(competition_ID)
        self.set_winnerName(winnerName)
        self.set_numberOfParticipants(numberOfParticipants)
    
    def set_resultID (self, resultID):
        self.resultID = resultID
    
    def set_competition_ID (self, competition_ID):
        self.competitionName = competition_ID
    
    def set_winnerName (self, winnerName):
        self.competition_ID = winnerName
    
    def set_numberOfParticipants (self, numberOfParticipants):
        self.numberOfParticipants = numberOfParticipants

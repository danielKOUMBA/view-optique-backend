from app.extension import db
from datetime import datetime

class Cout(db.Model):
    tablename='cout'
     
    id=db.Column(db.Integer,primary_key=True)
    nom=db.Column(db.String)
    prix=db.Column(db.Integer,nullable=False)
    date=db.Column(db.Date,default=datetime.utcnow)
        
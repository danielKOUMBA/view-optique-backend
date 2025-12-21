from app.extension import db
from datetime import datetime

class Commande(db.Model):
    tablename='commande'

    id=db.Column(db.Integer,primary_key=True)
    nom=db.Column(db.String)
    numero=db.Column(db.String)
    produits=db.Column(db.String)
    status=db.Column(db.String)
    type=db.Column(db.String)
    date=db.Column(db.Date,default=datetime.utcnow)
    prix_avancer=db.Column(db.Integer)
    prix_total=db.Column(db.Integer)
    

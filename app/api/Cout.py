from flask import Flask,request,jsonify,Blueprint
from app.models import Cout
from app.extension import db 
from datetime import datetime
from flask_jwt_extended import jwt_required,get_jwt_identity

cout_bp=Blueprint('cout_bp',__name__)

@cout_bp.route('/cout',methods=['POST'])
@jwt_required()
def Couts():
    admin=get_jwt_identity()
    data=request.get_json()
    if admin=='admin suppreme':
        date_str=data.get('date')
        date_ob=datetime.strptime(date_str,'%Y-%m-%d').date()
        date_obj=date_ob.strftime('%Y-%m-%d')
        cout=Cout(nom=data.get('depense'),prix=data.get('somme'),date=date_obj)
        db.session.add(cout)
        db.session.commit()
        return jsonify(['Depenses enregistrer avec succes'])
    
    return jsonify({
            'erreur':"Vous n'etes pas eligible"
    })
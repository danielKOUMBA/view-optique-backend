from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy
from flask_jwt_extended import JWTManager
from flask_migrate import Migrate
from elasticsearch import Elasticsearch

db=SQLAlchemy()
migrate=Migrate()
jwt=JWTManager()
cors=CORS()
es=Elasticsearch('http://localhost:9200')
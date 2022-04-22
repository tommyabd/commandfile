from sqlite3 import dbapi2
from main import db
from sqlalchemy import Column,Integer,String

class Veri(db.Model):
    id = db.Column(db.Integer(), primary_key=True)
    deger = db.Column(db.String())
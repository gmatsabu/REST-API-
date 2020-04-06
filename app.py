from flask import Flask,request,jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
import os

# Init my app
app = Flask(__name__)
basedir = os.path.abspath(os.path.dirname(__file__))

#My DataBase
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir,'db.sqlite')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False 

# Initialise db
db = SQLAlchemy(app)

#Init ma
ma = Marshmallow(app)

#Computer Class

class Computer(db.Model):
    id = db.Column(db.Integer,primary_key=True)
    hard_drive_type = db.Column(db.String(100),unique=True)
    processor = db.Column(db.String(100))
    amount_of_ram = db.Column(db.Integer)
    maximum_ram = db.Column(db.Integer)
    hard_drive_space = db.Column(db.String(100))
    form_factor = db.Column(db.String(100))

    def __init__(self,hard_drive_type,processor,amount_of_ram,maximum_ram,hard_drive_space,form_factor):
       self.hard_drive_type = hard_drive_type
       self.processor = processor
       self.amount_of_ram = amount_of_ram
       self.maximum_ram = maximum_ram
       self.hard_drive_space = hard_drive_space
       self.form_factor = form_factor

# Computer Schema

class Computer(ma.Schema):
    class Meta:
        fields = ('id','hard_drive_type','processor','amount_of_ram','hard_drive_space','form_factor')

# Initiating Schema
computer_schema = ComputerSchema(strict=False)
computers_schema = ComputerSchema(many=True, strict=False)


#Create Computer

#Add a computer
@app.route('/computer',methods=['GET'])
def add_computer():
    hard_drive_type = request.jsonj['hard_drive_type']
    processor = request.jsonj['processor']
    amount_of_ram = request.jsonj['amount_of_ram']
    maximum_ram = request.jsonj['maximum_ram']
    hard_drive_space = request.jsonj[' hard_drive_space']
    form_factor  = request.jsonj['form_factor ']

    new_computer =  Computer(hard_drive_type,processor,amount_of_ram, maximum_ram,hard_drive_space,form_factor)

    db.session = Computer(new_computer)
    db.session.commit()

    return computer_schema.jsonify(new_computer)


#List of all computers
@app.route('/computer',methods=['GET'])
def get_computers():
    all_computers = Computer.query.all()
    result = computer_schema.dumb(all_computers)
    return jsonify(result.data)


#Edit a computer
@app.route('/computer',methods=['PUT'])
def update_computers():
   computer = Computer.query.get(id)
    result = computer_schema.dumb(all_computers)
    return jsonify(result.data)

computer.hard_drive_type =  hard_drive_type
computer.processor= processor
computer.amount_of_ram = amount_of_ram
computer.maximum_ram = maximum_ram
computer.hard_drive_space = hard_drive_space
computer.form_factor = form_factor

db.session.commit()

return computer.jsonify(product)

#Delete a computer
@app.route('/computer/<id>',methods=['DELETE'])
def delete_computer(id):
    computer = Computer.query.get(id)
    db.session.delete(computer)
    db.session.commit()

    return computer_schema.jsonify(product)


#Run My Server
if __name__ == '__main__':
    app.run(debug=True)
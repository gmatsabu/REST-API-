
from sqlalchemy import create_engine, Column, String, Integer
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker



engine = create_engine('postgresql+psycopg2://user:pass@localhost/computer')
engine.connect()

Session = sessionmaker(bind=engine)
session = Session() 


Base = declarative_base()


class Application(Base):

    __tablename__ = 'application'   
    
    id = Column(Integer, primary_key=True)
    hard_drive_type = Column(String)
    processor = Column(String)
    amount_of_ram = Column(Integer)
    maximum_ram = Column(Integer)
    hard_drive_space = Column(String)
    form_factor = Column(String)


    def __init__(self,hard_drive_type,processor, amount_of_ram,maximum_ram,hard_drive_space,form_factor):
        self.hard_drive_type = hard_drive_type
        self.processor = processor
        self.amount_of_ram = amount_of_ram
        self.maximum_ram = maximum_ram
        self.hard_drive_space = hard_drive_space
        self.form_factor =  form_factor

    def save_applications(self):
        session.add(self)
        session.commit()

app = Application("rmp","GHz",16,32,"GB","NONE")
app.save_applications()

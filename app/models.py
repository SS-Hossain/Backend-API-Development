# app/models.py
from sqlalchemy import Column, Integer, String, Date, JSON
from .database import Base

class WheelSpecification(Base):
    __tablename__ = "wheel_specifications"

    id = Column(Integer, primary_key=True, index=True)
    form_number = Column(String, unique=True, index=True)
    submitted_by = Column(String)
    submitted_date = Column(Date)
    fields = Column(JSON) # Using JSON type to store the nested fields object
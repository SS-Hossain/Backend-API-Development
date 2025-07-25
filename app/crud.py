# app/crud.py
from sqlalchemy.orm import Session
from . import models, schemas
from datetime import date
from typing import Optional

def create_wheel_specification(db: Session, spec: schemas.WheelSpecificationCreate):
    # Convert Pydantic model to a dictionary to store in the DB model
    db_spec = models.WheelSpecification(
        form_number=spec.formNumber,
        submitted_by=spec.submittedBy,
        submitted_date=spec.submittedDate,
        fields=spec.fields.dict() # Store the fields object as JSON
    )
    db.add(db_spec)
    db.commit()
    db.refresh(db_spec)
    return db_spec

def get_wheel_specifications(db: Session, form_number: Optional[str], submitted_by: Optional[str], submitted_date: Optional[date]):
    query = db.query(models.WheelSpecification)
    
    if form_number:
        query = query.filter(models.WheelSpecification.form_number == form_number)
    if submitted_by:
        query = query.filter(models.WheelSpecification.submitted_by == submitted_by)
    if submitted_date:
        query = query.filter(models.WheelSpecification.submitted_date == submitted_date)
        
    return query.all()
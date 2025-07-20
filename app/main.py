# app/main.py
from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List, Optional
from datetime import date

from . import crud, models, schemas
from .database import engine, get_db

# This line creates the database tables if they don't exist
models.Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="KPA-ERP Forms API",
    description="API for submitting and retrieving KPA forms.",
    version="1.0.0"
)

@app.post("/api/forms/wheel-specifications", status_code=201)
def create_wheel_spec_endpoint(spec: schemas.WheelSpecificationCreate, db: Session = Depends(get_db)):
    """
    Endpoint to submit a new wheel specification form.
    """
    db_spec = crud.create_wheel_specification(db=db, spec=spec)
    
    # Construct the response to exactly match the Postman collection
    return {
        "success": True,
        "message": "Wheel specification submitted successfully.",
        "data": {
            "formNumber": db_spec.form_number,
            "submittedBy": db_spec.submitted_by,
            "submittedDate": db_spec.submitted_date.isoformat(),
            "status": "Saved"
        }
    }

@app.get("/api/forms/wheel-specifications")
def read_wheel_specs_endpoint(
    formNumber: Optional[str] = None, 
    submittedBy: Optional[str] = None, 
    submittedDate: Optional[date] = None, 
    db: Session = Depends(get_db)
):
    """
    Endpoint to get wheel specification forms, with optional filters.
    """
    specs = crud.get_wheel_specifications(
        db, form_number=formNumber, submitted_by=submittedBy, submitted_date=submittedDate
    )
    
    # Format the data to match the Postman collection example
    formatted_data = []
    for spec in specs:
        # Pydantic's alias generator doesn't work well on nested dicts, so we map manually
        formatted_data.append({
            "formNumber": spec.form_number,
            "submittedBy": spec.submitted_by,
            "submittedDate": spec.submitted_date.isoformat(),
            "fields": spec.fields # The fields are already in a JSON-compatible dict
        })
        
    return {
        "success": True,
        "message": "Filtered wheel specification forms fetched successfully.",
        "data": formatted_data
    }

# Bonus: Add a root endpoint for easy testing
@app.get("/")
def read_root():
    return {"message": "Welcome to the KPA-ERP API!"}
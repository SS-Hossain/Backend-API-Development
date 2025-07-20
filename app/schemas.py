# app/schemas.py
from pydantic import BaseModel
from datetime import date
from typing import Dict, Any

# Pydantic model for the nested 'fields' object
class Fields(BaseModel):
    treadDiameterNew: str
    lastShopIssueSize: str
    condemningDia: str
    wheelGauge: str
    variationSameAxle: str
    variationSameBogie: str
    variationSameCoach: str
    wheelProfile: str
    intermediateWWP: str
    bearingSeatDiameter: str
    rollerBearingOuterDia: str
    rollerBearingBoreDia: str
    rollerBearingWidth: str
    axleBoxHousingBoreDia: str
    wheelDiscWidth: str

# Pydantic model for the main form submission (request body)
class WheelSpecificationCreate(BaseModel):
    formNumber: str
    submittedBy: str
    submittedDate: date
    fields: Fields

# Pydantic model for the data returned by the API (response body)
class WheelSpecificationResponse(BaseModel):
    id: int
    formNumber: str
    submittedBy: str
    submittedDate: date
    fields: Fields

    class Config:
        from_attributes = True # Allows mapping from SQLAlchemy model to this Pydantic model
        # This alias generator will convert snake_case (like form_number) to camelCase (formNumber)
        @classmethod
        def alias_generator(cls, string: str) -> str:
            return ''.join(word.capitalize() if i != 0 else word for i, word in enumerate(string.split('_')))
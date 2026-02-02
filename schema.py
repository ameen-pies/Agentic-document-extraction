from pydantic import BaseModel, field_validator
from typing import Optional


class image(BaseModel):
    invoice_number: Optional[str] = None
    invoice_date: Optional[str] = None
    vendor_name: Optional[str] = None
    total_amount: Optional[str] = None
    currency: Optional[str] = None
    
    @field_validator('total_amount', mode='before')
    @classmethod
    def convert_amount_to_string(cls, v):
        """Convert numeric amounts to strings"""
        if v is None:
            return None
        if isinstance(v, (int, float)):
            return str(v)
        return v


class InvoiceData(BaseModel):
    invoice_number: Optional[str] = None
    invoice_date: Optional[str] = None
    vendor_name: Optional[str] = None
    total_amount: Optional[str] = None
    currency: Optional[str] = None
    
    @field_validator('total_amount', mode='before')
    @classmethod
    def convert_amount_to_string(cls, v):
        """Convert numeric amounts to strings"""
        if v is None:
            return None
        if isinstance(v, (int, float)):
            return str(v)
        return v

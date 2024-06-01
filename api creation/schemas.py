from pydantic import BaseModel
from typing import Optional
from datetime import date, datetime

# User schemas
class UserBase(BaseModel):
    Username: str
    Email: str
    Role: str

class UserCreate(UserBase):
    Password: str

class User(UserBase):
    UserID: int
    CreatedAt: datetime
    UpdatedAt: datetime

class UserLogin(BaseModel):
    Email: str
    Password: str
    
    class Config:
        orm_mode = True

# Patient schemas
class PatientBase(BaseModel):
    UserID: int
    FirstName: str
    LastName: str
    DateOfBirth: date
    Gender: str
    ContactNumber: Optional[str] = None
    Address: Optional[str] = None

class PatientCreate(PatientBase):
    pass

class Patient(PatientBase):
    PatientID: int
    CreatedAt: datetime
    UpdatedAt: datetime

    class Config:
        orm_mode = True

# Appointment schemas
class AppointmentBase(BaseModel):
    PatientID: int
    DoctorID: int
    AppointmentDate: datetime
    Reason: Optional[str] = None
    Status: Optional[str] = None

class AppointmentCreate(AppointmentBase):
    pass

class Appointment(AppointmentBase):
    AppointmentID: int
    Status: str
    CreatedAt: datetime
    UpdatedAt: datetime

    class Config:
        orm_mode = True

from sqlalchemy import Column, Integer, String, Enum, ForeignKey, Date, DateTime, TIMESTAMP
from sqlalchemy.orm import relationship
from database import Base
import enum
from datetime import datetime

# Enum definitions for role, gender, and status
class RoleEnum(str, enum.Enum):
    Admin = "Admin"
    Doctor = "Doctor"
    Assistant = "Assistant"

class GenderEnum(str, enum.Enum):
    Male = "Male"
    Female = "Female"
    Other = "Other"

class StatusEnum(str, enum.Enum):
    Scheduled = "Scheduled"
    Completed = "Completed"
    Cancelled = "Cancelled"

# User model
class User(Base):
    __tablename__ = 'Users'
    UserID = Column(Integer, primary_key=True, index=True)
    Username = Column(String(50), unique=True, index=True, nullable=False)
    PasswordHash = Column(String(255), nullable=False)
    Email = Column(String(100), unique=True, index=True, nullable=False)
    Role = Column(Enum(RoleEnum), nullable=False)
    CreatedAt = Column(TIMESTAMP, default=datetime.now)
    UpdatedAt = Column(TIMESTAMP, default=datetime.now, onupdate=datetime.now)

# Patient model
class Patient(Base):
    __tablename__ = 'Patients'
    PatientID = Column(Integer, primary_key=True, index=True)
    UserID = Column(Integer, ForeignKey('Users.UserID'), nullable=False)
    FirstName = Column(String(50), nullable=False)
    LastName = Column(String(50), nullable=False)
    DateOfBirth = Column(Date, nullable=False)
    Gender = Column(Enum(GenderEnum), nullable=False)
    ContactNumber = Column(String(15))
    Address = Column(String(255))
    CreatedAt = Column(TIMESTAMP, default=datetime.now)
    UpdatedAt = Column(TIMESTAMP, default=datetime.now, onupdate=datetime.now)

    user = relationship("User")

# Appointment model
class Appointment(Base):
    __tablename__ = 'Appointments'
    AppointmentID = Column(Integer, primary_key=True, index=True)
    PatientID = Column(Integer, ForeignKey('Patients.PatientID'), nullable=False)
    DoctorID = Column(Integer, ForeignKey('Users.UserID'), nullable=False)
    AppointmentDate = Column(DateTime, nullable=False)
    Reason = Column(String(255))
    Status = Column(Enum(StatusEnum), default=StatusEnum.Scheduled)
    CreatedAt = Column(TIMESTAMP, default=datetime.now)
    UpdatedAt = Column(TIMESTAMP, default=datetime.now, onupdate=datetime.now)

    patient = relationship("Patient")
    doctor = relationship("User")

from datetime import date, datetime
from uuid import UUID

from pydantic import BaseModel, ConfigDict, Field


class StudentBase(BaseModel):
    name: str = Field(
        ...,
        min_length=1,
        max_length=150,
    )
    phone: str | None = None
    email: str | None = None
    course_id: UUID | None = None
    join_date: date | None = None
    status: str = Field(
        ...,
        min_length=1,
        max_length=50,
    )
    student_photo: str | None = None


class StudentCreate(StudentBase):
    pass


class StudentUpdate(BaseModel):
    name: str | None = Field(
        default=None,
        min_length=1,
        max_length=150,
    )
    phone: str | None = None
    email: str | None = None
    course_id: UUID | None = None
    join_date: date | None = None
    status: str | None = Field(
        default=None,
        min_length=1,
        max_length=50,
    )
    student_photo: str | None = None


class StudentResponse(StudentBase):
    id: UUID
    student_id: str
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)
from datetime import date, datetime
from uuid import UUID

from pydantic import BaseModel, ConfigDict, Field


class DemoBookingBase(BaseModel):
    name: str = Field(
        ...,
        min_length=1,
        max_length=150,
    )
    phone: str = Field(
        ...,
        min_length=1,
        max_length=30,
    )
    email: str | None = None
    course_id: UUID | None = None
    preferred_date: date | None = None
    preferred_time: str | None = None
    message: str | None = None
    status: str = Field(
        default="New",
        min_length=1,
        max_length=50,
    )
    admin_notes: str | None = None
    converted_student_id: UUID | None = None
    converted_at: datetime | None = None


class DemoBookingCreate(BaseModel):
    name: str = Field(
        ...,
        min_length=1,
        max_length=150,
    )
    phone: str = Field(
        ...,
        min_length=1,
        max_length=30,
    )
    email: str | None = None
    course_id: UUID | None = None
    preferred_date: date | None = None
    preferred_time: str | None = None
    message: str | None = None


class DemoBookingUpdate(BaseModel):
    name: str | None = Field(
        default=None,
        min_length=1,
        max_length=150,
    )
    phone: str | None = Field(
        default=None,
        min_length=1,
        max_length=30,
    )
    email: str | None = None
    course_id: UUID | None = None
    preferred_date: date | None = None
    preferred_time: str | None = None
    message: str | None = None
    status: str | None = Field(
        default=None,
        min_length=1,
        max_length=50,
    )
    admin_notes: str | None = None
    converted_student_id: UUID | None = None
    converted_at: datetime | None = None


class DemoBookingResponse(DemoBookingBase):
    id: UUID
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)
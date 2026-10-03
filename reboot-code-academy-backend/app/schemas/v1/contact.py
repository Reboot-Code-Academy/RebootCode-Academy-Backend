from datetime import datetime
from uuid import UUID

from pydantic import BaseModel, ConfigDict, Field


class ContactBase(BaseModel):
    phone: str | None = Field(default=None, max_length=30)
    whatsapp: str | None = Field(default=None, max_length=30)
    email: str | None = Field(default=None, max_length=150)
    support_email: str | None = Field(default=None, max_length=150)

    address_line1: str | None = None
    address_line2: str | None = None
    city: str | None = Field(default=None, max_length=100)
    state: str | None = Field(default=None, max_length=100)
    pincode: str | None = Field(default=None, max_length=20)

    instagram: str | None = None
    facebook: str | None = None
    linkedin: str | None = None
    youtube: str | None = None
    telegram: str | None = None

    monday_friday: str | None = None
    saturday: str | None = None
    sunday: str | None = None

    google_maps_url: str | None = None


class ContactCreate(ContactBase):
    pass


class ContactUpdate(ContactBase):
    pass


class ContactResponse(ContactBase):
    id: UUID
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)
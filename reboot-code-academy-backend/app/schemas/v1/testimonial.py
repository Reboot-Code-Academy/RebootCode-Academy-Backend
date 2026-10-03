from datetime import datetime
from uuid import UUID

from pydantic import BaseModel, ConfigDict, Field


class TestimonialBase(BaseModel):
    student_name: str = Field(..., min_length=1, max_length=150)
    course: str | None = Field(default=None, max_length=150)
    review: str | None = None
    rating: int | None = Field(default=None, ge=1, le=5)
    photo_url: str | None = None
    is_active: bool = True


class TestimonialCreate(TestimonialBase):
    pass


class TestimonialUpdate(BaseModel):
    student_name: str | None = Field(
        default=None,
        min_length=1,
        max_length=150
    )
    course: str | None = Field(default=None, max_length=150)
    review: str | None = None
    rating: int | None = Field(default=None, ge=1, le=5)
    photo_url: str | None = None
    is_active: bool | None = None


class TestimonialResponse(TestimonialBase):
    id: UUID
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)
from datetime import datetime
from uuid import UUID

from pydantic import BaseModel, ConfigDict, Field


class CourseBase(BaseModel):
    name: str = Field(..., min_length=1, max_length=150)
    description: str | None = None
    level: str | None = None
    duration: str | None = None
    topics: str | None = None
    image_url: str | None = None
    is_active: bool = True


class CourseCreate(CourseBase):
    pass


class CourseUpdate(BaseModel):
    name: str | None = Field(
        default=None,
        min_length=1,
        max_length=150,
    )
    description: str | None = None
    level: str | None = None
    duration: str | None = None
    topics: str | None = None
    image_url: str | None = None
    is_active: bool | None = None


class CourseResponse(CourseBase):
    id: UUID
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)
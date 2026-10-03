from datetime import datetime
from uuid import UUID

from pydantic import BaseModel, ConfigDict, Field


class CourseMaterialBase(BaseModel):
    course_id: UUID
    title: str = Field(
        ...,
        min_length=1,
        max_length=200,
    )
    type: str = Field(
        ...,
        min_length=1,
        max_length=50,
    )
    description: str | None = None
    resource_url: str | None = None
    display_order: int = 0
    is_active: bool = True


class CourseMaterialCreate(CourseMaterialBase):
    pass


class CourseMaterialUpdate(BaseModel):
    course_id: UUID | None = None

    title: str | None = Field(
        default=None,
        min_length=1,
        max_length=200,
    )

    type: str | None = Field(
        default=None,
        min_length=1,
        max_length=50,
    )

    description: str | None = None
    resource_url: str | None = None
    display_order: int | None = None
    is_active: bool | None = None


class CourseMaterialResponse(CourseMaterialBase):
    id: UUID
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)
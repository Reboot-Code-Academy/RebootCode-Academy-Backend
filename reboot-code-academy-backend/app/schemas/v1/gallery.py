from datetime import datetime
from uuid import UUID

from pydantic import BaseModel, ConfigDict, Field


class GalleryBase(BaseModel):
    title: str = Field(..., min_length=1, max_length=150)
    category: str = Field(..., min_length=1, max_length=100)
    description: str | None = None
    image_url: str | None = None
    video_url: str | None = None
    is_active: bool = True


class GalleryCreate(GalleryBase):
    pass


class GalleryUpdate(BaseModel):
    title: str | None = Field(
        default=None,
        min_length=1,
        max_length=150,
    )
    category: str | None = Field(
        default=None,
        min_length=1,
        max_length=100,
    )
    description: str | None = None
    image_url: str | None = None
    video_url: str | None = None
    is_active: bool | None = None


class GalleryResponse(GalleryBase):
    id: UUID
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)
from datetime import date, datetime
from uuid import UUID

from pydantic import BaseModel, ConfigDict, Field


class AnnouncementBase(BaseModel):
    label: str = Field(
        ...,
        min_length=1,
        max_length=100,
    )

    text: str = Field(
        ...,
        min_length=1,
    )

    action_path: str | None = None

    start_date: date | None = None

    end_date: date | None = None

    is_active: bool = True


class AnnouncementCreate(AnnouncementBase):
    pass


class AnnouncementUpdate(BaseModel):
    label: str | None = Field(
        default=None,
        min_length=1,
        max_length=100,
    )

    text: str | None = Field(
        default=None,
        min_length=1,
    )

    action_path: str | None = None

    start_date: date | None = None

    end_date: date | None = None

    is_active: bool | None = None


class AnnouncementResponse(AnnouncementBase):
    id: UUID

    created_at: datetime

    updated_at: datetime

    model_config = ConfigDict(
        from_attributes=True
    )
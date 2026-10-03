from uuid import UUID

from fastapi import APIRouter, HTTPException, Response

from app.schemas.v1.announcement import (
    AnnouncementCreate,
    AnnouncementResponse,
    AnnouncementUpdate,
)
from app.services.announcements import (
    create_announcement,
    delete_announcement,
    get_announcement,
    get_announcements,
    update_announcement,
)


router = APIRouter(
    prefix="/announcements",
    tags=["Announcements"],
)


@router.get(
    "",
    response_model=list[AnnouncementResponse],
)
async def list_announcements():
    return await get_announcements()


@router.get(
    "/{announcement_id}",
    response_model=AnnouncementResponse,
)
async def retrieve_announcement(
    announcement_id: UUID,
):
    announcements = await get_announcement(
        announcement_id
    )

    if not announcements:
        raise HTTPException(
            status_code=404,
            detail="Announcement not found",
        )

    return announcements[0]


@router.post(
    "",
    response_model=AnnouncementResponse,
    status_code=201,
)
async def create(
    announcement: AnnouncementCreate,
):
    if (
        announcement.start_date
        and announcement.end_date
        and announcement.start_date
        > announcement.end_date
    ):
        raise HTTPException(
            status_code=400,
            detail="End date cannot be before start date.",
        )

    data = announcement.model_dump(
        mode="json"
    )

    announcements = await create_announcement(
        data
    )

    return announcements[0]


@router.put(
    "/{announcement_id}",
    response_model=AnnouncementResponse,
)
async def update(
    announcement_id: UUID,
    announcement: AnnouncementUpdate,
):
    data = announcement.model_dump(
        exclude_unset=True,
        mode="json",
    )

    if (
        data.get("start_date")
        and data.get("end_date")
        and data["start_date"]
        > data["end_date"]
    ):
        raise HTTPException(
            status_code=400,
            detail="End date cannot be before start date.",
        )

    announcements = await update_announcement(
        announcement_id,
        data,
    )

    if not announcements:
        raise HTTPException(
            status_code=404,
            detail="Announcement not found",
        )

    return announcements[0]


@router.delete(
    "/{announcement_id}",
    status_code=204,
)
async def remove(
    announcement_id: UUID,
):
    await delete_announcement(
        announcement_id
    )

    return Response(status_code=204)
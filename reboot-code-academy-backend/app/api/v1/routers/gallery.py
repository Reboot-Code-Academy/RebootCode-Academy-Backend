from uuid import UUID

from fastapi import APIRouter, HTTPException, Response, status

from app.schemas.v1.gallery import (
    GalleryCreate,
    GalleryResponse,
    GalleryUpdate,
)
from app.services.gallery import gallery_service


router = APIRouter(
    prefix="/gallery",
    tags=["Gallery"],
)


@router.get(
    "",
    response_model=list[GalleryResponse],
)
async def get_gallery_items():
    return await gallery_service.get_gallery_items()


@router.get(
    "/{gallery_id}",
    response_model=GalleryResponse,
)
async def get_gallery_item(gallery_id: UUID):
    gallery_items = await gallery_service.get_gallery_item(
        gallery_id
    )

    if not gallery_items:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Gallery item not found",
        )

    return gallery_items[0]


@router.post(
    "",
    response_model=GalleryResponse,
    status_code=status.HTTP_201_CREATED,
)
async def create_gallery_item(
    gallery: GalleryCreate,
):
    gallery_items = await gallery_service.create_gallery_item(
        gallery
    )

    return gallery_items[0]


@router.put(
    "/{gallery_id}",
    response_model=GalleryResponse,
)
async def update_gallery_item(
    gallery_id: UUID,
    gallery: GalleryUpdate,
):
    gallery_items = await gallery_service.update_gallery_item(
        gallery_id,
        gallery,
    )

    if not gallery_items:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Gallery item not found",
        )

    return gallery_items[0]


@router.delete(
    "/{gallery_id}",
    status_code=status.HTTP_204_NO_CONTENT,
)
async def delete_gallery_item(gallery_id: UUID):
    await gallery_service.delete_gallery_item(
        gallery_id
    )

    return Response(
        status_code=status.HTTP_204_NO_CONTENT
    )
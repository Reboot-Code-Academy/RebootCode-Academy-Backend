from uuid import UUID

from fastapi import APIRouter, HTTPException, Response, status

from app.schemas.v1.contact import (
    ContactCreate,
    ContactResponse,
    ContactUpdate,
)
from app.services.contact import contact_service


router = APIRouter(
    prefix="/contact",
    tags=["Contact Information"],
)


@router.get(
    "",
    response_model=ContactResponse,
)
async def get_contact_information():
    contacts = await contact_service.get_contact_information()

    if not contacts:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Contact information not found",
        )

    return contacts[0]


@router.post(
    "",
    response_model=ContactResponse,
    status_code=status.HTTP_201_CREATED,
)
async def create_contact_information(
    contact: ContactCreate,
):
    contacts = await contact_service.create_contact_information(
        contact
    )

    return contacts[0]


@router.put(
    "/{contact_id}",
    response_model=ContactResponse,
)
async def update_contact_information(
    contact_id: UUID,
    contact: ContactUpdate,
):
    contacts = await contact_service.update_contact_information(
        contact_id,
        contact,
    )

    if not contacts:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Contact information not found",
        )

    return contacts[0]


@router.delete(
    "/{contact_id}",
    status_code=status.HTTP_204_NO_CONTENT,
)
async def delete_contact_information(
    contact_id: UUID,
):
    await contact_service.delete_contact_information(
        contact_id
    )

    return Response(
        status_code=status.HTTP_204_NO_CONTENT
    )
from uuid import UUID

from fastapi import APIRouter, HTTPException, Response, status

from app.schemas.v1.demo_booking import (
    DemoBookingCreate,
    DemoBookingResponse,
    DemoBookingUpdate,
)
from app.services.demo_bookings import demo_booking_service


router = APIRouter(
    prefix="/demo-bookings",
    tags=["Demo Bookings"],
)


@router.get(
    "",
    response_model=list[DemoBookingResponse],
)
async def get_demo_bookings():
    return await demo_booking_service.get_demo_bookings()


@router.get(
    "/{booking_id}",
    response_model=DemoBookingResponse,
)
async def get_demo_booking(booking_id: UUID):
    bookings = await demo_booking_service.get_demo_booking(
        booking_id
    )

    if not bookings:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Demo booking not found",
        )

    return bookings[0]


@router.post(
    "",
    response_model=DemoBookingResponse,
    status_code=status.HTTP_201_CREATED,
)
async def create_demo_booking(
    booking: DemoBookingCreate,
):
    bookings = await demo_booking_service.create_demo_booking(
        booking
    )

    return bookings[0]


@router.put(
    "/{booking_id}",
    response_model=DemoBookingResponse,
)
async def update_demo_booking(
    booking_id: UUID,
    booking: DemoBookingUpdate,
):
    bookings = await demo_booking_service.update_demo_booking(
        booking_id,
        booking,
    )

    if not bookings:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Demo booking not found",
        )

    return bookings[0]

@router.post(
    "/{booking_id}/convert",
)
async def convert_demo_booking(
    booking_id: UUID,
):
    result, error = await demo_booking_service.convert_to_student(
        booking_id
    )

    if error:
        if error == "Demo booking not found":
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail=error,
            )

        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail=error,
        )

    return result

@router.delete(
    "/{booking_id}",
    status_code=status.HTTP_204_NO_CONTENT,
)
async def delete_demo_booking(booking_id: UUID):
    await demo_booking_service.delete_demo_booking(
        booking_id
    )

    return Response(
        status_code=status.HTTP_204_NO_CONTENT
    )
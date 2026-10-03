from uuid import UUID

from fastapi import APIRouter, HTTPException, Response

from app.schemas.v1.testimonial import (
    TestimonialCreate,
    TestimonialResponse,
    TestimonialUpdate,
)
from app.services.testimonials import testimonial_service


router = APIRouter(
    prefix="/testimonials",
    tags=["Testimonials"],
)


@router.get("", response_model=list[TestimonialResponse])
async def get_testimonials():
    return await testimonial_service.get_testimonials()


@router.get(
    "/{testimonial_id}",
    response_model=TestimonialResponse,
)
async def get_testimonial(testimonial_id: UUID):
    testimonials = await testimonial_service.get_testimonial(
        testimonial_id
    )

    if not testimonials:
        raise HTTPException(
            status_code=404,
            detail="Testimonial not found",
        )

    return testimonials[0]


@router.post(
    "",
    response_model=TestimonialResponse,
    status_code=201,
)
async def create_testimonial(
    testimonial: TestimonialCreate,
):
    testimonials = await testimonial_service.create_testimonial(
        testimonial
    )

    return testimonials[0]


@router.put(
    "/{testimonial_id}",
    response_model=TestimonialResponse,
)
async def update_testimonial(
    testimonial_id: UUID,
    testimonial: TestimonialUpdate,
):
    testimonials = await testimonial_service.update_testimonial(
        testimonial_id,
        testimonial,
    )

    if not testimonials:
        raise HTTPException(
            status_code=404,
            detail="Testimonial not found",
        )

    return testimonials[0]


@router.delete(
    "/{testimonial_id}",
    status_code=204,
)
async def delete_testimonial(testimonial_id: UUID):
    await testimonial_service.delete_testimonial(
        testimonial_id
    )

    return Response(status_code=204)
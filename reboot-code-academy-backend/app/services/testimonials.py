from uuid import UUID

from app.database import supabase
from app.schemas.v1.testimonial import (
    TestimonialCreate,
    TestimonialUpdate,
)


class TestimonialService:

    async def get_testimonials(self):
        return await supabase.get(
            "testimonials",
            "?select=*&order=created_at.desc",
        )

    async def get_testimonial(self, testimonial_id: UUID):
        return await supabase.get(
            "testimonials",
            f"?id=eq.{testimonial_id}&select=*",
        )

    async def create_testimonial(
        self,
        testimonial: TestimonialCreate,
    ):
        data = testimonial.model_dump(mode="json")

        return await supabase.post(
            "testimonials",
            data,
        )

    async def update_testimonial(
        self,
        testimonial_id: UUID,
        testimonial: TestimonialUpdate,
    ):
        data = testimonial.model_dump(
            exclude_unset=True,
            mode="json",
        )

        return await supabase.patch(
            "testimonials",
            f"?id=eq.{testimonial_id}",
            data,
        )

    async def delete_testimonial(
        self,
        testimonial_id: UUID,
    ):
        return await supabase.delete(
            "testimonials",
            f"?id=eq.{testimonial_id}",
        )


testimonial_service = TestimonialService()
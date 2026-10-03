from uuid import UUID

from app.database import supabase
from app.schemas.v1.course_material import (
    CourseMaterialCreate,
    CourseMaterialUpdate,
)


class CourseMaterialService:

    async def get_course_materials(self):
        return await supabase.get(
            "course_materials",
            "?select=*&order=display_order.asc,created_at.desc",
        )

    async def get_course_material(
        self,
        material_id: UUID,
    ):
        return await supabase.get(
            "course_materials",
            f"?id=eq.{material_id}&select=*",
        )

    async def create_course_material(
        self,
        material: CourseMaterialCreate,
    ):
        data = material.model_dump(
            mode="json",
        )

        return await supabase.post(
            "course_materials",
            data,
        )

    async def update_course_material(
        self,
        material_id: UUID,
        material: CourseMaterialUpdate,
    ):
        data = material.model_dump(
            exclude_unset=True,
            mode="json",
        )

        return await supabase.patch(
            "course_materials",
            f"?id=eq.{material_id}",
            data,
        )

    async def delete_course_material(
        self,
        material_id: UUID,
    ):
        return await supabase.delete(
            "course_materials",
            f"?id=eq.{material_id}",
        )


course_material_service = CourseMaterialService()
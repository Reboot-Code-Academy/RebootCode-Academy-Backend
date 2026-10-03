from uuid import UUID

from app.database import supabase
from app.schemas.v1.course import (
    CourseCreate,
    CourseUpdate,
)


class CourseService:

    async def get_courses(self):
        return await supabase.get(
            "courses",
            "?select=*&order=created_at.desc",
        )

    async def get_course(self, course_id: UUID):
        return await supabase.get(
            "courses",
            f"?id=eq.{course_id}&select=*",
        )

    async def create_course(
        self,
        course: CourseCreate,
    ):
        return await supabase.post(
            "courses",
            course.model_dump(),
        )

    async def update_course(
        self,
        course_id: UUID,
        course: CourseUpdate,
    ):
        data = course.model_dump(
            exclude_unset=True
        )

        return await supabase.patch(
            "courses",
            f"?id=eq.{course_id}",
            data,
        )

    async def delete_course(
        self,
        course_id: UUID,
    ):
        return await supabase.delete(
            "courses",
            f"?id=eq.{course_id}",
        )


course_service = CourseService()
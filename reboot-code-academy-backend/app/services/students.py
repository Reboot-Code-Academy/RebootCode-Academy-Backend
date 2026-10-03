from app.database import supabase
from app.schemas.v1.student import (
    StudentCreate,
    StudentUpdate,
)


class StudentService:

    async def get_students(self):
        students = await supabase.get(
            "students",
            "?select=*&order=created_at.desc",
        )

        return [
            {
                **student,
                "student_photo": student.get("photo_url"),
            }
            for student in students
        ]

    async def get_student(self, student_id: str):
        students = await supabase.get(
            "students",
            f"?student_id=eq.{student_id}&select=*",
        )

        return [
            {
                **student,
                "student_photo": student.get("photo_url"),
            }
            for student in students
        ]

    async def create_student(
        self,
        student: StudentCreate,
    ):
        data = student.model_dump(mode="json")

        data["photo_url"] = data.pop(
            "student_photo",
            None,
        )

        students = await supabase.post(
            "students",
            data,
        )

        return [
            {
                **item,
                "student_photo": item.get("photo_url"),
            }
            for item in students
        ]

    async def update_student(
        self,
        student_id: str,
        student: StudentUpdate,
    ):
        data = student.model_dump(
            exclude_unset=True,
            mode="json",
        )

        if "student_photo" in data:
            data["photo_url"] = data.pop(
                "student_photo"
            )

        students = await supabase.patch(
            "students",
            f"?student_id=eq.{student_id}",
            data,
        )

        return [
            {
                **item,
                "student_photo": item.get("photo_url"),
            }
            for item in students
        ]

    async def delete_student(
        self,
        student_id: str,
    ):
        return await supabase.delete(
            "students",
            f"?student_id=eq.{student_id}",
        )


student_service = StudentService()
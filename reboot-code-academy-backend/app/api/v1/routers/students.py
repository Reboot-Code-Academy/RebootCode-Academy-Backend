from fastapi import APIRouter, HTTPException, Response, status

from app.schemas.v1.student import (
    StudentCreate,
    StudentResponse,
    StudentUpdate,
)
from app.services.students import student_service


router = APIRouter(
    prefix="/students",
    tags=["Students"],
)


@router.get(
    "",
    response_model=list[StudentResponse],
)
async def get_students():
    return await student_service.get_students()


@router.get(
    "/{student_id}",
    response_model=StudentResponse,
)
async def get_student(student_id: str):
    students = await student_service.get_student(
        student_id
    )

    if not students:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Student not found",
        )

    return students[0]


@router.post(
    "",
    response_model=StudentResponse,
    status_code=status.HTTP_201_CREATED,
)
async def create_student(
    student: StudentCreate,
):
    students = await student_service.create_student(
        student
    )

    return students[0]


@router.put(
    "/{student_id}",
    response_model=StudentResponse,
)
async def update_student(
    student_id: str,
    student: StudentUpdate,
):
    students = await student_service.update_student(
        student_id,
        student,
    )

    if not students:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Student not found",
        )

    return students[0]


@router.delete(
    "/{student_id}",
    status_code=status.HTTP_204_NO_CONTENT,
)
async def delete_student(student_id: str):
    await student_service.delete_student(
        student_id
    )

    return Response(
        status_code=status.HTTP_204_NO_CONTENT
    )
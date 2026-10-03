from uuid import UUID

from fastapi import APIRouter, HTTPException, Response, status

from app.schemas.v1.course_material import (
    CourseMaterialCreate,
    CourseMaterialResponse,
    CourseMaterialUpdate,
)
from app.services.course_materials import (
    course_material_service,
)


router = APIRouter(
    prefix="/course-materials",
    tags=["Course Materials"],
)


@router.get(
    "",
    response_model=list[CourseMaterialResponse],
)
async def get_course_materials():
    return await course_material_service.get_course_materials()


@router.get(
    "/{material_id}",
    response_model=CourseMaterialResponse,
)
async def get_course_material(
    material_id: UUID,
):
    materials = await course_material_service.get_course_material(
        material_id
    )

    if not materials:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Course material not found",
        )

    return materials[0]


@router.post(
    "",
    response_model=CourseMaterialResponse,
    status_code=status.HTTP_201_CREATED,
)
async def create_course_material(
    material: CourseMaterialCreate,
):
    materials = await course_material_service.create_course_material(
        material
    )

    return materials[0]


@router.put(
    "/{material_id}",
    response_model=CourseMaterialResponse,
)
async def update_course_material(
    material_id: UUID,
    material: CourseMaterialUpdate,
):
    materials = await course_material_service.update_course_material(
        material_id,
        material,
    )

    if not materials:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Course material not found",
        )

    return materials[0]


@router.delete(
    "/{material_id}",
    status_code=status.HTTP_204_NO_CONTENT,
)
async def delete_course_material(
    material_id: UUID,
):
    await course_material_service.delete_course_material(
        material_id
    )

    return Response(status_code=status.HTTP_204_NO_CONTENT)
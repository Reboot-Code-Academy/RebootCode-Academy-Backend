from uuid import UUID, uuid4

from fastapi import (
    APIRouter,
    File,
    HTTPException,
    Response,
    UploadFile,
)

from app.database import supabase
from app.schemas.v1.course import (
    CourseCreate,
    CourseResponse,
    CourseUpdate,
)


router = APIRouter(
    prefix="/courses",
    tags=["Courses"],
)


# --------------------------------------------------
# GET ALL COURSES
# --------------------------------------------------

@router.get(
    "",
    response_model=list[CourseResponse],
)
async def get_courses():
    return await supabase.get(
        "courses",
        "?select=*&order=created_at.desc",
    )


# --------------------------------------------------
# GET SINGLE COURSE
# --------------------------------------------------

@router.get(
    "/{course_id}",
    response_model=CourseResponse,
)
async def get_course(course_id: UUID):
    courses = await supabase.get(
        "courses",
        f"?id=eq.{course_id}&select=*",
    )

    if not courses:
        raise HTTPException(
            status_code=404,
            detail="Course not found",
        )

    return courses[0]


# --------------------------------------------------
# CREATE COURSE
# --------------------------------------------------

@router.post(
    "",
    response_model=CourseResponse,
    status_code=201,
)
async def create_course(course: CourseCreate):
    data = course.model_dump(mode="json")

    courses = await supabase.post(
        "courses",
        data,
    )

    return courses[0]


# --------------------------------------------------
# UPDATE COURSE
# --------------------------------------------------

@router.put(
    "/{course_id}",
    response_model=CourseResponse,
)
async def update_course(
    course_id: UUID,
    course: CourseUpdate,
):
    data = course.model_dump(
        exclude_unset=True,
        mode="json",
    )

    courses = await supabase.patch(
        "courses",
        f"?id=eq.{course_id}",
        data,
    )

    if not courses:
        raise HTTPException(
            status_code=404,
            detail="Course not found",
        )

    return courses[0]


# --------------------------------------------------
# DELETE COURSE
# --------------------------------------------------

@router.delete(
    "/{course_id}",
    status_code=204,
)
async def delete_course(course_id: UUID):
    await supabase.delete(
        "courses",
        f"?id=eq.{course_id}",
    )

    return Response(status_code=204)


# --------------------------------------------------
# UPLOAD COURSE IMAGE
# --------------------------------------------------

@router.post(
    "/{course_id}/image",
)
async def upload_course_image(
    course_id: UUID,
    file: UploadFile = File(...),
):
    # Check course exists
    courses = await supabase.get(
        "courses",
        f"?id=eq.{course_id}&select=id",
    )

    if not courses:
        raise HTTPException(
            status_code=404,
            detail="Course not found",
        )

    # Validate file type
    if not file.content_type:
        raise HTTPException(
            status_code=400,
            detail="File type could not be determined",
        )

    if not file.content_type.startswith("image/"):
        raise HTTPException(
            status_code=400,
            detail="Only image files are allowed",
        )

    # Read file
    file_content = await file.read()

    if not file_content:
        raise HTTPException(
            status_code=400,
            detail="Uploaded image is empty",
        )

    # Get extension
    if file.filename and "." in file.filename:
        extension = (
            file.filename
            .rsplit(".", 1)[-1]
            .lower()
        )
    else:
        extension = "jpg"

    # Create unique storage path
    file_path = (
        f"courses/{course_id}/"
        f"{uuid4()}.{extension}"
    )

    try:
        # Upload to Supabase Storage
        image_url = await supabase.upload_storage(
            bucket="course-images",
            path=file_path,
            file_content=file_content,
            content_type=file.content_type,
        )

        # Save URL in courses table
        updated_courses = await supabase.patch(
            "courses",
            f"?id=eq.{course_id}",
            {
                "image_url": image_url,
            },
        )

        if not updated_courses:
            raise HTTPException(
                status_code=404,
                detail="Course not found",
            )

        return {
            "message": "Course image uploaded successfully",
            "image_url": image_url,
        }

    except HTTPException:
        raise

    except Exception as error:
        print(
            "Course image upload error:",
            error,
        )

        raise HTTPException(
            status_code=500,
            detail="Could not upload course image",
        )
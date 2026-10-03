from uuid import UUID
from datetime import datetime, timezone
from app.database import supabase
from app.schemas.v1.demo_booking import (
    DemoBookingCreate,
    DemoBookingUpdate,
)


class DemoBookingService:

    async def get_demo_bookings(self):
        return await supabase.get(
            "demo_bookings",
            "?select=*&order=created_at.desc",
        )

    async def convert_to_student(
        self,
        booking_id: UUID,
    ):
        # Get the demo booking
        bookings = await supabase.get(
            "demo_bookings",
            f"?id=eq.{booking_id}&select=*",
        )

        if not bookings:
            return None, "Demo booking not found"

        booking = bookings[0]

        # Prevent duplicate conversion
        if booking.get("converted_student_id"):
            return None, "Demo booking already converted"

        # Check whether phone already exists
        existing_phone = await supabase.get(
            "students",
            f"?phone=eq.{booking['phone']}&select=*",
        )

        if existing_phone:
            return None, "A student with this phone number already exists"

        # Check whether email already exists
        if booking.get("email"):
            existing_email = await supabase.get(
                "students",
                f"?email=eq.{booking['email']}&select=*",
            )

            if existing_email:
                return None, "A student with this email already exists"

        # Create student
        student_data = {
            "name": booking["name"],
            "phone": booking["phone"],
            "email": booking.get("email"),
            "course_id": booking.get("course_id"),
            "join_date": datetime.now(
                timezone.utc
            ).date().isoformat(),
            "status": "Active",
            "photo_url": None,
        }

        students = await supabase.post(
            "students",
            student_data,
        )

        if not students:
            return None, "Student creation failed"

        student = students[0]

        # Update demo booking
        converted_at = datetime.now(
            timezone.utc
        ).isoformat()

        updated_bookings = await supabase.patch(
            "demo_bookings",
            f"?id=eq.{booking_id}",
            {
                "converted_student_id": student["id"],
                "converted_at": converted_at,
                "status": "Completed",
            },
        )

        return {
            "student": student,
            "demo_booking": updated_bookings[0],
        }, None
        
    async def get_demo_booking(
        self,
        booking_id: UUID,
    ):
        return await supabase.get(
            "demo_bookings",
            f"?id=eq.{booking_id}&select=*",
        )

    async def create_demo_booking(
        self,
        booking: DemoBookingCreate,
    ):
        data = booking.model_dump(
            mode="json",
        )

        return await supabase.post(
            "demo_bookings",
            data,
        )

    async def update_demo_booking(
        self,
        booking_id: UUID,
        booking: DemoBookingUpdate,
    ):
        data = booking.model_dump(
            exclude_unset=True,
            mode="json",
        )

        return await supabase.patch(
            "demo_bookings",
            f"?id=eq.{booking_id}",
            data,
        )

    async def delete_demo_booking(
        self,
        booking_id: UUID,
    ):
        return await supabase.delete(
            "demo_bookings",
            f"?id=eq.{booking_id}",
        )


demo_booking_service = DemoBookingService()
from uuid import UUID

from app.database import supabase


async def get_announcements():
    return await supabase.get(
        "announcements",
        "?select=*&order=created_at.desc",
    )


async def get_announcement(
    announcement_id: UUID,
):
    return await supabase.get(
        "announcements",
        f"?id=eq.{announcement_id}&select=*",
    )


async def create_announcement(
    data: dict,
):
    return await supabase.post(
        "announcements",
        data,
    )


async def update_announcement(
    announcement_id: UUID,
    data: dict,
):
    return await supabase.patch(
        "announcements",
        f"?id=eq.{announcement_id}",
        data,
    )


async def delete_announcement(
    announcement_id: UUID,
):
    return await supabase.delete(
        "announcements",
        f"?id=eq.{announcement_id}",
    )
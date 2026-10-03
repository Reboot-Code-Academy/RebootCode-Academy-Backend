from uuid import UUID

from app.database import supabase
from app.schemas.v1.contact import (
    ContactCreate,
    ContactUpdate,
)


class ContactService:

    async def get_contact_information(self):
        return await supabase.get(
            "contact_information",
            "?select=*&limit=1",
        )

    async def create_contact_information(
        self,
        contact: ContactCreate,
    ):
        data = contact.model_dump(
            mode="json",
        )

        return await supabase.post(
            "contact_information",
            data,
        )

    async def update_contact_information(
        self,
        contact_id: UUID,
        contact: ContactUpdate,
    ):
        data = contact.model_dump(
            exclude_unset=True,
            mode="json",
        )

        return await supabase.patch(
            "contact_information",
            f"?id=eq.{contact_id}",
            data,
        )

    async def delete_contact_information(
        self,
        contact_id: UUID,
    ):
        return await supabase.delete(
            "contact_information",
            f"?id=eq.{contact_id}",
        )


contact_service = ContactService()
from uuid import UUID

from app.database import supabase
from app.schemas.v1.gallery import (
    GalleryCreate,
    GalleryUpdate,
)


class GalleryService:

    async def get_gallery_items(self):
        return await supabase.get(
            "gallery_items",
            "?select=*&order=created_at.desc",
        )

    async def get_gallery_item(self, gallery_id: UUID):
        return await supabase.get(
            "gallery_items",
            f"?id=eq.{gallery_id}&select=*",
        )

    async def create_gallery_item(
        self,
        gallery: GalleryCreate,
    ):
        return await supabase.post(
            "gallery_items",
            gallery.model_dump(mode="json"),
        )

    async def update_gallery_item(
        self,
        gallery_id: UUID,
        gallery: GalleryUpdate,
    ):
        data = gallery.model_dump(
            exclude_unset=True,
            mode="json",
        )

        return await supabase.patch(
            "gallery_items",
            f"?id=eq.{gallery_id}",
            data,
        )

    async def delete_gallery_item(
        self,
        gallery_id: UUID,
    ):
        return await supabase.delete(
            "gallery_items",
            f"?id=eq.{gallery_id}",
        )


gallery_service = GalleryService()
import httpx

from app.core.config import settings


class SupabaseClient:
    def __init__(self):
        self.base_url = f"{settings.supabase_url}/rest/v1"

        self.headers = {
            "apikey": settings.supabase_service_role_key,
            "Authorization": (
                f"Bearer {settings.supabase_service_role_key}"
            ),
            "Content-Type": "application/json",
        }

    async def get(self, table: str, query: str = ""):
        async with httpx.AsyncClient() as client:
            response = await client.get(
                f"{self.base_url}/{table}{query}",
                headers=self.headers,
            )

        response.raise_for_status()
        return response.json()

    async def post(self, table: str, data: dict):
        headers = {
            **self.headers,
            "Prefer": "return=representation",
        }

        async with httpx.AsyncClient() as client:
            response = await client.post(
                f"{self.base_url}/{table}",
                headers=headers,
                json=data,
            )

        response.raise_for_status()
        return response.json()

    async def patch(
        self,
        table: str,
        query: str,
        data: dict,
    ):
        headers = {
            **self.headers,
            "Prefer": "return=representation",
        }

        async with httpx.AsyncClient() as client:
            response = await client.patch(
                f"{self.base_url}/{table}{query}",
                headers=headers,
                json=data,
            )

        response.raise_for_status()
        return response.json()

    async def delete(
        self,
        table: str,
        query: str,
    ):
        async with httpx.AsyncClient() as client:
            response = await client.delete(
                f"{self.base_url}/{table}{query}",
                headers=self.headers,
            )

        response.raise_for_status()
        return True

    async def upload_storage(
        self,
        bucket: str,
        path: str,
        file_content: bytes,
        content_type: str,
    ):
        headers = {
            "apikey": settings.supabase_service_role_key,
            "Authorization": (
                f"Bearer {settings.supabase_service_role_key}"
            ),
            "Content-Type": content_type,
            "x-upsert": "true",
        }

        async with httpx.AsyncClient() as client:
            response = await client.post(
                (
                    f"{settings.supabase_url}"
                    f"/storage/v1/object/{bucket}/{path}"
                ),
                headers=headers,
                content=file_content,
            )

        response.raise_for_status()

        return (
            f"{settings.supabase_url}"
            f"/storage/v1/object/public/{bucket}/{path}"
        )


supabase = SupabaseClient()
import asyncio
from typing import Optional
from httpx import AsyncClient, Timeout


class Request:
    def __init__(
        self,
        method: str,
        url: str,
        *,
        headers: Optional[dict] = None,
        body: Optional[dict] = None
    ) -> None:
        self.method = method
        self.url = url
        self.headers = headers
        self.body = body

        self.client = AsyncClient()
        self.loop = asyncio.get_event_loop()

    def __del__(self):
        try:
            self.loop.run_until_complete(self.client.aclose())
        except Exception:
            # i have no clue what the exception means
            pass

    async def make(self):
        try:
            response = await self.client.request(
                self.method,
                self.url,
                json=self.body,
                headers=self.headers,
                timeout=Timeout(timeout=30),
            )

            if not response.is_error:
                return True
        except Exception:
            pass

        return False

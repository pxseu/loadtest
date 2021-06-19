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

    async def make(self, client: AsyncClient):
        try:
            response = await client.request(
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

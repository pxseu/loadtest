from typing import Optional
from httpx import request, Timeout


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

    async def make(self) -> bool:
        try:
            response = request(
                self.method,
                self.url,
                json=self.body,
                headers=self.headers,
                timeout=Timeout(timeout=30),
            )

            if not response.is_error:
                return True
        except:
            pass

        return False

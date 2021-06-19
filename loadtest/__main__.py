import asyncio

from httpx import AsyncClient
from Request import Request


async def main(amount: int, request: Request):
    async with AsyncClient() as client:
        tasks = [request.make(client) for _ in range(amount)]
        results = await asyncio.gather(*tasks)
        completed = [res for res in results if res]

    print(f"Completed {len(completed)} out of {amount}")


if __name__ == "__main__":
    request = Request(method="GET", url="https://www.pxseu.com")

    asyncio.run(main(amount=400, request=request))

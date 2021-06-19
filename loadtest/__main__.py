import asyncio
from Request import Request


async def main(amount: int, request: Request):
    tasks = [request.make() for _ in range(amount)]

    results = await asyncio.gather(*tasks)

    completed = [res for res in results if res]

    print(f"Completed {len(completed)} out of {amount}")


if __name__ == "__main__":
    request = Request(method="GET", url="http://localhost:8080/")

    asyncio.run(main(amount=300, request=request))

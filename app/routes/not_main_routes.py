from fastapi import APIRouter

not_main_router = APIRouter()


@not_main_router.get("/items/{item_id}")
async def read_item(item_id: int, q: str | None = None):
    return {"item_id": item_id, "q": q}

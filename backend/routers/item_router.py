from fastapi import APIRouter

router = APIRouter()


@router.get("/items")
async def get_items():
    return {"message": "List of items"}

# Это и есть корневой роут
from typing import Annotated

from fastapi import Path, APIRouter

router = APIRouter(prefix="/items", tags=["items"])

@router.get("/hello/")
async def root():
    return {"message": "hello world",}


@router.get("/latest/")
async def read_items():
    return [{"item1": "Foo"}, {"item_2": "Bar"}]


@router.get("/{item_id}/")
async def read_items(item_id: Annotated[int, Path(ge=1, lt=1_000_000)]):
    return {
        'item_id': {
            'id': item_id,
                },
        }


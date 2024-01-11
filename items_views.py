from typing import Annotated

from fastapi import APIRouter, Path

router = APIRouter(prefix="/items", tags=["Items"])


@router.get("/items/")
def list_items():
    return [
        "Item1",
        "Item2",
        "Item3",
    ]


@router.get("/items/latest/")
def get_latest_item():
    return {"item": {"id": "0", "name": "latest"}}


@router.get("/items/{item_id}/")
def get_item_by_id(item_id: Annotated[int, Path(ge=1, lt=100000)]):
    return {
        "item": {
            "id": item_id,
        },
    }


from pydantic import BaseModel, ConfigDict


class ProductBase(BaseModel):
    district: str
    exact_location: str
    description: str
    usable_area: int


class ProductCreate(ProductBase):
    pass


class ProductUpdate(ProductCreate):
    pass


class ProductUpdatePartial(ProductCreate):
    district: str | None = None
    exact_location: str | None = None
    description: str | None = None
    usable_area: int | None = None


class Product(ProductBase):
    model_config = ConfigDict(from_attributes=True)
    id: int

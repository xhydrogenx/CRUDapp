from sqlalchemy.orm import Mapped

from .base import Base


class Product(Base):
    district: Mapped[str]
    exact_location: Mapped[str]
    description: Mapped[str]
    usable_area: Mapped[int]

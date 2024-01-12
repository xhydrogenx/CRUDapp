"""Create products table

Revision ID: 9ecfa3a78d5f
Revises: 
Create Date: 2024-01-12 11:55:46.685428

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = "9ecfa3a78d5f"
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table(
        "products",
        sa.Column("district", sa.String(), nullable=False),
        sa.Column("exact_location", sa.String(), nullable=False),
        sa.Column("description", sa.String(), nullable=False),
        sa.Column("usable_area", sa.Integer(), nullable=False),
        sa.Column("id", sa.Integer(), nullable=False),
        sa.PrimaryKeyConstraint("id"),
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table("products")
    # ### end Alembic commands ###

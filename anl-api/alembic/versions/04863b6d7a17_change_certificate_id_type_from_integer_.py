"""Change certificate id type from integer to big integer

Revision ID: 04863b6d7a17
Revises: 73f28440d5da
Create Date: 2021-08-21 07:00:26.104463

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = "04863b6d7a17"
down_revision = "73f28440d5da"
branch_labels = None
depends_on = None


def upgrade():
    op.alter_column(
        "certificate",
        "id",
        existing_type=sa.INTEGER(),
        type_=sa.BigInteger(),
        existing_nullable=False,
        autoincrement=True,
    )


def downgrade():
    op.alter_column(
        "certificate",
        "id",
        existing_type=sa.BigInteger(),
        type_=sa.INTEGER(),
        existing_nullable=False,
        autoincrement=True,
    )

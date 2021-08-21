"""Remove unique constraints from unit guid

Revision ID: 73f28440d5da
Revises: 2006acebef95
Create Date: 2021-08-21 04:15:06.015716

"""
from alembic import op


# revision identifiers, used by Alembic.
revision = "73f28440d5da"
down_revision = "2006acebef95"
branch_labels = None
depends_on = None


def upgrade():
    op.drop_constraint("unit_guid_key", "unit", type_="unique")


def downgrade():
    op.create_unique_constraint("unit_guid_key", "unit", ["guid"])

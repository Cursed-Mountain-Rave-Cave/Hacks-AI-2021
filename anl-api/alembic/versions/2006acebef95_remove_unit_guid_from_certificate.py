"""Remove unit guid from certificate

Revision ID: 2006acebef95
Revises: ca42e0f71125
Create Date: 2021-08-21 04:13:30.890834

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = "2006acebef95"
down_revision = "ca42e0f71125"
branch_labels = None
depends_on = None


def upgrade():
    op.drop_constraint("certificate_unit_guid_fkey", "certificate", type_="foreignkey")
    op.drop_column("certificate", "unit_guid")


def downgrade():
    op.add_column(
        "certificate",
        sa.Column("unit_guid", sa.VARCHAR(length=36), autoincrement=False, nullable=True),
    )
    op.create_foreign_key(
        "certificate_unit_guid_fkey", "certificate", "unit", ["unit_guid"], ["guid"]
    )

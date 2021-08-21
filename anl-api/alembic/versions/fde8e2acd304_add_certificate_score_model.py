"""Add certificate score model

Revision ID: fde8e2acd304
Revises: 04863b6d7a17
Create Date: 2021-08-21 11:01:42.889637

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = "fde8e2acd304"
down_revision = "04863b6d7a17"
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        "certificate_score",
        sa.Column("id", sa.BigInteger(), nullable=False),
        sa.Column("certificate_id", sa.BigInteger(), nullable=False),
        sa.Column("active", sa.Boolean(), server_default="True", nullable=True),
        sa.Column("approved", sa.Boolean(), server_default="False", nullable=True),
        sa.Column("denied", sa.Boolean(), server_default="False", nullable=True),
        sa.Column("score", sa.Float(), nullable=True),
        sa.Column("score_violation_type", sa.String(length=100), nullable=True),
        sa.Column(
            "score_date", sa.DateTime(), server_default=sa.text("CURRENT_TIMESTAMP"), nullable=True
        ),
        sa.Column("resolution_date", sa.DateTime(), nullable=True),
        sa.ForeignKeyConstraint(
            ["certificate_id"],
            ["certificate.id"],
        ),
        sa.PrimaryKeyConstraint("id"),
    )


def downgrade():
    op.drop_table("certificate_score")

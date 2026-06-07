"""add phones to scan_result

Revision ID: a1b2c3d4e5f6
Revises: 31c17b92187a
Create Date: 2026-06-07
"""
from alembic import op
import sqlalchemy as sa

revision = 'a1b2c3d4e5f6'
down_revision = '31c17b92187a'
branch_labels = None
depends_on = None


def upgrade():
    op.add_column('scan_result', sa.Column('phones', sa.Text(), nullable=True))


def downgrade():
    op.drop_column('scan_result', 'phones')

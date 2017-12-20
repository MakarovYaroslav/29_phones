"""add phone column

Revision ID: 2c040f2f8074
Revises: d6a4042037bd
Create Date: 2017-12-20 13:16:10.357355

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '2c040f2f8074'
down_revision = 'd6a4042037bd'
branch_labels = None
depends_on = None


def upgrade():
    op.add_column('orders', sa.Column('formatted_phone', sa.String(20)))


def downgrade():
    op.drop_column('orders', 'formatted_phone')

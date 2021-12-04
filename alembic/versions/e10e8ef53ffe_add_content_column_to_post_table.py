"""add content column to post table

Revision ID: e10e8ef53ffe
Revises: 6697b3f53fa5
Create Date: 2021-12-03 19:15:03.757993

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'e10e8ef53ffe'
down_revision = '6697b3f53fa5'
branch_labels = None
depends_on = None


def upgrade():
    op.add_column('posts', sa.Column('content', sa.String(), nullable=False))
    pass


def downgrade():
    op.drop_column('posts','content')
    pass

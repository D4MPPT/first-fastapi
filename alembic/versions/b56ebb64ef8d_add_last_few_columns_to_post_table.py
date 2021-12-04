"""add last few columns to post table

Revision ID: b56ebb64ef8d
Revises: a52c257c2973
Create Date: 2021-12-03 19:39:40.789517

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'b56ebb64ef8d'
down_revision = 'a52c257c2973'
branch_labels = None
depends_on = None


def upgrade():
    op.add_column('posts',sa.Column('published', sa.Boolean(), server_default='True', nullable=False),)
    op.add_column('posts', sa.Column('created_at', sa.TIMESTAMP(timezone=True),nullable=False,server_default=sa.text('NOW()')),)
    pass


def downgrade():
    op.drop_column('posts','published')
    op.drop_column('posts','created_at')
    pass

"""add user table

Revision ID: 848d075629f9
Revises: e10e8ef53ffe
Create Date: 2021-12-03 19:22:35.569733

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '848d075629f9'
down_revision = 'e10e8ef53ffe'
branch_labels = None
depends_on = None


def upgrade():
    op.create_table('users',
        sa.Column('id', sa.Integer(), nullable=False),
        sa.Column('email',sa.String(), nullable=False),
        sa.Column('password', sa.String(), nullable=False),
        sa.Column('created_at',sa.TIMESTAMP(timezone=True),nullable=False,server_default=sa.text('now()')),
        sa.PrimaryKeyConstraint('id'),
        sa.UniqueConstraint('email')
    )
    pass


def downgrade():
    op.drop_table('users')
    pass

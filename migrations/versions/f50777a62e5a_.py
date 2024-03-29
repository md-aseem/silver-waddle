"""empty message

Revision ID: f50777a62e5a
Revises: a0786f08774a
Create Date: 2024-02-01 16:39:49.466688

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'f50777a62e5a'
down_revision = 'a0786f08774a'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('users', schema=None) as batch_op:
        batch_op.add_column(sa.Column('file_path', sa.String(), server_default='', nullable=False))
        batch_op.add_column(sa.Column('word_count', sa.Integer(), server_default='0', nullable=False))

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('users', schema=None) as batch_op:
        batch_op.drop_column('word_count')
        batch_op.drop_column('file_path')

    # ### end Alembic commands ###

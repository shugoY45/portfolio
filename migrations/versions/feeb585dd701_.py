"""empty message

Revision ID: feeb585dd701
Revises: dd6e0664ad5f
Create Date: 2020-11-13 14:42:10.747055

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'feeb585dd701'
down_revision = 'dd6e0664ad5f'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('shiftconfig',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('store_opentime', sa.Time(), nullable=True),
    sa.Column('store_closetime', sa.Time(), nullable=True),
    sa.Column('job_divtime', sa.Time(), nullable=True),
    sa.Column('min_shift', sa.Time(), nullable=True),
    sa.Column('restnd_mint', sa.Time(), nullable=True),
    sa.Column('resttime', sa.Time(), nullable=True),
    sa.Column('restname', sa.String(), nullable=True),
    sa.Column('priorty_max', sa.Integer(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('shiftconfig')
    # ### end Alembic commands ###

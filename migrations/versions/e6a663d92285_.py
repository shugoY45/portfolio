"""empty message

Revision ID: e6a663d92285
Revises: 9c43f5a897fd
Create Date: 2020-11-26 14:36:33.092406

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'e6a663d92285'
down_revision = '9c43f5a897fd'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('job', sa.Column('priority', sa.Integer(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('job', 'priority')
    # ### end Alembic commands ###

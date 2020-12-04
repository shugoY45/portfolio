"""empty message

Revision ID: aa45826090e0
Revises: 3154acdeaeb7
Create Date: 2020-12-04 14:41:09.921202

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'aa45826090e0'
down_revision = '3154acdeaeb7'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('shift', sa.Column('be_indispensable', sa.Boolean(), nullable=True))
    op.add_column('shift', sa.Column('employee_priority', sa.String(length=3), nullable=True))
    op.add_column('shift', sa.Column('helper_priority', sa.String(length=3), nullable=True))
    op.add_column('shift', sa.Column('parttime_priority', sa.String(length=3), nullable=True))
    op.add_column('shift', sa.Column('position', sa.String(length=20), nullable=True))
    op.add_column('shift', sa.Column('priority', sa.String(length=3), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('shift', 'priority')
    op.drop_column('shift', 'position')
    op.drop_column('shift', 'parttime_priority')
    op.drop_column('shift', 'helper_priority')
    op.drop_column('shift', 'employee_priority')
    op.drop_column('shift', 'be_indispensable')
    # ### end Alembic commands ###
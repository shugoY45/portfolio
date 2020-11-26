"""empty message

Revision ID: bf04a865d47b
Revises: e6a663d92285
Create Date: 2020-11-26 14:40:04.661565

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'bf04a865d47b'
down_revision = 'e6a663d92285'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('job', sa.Column('employee_priority2', sa.Integer(), nullable=True))
    op.add_column('job', sa.Column('helper_priority2', sa.Integer(), nullable=True))
    op.add_column('job', sa.Column('parttime_priority2', sa.Integer(), nullable=True))
    op.add_column('job', sa.Column('priority3', sa.String(length=3), nullable=True))
    op.add_column('job', sa.Column('weight2', sa.Integer(), nullable=True))
    op.drop_column('job', 'employee_priority')
    op.drop_column('job', 'weight')
    op.drop_column('job', 'helper_priority')
    op.drop_column('job', 'priority')
    op.drop_column('job', 'parttime_priority')
    op.drop_column('job', 'priority2')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('job', sa.Column('priority2', sa.VARCHAR(length=3), autoincrement=False, nullable=True))
    op.add_column('job', sa.Column('parttime_priority', sa.INTEGER(), autoincrement=False, nullable=True))
    op.add_column('job', sa.Column('priority', sa.INTEGER(), autoincrement=False, nullable=True))
    op.add_column('job', sa.Column('helper_priority', sa.INTEGER(), autoincrement=False, nullable=True))
    op.add_column('job', sa.Column('weight', sa.INTEGER(), autoincrement=False, nullable=True))
    op.add_column('job', sa.Column('employee_priority', sa.INTEGER(), autoincrement=False, nullable=True))
    op.drop_column('job', 'weight2')
    op.drop_column('job', 'priority3')
    op.drop_column('job', 'parttime_priority2')
    op.drop_column('job', 'helper_priority2')
    op.drop_column('job', 'employee_priority2')
    # ### end Alembic commands ###

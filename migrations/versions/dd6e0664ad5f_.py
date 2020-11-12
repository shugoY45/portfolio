"""empty message

Revision ID: dd6e0664ad5f
Revises: ec38fcc474a9
Create Date: 2020-11-10 14:59:24.496404

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'dd6e0664ad5f'
down_revision = 'ec38fcc474a9'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('shift',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('one_date', sa.DateTime(), nullable=False),
    sa.Column('workername', sa.String(length=20), nullable=False),
    sa.Column('jobname', sa.String(length=20), nullable=False),
    sa.Column('starttime', sa.DateTime(), nullable=True),
    sa.Column('endtime', sa.DateTime(), nullable=True),
    sa.Column('jobweight', sa.Integer(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('shift')
    # ### end Alembic commands ###
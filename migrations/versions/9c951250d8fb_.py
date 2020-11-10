"""empty message

Revision ID: 9c951250d8fb
Revises: f4baf5d1649e
Create Date: 2020-11-09 15:15:09.721952

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '9c951250d8fb'
down_revision = 'f4baf5d1649e'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('worker', sa.Column('fri', sa.Boolean(), nullable=True))
    op.add_column('worker', sa.Column('friendtime', sa.Time(), nullable=True))
    op.add_column('worker', sa.Column('fristarttime', sa.Time(), nullable=True))
    op.add_column('worker', sa.Column('mon', sa.Boolean(), nullable=True))
    op.add_column('worker', sa.Column('monendtime', sa.Time(), nullable=True))
    op.add_column('worker', sa.Column('monstarttime', sa.Time(), nullable=True))
    op.add_column('worker', sa.Column('sat', sa.Boolean(), nullable=True))
    op.add_column('worker', sa.Column('satendtime', sa.Time(), nullable=True))
    op.add_column('worker', sa.Column('satstarttime', sa.Time(), nullable=True))
    op.add_column('worker', sa.Column('sun', sa.Boolean(), nullable=True))
    op.add_column('worker', sa.Column('sunendtime', sa.Time(), nullable=True))
    op.add_column('worker', sa.Column('sunstarttime', sa.Time(), nullable=True))
    op.add_column('worker', sa.Column('thu', sa.Boolean(), nullable=True))
    op.add_column('worker', sa.Column('thuendtime', sa.Time(), nullable=True))
    op.add_column('worker', sa.Column('thustarttime', sa.Time(), nullable=True))
    op.add_column('worker', sa.Column('tue', sa.Boolean(), nullable=True))
    op.add_column('worker', sa.Column('tueendtime', sa.Time(), nullable=True))
    op.add_column('worker', sa.Column('tuestarttime', sa.Time(), nullable=True))
    op.add_column('worker', sa.Column('wed', sa.Boolean(), nullable=True))
    op.add_column('worker', sa.Column('wedendtime', sa.Time(), nullable=True))
    op.add_column('worker', sa.Column('wedstarttime', sa.Time(), nullable=True))
    op.drop_column('worker', 'Monendtime')
    op.drop_column('worker', 'Satendtime')
    op.drop_column('worker', 'Sun')
    op.drop_column('worker', 'Wed')
    op.drop_column('worker', 'Sunstarttime')
    op.drop_column('worker', 'Tueendtime')
    op.drop_column('worker', 'Wedendtime')
    op.drop_column('worker', 'Tue')
    op.drop_column('worker', 'Friendtime')
    op.drop_column('worker', 'Thuendtime')
    op.drop_column('worker', 'Monstarttime')
    op.drop_column('worker', 'Mon')
    op.drop_column('worker', 'Sat')
    op.drop_column('worker', 'Satstarttime')
    op.drop_column('worker', 'Thu')
    op.drop_column('worker', 'Thustarttime')
    op.drop_column('worker', 'Wedstarttime')
    op.drop_column('worker', 'Sunendtime')
    op.drop_column('worker', 'Tuestarttime')
    op.drop_column('worker', 'Fristarttime')
    op.drop_column('worker', 'Fri')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('worker', sa.Column('Fri', sa.BOOLEAN(), autoincrement=False, nullable=True))
    op.add_column('worker', sa.Column('Fristarttime', sa.VARCHAR(length=10), autoincrement=False, nullable=True))
    op.add_column('worker', sa.Column('Tuestarttime', sa.VARCHAR(length=10), autoincrement=False, nullable=True))
    op.add_column('worker', sa.Column('Sunendtime', sa.VARCHAR(length=10), autoincrement=False, nullable=True))
    op.add_column('worker', sa.Column('Wedstarttime', sa.VARCHAR(length=10), autoincrement=False, nullable=True))
    op.add_column('worker', sa.Column('Thustarttime', sa.VARCHAR(length=10), autoincrement=False, nullable=True))
    op.add_column('worker', sa.Column('Thu', sa.BOOLEAN(), autoincrement=False, nullable=True))
    op.add_column('worker', sa.Column('Satstarttime', sa.VARCHAR(length=10), autoincrement=False, nullable=True))
    op.add_column('worker', sa.Column('Sat', sa.BOOLEAN(), autoincrement=False, nullable=True))
    op.add_column('worker', sa.Column('Mon', sa.BOOLEAN(), autoincrement=False, nullable=True))
    op.add_column('worker', sa.Column('Monstarttime', sa.VARCHAR(length=10), autoincrement=False, nullable=True))
    op.add_column('worker', sa.Column('Thuendtime', sa.VARCHAR(length=10), autoincrement=False, nullable=True))
    op.add_column('worker', sa.Column('Friendtime', sa.VARCHAR(length=10), autoincrement=False, nullable=True))
    op.add_column('worker', sa.Column('Tue', sa.BOOLEAN(), autoincrement=False, nullable=True))
    op.add_column('worker', sa.Column('Wedendtime', sa.VARCHAR(length=10), autoincrement=False, nullable=True))
    op.add_column('worker', sa.Column('Tueendtime', sa.VARCHAR(length=10), autoincrement=False, nullable=True))
    op.add_column('worker', sa.Column('Sunstarttime', sa.VARCHAR(length=10), autoincrement=False, nullable=True))
    op.add_column('worker', sa.Column('Wed', sa.BOOLEAN(), autoincrement=False, nullable=True))
    op.add_column('worker', sa.Column('Sun', sa.BOOLEAN(), autoincrement=False, nullable=True))
    op.add_column('worker', sa.Column('Satendtime', sa.VARCHAR(length=10), autoincrement=False, nullable=True))
    op.add_column('worker', sa.Column('Monendtime', sa.VARCHAR(length=10), autoincrement=False, nullable=True))
    op.drop_column('worker', 'wedstarttime')
    op.drop_column('worker', 'wedendtime')
    op.drop_column('worker', 'wed')
    op.drop_column('worker', 'tuestarttime')
    op.drop_column('worker', 'tueendtime')
    op.drop_column('worker', 'tue')
    op.drop_column('worker', 'thustarttime')
    op.drop_column('worker', 'thuendtime')
    op.drop_column('worker', 'thu')
    op.drop_column('worker', 'sunstarttime')
    op.drop_column('worker', 'sunendtime')
    op.drop_column('worker', 'sun')
    op.drop_column('worker', 'satstarttime')
    op.drop_column('worker', 'satendtime')
    op.drop_column('worker', 'sat')
    op.drop_column('worker', 'monstarttime')
    op.drop_column('worker', 'monendtime')
    op.drop_column('worker', 'mon')
    op.drop_column('worker', 'fristarttime')
    op.drop_column('worker', 'friendtime')
    op.drop_column('worker', 'fri')
    # ### end Alembic commands ###
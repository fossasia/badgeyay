"""empty message

Revision ID: b6414a3cd355
Revises: 90bcaf09b4eb
Create Date: 2018-07-19 22:02:35.118302

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'b6414a3cd355'
down_revision = '90bcaf09b4eb'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('Badges', sa.Column('deleted_at', sa.DateTime(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('Badges', 'deleted_at')
    # ### end Alembic commands ###
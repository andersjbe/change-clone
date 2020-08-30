"""create_petition

Revision ID: a90c7ca129ac
Revises: 167c529ab94f
Create Date: 2020-08-30 13:19:20.141981

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'a90c7ca129ac'
down_revision = '167c529ab94f'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('petitions',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('image_url', sa.String(), nullable=True),
    sa.Column('header', sa.String(length=100), nullable=False),
    sa.Column('description', sa.String(length=2000), nullable=False),
    sa.Column('goal', sa.Integer(), nullable=False),
    sa.Column('current', sa.Integer(), nullable=True),
    sa.Column('creator_id', sa.Integer(), nullable=False),
    sa.Column('topic_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['creator_id'], ['users.id'], ),
    sa.ForeignKeyConstraint(['topic_id'], ['topics.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('petitions')
    # ### end Alembic commands ###

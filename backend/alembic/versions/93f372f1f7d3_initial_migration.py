"""Initial migration

Revision ID: 93f372f1f7d3
Revises: 
Create Date: 2025-07-06 23:00:00.000000

"""

from alembic import op
import sqlalchemy as sa

# revision identifiers, used by Alembic.
revision = '93f372f1f7d3'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        'issues',
        sa.Column('id', sa.Integer(), primary_key=True),
        sa.Column('title', sa.String(), nullable=True),
        # add more columns here if your models have them
    )
    op.create_index(op.f('ix_issues_id'), 'issues', ['id'], unique=False)


def downgrade():
    op.drop_index(op.f('ix_issues_id'), table_name='issues')
    op.drop_table('issues')

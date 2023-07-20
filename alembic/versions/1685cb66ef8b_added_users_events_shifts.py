"""Added Users, Events, Shifts

Revision ID: 1685cb66ef8b
Revises: 
Create Date: 2023-07-20 15:24:55.282124

"""
from alembic import op
import sqlalchemy as sa
import fastapi_utils


# revision identifiers, used by Alembic.
revision = '1685cb66ef8b'
down_revision = None
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.create_table('users',
        sa.Column('id', fastapi_utils.guid_type.GUID(), nullable=False),
        sa.Column('firstname', sa.String(), nullable=False),
        sa.Column('middlename', sa.String(), nullable=False),
        sa.Column('lastname', sa.String(), nullable=False),
        sa.PrimaryKeyConstraint('id')
    )
    op.create_table('shifts',
        sa.Column('id', fastapi_utils.guid_type.GUID(), nullable=False),
        sa.Column('user_id', fastapi_utils.guid_type.GUID(), nullable=True),
        sa.Column('starts_at', sa.DateTime(timezone=True), nullable=False),
        sa.Column('ends_at', sa.DateTime(timezone=True), nullable=False),
        sa.Column('work_time', sa.Interval(), nullable=False),
        sa.ForeignKeyConstraint(['user_id'], ['users.id'], name='fk_shifts__user_id', onupdate='CASCADE', ondelete='CASCADE'),
        sa.PrimaryKeyConstraint('id')
    )
    op.create_table('events',
        sa.Column('id', fastapi_utils.guid_type.GUID(), nullable=False),
        sa.Column('user_id', fastapi_utils.guid_type.GUID(), nullable=False),
        sa.Column('shift_id', fastapi_utils.guid_type.GUID(), nullable=True),
        sa.Column('in_shift', sa.Boolean(), nullable=False),
        sa.Column('is_work', sa.Boolean(), nullable=False),
        sa.Column('starts_at', sa.DateTime(timezone=True), nullable=False),
        sa.Column('ends_at', sa.DateTime(timezone=True), nullable=False),
        sa.ForeignKeyConstraint(['shift_id'], ['shifts.id'], name='fk_events__shift_id', onupdate='CASCADE', ondelete='CASCADE'),
        sa.ForeignKeyConstraint(['user_id'], ['users.id'], name='fk_events__user_id', onupdate='CASCADE', ondelete='CASCADE'),
        sa.PrimaryKeyConstraint('id')
    )


def downgrade() -> None:
    op.drop_table('events')
    op.drop_table('shifts')
    op.drop_table('users')

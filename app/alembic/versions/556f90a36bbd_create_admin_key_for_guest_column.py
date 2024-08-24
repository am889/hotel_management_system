"""create admin key for guest column

Revision ID: 556f90a36bbd
Revises: 
Create Date: 2024-07-23 17:44:27.710033

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '556f90a36bbd'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.add_column('guests',sa.Column('emergency_name',sa.String(),nullable=True))
    op.add_column('guests',sa.Column('admin_id',sa.Integer(),nullable=True))
def downgrade() -> None:
    pass

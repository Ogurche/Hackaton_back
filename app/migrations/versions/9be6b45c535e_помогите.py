"""помогите

Revision ID: 9be6b45c535e
Revises: 1e06fcab1f38
Create Date: 2023-09-18 22:51:08.195547

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '9be6b45c535e'
down_revision: Union[str, None] = '1e06fcab1f38'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass

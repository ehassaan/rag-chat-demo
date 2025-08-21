"""added timestamp columns

Revision ID: 24daf5188ab8
Revises: 23b06f3e7ebe
Create Date: 2025-08-21 20:02:37.842815

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa
import sqlmodel


# revision identifiers, used by Alembic.
revision: str = '24daf5188ab8'
down_revision: Union[str, None] = '23b06f3e7ebe'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass

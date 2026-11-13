"""Reference migration for bonus 2; intentionally not run by Alembic.

This file stays outside ``alembic/versions`` and shows how to rename a column
without replacing it and losing the values stored in it.
"""

from alembic import op


def upgrade() -> None:
    """Rename description to summary while preserving every value."""
    op.alter_column(
        "courses",
        "description",
        new_column_name="summary",
    )


def downgrade() -> None:
    """Restore the original column name without recreating the column."""
    op.alter_column(
        "courses",
        "summary",
        new_column_name="description",
    )

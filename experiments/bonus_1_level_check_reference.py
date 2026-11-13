"""Reference migration for bonus 1; intentionally not run by Alembic.

This file stays outside ``alembic/versions`` so it cannot change the real
migration chain. It demonstrates the manual CHECK migration from the lab.
"""

from alembic import op


def upgrade() -> None:
    """Allow only the three course levels used by the application."""
    op.create_check_constraint(
        op.f("courses_level_check"),
        "courses",
        "level IN ('beginner', 'intermediate', 'advanced')",
    )


def downgrade() -> None:
    """Remove the level CHECK using its already formatted name."""
    op.drop_constraint(
        op.f("courses_level_check"),
        "courses",
        type_="check",
    )

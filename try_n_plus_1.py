from sqlalchemy import event, select
from sqlalchemy.orm import Session, selectinload

from db import engine
from models import Course


# Warm up the first connection so dialect service queries are not counted.
with engine.connect():
    pass

queries: list[str] = []


@event.listens_for(engine, "before_cursor_execute")
def count_query(conn, cursor, statement, parameters, context, executemany):
    queries.append(statement)


def count_enrollments(*options) -> int:
    queries.clear()
    with Session(engine) as session:
        courses = session.scalars(select(Course).options(*options)).all()
        return sum(len(course.enrollments) for course in courses)


variants = [
    ("lazy", []),
    ("selectinload", [selectinload(Course.enrollments)]),
]

for name, options in variants:
    total = count_enrollments(*options)
    print(f"{name:13} enrollments: {total}, queries: {len(queries)}")

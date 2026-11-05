from sqlalchemy import func, select
from sqlalchemy.orm import Session

from db import engine
from models import Enrollment, Student


def counts(session: Session) -> tuple[int, int]:
    students = session.scalar(select(func.count(Student.id)))
    enrollments = session.scalar(select(func.count(Enrollment.id)))
    assert students is not None and enrollments is not None
    return students, enrollments


with Session(engine) as session:
    before = counts(session)
    student = session.get(Student, 3)
    assert student is not None
    session.delete(student)
    session.flush()
    during = counts(session)
    session.rollback()

with Session(engine) as session:
    after = counts(session)

print("before delete:", before)
print("after flush with database cascade:", during)
print("after rollback:", after)

from sqlalchemy import update
from sqlalchemy.orm import Session

from db import engine
from models import Course


COURSE_ID = "api-design"


def likes_in_database() -> int:
    with Session(engine) as session:
        course = session.get(Course, COURSE_ID)
        assert course is not None
        return course.likes


def restore_likes(value: int) -> None:
    with Session(engine) as session:
        session.execute(
            update(Course).where(Course.id == COURSE_ID).values(likes=value)
        )
        session.commit()


initial = likes_in_database()

with Session(engine) as alice, Session(engine) as bob:
    a = alice.get(Course, COURSE_ID)
    b = bob.get(Course, COURSE_ID)
    assert a is not None and b is not None
    print("ordinary writes read", a.likes, "and", b.likes)
    a.likes += 1
    alice.commit()
    b.likes += 1
    bob.commit()

print("after two ordinary writes:", likes_in_database(), "(one update lost)")
restore_likes(initial)

with Session(engine) as alice, Session(engine) as bob:
    a = alice.get(Course, COURSE_ID)
    b = bob.get(Course, COURSE_ID)
    assert a is not None and b is not None
    a.likes = Course.likes + 1
    alice.commit()
    b.likes = Course.likes + 1
    bob.commit()

print("after two atomic writes:", likes_in_database(), "(both updates kept)")
restore_likes(initial)
print("restored initial value:", likes_in_database())

import random

from db import Session, engine
from faker import Faker
from models import Base, Grade, Group, Student, Subject, Teacher

fake = Faker()

Base.metadata.create_all(bind=engine)


def seed():
    with Session() as session:
        groups = [Group(name=f"Group {i}") for i in range(1, 4)]
        session.add_all(groups)

        teachers = [Teacher(full_name=fake.name()) for _ in range(5)]
        session.add_all(teachers)

        subjects = [
            Subject(name=fake.job(), teacher=random.choice(teachers)) for _ in range(7)
        ]
        session.add_all(subjects)

        students = [
            Student(full_name=fake.name(), group=random.choice(groups))
            for _ in range(40)
        ]
        session.add_all(students)
        session.commit()

        grades = []
        for student in students:
            for subject in subjects:
                for _ in range(random.randint(10, 20)):
                    grades.append(
                        Grade(
                            student=student,
                            subject=subject,
                            grade=round(random.uniform(60, 100), 2),
                            date_received=fake.date_between(
                                start_date="-6M", end_date="today"
                            ),
                        )
                    )
        session.add_all(grades)
        session.commit()


if __name__ == "__main__":
    seed()

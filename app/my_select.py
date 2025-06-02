from db import Session
from models import Grade, Group, Student, Subject
from sqlalchemy import Numeric, cast, func


# 1. Top 5 students with the highest average grade across all subjects
def select_1():
    with Session() as session:
        return (
            session.query(
                Student.full_name,
                func.round(cast(func.avg(Grade.grade), Numeric), 2).label("avg_grade"),
            )
            .join(Grade)
            .group_by(Student.id)
            .order_by(func.avg(Grade.grade).desc())
            .limit(5)
            .all()
        )


# 2. Student with the highest average grade for a given subject
def select_2(subject_id):
    with Session() as session:
        return (
            session.query(
                Student.full_name,
                func.round(cast(func.avg(Grade.grade), Numeric), 2).label("avg"),
            )
            .join(Grade)
            .filter(Grade.subject_id == subject_id)
            .group_by(Student.id)
            .order_by(func.avg(Grade.grade).desc())
            .first()
        )


# 3. Average grade in each group for a specific subject
def select_3(subject_id):
    with Session() as session:
        return (
            session.query(
                Group.name,
                func.round(cast(func.avg(Grade.grade), Numeric), 2).label("avg"),
            )
            .join(Student)
            .join(Group)
            .join(Grade)
            .filter(Grade.subject_id == subject_id)
            .group_by(Group.id)
            .all()
        )


# 4. Average grade across all students and subjects
def select_4():
    with Session() as session:
        return session.query(
            func.round(cast(func.avg(Grade.grade), Numeric), 2)
        ).scalar()


# 5. List of courses taught by a specific teacher
def select_5(teacher_id):
    with Session() as session:
        return (
            session.query(Subject.name).filter(Subject.teacher_id == teacher_id).all()
        )


# 6. List of students in a specific group
def select_6(group_id):
    with Session() as session:
        return (
            session.query(Student.full_name).filter(Student.group_id == group_id).all()
        )


# 7. Grades of students in a specific group and subject
def select_7(group_id, subject_id):
    with Session() as session:
        return (
            session.query(Student.full_name, Grade.grade)
            .join(Grade)
            .filter(Student.group_id == group_id, Grade.subject_id == subject_id)
            .all()
        )


# 8. Average grade given by a teacher across their subjects
def select_8(teacher_id):
    with Session() as session:
        return (
            session.query(func.round(cast(func.avg(Grade.grade), Numeric), 2))
            .join(Subject)
            .filter(Subject.teacher_id == teacher_id)
            .scalar()
        )


# 9. List of subjects a student attends
def select_9(student_id):
    with Session() as session:
        return (
            session.query(Subject.name)
            .join(Grade)
            .filter(Grade.student_id == student_id)
            .distinct()
            .all()
        )


# 10. Subjects a student attends taught by a specific teacher
def select_10(student_id, teacher_id):
    with Session() as session:
        return (
            session.query(Subject.name)
            .join(Grade)
            .filter(Grade.student_id == student_id, Subject.teacher_id == teacher_id)
            .distinct()
            .all()
        )


# 11. Average grade a teacher gives to a specific student (optional advanced)
def select_11(student_id, teacher_id):
    with Session() as session:
        return (
            session.query(func.round(cast(func.avg(Grade.grade), Numeric), 2))
            .join(Subject)
            .filter(Subject.teacher_id == teacher_id, Grade.student_id == student_id)
            .scalar()
        )


# 12. Grades of students in a group for a subject on the latest lesson
# date (optional advanced)
def select_12(group_id, subject_id):
    with Session() as session:
        latest_date = (
            session.query(func.max(Grade.date_received))
            .filter(Grade.subject_id == subject_id)
            .scalar()
        )

        return (
            session.query(Student.full_name, Grade.grade, Grade.date_received)
            .join(Grade)
            .filter(
                Student.group_id == group_id,
                Grade.subject_id == subject_id,
                Grade.date_received == latest_date,
            )
            .all()
        )

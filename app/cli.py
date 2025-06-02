import argparse

from colorama import Fore, init
from db import Session
from models import Group, Student, Subject, Teacher

init(autoreset=True)


def create_teacher(name):
    with Session() as session:
        t = Teacher(full_name=name)
        session.add(t)
        session.commit()
        print(Fore.GREEN + f"✔ Teacher '{name}' created.")


def list_teachers():
    with Session() as session:
        teachers = session.query(Teacher).all()
        if teachers:
            for t in teachers:
                print(Fore.CYAN + f"[ID {t.id}] {t.full_name}")
        else:
            print(Fore.YELLOW + "No teachers found.")


def update_teacher(t_id, name):
    with Session() as session:
        teacher = session.query(Teacher).filter_by(id=t_id).first()
        if teacher:
            teacher.full_name = name
            session.commit()
            print(Fore.GREEN + f"✔ Teacher ID {t_id} updated.")
        else:
            print(Fore.RED + f"✘ Teacher ID {t_id} not found.")


def remove_teacher(t_id):
    with Session() as session:
        teacher = session.query(Teacher).filter_by(id=t_id).first()
        if teacher:
            session.delete(teacher)
            session.commit()
            print(Fore.GREEN + f"✔ Teacher ID {t_id} removed.")
        else:
            print(Fore.RED + f"✘ Teacher ID {t_id} not found.")


def create_group(name):
    with Session() as session:
        g = Group(name=name)
        session.add(g)
        session.commit()
        print(Fore.GREEN + f"✔ Group '{name}' created.")


def list_groups():
    with Session() as session:
        groups = session.query(Group).all()
        if groups:
            for g in groups:
                print(Fore.CYAN + f"[ID {g.id}] {g.name}")
        else:
            print(Fore.YELLOW + "No groups found.")


def update_group(group_id, name):
    with Session() as session:
        group = session.query(Group).filter_by(id=group_id).first()
        if group:
            group.name = name
            session.commit()
            print(Fore.GREEN + f"✔ Group ID {group_id} updated.")
        else:
            print(Fore.RED + f"✘ Group ID {group_id} not found.")


def remove_group(group_id):
    with Session() as session:
        group = session.query(Group).filter_by(id=group_id).first()
        if group:
            session.delete(group)
            session.commit()
            print(Fore.GREEN + f"✔ Group ID {group_id} removed.")
        else:
            print(Fore.RED + f"✘ Group ID {group_id} not found.")


def create_student(name, group_id):
    with Session() as session:
        s = Student(full_name=name, group_id=group_id)
        session.add(s)
        session.commit()
        print(Fore.GREEN + f"✔ Student '{name}' created in group {group_id}.")


def list_students():
    with Session() as session:
        students = session.query(Student).all()
        if students:
            for s in students:
                print(
                    Fore.CYAN
                    + f"[ID {
                        s.id}] {
                        s.full_name} (Group {
                        s.group_id})"
                )
        else:
            print(Fore.YELLOW + "No students found.")


def update_student(student_id, name, group_id):
    with Session() as session:
        student = session.query(Student).filter_by(id=student_id).first()
        if student:
            student.full_name = name
            student.group_id = group_id
            session.commit()
            print(Fore.GREEN + f"✔ Student ID {student_id} updated.")
        else:
            print(Fore.RED + f"✘ Student ID {student_id} not found.")


def remove_student(student_id):
    with Session() as session:
        student = session.query(Student).filter_by(id=student_id).first()
        if student:
            session.delete(student)
            session.commit()
            print(Fore.GREEN + f"✔ Student ID {student_id} removed.")
        else:
            print(Fore.RED + f"✘ Student ID {student_id} not found.")


def create_subject(name, teacher_id):
    with Session() as session:
        s = Subject(name=name, teacher_id=teacher_id)
        session.add(s)
        session.commit()
        print(Fore.GREEN + f"✔ Subject '{name}' created with Teacher ID {teacher_id}.")


def list_subjects():
    with Session() as session:
        subjects = session.query(Subject).all()
        if subjects:
            for s in subjects:
                print(
                    Fore.CYAN
                    + f"[ID {
                        s.id}] {
                        s.name} (Teacher {
                        s.teacher_id})"
                )
        else:
            print(Fore.YELLOW + "No subjects found.")


def update_subject(subject_id, name, teacher_id):
    with Session() as session:
        subject = session.query(Subject).filter_by(id=subject_id).first()
        if subject:
            subject.name = name
            subject.teacher_id = teacher_id
            session.commit()
            print(Fore.GREEN + f"✔ Subject ID {subject_id} updated.")
        else:
            print(Fore.RED + f"✘ Subject ID {subject_id} not found.")


def remove_subject(subject_id):
    with Session() as session:
        subject = session.query(Subject).filter_by(id=subject_id).first()
        if subject:
            session.delete(subject)
            session.commit()
            print(Fore.GREEN + f"✔ Subject ID {subject_id} removed.")
        else:
            print(Fore.RED + f"✘ Subject ID {subject_id} not found.")


def handle_cli():
    parser = argparse.ArgumentParser()
    parser.add_argument("-a", "--action", required=True)
    parser.add_argument("-m", "--model", required=True)
    parser.add_argument("--id", type=int)
    parser.add_argument("-n", "--name")
    parser.add_argument("--group_id", type=int)
    parser.add_argument("--teacher_id", type=int)

    args = parser.parse_args()

    if args.model == "Teacher":
        if args.action == "create":
            create_teacher(args.name)
        elif args.action == "list":
            list_teachers()
        elif args.action == "update":
            update_teacher(args.id, args.name)
        elif args.action == "remove":
            remove_teacher(args.id)

    elif args.model == "Group":
        if args.action == "create":
            create_group(args.name)
        elif args.action == "list":
            list_groups()
        elif args.action == "update":
            update_group(args.id, args.name)
        elif args.action == "remove":
            remove_group(args.id)

    elif args.model == "Student":
        if args.action == "create":
            create_student(args.name, args.group_id)
        elif args.action == "list":
            list_students()
        elif args.action == "update":
            update_student(args.id, args.name, args.group_id)
        elif args.action == "remove":
            remove_student(args.id)

    elif args.model == "Subject":
        if args.action == "create":
            create_subject(args.name, args.teacher_id)
        elif args.action == "list":
            list_subjects()
        elif args.action == "update":
            update_subject(args.id, args.name, args.teacher_id)
        elif args.action == "remove":
            remove_subject(args.id)

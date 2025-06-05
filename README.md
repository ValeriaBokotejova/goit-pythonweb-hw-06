# goit-pythonweb-hw-06

# 📚 University Database CLI App

A simple command-line interface app to manage a university database — teachers, students, groups, subjects, and grades.

## 🚀 Features

- Manage entities: Teacher, Student, Group, Subject
- Generate fake data using `Faker`
- Run analytical SELECT queries with `argparse`
- Alembic migrations + PostgreSQL support

## 🛠️ Setup

```bash
# Create and activate venv
python3 -m venv venv
source venv/bin/activate

# Install requirements
pip install -r requirements.txt

# Run PostgreSQL via Docker
docker run --name university-db -e POSTGRES_PASSWORD=mypassword -p 5432:5432 -d postgres

# Run migrations
alembic upgrade head

# Seed DB with fake data
python app/seed.py

```

## 📊 Run Queries

```bash
# List available SELECT queries
python app/run_selects.py --list

# Example: top 5 students by average grade
python app/run_selects.py -n select_1
```

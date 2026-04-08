import sqlalchemy
from sqlalchemy import select
from sqlalchemy.orm import declarative_base, Session
from connector import connection_params

engine = sqlalchemy.create_engine(f"mariadb+mariadbconnector://{connection_params["user"]}:{connection_params["password"]}@{connection_params["host"]}/{connection_params["database"]}")

Base = declarative_base()

class Employee(Base):
    __tablename__ = 'employees'
    id = sqlalchemy.Column(sqlalchemy.Integer, primary_key=True)
    first_name = sqlalchemy.Column(sqlalchemy.String(length=100))
    last_name = sqlalchemy.Column(sqlalchemy.String(length=100))
    active = sqlalchemy.Column(sqlalchemy.Boolean, default=True)

# Base.metadata.create_all(engine)

session = Session(engine)

# newEmployee = Employee(first_name="Bob", last_name="Mortimor")
# session.add(newEmployee)
# session.commit()

statement = select(Employee)
for row in session.execute(statement).all():
    for data in row:
        print(f"{data.first_name} {data.last_name} {data.active} {data.id}")

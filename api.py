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


# newEmployee = Employee(first_name="Rob", last_name="Hedgpeth")
# session.add(newEmployee)
# session.commit()

statement = select(Employee).where(Employee.first_name == "Rob")
with Session(engine) as session:
    for row in session.execute(statement):
        print(row)

row = session.execute(select(Employee)).first()
print(row[0].first_name)
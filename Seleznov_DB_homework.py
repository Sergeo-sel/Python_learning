from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

Base = declarative_base()


class Car(Base):
    __tablename__ = 'car'

    car_id = Column(Integer, primary_key=True)
    reg_number = Column(String(50))
    model = Column(String(100))
    company_id = Column(Integer, ForeignKey('company.company_id'))


class Company(Base):
    __tablename__ = 'company'

    company_id = Column(Integer, primary_key=True)
    name = Column(String(50))
    address = Column(String(100))


DATABASE_URI = 'postgresql://{user}:{password}@{host}:{port}/{database}'


engine = create_engine(
    DATABASE_URI.format(
        host='localhost',
        database='postgres',
        user='postgres',
        password='3252',
        port=5432,
    )
)

Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)

session = Session()

added_companys: list[Company] = [
    Company(name='Liubava', address='Kyiv, Tiraspolska,54'),
    Company(name='First company', address='Kyiv, Lobanovska,54'),
    Company(name='Second company', address='Kyiv, Konstantinivsca,333')
]

added_cars: list[Car] = [
    Car(reg_number='AA 5566 ТО', model='Reno', company_id=1),
    Car(reg_number='AA 3333 Тk', model='Volvo', company_id=1),
    Car(reg_number='AA 4444 Тk', model='Volvo', company_id=2)
]

session.bulk_save_objects(added_companys)

session.bulk_save_objects(added_cars)

session.commit()

Liubava_cars = (
    session.query(Car.car_id, Car.model, Car.reg_number)
    .join(Company)
    .filter(Company.name == 'Liubava')).all()

print(Liubava_cars)

session.close()

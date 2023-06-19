from sqlalchemy import Column, Integer
from sqlalchemy.orm import relationship


from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()


class Bay(Base):
    __tablename__ = "bays"

    id = Column(Integer, primary_key=True, index=True)
    number = Column(Integer, unique=True, nullable=False)

    bookings = relationship("Booking", back_populates="bay")

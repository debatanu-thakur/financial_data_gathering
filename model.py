from sqlalchemy import Column, BigInteger, String, Numeric, PrimaryKeyConstraint, DateTime
from sqlalchemy.ext.declarative import declarative_base
from datetime import datetime

Base = declarative_base()

class Financial(Base):
    __tablename__ = "tbl.financials"

    symbol = Column(String(10), unique=False, nullable=False)
    date = Column(DateTime, unique=False, nullable=False, default=datetime.utcnow)
    open_price = Column(Numeric(precision=10, scale=2), nullable=False)
    close_price = Column(Numeric(precision=10, scale=2), nullable=False)
    volume = Column(BigInteger, nullable=False)
    
    __table_args__ = (
            PrimaryKeyConstraint('symbol', 'date'),
        )

    def __repr__(self):
        return f'<Daily sold {self.volume} for {self.symbol} on {self.date} with open price {self.open_price} and closed price {self.close_price}>'

    def __init__(self, symbol, date, open_price, close_price, volume):
        self.symbol = symbol
        self.date = date
        self.open_price = open_price
        self.close_price = close_price
        self.volume = volume


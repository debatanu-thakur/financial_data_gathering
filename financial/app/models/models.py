from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

db = SQLAlchemy()

class Financial(db.Model):
    __tablename__ = "tbl.financials"

    symbol = db.Column(db.String(10), unique=False, nullable=False)
    date = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    open_price = db.Column(db.Numeric(precision=10, scale=2), nullable=False)
    close_price = db.Column(db.Numeric(precision=10, scale=2), nullable=False)
    volume = db.Column(db.BigInteger, nullable=False)
    
    __table_args__ = (
            db.PrimaryKeyConstraint('symbol', 'date'),
        )

    def __repr__(self):
        return f'<Daily sold {self.volume} for {self.symbol} on {self.date} with open price {self.open_price} and closed price {self.close_price}>'

    def __init__(self, symbol, date, open_price, close_price, volume):
        self.symbol = symbol
        self.date = date
        self.open_price = open_price
        self.close_price = close_price
        self.volume = volume


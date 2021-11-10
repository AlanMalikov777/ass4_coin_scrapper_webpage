from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Data(Base):
    __tablename__ = 'news'
    news_id = Column(Integer(), primary_key=True)
    news_text = Column(String())
    def toJSON(self):       
        json = {
            "news_id":self.news_id,
            "news_text":self.news_text
        }

        return json
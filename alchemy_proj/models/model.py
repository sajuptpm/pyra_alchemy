from sqlalchemy import (
    Column,
    Integer,
    Text,
    String
    )

from alchemy_proj.models import (
    DBSession,
    Base,
    )

##SM:We should import all Model classes into scripts/initializedb.py
##SM:So we can update DB with command #initialize_alchemy_proj_db development.ini
class MyModel(Base):
    __tablename__ = 'models'
    id = Column(Integer, primary_key=True)
    #name = Column(Text, unique=True)
    name = Column(String(255), unique=True)
    value = Column(Integer)

    def __init__(self, name=None, value=None):
        self.name = name
        self.value = value

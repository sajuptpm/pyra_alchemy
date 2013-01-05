
from datetime import datetime

from sqlalchemy import (
    Column,
    Integer,
    Text,
    String,
    Unicode,
    Sequence,
    Boolean,
    DateTime,
    )

from alchemy_proj.models import (
    DBSession,
    Base,
    )


##SM:We should import all Model classes into scripts/initializedb.py
##SM:So we can update DB with command #initialize_alchemy_proj_db development.ini
class User(Base):
    """
    
    """
    __tablename__ = 'users'
    user_id = Column(Integer, Sequence('user_id_seq'), primary_key=True)
    firstname=Column(Unicode(50), nullable=False)
    lastname=Column(Unicode(50), nullable=False)
    phone_number=Column(Unicode(20))
    status=Column(Boolean, default=True)
    user_name = Column(Unicode(255), unique=True, nullable=False)    
    email_address = Column(Unicode(255), unique=True, nullable=False,
                           info={'rum': {'field':'Email'}})
    display_name = Column(Unicode(255))  
    _password = Column('password', Unicode(80),
                       info={'rum': {'field':'Password'}})    
    created_by=Column(Unicode(255))
    created_date = Column(DateTime)
    modified_by=Column(Unicode(255))
    modified_date= Column(DateTime, default=datetime.now)
    type=Column(Unicode(50))

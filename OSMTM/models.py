import transaction

from sqlalchemy import Column
from sqlalchemy import Integer
from sqlalchemy import Unicode
from sqlalchemy import Table
from sqlalchemy import Column
from sqlalchemy import ForeignKey

from sqlalchemy.exc import IntegrityError
from sqlalchemy.ext.declarative import declarative_base

from sqlalchemy.orm import scoped_session
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import relationship

from zope.sqlalchemy import ZopeTransactionExtension

DBSession = scoped_session(sessionmaker(extension=ZopeTransactionExtension()))
Base = declarative_base()

class Tile(Base):
    __tablename__ = "tiles"
    id = Column(Integer, primary_key=True)
    x = Column(Integer)
    y = Column(Integer)

    def __init__(self, x, y):
        self.x = x
        self.y = y

job_tiles = Table('job_tiles', Base.metadata,
    Column('job_id', Integer, ForeignKey('jobs.id')),
    Column('tile_id', Integer, ForeignKey('tiles.id'))
)

class Job(Base):
    """ The SQLAlchemy declarative model class for a Page object. """
    __tablename__ = 'jobs'
    id = Column(Integer, primary_key=True)
    title = Column(Unicode, unique=True)
    description = Column(Unicode)
    geometry = Column(Unicode)
    workflow = Column(Unicode)
    zoom = Column(Integer)
    tiles = relationship(Tile, secondary=job_tiles)

    def __init__(self, title=None, description=None, geometry=None, workflow=None, zoom=None):
        self.title = title
        self.descript = description
        self.geometry = geometry
        self.workflow = workflow
        self.zoom = zoom

class User(Base):
    __tablename__ = "users"
    username = Column(Unicode, primary_key=True)
    role = Column(Integer) # 0 - newbie, 1 - advanced, 2 - admin

    def __init__(self, username, role=0):
        self.username = username

def populate():
    session = DBSession()
    job = Job(u'Sendai Quake, Spot Imagery Tracing',
            u'A short description',
            'POLYGON((15682967.276231 4613965.847168, 15683464.116915 4611581.6652221, 15686330.505475 4612019.5348445, 15687247.749814 4613868.5228206, 15686330.505475 4616058.5430414, 15685260.387079 4615961.1989223, 15682967.276231 4613965.847168))',
            u'Trace buildings from satellite imagery, Survey buildings to create attribute information, Enter survey information, Quality Assurance Check by Work Lead',
            12)
    session.add(job)
    user = User(u'pgiraud')
    user.role = 2
    session.add(user)
    user = User(u'vdb')
    user.role = 2
    session.add(user)
    user = User(u'wonderchook')
    user.role = 2
    session.add(user)
    session.flush()
    transaction.commit()
    
def initialize_sql(engine):
    DBSession.configure(bind=engine)
    Base.metadata.bind = engine
    Base.metadata.create_all(engine)
    try:
        populate()
    except IntegrityError:
        # already created
        pass

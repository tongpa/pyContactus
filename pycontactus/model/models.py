from sqlalchemy import Table, ForeignKey, Column, and_, func,sql
from sqlalchemy.types import Unicode,   DateTime, Date, Integer, String, Text,Boolean,BigInteger,SmallInteger,CHAR,TIMESTAMP
from sqlalchemy.orm import backref, relation

from pycontactus.model import DeclarativeBase
from tgext.pluggable import app_model, primary_key
from datetime import datetime
from sqlalchemy.dialects.mysql import BIT
from surveymodel import DeclarativeBase, metadata, DBSession
from surveyobject.mastermodel import MasterBase
from surveymodel.voter import Telephone

__all__ = ['DetailReport', 'DetailReportType']

class DetailReport(MasterBase, DeclarativeBase):   
    __tablename__ = 'cts_detail_report'

    id_detail_report = Column(BigInteger, autoincrement=True, primary_key=True)
    
    id_detail_report_type = Column( BigInteger,ForeignKey('cts_detail_report_type.id_detail_report_type'), nullable=False, index=True) ;
    detail_report_type = relation('DetailReportType', backref='cts_detail_report_id_detail_report_type');
    
    user_id  = Column( BigInteger,ForeignKey('tg_user.user_id'), nullable=True, index=True) ;
    user = relation('User', backref='cts_detail_report_user_id');
    
    telephone_number = Column(String(255), nullable=True);    
    reporter  = Column(String(255), nullable=True);
    email  = Column(String(255), nullable=True);
    message  = Column(Text, nullable=True);
   
    active = Column(BIT, nullable=True, default=1);
    
    create_date = Column(DateTime, default=datetime.now)
    update_date = Column(DateTime ,onupdate=sql.func.utc_timestamp())
    
    
    def __init__(self, id_detail_report =None, id_detail_report_type=None, user_id=None ,telephone_number=None, reporter=None, email=None, message=None, create_date=None, update_date=None, active=1):
        super(DetailReport, self).__init__(DBSession) 
        
        self.id_detail_report =id_detail_report
        self.id_detail_report_type=id_detail_report_type
        self.user_id=user_id
        self.telephone_number=telephone_number
        self.reporter=reporter
        self.email=email
        self.message=message
        
        self.active=active
        
 
      
        
    def __str__(self):
        return '<DetailReport : id_detail_report = %s, email=%s>' % (self.id_detail_report, self.email )    
    
    @classmethod  
    def getAll(cls, act= 1):
        return DBSession.query(cls).filter(cls.active == str(act).decode('utf-8')).all();    
    
    @classmethod  
    def getById(cls,id_detail_report=0, act=1):
        return DBSession.query(cls).filter(cls.id_detail_report == str(id_detail_report),cls.active == str(act)).first();

class DetailReportType(MasterBase, DeclarativeBase):   
    __tablename__ = 'cts_detail_report_type'

    id_detail_report_type = Column(BigInteger, autoincrement=True, primary_key=True)
    
    description = Column(String(255),unique=True, nullable=False)
    
    active = Column(BIT, nullable=True, default=1);
    
    create_date = Column(DateTime, default=datetime.now)
    update_date = Column(DateTime ,onupdate=sql.func.utc_timestamp())
    
    def __init__(self):
        super(DetailReportType, self).__init__(DBSession) 
        self.active = 1;
        self.create_date =  datetime.now();
    
    def __str__(self):
        return '<DetailReportType : id_detail_report_type = %s, description=%s>' % (self.id_detail_report_type, self.description )
    
    @classmethod  
    def getAll(cls, act= 1):
        return DBSession.query(cls).filter(cls.active == str(act).decode('utf-8')).all();
    
    
    
    
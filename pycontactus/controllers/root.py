# -*- coding: utf-8 -*-
"""Main Controller"""

from tg import TGController
from tg import expose, flash, require, url, lurl, request, redirect, validate
from tg.i18n import ugettext as _

from tgext.pylogservice import LogDBHandler
from tgext.pyutilservice import ManageSession, Utility, extraLog

from tg.configuration import AppConfig, config
from tg.controllers.util import auth_force_logout
from surveyobject.languageobject import LanguageObject
from surveyobject import JsontoObject

from pycontactus import model
from pycontactus.model import DBSession
import sys
import json

import logging;
log = logging.getLogger(__name__);
__all__ = ['RootController']

class RootController(TGController):
    
    def __init__(self):
        
        dh = LogDBHandler( config=config,request=request);        
        log.addHandler(dh)
        
    @expose('pycontactus.templates.index')
    def index(self, failure=None,came_from=lurl('/')):
        reload(sys).setdefaultencoding('utf8')
        self.email=''
        self.reporter=''
        if request.identity:           
            user=request.identity['user']; 
            self.email=user.email_address 
            self.reporter=user.display_name
        self.report_type=[]     
        self.report_type = model.DetailReportType.getAll(1)
        return dict(page='contactus', 
                    reporttype=self.report_type, 
                    email_address=self.email, 
                    reporter=self.reporter)
    
    def __toContactUs(self,dic):   
        self.ContactUs = model.DetailReport();
        self.ContactUs.id_detail_report_type = dic.get('id_detail_report_type')       
        self.ContactUs.reporter = dic.get('reporter')
        self.ContactUs.email = dic.get('email')
        self.ContactUs.message = dic.get('message')
        self.ContactUs.telephone_number = dic.get('telephone')
                
        return self.ContactUs
    
    @expose('json')
    def addContactUs(self,  **kw):
        reload(sys).setdefaultencoding('utf8')     
        self.userid=None 
        self.ContactUs = json.loads(request.body, encoding=request.charset, object_hook=self.__toContactUs)
        log.info(request.body, extra=extraLog())
        
        if request.identity:
            user=request.identity['user']; 
            self.ContactUs.user_id=user.user_id
            self.ContactUs.reporter=user.display_name
            self.ContactUs.email=user.user_name
            
        self.ContactUs.save()
        return dict(status=True,header = "Information" ,  message= LanguageObject.getdata(key="msg_save_success_contactus", code=True) )    

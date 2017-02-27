# -*- coding: utf-8 -*-
"""Main Controller"""

from tg import TGController
from tg import expose, flash, require, url, lurl, request, redirect, validate
from tg.i18n import ugettext as _


from tgext.pylogservice import LogDBHandler
from tgext.pyutilservice import ManageSession, Utility, extraLog

from tg.configuration import AppConfig, config
from tg.controllers.util import auth_force_logout


from pycontactus import model
from pycontactus.model import DBSession
import sys
import json

from manage import ManageControllers
import logging;
log = logging.getLogger(__name__);
__all__ = ['RootController']

class RootController(TGController):
    
    def __init__(self):
        self.manage = ManageControllers();
        
        
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
        return dict(page='contactus', reporttype=self.report_type, email_address=self.email, reporter=self.reporter)
 
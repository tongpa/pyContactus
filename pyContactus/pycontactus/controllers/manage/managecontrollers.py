# -*- coding: utf-8 -*-
"""Main Controller"""

from tg import TGController
from tg import expose, flash, require, url, lurl, request, redirect, validate
from tg.i18n import ugettext as _

from surveyobject.languageobject import LanguageObject

from pycontactus import model
from pycontactus.model import DBSession
import sys
import json

__all__ = ['ManageControllers']

class ManageControllers(TGController):
    
   
    @expose('json')
    def AddContactUs(self, **kw):
        reload(sys).setdefaultencoding('utf8') 
               
        self.ContactUs = model.DetailReport();
        self.ContactUs.id_detail_report_type = 1
        self.ContactUs.email = kw['email']
        self.ContactUs.message = kw['message']
        self.ContactUs.save()
        if self.ContactUs :
            flash(_(LanguageObject.getdata("msg_save_success")), 'warning')             
        else :
            flash(_(LanguageObject.getdata("female")), 'warning') 
        redirect('/contactus')
        

        
      
# -*- coding: utf-8 -*-
"""Main Controller"""

from tg import TGController
from tg import expose, flash, require, url, lurl, request, redirect, validate
from tg.i18n import ugettext as _

from pycontactus import model
from pycontactus.model import DBSession
import sys
import json

__all__ = ['ManageControllers']

class ManageControllers(TGController):
    
   
    @expose()
    def AddContactUs(self, **kw):
        reload(sys).setdefaultencoding('utf8') 
        self.success = True
        try :
            self.ContactUs = model.DetailReport();
            self.ContactUs.id_detail_report_type = 1
            self.ContactUs.email = kw['email']
            self.ContactUs.message = kw['message']
            self.ContactUs.save()
            if self.ContactUs :
                self.result = True
                self.message = 'Add Contact Us Success.'
        except Exception as e:
            self.result =False;
            self.message = '' + str(e); 
        return dict(success=self.success, result=self.result, message=self.message)

        
      
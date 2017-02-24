# -*- coding: utf-8 -*-
"""Main Controller"""

from tg import TGController
from tg import expose, flash, require, url, lurl, request, redirect, validate
from tg.i18n import ugettext as _

from pycontactus import model
from pycontactus.model import DBSession

class RootController(TGController):
    
    @expose('pycontactus.templates.index')
    def index(self):
       
        
        return dict()

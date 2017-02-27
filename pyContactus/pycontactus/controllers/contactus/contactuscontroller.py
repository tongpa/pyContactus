# -*- coding: utf-8 -*-
"""Main Controller"""
from tg import TGController
from tg import expose, flash, require, url, lurl, request, redirect, validate, config
from tg.i18n import ugettext as _

from pycontactus import model
from pycontactus.model import DBSession
import sys
import json

log = logging.getLogger(__name__);
#from  logsurvey import LogDBHandler;
from tgext.pylogservice import LogDBHandler


__all__ = ['ContactusController']


class ContactusController(BaseController):
    allow_only = predicates.not_anonymous()
    def __init__(self):
        self.utility = Utility();  
       
        dh = LogDBHandler( config=config,request=request)
        log.addHandler(dh)
        
        self.__getMasterData()


        return dict(success=self.success, result=self.result, message=self.message)
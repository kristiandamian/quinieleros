# -*- coding: utf-8 -*-
import logging
import webapp2
import webob.multidict

from webapp2_extras import auth, sessions, jinja2
from jinja2.runtime import TemplateNotFound

from lib.simpleauth import SimpleAuthHandler

from auth.handlers import BaseRequestHandler

class gruposHandler(BaseRequestHandler):
  def get(self):
    """Handles GET /profile"""
    if self.logged_in:
      self.render('profile.html', {
        'user': self.current_user,
        'session': self.auth.get_user_by_session()
      })
    else:
      self.redirect('/')

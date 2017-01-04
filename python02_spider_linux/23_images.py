# -*- coding: utf8 -*-
import urllib2
open('.//google-logo.gif','wb').write(urllib2.urlopen('http://www.google.com/images/logo_sm.gif').read()) 

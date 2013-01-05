from pyramid.config import Configurator
from sqlalchemy import engine_from_config
#from pyramid.session import UnencryptedCookieSessionFactoryConfig
import pyramid_beaker

from .models import (
    DBSession,
    Base,
    )


def main(global_config, **settings):
	""" This function returns a Pyramid WSGI application.
	"""
	print "===__init_.py===main===global_config===", global_config
	print "===__init_.py===main===settings===", settings
	engine = engine_from_config(settings, 'sqlalchemy.')
	DBSession.configure(bind=engine)
	Base.metadata.bind = engine

	"""
	###SM Issue:
    session factory implementation is provided in the Pyramid core has following limitations
	* Keys and values of session data must be pickleable. This means, typically, 
		that they are instances of basic types of objects, such as strings, lists, 
		dictionaries, tuples, integers, etc. If you place an object in a session data 
		key or value that is not pickleable, an error will be raised when the session is serialized.
	* So use alternate session factory named "pyramid_beaker".

    ##Adb SM:You can configure this session factory in your Pyramid application by 
    ##using the session_factory argument to the Configurator class:
    ##http://docs.pylonsproject.org/projects/pyramid/en/1.0-branch/narr/sessions.html
    my_session_factory = UnencryptedCookieSessionFactoryConfig('itsaseekreet')
    ##Configurator
    config = Configurator(settings=settings, session_factory=my_session_factory)
	"""
	
	###Configurator###
	config = Configurator(settings=settings)

	###Session###
	##Adb SM: new session factory "pyramid_beaker", support to save object.
	##http://docs.pylonsproject.org/projects/pyramid_beaker/en/latest/
	## or session_factory = pyramid_beaker.session_factory_from_settings(settings)
	config.include('pyramid_beaker')
	session_factory = pyramid_beaker.BeakerSessionFactoryConfig()
	config.set_session_factory(session_factory)

	###Transaction###
	##Adb SM:
	##http://docs.pylonsproject.org/projects/pyramid_beaker/en/latest/
	config.include('pyramid_tm')

    ###Commented by SM
    #config.add_static_view('static', 'static', cache_max_age=3600)
    #config.add_route('home', '/')
    #config.scan()
    
	##Adb SM:		
	config.include('.routes')
	config.scan('.models')
	config.scan('.views') # controllers

	return config.make_wsgi_app()




















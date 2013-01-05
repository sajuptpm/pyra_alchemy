
from . import (route,
		user,
	     	)

##Adb SM	
_routes = (route,
	   user,
	)


def includeme(config):
    """
		config.include('.routes') invoke the method includeme
    """
    ##SM:path should be like 'alchemy_proj:static/', since moved routes into dir.
    config.add_static_view('static', 'alchemy_proj:static/', cache_max_age=3600)
    config.add_route('home', '/')

    ##Adb SM	
    for x in _routes:	
    	x.includeme(config)

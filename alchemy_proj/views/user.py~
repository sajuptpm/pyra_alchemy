
from pyramid.response import Response
from pyramid.view import view_config

from sqlalchemy.exc import DBAPIError

#from pyramid.security import (remember,forget)


from alchemy_proj.models import (
    DBSession,
    )

from alchemy_proj.models.user import (
    User,
    )

class Userviews(object):
	"""
	"""
	def __init__(self, context, request):
		"""
		""" 	
		self.context = context
		self.request = request
		self.session = self.request.session

	##SM:route_name should match with the name of config.add_route
	##SM:renderer='json' to return json object to client
	@view_config(route_name='login', renderer='json')
	def login(self):
		"""
		"""
		print "=====login========self.session========", self.session 
		try:
			user = DBSession.query(User).filter(User.user_name == "saju").first()
			if user:
				self.session["vv"] = user.user_name
				##SM:Check whether session allow to save object.	
				self.session["ss"] = self
				self.session.changed()##Save
		except DBAPIError:
			return Response(conn_err_msg, content_type='text/plain', status_int=500)
		return {"success":True, "msg":"Login success"}

	@view_config(route_name='logout', renderer='json')
	def logout(self):
		"""
		"""
		print "=====login========self.session========", self.session 
		#forget(self.request)
		self.session.invalidate()##Clear
		return {"success":True, "msg":"Logout success"}


	





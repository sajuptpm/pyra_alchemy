
from pprint import pprint

from pyramid.response import Response
from pyramid.view import view_config

from sqlalchemy.exc import DBAPIError

from alchemy_proj.debug_utils.utils import (
    view_debug,
    )


from alchemy_proj.models import (
    DBSession,
    )

from alchemy_proj.models.model import (
    MyModel,
    )


class Sampleviews(object):
	"""
	"""
	def __init__(self, context, request):
		"""
		""" 	
		self.context = context
		self.request = request
		self.session = self.request.session


	##SM:route_name should match with the name of config.add_route
	@view_config(route_name='home', renderer='../templates/mytemplate.pt')
	def my_view(self):
		"""
		"""
		try:
			one = DBSession.query(MyModel).filter(MyModel.name == 'one').first()
		except DBAPIError:
			return Response(conn_err_msg, content_type='text/plain', status_int=500)
		return {'one': one, 'project': 'alchemy_proj'}


	##SM:route_name should match with the name of config.add_route
	##SM:renderer='json' to return json object to client
	@view_debug()
	@view_config(route_name='addname', renderer='json')
	def transaction_test(self):
		"""
		"""
		msg = ""
		try:
			if self.request.params:
				name = self.request.params.get("name")
				trans = self.request.params.get("trans", "1")
			fst = DBSession.query(MyModel).filter(MyModel.name == name).first()
			if fst:
				msg = "row already exist with name:%s" %(name)
			else:
				d = MyModel()
				d.name = name
				d.value = "30"
				DBSession.add(d)
				msg = "Row successfully saved"

				if not int(trans):##Abort/Commit Transaction
					raise Exception("Abort Transaction")

		except DBAPIError:
			return Response(conn_err_msg, content_type='text/plain', status_int=500)
		return {"success":True, "msg":msg}


conn_err_msg = """\
Pyramid is having a problem using your SQL database.  The problem
might be caused by one of the following things:

1.  You may need to run the "initialize_alchemy_proj_db" script
    to initialize your database tables.  Check your virtual 
    environment's "bin" directory for this script and try to run it.

2.  Your database server may not be running.  Check that the
    database server referred to by the "sqlalchemy.url" setting in
    your "development.ini" file is running.

After you fix the problem, please restart the Pyramid application to
try it again.
"""


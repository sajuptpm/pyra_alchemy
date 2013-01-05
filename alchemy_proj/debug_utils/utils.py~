
from pprint import pprint

def view_debug():
	"""
		##Adb:SM
	"""
	def wrap(fun):
		"""
		"""
		def inner_wrap(*args, **kwargs):
			"""
			"""
			self_instance = None
			if args:
				self_instance = args[0]
			if self_instance:
				#print "===self.request===", self_instance.request
				#print "===pprint(vars(self.request))===", pprint(vars(self_instance.request))
				print "===pprint(self.request.params)===", pprint(self_instance.request.params)
				print "===pprint(self.session)===", self_instance.session
			return fun(*args, **kwargs)
		return inner_wrap
	return wrap
























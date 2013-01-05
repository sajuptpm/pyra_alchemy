import os
import sys
import transaction

from sqlalchemy import engine_from_config

from pyramid.paster import (
    get_appsettings,
    setup_logging,
    )

from ..models import (
    DBSession,
    Base,
    )

from alchemy_proj.models.model import (
    MyModel,
    )

from alchemy_proj.models.user import (
    User,
    )


def usage(argv):
    cmd = os.path.basename(argv[0])
    print('usage: %s <config_uri>\n'
          '(example: "%s development.ini")' % (cmd, cmd))
    sys.exit(1)


def main(argv=sys.argv):
    if len(argv) != 2:
        usage(argv)
    config_uri = argv[1]
    setup_logging(config_uri)
    settings = get_appsettings(config_uri)
    engine = engine_from_config(settings, 'sqlalchemy.')
    DBSession.configure(bind=engine)
    Base.metadata.create_all(engine)
    ##SM:Populate tables with dummy data
    with transaction.manager:
        model = DBSession.query(MyModel).filter(MyModel.name=='one').first()
	if not model:
        	model = MyModel(name='one', value=1)
        	DBSession.add(model)
		print "added mymodel"
        user = DBSession.query(User).filter(User.user_name=='saju').first()
	if not user:
        	user = User()
		user.firstname = "saju"
		user.lastname = "m"
		user.user_name = "saju"
		user.email_address = "saju@xx.com"
		user._password = "saju"
        	DBSession.add(user)
		print "added user"


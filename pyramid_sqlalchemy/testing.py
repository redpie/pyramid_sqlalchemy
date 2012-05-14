from pyramid_sqlalchemy import Session, db_init, db_upgrade

def setUp():
    pass

def tearDown():
    pass

def setUpMigrate():
    """ Runs migrations before each test """
    engine = create_engine('sqlite://', echo=True)
    Session.configure(bind=engine)
    db_init(engine)
    db_upgrade(engine)

def tearDownMigrate():
    Session.remove()

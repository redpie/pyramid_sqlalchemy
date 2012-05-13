import os
import sys
import logging

from pyramid.paster import bootstrap, setup_logging
from pyramid_sqlalchemy import db_init, db_upgrade
from migrate.exceptions import DatabaseAlreadyControlledError

def init_scripts(argv):
    global LOG
    config_uri = argv[1]
    setup_logging(config_uri)
    bootstrap(config_uri)
    LOG = logging.getLogger(__name__)

def init_db_usage(argv):
    cmd = os.path.basename(argv[0])
    print('usage: %s <config_uri>\n'
          '(example: "%s development.ini")' % (cmd, cmd))
    sys.exit(1)

def init_db(argv=sys.argv):
    if len(argv) != 2:
        init_db_usage(argv)

    init_scripts(argv)

    from pyramid_sqlalchemy import engine
    engine.echo = True

    try:
        db_init(engine)
    except DatabaseAlreadyControlledError:
        _log("Database already under version control")
        sys.exit(2)
    else:
        _log("Database now under version control")
        sys.exit(0)

def migrate_db_usage(argv):
    cmd = os.path.basename(argv[0])
    print('usage: %s <config_uri> [version]\n'
          '(example: "%s development.ini 12")' % (cmd, cmd))
    sys.exit(1)

def migrate_db(argv=sys.argv):
    if len(argv) < 2 or len(argv) > 3:
        migrate_db_usage(argv)

    init_scripts(argv)

    if len(argv) == 2:
        version = None
    else:
        version = argv[2]

    from pyramid_sqlalchemy import engine
    engine.echo = True

    try:
        db_upgrade(engine, version=version)
    except KeyError, e:
        _log("Version '%s' not found" % str(version))
        sys.exit(2)
    else:
        _log("Database migration complete")
        sys.exit(0)

def _log(msg):
    LOG.warn(msg)
    print(msg)

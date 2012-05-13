import migrate
import distutils.version as dist_version
from migrate.versioning import util as migrate_util

# NOTE(kiall): See http://code.google.com/p/sqlalchemy-migrate/issues/detail?id=72.
#              Remove after 0.7.3 release. Code nabbed from OpenStack Nova.
@migrate_util.decorator
def patched_with_engine(f, *a, **kw):
    url = a[0]
    engine = migrate_util.construct_engine(url, **kw)

    try:
        kw['engine'] = engine
        return f(*a, **kw)
    finally:
        if isinstance(engine, migrate_util.Engine) and engine is not url:
            migrate_util.log.debug('Disposing SQLAlchemy engine %s', engine)
            engine.dispose()


# TODO(kiall): When migrate 0.7.3 is released this can be removed
MIN_PKG_VERSION = dist_version.StrictVersion('0.7.3')
if (not hasattr(migrate, '__version__') or
    dist_version.StrictVersion(migrate.__version__) < MIN_PKG_VERSION):
    migrate_util.with_engine = patched_with_engine

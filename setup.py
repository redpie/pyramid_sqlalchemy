#!/usr/bin/env python
import os

from setuptools import setup, find_packages

here = os.path.abspath(os.path.dirname(__file__))

install_requires = [
    'pyramid>=1.3',
    'SQLAlchemy',
    'sqlalchemy-migrate',
    'zope.sqlalchemy'
]

tests_require = [
    'coverage'
]

setup_requires = [
    'nose'
]

dependency_links = []

setup(name='pyramid_sqlalchemy',
      version='0.1',
      description='Simple SQLAlchemy boilerplate reduction for Pyramid',
      long_description='Simple SQLAlchemy boilerplate reduction for Pyramid',
      classifiers=[],
      author='Kiall Mac Innes',
      author_email='kiall@managedit.ie',
      url='https://github.com/managedit/pyramid_sqlalchemy',
      license="BSD",
      keywords='pylons pyramid sqlalchemy orm migrate migrations database',
      packages=find_packages(),
      include_package_data=True,
      zip_safe=False,
      dependency_links=dependency_links,
      install_requires=install_requires,
      tests_require=tests_require,
      test_suite='pyramid_sqlalchemy.tests',
      setup_requires=setup_requires,
      entry_points="""\
      [console_scripts]
      pdbinit = pyramid_sqlalchemy.scripts:init_db
      pdbmigrate = pyramid_sqlalchemy.scripts:migrate_db
      """
      )


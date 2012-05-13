import os
import unittest
from pyramid import testing

class Test(unittest.TestCase):
    """
    Basic tests for Pyramid SQLAlchemy integration

    TODO..
    """
    def setUp(self):
        self.request = testing.DummyRequest()
        self.config = testing.setUp(request=self.request)
        self.request.registry = self.config.registry

        here = os.path.abspath(os.path.dirname(__file__))
        repository_path = os.path.join(here, 'test_repository')

        self.config.registry.settings.update({
            'sqlalchemy.url': 'sqlite://',
            'sqlalchemy_migrate.repository': repository_path
        })

    def tearDown(self):
        testing.tearDown()
        del self.config

    def test_includeme(self):
        from pyramid_sqlalchemy import includeme

        includeme(self.config)

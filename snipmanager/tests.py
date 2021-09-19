import datetime

from django.test import TestCase
from django.utils import timezone
from .models import Snips


class SnipsModelTests(TestCase):

    def test_example(self):
        """
        test comment
        """
        obj = Snips()
        obj.title = "hi"
        self.assertIs(obj.title,"hi")
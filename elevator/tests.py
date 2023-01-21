import json
from unittest.mock import patch, Mock

from django.test import TestCase
from django.urls import reverse


CONTENT_TYPE = "application/json; charset=utf-8"

# Testing for elevator views to be changed later on
class ElevatorViewsTestCase(TestCase):
    """
    Test cases for elevator modules
    """
    def test_create_elevator(self):
        """
        Testing for create new elevator
        """
        payload = {}

        response = self.client.post(reverse('create_new_elevator'), payload, content_type=CONTENT_TYPE)
        response_json = response.json()
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response_json.get('status'), 'created')

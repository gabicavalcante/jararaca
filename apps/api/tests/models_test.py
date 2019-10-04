from django.test import TestCase
from apps.api.models import Attendee
from django.urls import reverse
from model_mommy import mommy


class AttendeeTest(TestCase):
    """
    Class to Test Attendee Model 
    """

    def create_attendee(self):
        return mommy.make(Attendee)

    def test_attendee_creation(self):
        attendee = self.create_attendee()
        self.assertTrue(isinstance(attendee, Attendee))
        #self.assertEqual(attendee.__unicode__(), '%s (%s)' %
        #                 (attendee.name, attendee.uuid))

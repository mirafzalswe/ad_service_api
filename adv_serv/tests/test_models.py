from django.test import TestCase
from ..models import Ad

class AdModelTest(TestCase):

    def setUp(self):
        self.ad = Ad.objects.create(
            title='smthing smthing',
            ad_id=1,
            author='Mr me',
            views=100,
            position=1
        )

    def test_ad_creation(self):
        self.assertEqual(self.ad.title, 'smthing smthing')
        self.assertEqual(self.ad.ad_id, 1)
        self.assertEqual(self.ad.author, 'Mr me')
        self.assertEqual(self.ad.views, 100)
        self.assertEqual(self.ad.position, 1)
        self.assertEqual(str(self.ad), 'smthing smthing')

from django.test import TestCase
from ..models import Ad
from ..serializers import AdSerializer

class AdSerializerTest(TestCase):

    def setUp(self):
        self.ad_attributes = {
            'title': 'smthing smthing',
            'ad_id': 1,
            'author': 'mr Me',
            'views': 100,
            'position': 1
        }

        self.ad = Ad.objects.create(**self.ad_attributes)
        self.serializer = AdSerializer(instance=self.ad)

    def test_contains_expected_fields(self):
        data = self.serializer.data
        self.assertCountEqual(data.keys(), ['title', 'ad_id', 'author', 'views', 'position'])

    def test_title_field_content(self):
        data = self.serializer.data
        self.assertEqual(data['title'], self.ad_attributes['title'])

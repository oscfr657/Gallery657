
from django.test import TestCase
from ..models import Collection


class CollectionTest(TestCase):
    """ Test module for Collection model """

    def setUp(self):
        Collection.objects.create(title='Paintings')
        Collection.objects.create(title='Photos')

    def test_collection_title(self):
        collection_paintings = Collection.objects.get(title='Paintings')
        collection_photos = Collection.objects.get(title='Photos')
        self.assertEqual(collection_paintings.title, 'Paintings')
        self.assertEqual(collection_photos.title, 'Photos')

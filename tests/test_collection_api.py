
import json
from rest_framework import status
from django.test import TestCase, Client
from ..models import Collection
from ..serializers import CollectionSerializer

client = Client()


class GetAllCollectionsTest(TestCase):
    """ Test module for GET all collections API """

    def setUp(self):
        Collection.objects.create(title='Paintings')
        Collection.objects.create(title='Photos')

    def test_get_all_collections(self):
        response = client.get('/gallery/api/collection/')
        collections = Collection.objects.all()
        serializer = CollectionSerializer(collections, many=True)
        self.assertEqual(response.data['results'], serializer.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)


class GetSingleCollectionTest(TestCase):
    """ Test module for GET single collection API """

    def setUp(self):
        self.paintings = Collection.objects.create(title='Paintings')

    def test_get_valid_single_collection(self):
        response = client.get('/gallery/api/collection/{0}/'.format(self.paintings.pk))
        collection = Collection.objects.get(pk=self.paintings.pk)
        serializer = CollectionSerializer(collection)
        self.assertEqual(response.data, serializer.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_invalid_single_collection(self):
        response = client.get('/gallery/api/collection/30')
        self.assertEqual(response['Content-Length'], '0')


class BlockCreateCollectionTest(TestCase):
    """ Test module for creating a new collection """

    def setUp(self):
        self.collection = {'title': 'Muffin'}

    def test_fail_create_collection(self):
        response = client.post('/gallery/api/collection/',
                               data=json.dumps(self.collection),
                               content_type='application/json'
                               )
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)


class BlockUpdateCollectionTest(TestCase):
    """ Test module for updating a collection """

    def setUp(self):
        self.paintings = Collection.objects.create(title='Paintings')
        self.update_data = {'title': 'Photo'}

    def test_fail_update_collection(self):
        response = client.put('/gallery/api/collection/{0}/'.format(self.paintings.pk),
                              data=json.dumps(self.update_data),
                              content_type='application/json'
                              )
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)


class BlockDeleteCollectionTest(TestCase):
    """ Test module for deleting a collection """

    def setUp(self):
        self.paintings = Collection.objects.create(title='Paintings')

    def test_fail_delete_collection(self):
        response = client.delete('/gallery/api/collection/{0}/'.format(
            self.paintings.pk))
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
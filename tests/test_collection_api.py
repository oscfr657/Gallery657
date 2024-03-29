
import json

from django.utils import timezone

from django.test import TestCase, Client
from django.contrib.sites.models import Site

from rest_framework import status

from gallery657.models import Collection
from gallery657.serializers import CollectionSerializer

CLIENT = Client()


class GetAllCollectionsTest(TestCase):
    """ Test module for GET all collections API """

    def setUp(self):
        site = Site.objects.get(id=1)
        site.name = 'Test Site'
        site.save()
        now = timezone.now()
        collectiion1 = Collection.objects.create(
            title='Paintings',
            pub_date=now,
            slug='paintings')
        collectiion1.sites.add(site)
        collectiion1.save()
        collectiion2 = Collection.objects.create(
            title='Photos',
            pub_date=now,
            slug='photos')
        collectiion2.sites.add(site)
        collectiion2.save()

    def test_get_all_collections(self):
        response = CLIENT.get('/gallery657/api/collection/')
        collections = Collection.objects.all()
        serializer = CollectionSerializer(collections, many=True)
        self.assertEqual(response.data, serializer.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)


class GetSingleCollectionTest(TestCase):
    """ Test module for GET single collection API """

    def setUp(self):
        site = Site.objects.get(id=1)
        site.name = 'Test Site'
        site.save()
        now = timezone.now()
        self.paintings = Collection.objects.create(
            title='Paintings',
            pub_date=now,
            slug='paintings')
        self.paintings.sites.add(site)
        self.paintings.save()

    def test_get_valid_single_collection(self):
        response = CLIENT.get('/gallery657/api/collection/?collection_slug={0}'.format(self.paintings.slug))
        collection = Collection.objects.get(pk=self.paintings.pk)
        serializer = CollectionSerializer(collection)
        self.assertEqual(json.loads(response.content)[0], serializer.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_invalid_single_collection(self):
        response = CLIENT.get('/gallery657/api/collection/30')
        self.assertEqual(response['Content-Length'], '0')


class BlockCreateCollectionTest(TestCase):
    """ Test module for creating a new collection """

    def setUp(self):
        self.collection = {'title': 'Muffin'}

    def test_fail_create_collection(self):
        response = CLIENT.post('/gallery657/api/collection/',
                               data=json.dumps(self.collection),
                               content_type='application/json')
        self.assertEqual(response.status_code, status.HTTP_405_METHOD_NOT_ALLOWED)


class BlockUpdateCollectionTest(TestCase):
    """ Test module for updating a collection """

    def setUp(self):
        self.paintings = Collection.objects.create(title='Paintings')
        self.update_data = {'title': 'Photo'}

    def test_fail_update_collection(self):
        response = CLIENT.put('/gallery657/api/collection/{0}/'.format(self.paintings.pk),
                              data=json.dumps(self.update_data),
                              content_type='application/json')
        self.assertEqual(response.status_code, status.HTTP_405_METHOD_NOT_ALLOWED)


class BlockDeleteCollectionTest(TestCase):
    """ Test module for deleting a collection """

    def setUp(self):
        self.paintings = Collection.objects.create(title='Paintings')

    def test_fail_delete_collection(self):
        response = CLIENT.delete('/gallery657/api/collection/{0}/'.format(
            self.paintings.pk))
        self.assertEqual(response.status_code, status.HTTP_405_METHOD_NOT_ALLOWED)

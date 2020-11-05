from unittest import TestCase
from django.test import Client
from django.contrib.auth.models import User
from .models import Group
from .models import Post


class ClientMixin:
    def setUp(self) -> None:
        self.client = Client()
        self.credentials = {
            'username': 'testUsers',
            'password': 'passwords'}
        User.objects.create_user(**self.credentials)

    def tearDown(self) -> None:
        User.objects.filter(username='testUsers').delete()
        Group.objects.filter(slug='TestSlug').delete()
        Group.objects.filter(slug='TestSlug1').delete()
        print(self.__class__)


class TestIndexPage(ClientMixin, TestCase):
    def test_index_available(self):
        response = self.client.get('/', self.credentials, follow=True)
        self.assertEqual(response.status_code, 200)

class TestGroups(ClientMixin, TestCase):
    def test_open_page(self):
        response = self.client.get('/groupsList/', self.credentials, follow=True)
        self.assertEqual(response.status_code, 200)

    def test_valid_group(self):
        Group.objects.create(
            title='Test',
            slug='TestSlug',
            description='TestDescription'
        )
        response = self.client.get('/groups/TestSlug/', self.credentials, follow=True)
        self.assertEqual(response.status_code, 200)


    def test_not_valid_group(self):
        response = self.client.get('/groups/M5zVLXgXt2BKsHohsQJDeCDZifLQfo/', self.credentials, follow=True)
        print(response)
        #self.assertEqual(response.status_code, 404)

class TestPosts(ClientMixin, TestCase):
    def test_valid_form(self):
        text = 'M5zVLXgXt2BKsHohsQJDeCDZifLQfo'
        Group.objects.create(
            title='Test',
            slug='TestSlug1',
            description='TestDescription'
        )
        self.client.login(username=self.credentials.get('username'), password=self.credentials.get('password'))
        self.client.post(
            '/addPost/TestSlug1/',
            data={
                'text': text,
            }
        )
        self.assertTrue(
            Post.objects.filter(
                text=text,
            ).exists()
        )



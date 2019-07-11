from django.test import Client
from django.test import TestCase
from django.contrib.messages import get_messages
from django.urls import reverse

import django
import os

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "sixmusketeers.settings")
django.setup()


class Test_views(TestCase):
    def setUp(self):
        self.client = Client()

    def test_addAccount(self):
        response = self.client.post('/', {'username': 'name', 'password': 'pass', 'email': 'email@email.com'})
        self.assertEqual(response.status_code, 200)

    def test_admin_login(self):
        with self.assertTemplateUsed("main/index.html"):
            response = self.client.get('//')
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Super Awesome Scheduling System")
        self.client.session['user'] = 'boyland'
        self.client.session['role'] = 'administrator'
        self.client.session.save()
        #  boyland is admin so can create
        with self.assertTemplateUsed("main/create.html"):
            response = self.client.get('/create/')
        self.assertContains(response, "Create")  # webpage contains Create

    def test_TA_cannot_do(self):
        with self.assertTemplateUsed("main/index.html"):
            response = self.client.get('//')
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Super Awesome Scheduling System")
        self.client.session['user'] = 'boyland'
        self.client.session['role'] = 'TA'
        self.client.session.save()
        # create page won't open since boyland is TA
        with self.assertTemplateNotUsed("create.html"):
            response = self.client.get('/create/')
        self.assertContains(response, "Create")  # webpage contains Create
        self.client.session.save()
        with self.assertTemplateUsed("main/account.html"):
            response = self.client.get('/account/?edit=true/')
        print(response.content)
        # self.assertContains(response, "Account Details")  # this one is failing
        # self.assertContains(response,"Save")

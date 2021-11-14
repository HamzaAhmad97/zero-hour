from django.http import response
from django.test import TestCase
from django.test.testcases import SimpleTestCase
from django.urls import reverse

class TestGenerals(SimpleTestCase):
    def test_home_status_code(self):
        url = reverse("home")
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_about_status_code(self):
        url = reverse("about")
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_home_view_uses_correct_template(self):
        response = self.client.get(reverse('home'))
        self.assertTemplateUsed(response, 'generals/home.html')

    def test_about_view_uses_correct_template(self):
        response = self.client.get(reverse('about'))
        self.assertTemplateUsed(response, 'generals/about.html')

    def test_generals_in_context(self):
        response = self.client.get(reverse('home'))
        self.assertTrue('generals' in response.context)
        self.assertEqual(len(response.context['generals']), 9)
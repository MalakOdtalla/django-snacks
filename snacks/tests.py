from django.test import TestCase
from django.urls import reverse

# Create your tests here.
class snacks_test(TestCase):
    def test_home_page_status_code(self):
        expected = 200
        url = reverse('home')
        response = self.client.get(url)
        actual = response.status_code
        self.assertEquals(expected, actual)

    def test_home_page_template(self):
        url = reverse('home')
        response = self.client.get(url)
        actual = 'Home.html'
        self.assertTemplateUsed(response, actual)

    def test_about_page_status_code(self):
        expected = 200
        url = reverse('about')
        response = self.client.get(url)
        actual = response.status_code
        self.assertEquals(expected, actual)

    def test_about_page_template(self):
        url = reverse('about')
        response = self.client.get(url)
        actual = 'About.html'
        self.assertTemplateUsed(response, actual)
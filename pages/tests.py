from django.test import SimpleTestCase
from django.urls import reverse

# Testing for homepage requests
class HomepageTests(SimpleTestCase):
    def test_url_exists_at_correct_location(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
    
    def test_url_available_by_name(self):
        response = self.client.get(reverse('home1'))
        self.assertEqual(response.status_code, 200)
    
    def test_template_name_correct(self): # new
        response = self.client.get(reverse("home1"))
        self.assertTemplateUsed(response, "home.html")
    
    def test_template_content(self): # new
        response = self.client.get(reverse("home1"))
        self.assertContains(response, "<h1>Homepage</h1>")

# Testing for aboutpage requests
class AboutpageTests(SimpleTestCase):
    def test_url_exists_at_correct_location(self):
        response = self.client.get('/about/')
        self.assertEqual(response.status_code, 200)
    
    def test_url_available_by_name(self):
        response = self.client.get(reverse('about'))
        self.assertEqual(response.status_code, 200)
    
    def test_template_name_correct(self): # new
        response = self.client.get(reverse("about"))
        self.assertTemplateUsed(response, "about.html")
    
    def test_template_content(self): # new
        response = self.client.get(reverse("about"))
        self.assertContains(response, "<h1>About page</h1>")
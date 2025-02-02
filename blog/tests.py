from django.test import TestCase
from django.urls import reverse
from .models import FAQ

class FAQViewTests(TestCase):

    @classmethod
    def setUpTestData(cls):
        # Create sample FAQ entries for testing
        FAQ.objects.create(question="What is Django?", answer="A web framework.")
        FAQ.objects.create(question="Who Developed You?", answer="Nenavath Sunil")

    def test_faq_list_view(self):
        response = self.client.get(reverse('faq_list'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "What is Django?")
        self.assertContains(response, "A web framework.")

    def test_faq_list_class_view(self):
        response = self.client.get(reverse('faq_list_class'))
        self.assertEqual(response.status_code, 200)
        self.assertJSONEqual(response.content, [
            {"question": "What is Django?", "answer": "A web framework."},
            {"question": "Who Developed You?", "answer": "Nenavath Sunil"}
        ])

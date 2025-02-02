
from django.urls import path
from .views import FAQListView  # Import your views

urlpatterns = [
    path('faqs/', FAQListView.as_view(), name='faq_list'),  # Example URL for FAQs
    # Add other URL patterns for your blog app here
]

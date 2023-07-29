from django.urls import path
from .views import RandomQuoteView

urlpatterns = [path("", RandomQuoteView.as_view())]

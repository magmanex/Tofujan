from django.urls import path
from . import views
from django.views.decorators.csrf import csrf_exempt

urlpatterns = [
    path('webhooks/tutorial/', csrf_exempt(views.TutorialBotView.as_view())),
]

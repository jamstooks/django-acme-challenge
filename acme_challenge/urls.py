from django.conf.urls import url
from views import ACMEChallengeView

urlpatterns = [
    url(
        r'^(?P<challenge_slug>[\w\-]+)$',
        ACMEChallengeView.as_view(),
        name='acme-challenge'
    ),
]

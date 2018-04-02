from django.views.generic import TemplateView
from django.conf import settings
from django.http import Http404


class ACMEChallengeView(TemplateView):
    """
        If the appropriate settings vars are set and the slug matches the url,
        then serve the ACME Challenge value
    """
    template_name = "acme_challenge/default.txt"
    
    def get_context_data(self, **kwargs):
        if settings.ACME_CHALLENGE_URL_SLUG and settings.ACME_CHALLENGE_TEMPLATE_CONTENT:
            if self.kwargs['challenge_slug'] == settings.ACME_CHALLENGE_URL_SLUG:
                context = super(ACMEChallengeView, self).get_context_data(**kwargs)
                context['ACME_CHALLENGE_TEMPLATE_CONTENT'] = settings.ACME_CHALLENGE_TEMPLATE_CONTENT
                return context
        raise Http404

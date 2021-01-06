from django.views.generic import FormView
from django.urls import reverse

from .forms import ContactForm

class ContactFormView(FormView):
    form_class = ContactForm
    template_name = 'contacts/contact_form.html'

    def get_initial(self):
        """
        We wish to record where the visitor was BEFORE arriving at the contact
        page. We'll ultimately record this in the 'referer' field in our
        model. But for now, we'll initialize our form object to include this
        here, but only when creating the original form object. This way, no
        matter how many times the visitor has validation errors, etc., we'll
        still preserve this original HTTP_REFERER.
        """
        initial = super(ContactFormView, self).get_initial()
        initial['referer'] = self.request.META.get('HTTP_REFERER', ''),
        return initial

    def get_success_url(self):
        return reverse('index')

    def form_valid(self, form):
        self.object = form.save()
        return super(ContactFormView, self).form_valid(form)
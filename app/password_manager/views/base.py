from django.views.generic import TemplateView, ListView
from password_manager.models.entry_password import EntryPassword

class HomeView(ListView):
    template_name = "home.html"
    model = EntryPassword
    context_object_name = "websites"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["websites"] = EntryPassword.objects.all()
        return context

class WebSiteDataDetailView(DetailView):
    template_name = "website_data_detail.html"
    model = EntryPassword
    context = 'website'
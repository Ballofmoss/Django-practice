from urllib import response
from django import template
from django.views.generic import ListView, DetailView, CreateView, UpdateView
from password_manager.models.entry_password import EntryPassword
from django.shortcuts import render

class HomeView(ListView):
    template_name = "home.html"
    model = EntryPassword
    context_object_name = "websites"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["websites"] = EntryPassword.objects.all()
        return context

class WebSiteDataDetailView(DetailView):
    template_name = "item_data_website.html"
    model = EntryPassword
    context = 'website'

class WebsiteDataCreateView(CreateView):
    template_name = "website_form_create.html"
    model = EntryPassword
    form_class = EntryPassword  
    success_url = '/'

    def form_valid(self, form):
        response = super().form_valid(form)
        return render(self.request, "website_data_detail.html", context={
            'website': self.object
        })
    
class WebsiteDataUpdateView(UpdateView):
    template_name = "website_form_update.html"
    model = EntryPassword
    form_class = EntryPasswordForm
    context_object_name = 'website'
    success_url = '/'

    def form_valid(self, form):
        response = super().form_valid(form)
        return render(self.request, "website_data_detail.html", context={
            'website': self.object
        })
    
class WebsiteDataDeleteView(DetailView):
    model = EntryPassword
    success_url = '/'


class WebSiteSearchView(FormView):
    template_name = "website_form_search.html"
    form_class = SearchWebSiteForm
    
    def form_valid(self, form):
        response = super().form_valid(form)
        website = response.get('website')
        
        EntryPassword.objects.get(website__contains=website)
        
        return render(self.request, 'website_data_detail.html', context={
            'website': self.object
        })

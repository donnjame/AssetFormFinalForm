from django.shortcuts import render
from django.db.models import Q
from django.urls import reverse_lazy
from django.http import HttpResponse, request
from django.views.generic import (View,TemplateView,
                                ListView,DetailView,
                                CreateView,DeleteView,
                                UpdateView)
from . import models
from django.core.paginator import Paginator
from django.shortcuts import render
from django.urls import reverse, reverse_lazy
from form_app.models import BeaconAsset
# Create your views here.

class ThankView(TemplateView):
    template_name = 'thanks.html'

class TestView(TemplateView):
    template_name = 'index.html'

class BeaconAssetCreateView(CreateView):
    model=models.BeaconAsset
    fields = ('__all__')



from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.views.generic import View
from django.core.exceptions import PermissionDenied
from django import forms

from .models import Vacancy


class VacancyView(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'vacancy/vacancy_view.html', context={'vacancies': Vacancy.objects.all()})


class VacancyCreateView(View):
    def get(self, request, *args, **kwargs):
        new_post_form = NewPostForm()
        return render(request, 'vacancy/vacancy_create.html', {'form': new_post_form})

    def post(self, request, *args, **kwargs):
        request_user = User.objects.filter(username=request.user.username)[0]
        description = request.POST.get('description')
        if request_user.is_staff:
            Vacancy.objects.create(author=request_user, description=description)
            return redirect('/vacancies')
        raise PermissionDenied


class NewPostForm(forms.Form):
    description = forms.CharField(min_length=10, max_length=1024)

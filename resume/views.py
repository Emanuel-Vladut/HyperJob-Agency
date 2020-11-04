from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.views.generic import View
from django import forms

from .models import Resume


class ResumeView(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'resume/resume_view.html', context={'resumes': Resume.objects.all()})


class ResumeCreateView(View):
    def get(self, request, *args, **kwargs):
        new_post_form = NewPostForm()
        return render(request, 'resume/resume_create.html', {'form': new_post_form})

    def post(self, request, *args, **kwargs):
        request_user = User.objects.filter(username=request.user.username)[0]
        description = request.POST.get('description')
        Resume.objects.create(author=request_user, description=description)
        return redirect('/resumes')


class NewPostForm(forms.Form):
    description = forms.CharField(min_length=10, max_length=1024)

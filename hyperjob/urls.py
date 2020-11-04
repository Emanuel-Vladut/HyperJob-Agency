"""hyperjob URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.menu, name='menu')
Class-based views
    1. Add an import:  from other_app.views import Home
    # 2. Add a URL to urlpatterns:  path('', Home.as_view(), name='menu')
Including another Lconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.urls import path, include

from resume.views import ResumeCreateView
from vacancy.views import VacancyCreateView

from .views import (
    MenuPageView,
    MyLoginView,
    MyLogoutView,
    MySignupView,
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', MenuPageView.as_view()),
    path('menu/', MenuPageView.as_view()),
    path('vacancies/', include('vacancy.urls')),
    path('resumes/', include('resume.urls')),
]

urlpatterns += [
    path('login', MyLoginView.as_view(), name='user_login'),
    path('logout/', MyLogoutView.as_view(), name='user_logout'),
    path('signup', MySignupView.as_view(), name='signup'),
    path('resume/new', ResumeCreateView.as_view(), name='resume_add'),
    path('vacancy/new', VacancyCreateView.as_view(), name='vacancy_add'),

]

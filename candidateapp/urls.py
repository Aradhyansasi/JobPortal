from django.urls import path
from candidateapp import views

urlpatterns = [
    path('home',views.CandidateHomeView.as_view(), name='candhome'),
    path('profile/add', views.CandProfileCreateView.as_view(), name='candprofadd'),
    path('profile/view', views.CandProfileView.as_view(), name='candproview'),
    path('profile/alljob', views.CandiJobListView.as_view(), name='candalljob'),
    path('job/view/<int:id>', views.CandiJobDetailView.as_view(), name='candjobview'),
    path('job/apply/<int:id>', views.apply_now, name='candiapplynow'),
    path('job/applied', views.MyApplicationView.as_view(), name='candiappliedjobs'),
    path('job/notification', views.JobNotificationView.as_view(), name='notification'),
    path('profile/edit/<int:id>', views.CandiProfUpdateView.as_view(), name='candproedit'),
]
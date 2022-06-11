from django.urls import path
from employerapp import views

urlpatterns= [
    path('home/', views.EmployerHomeView.as_view(), name='emphome'),
    path('profile/add', views.EmployerProfileCreateView.as_view(), name='emppro'),
    path('profile/details', views.EmployerProfileView.as_view(), name='empdetails'),
    path('job/add', views.PostJobsView.as_view(), name='empjobadd'),
    path('job/list', views.ListJobView.as_view(), name='empjoblist'),
    path('job/detail/<int:id>', views.JobDetailView.as_view(), name='empjobdetail'),
    path('job/edit/<int:id>', views.JobEditView.as_view(), name='empjobedit'),
    path('job/delete/<int:id>', views.JobDeleteView.as_view(), name='empjobdelete'),
    path('job/application/<int:id>', views.ViewApplicationView.as_view(), name='empviewapplcn'),
    path('profile/candidate/<int:id>', views.CandidateProfileView.as_view(), name='candi_profile'),
    path('application/reject/<int:id>', views.UpdateApplication, name='reject'),
    path('application/accept/<int:id>', views.AcceptApplication, name='accept'),
    path('profile/update/<int:id>', views.EmpProfUpdateView.as_view(), name='empprofedit'),
]

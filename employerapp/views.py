from django.shortcuts import render, redirect
from django.views.generic import TemplateView, CreateView, ListView, DetailView, UpdateView, View
from employerapp.models import EmployerProfile, Jobs, Applications
from employerapp.forms import EmployerProfileForm, JobForm
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from candidateapp.decorators import signin_required
from django.core.mail import send_mail
from django.contrib import messages # to show popup messages
# Create your views here.


@method_decorator(signin_required,name="dispatch")
class EmployerHomeView(TemplateView):
    template_name = 'emp_home.html'

@method_decorator(signin_required,name="dispatch")
class EmployerProfileCreateView(CreateView):
    model = EmployerProfile
    form_class = EmployerProfileForm
    template_name = 'emp_profile.html'
    success_url = reverse_lazy('emphome')

    def form_valid(self, form):
        form.instance.user = self.request.user
        messages.success(self.request, "Profile has been created successfully")
        return super().form_valid(form)

@method_decorator(signin_required,name="dispatch")
class EmployerProfileView(TemplateView):
    template_name = 'emp_profileDetails.html'

@method_decorator(signin_required,name="dispatch")
class PostJobsView(CreateView):
    model = Jobs
    form_class = JobForm
    template_name = 'emp_jobAdd.html'
    success_url = reverse_lazy('emphome')

    def form_valid(self, form):
        form.instance.posted_by = self.request.user
        messages.success(self.request, "Job has been posted successfully")
        return super().form_valid(form)

@method_decorator(signin_required,name="dispatch")
class ListJobView(ListView):
    model = Jobs
    template_name = 'emp_viewJob.html'
    context_object_name = 'jobs'

    def get_queryset(self):
        return Jobs.objects.filter(posted_by=self.request.user).order_by('-posted_date')

@method_decorator(signin_required,name="dispatch")
class JobDetailView(DetailView):
    model = Jobs
    template_name = 'candiJobDetail.html'
    pk_url_kwarg = 'id'
    context_object_name = 'job'

@method_decorator(signin_required,name="dispatch")
class JobEditView(UpdateView):
    model = Jobs
    form_class = JobForm
    template_name = 'emp_jobEdit.html'
    pk_url_kwarg = 'id'
    success_url = reverse_lazy('emphome')

    def form_valid(self, form):
        form.instance.posted_by = self.request.user
        messages.success(self.request, "Job has been updated successfully")
        return super().form_valid(form)

@method_decorator(signin_required,name="dispatch")
class JobDeleteView(View):
    def get(self,request, *args, **kwargs):
        id = kwargs.get('id')
        job = Jobs.objects.get(id=id)
        job.delete()
        return redirect('empjoblist')

@method_decorator(signin_required,name="dispatch")
class ViewApplicationView(ListView):
    model = Applications
    template_name = 'emp_applications.html'
    context_object_name = 'application'

    def get_queryset(self):
        return Applications.objects.filter(job=self.kwargs.get('id'),status='applied')

@method_decorator(signin_required,name="dispatch")
class CandidateProfileView(DetailView):
    model = Applications
    template_name = 'candiprofile.html'
    context_object_name = 'prof'
    pk_url_kwarg = 'id'

@signin_required
def UpdateApplication(request, *args, **kwargs):
    appid = kwargs.get('id')
    qs = Applications.objects.get(id=appid)
    qs.status = 'rejected'
    qs.save()
    return redirect('emphome')

@signin_required
def AcceptApplication(request, *args, **kwargs):
    appid = kwargs.get('id')
    qs = Applications.objects.get(id=appid)
    qs.status = 'accepted'
    qs.save()
    send_mail(
        'Interview Notification',
        'Your job application accepted and interview is scheduled for 5-6-2022.',
        'aradhya.n.sasi101@gmail.com',
        ['aradhyansasi993@gmail.com'],
        fail_silently=False,
    )
    return redirect('emphome')

@method_decorator(signin_required,name="dispatch")
class EmpProfUpdateView(UpdateView):
    model = EmployerProfile
    form_class = EmployerProfileForm
    template_name = 'emp_profUpdate.html'
    success_url = reverse_lazy("emphome")
    pk_url_kwarg = 'id'

    def form_valid(self, form):
        messages.success(self.request, "Profile has been updated successfully")
        return super().form_valid(form)
from django.shortcuts import render, redirect
from django.views.generic import TemplateView, CreateView, DetailView, ListView, UpdateView
from candidateapp.forms import CandProfileForm
from candidateapp.models import CandidateProfile
from employerapp.models import Jobs, Applications
from django.urls import reverse_lazy
from candidateapp.filters import JobFilter
from django.utils.decorators import method_decorator
from candidateapp.decorators import signin_required
from django.contrib import messages
# Create your views here.

@method_decorator(signin_required,name="dispatch")
class CandidateHomeView(TemplateView):
    template_name = 'candhome.html'

    def get(self,request,*args,**kwargs):
        filter = JobFilter(request.GET,queryset=Jobs.objects.all())
        return render(request,'candhome.html',{'filter':filter})



@method_decorator(signin_required,name="dispatch")
class CandProfileCreateView(CreateView):
    model = CandidateProfile
    form_class = CandProfileForm
    template_name = 'candprofileadd.html'
    success_url = reverse_lazy('candhome')

    def form_valid(self, form):
        form.instance.user = self.request.user
        messages.success(self.request, "Profile has been created successfully")
        return super().form_valid(form)

@method_decorator(signin_required,name="dispatch")
class CandProfileView(TemplateView):
    template_name = 'candprofview.html'

@method_decorator(signin_required,name="dispatch")
class CandiJobListView(ListView):
    model = Jobs
    template_name = 'candiJobList.html'
    context_object_name = 'candiJobs'
    paginate_by = 2

@method_decorator(signin_required,name="dispatch")
class CandiJobDetailView(DetailView):
    model = Jobs
    template_name = 'candiJobDetail.html'
    context_object_name = 'job'
    pk_url_kwarg = 'id'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        qs = Applications.objects.filter(applicant=self.request.user,job=self.object)
        context['app']=qs
        return context

@signin_required
def apply_now(request, *args, **kwargs):
    job_id = kwargs.get('id')
    job = Jobs.objects.get(id=job_id)
    applicant = request.user
    Applications.objects.create(applicant=applicant, job=job)
    return redirect('candhome')


@method_decorator(signin_required,name="dispatch")
class MyApplicationView(ListView):
    model = Applications
    template_name = 'candiappliedjobs.html'
    context_object_name = 'applied'

    def get_queryset(self):
        return Applications.objects.filter(applicant=self.request.user)


@method_decorator(signin_required,name="dispatch")
class JobNotificationView(ListView):
    model = Applications
    template_name = 'candi_notification.html'
    context_object_name = 'application'

    def get_queryset(self):
        return Applications.objects.filter(applicant=self.request.user, status='accepted')

@method_decorator(signin_required,name="dispatch")
class CandiProfUpdateView(UpdateView):
    model = CandidateProfile
    form_class = CandProfileForm
    template_name = 'candProfEdit.html'
    success_url = reverse_lazy("candhome")
    pk_url_kwarg = 'id'

    def form_valid(self, form):
        messages.success(self.request, "Profile has been updated successfully")
        return super().form_valid(form)
from typing import Any
import datetime, logging
from django.conf import settings
from django.db import models
from django.forms.models import BaseModelForm
from django.http import Http404, HttpResponse, HttpResponseNotFound
from django.urls import reverse, reverse_lazy
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.views.generic import DetailView, ListView, UpdateView, DeleteView, CreateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models.query import QuerySet
from find_teams.models import Lamaran
from authentication.models import RegisteredUser
from .forms import VacancyCreationForm
from .models import LowonganRegu, TautanMediaSosialLowongan

logger = logging.getLogger('app_api')

class VacancyDetailView(DetailView):
    model = LowonganRegu
    pk_url_kwarg = 'vacancy_id'
    template_name = "find_members/vacancy_detail.html"
    context_object_name = "vacancy"
    
    def get_object(self):
        queryset = self.get_queryset()
        pk = self.kwargs.get(self.pk_url_kwarg)
        
        if pk is not None:
            queryset = queryset.filter(pk=pk)
        else:
            raise AttributeError("VacancyDetailView must be called with either an object pk or a slug.")
    
        try:
            return queryset.get()
        except queryset.model.DoesNotExist:
            res = render(self.request, "find_members/vacancy_detail.html", {"vacancy": None})
            res.status_code = 404
            return res
            # return HttpResponse("LowonganRegu matching query does not exist.", status=404)

class MyVacanciesDetailView(LoginRequiredMixin, ListView):
    model = LowonganRegu
    template_name = "find_members/my_vacancies.html"
    context_object_name = "vacancies"
    
    def get_queryset(self) -> QuerySet[Any]:
        # Return only the vacancies created by the current user
        return self.model.objects.owned_by_user(self.request.user)
        # return LowonganRegu.objects.filter(is_active=True, ketua=self.request.user)

# @login_required(login_url=settings.LOGIN_URL)
# def create_vacancy(request):

#     form = LowonganForm()

#     if request.method == 'POST':
#         form = LowonganForm(request.POST)
        
#         if form.is_valid():
#             lowongan = form.save(commit=False)

#             lowongan.ketua = request.user
#             lowongan.is_active = True
            
#             tautan_medsos_regu = TautanMediaSosialLowongan(
#                 website = request.POST.get('website'),
#                 instagram = request.POST.get('instagram'),
#                 twitter = request.POST.get('twitter'),
#                 linkedin = request.POST.get('linkedin'), 
#                 github = request.POST.get('github'),
#             )
#             tautan_medsos_regu.save()
#             lowongan.tautan_medsos_regu = tautan_medsos_regu

#             lowongan.save()

#             # if succesful, redirect to melihat daftar lowongan
#             return redirect('find_teams:show_vacancies')
        
#     context = {
#         'form': form
#     }

#     # if unsuccesful, reload form and display inputted values
#     for field, errors in form.errors.items():
#                 for error in errors:
#                     messages.error(request, f'{error}')

#     return render(request, 'find_members/create_vacancy.html', context)

class VacancyCreateView(CreateView):
    form_class = VacancyCreationForm
    success_url = reverse_lazy('find_teams:show_vacancies')
    template_name = 'find_members/create_vacancy.html'

    def form_valid(self, form: BaseModelForm) -> HttpResponse:
        return super().form_valid(form)
    
    def get(self, request):
        if not request.user.is_authenticated:
            return redirect(reverse('authentication:login'))
        
        form =  self.form_class()
        form.errors.clear()
        context = {
            "status": "Fetching form",
            "form": form,
        }

        return render(request, self.template_name, context, status=200)
    
    def post(self, request):
        form = self.form_class(request.POST, request.FILES)
        if form.is_valid():
            vacancy = form.save(commit=False)

            vacancy.ketua = request.user
            vacancy.is_active = True
            
            tautan_medsos_regu = TautanMediaSosialLowongan(
                website = request.POST.get('website'),
                instagram = request.POST.get('instagram'),
                twitter = request.POST.get('twitter'),
                linkedin = request.POST.get('linkedin'), 
                github = request.POST.get('github'),
            )
            tautan_medsos_regu.save()
            vacancy.tautan_medsos_regu = tautan_medsos_regu
            vacancy.save()
            messages.success(request, f"Vacancy created!")

            return redirect(self.success_url)
        else:
            # Add error messages for each invalid field
            for error in form.errors.values():
                messages.error(request, error.as_text())

            context = {
                "form": form,  # Pass the form with submitted data back to the template
                "status": "Form submission failed due to invalid data",
            }

            # Re-render the same page with the form containing user's data and errors
            return render(request, self.template_name, context)

class VacancyUpdateView(LoginRequiredMixin, UpdateView):
    model = LowonganRegu
    pk_url_kwarg = 'vacancy_id'
    template_name = "find_members/update_vacancy.html"
    success_url = reverse_lazy("find_teams:show_vacancies")

    fields = [
        'nama_regu', 'deskripsi_lowongan_regu', 'foto_lowongan_regu',
        'nama_lomba', 'bidang_lomba', 'tanggal_lomba', 'expiry',
        'jumlah_anggota_sekarang', 'total_anggota_dibutuhkan',
        'tautan_medsos_regu',
        ]
    def get_object(self):
        queryset = self.get_queryset()
        pk = self.kwargs.get(self.pk_url_kwarg)
        
        if pk is not None:
            queryset = queryset.filter(pk=pk)
        else:
            raise AttributeError("VacancyUpdateView must be called with either an object pk or a slug.")
    
        try:
            return queryset.get()
        except queryset.model.DoesNotExist:
            res = render(self.request, "find_members/update_vacancy.html", {"vacancy": None})
            res.status_code = 404
            return res
    
    def form_valid(self, form: BaseModelForm) -> HttpResponse:
        form.instance.ketua = self.request.user
        return super().form_valid(form)

class VacancyDeleteView(LoginRequiredMixin, DeleteView):
    model = LowonganRegu
    pk_url_kwarg = 'vacancy_id'
    template_name = "find_members/delete_vacancy.html"
    success_url = reverse_lazy("profile:show_my_vacancies")
    context_object_name = "vacancy"

    def get_object(self, queryset=None) -> LowonganRegu:
        try:
            return self.model.objects.get(ketua=self.request.user, id=self.kwargs["vacancy_id"])
        except LowonganRegu.DoesNotExist:
            raise Http404("Vacancy does not exist or you don't have permission to delete it")
    
    
def vacancy_applicants(request, vacancy_id):
    current_user = RegisteredUser.objects.get(id=request.COOKIES.get("user_id"))

    try:
        lowongan = LowonganRegu.objects.get(id=vacancy_id)
        
        # kalo coba access lowongan orang lain dari url, bakal ke redirect ke home aja
        if lowongan.ketua != current_user:
            messages.error(request, "Can't access")
            return redirect("core:home")
            
    except LowonganRegu.DoesNotExist:
        return HttpResponseNotFound("LowonganRegu not found")
    
    applicants = Lamaran.objects.filter(lowongan=lowongan)
    print(len(applicants))

    context = {
        'lowongan' : lowongan,
        'applicants': applicants,
    }

    return render(request, "find_members/vacancy_applicants.html", context)

def terima_tolak_lamaran(request, lamaran_id, status):
    lamaran = Lamaran.objects.get(id=lamaran_id)
    lowongan = lamaran.lowongan

    # Pastikan bahwa yang mengakses tampilan ini adalah pemilik lowongan
    if request.user == lamaran.lowongan.ketua:
        
        # if not lamaran.is_active():
        #     lamaran.status = 'Expired'
        if status == 'Accepted':
            lowongan.jumlah_anggota_sekarang += 1
            lowongan.save()
        lamaran.status = status
        lamaran.save()

    return redirect('find_members:vacancy_applicants', vacancy_id=lowongan.id) 

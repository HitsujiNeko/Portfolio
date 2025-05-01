from django.shortcuts import render, redirect
from django.contrib import messages
from django.views import View
from .models import Profile,MySkill, MyQualification,App
from .forms import ContactForm
from django.shortcuts import get_object_or_404
# Create your views here.

def get_index_context(form=None):
    profile = Profile.objects.first()
    skills = MySkill.objects.all()
    qualifications = MyQualification.objects.all()
    apps = App.objects.all()
    context = {
        "profile": profile,
        "skills": skills,
        "qualifications": qualifications,
        "apps" : apps,
        "form": form or ContactForm(),
    }
    return context


def index(request):
    context = get_index_context()
    return render(request, "portfolio/index.html", context)

class ContactView(View):
    def get(self, request):
        context = get_index_context()
        return render(request, "portfolio/index.html", context)

    def post(self, request):
        form = ContactForm(request.POST)
        if form.is_valid():
            # フォームのデータを処理する
            messages.success(request, "送信が完了しました！")
            return redirect('portfolio_app:index')
        context = get_index_context(form)
        return render(request, "portfolio/index.html", context)
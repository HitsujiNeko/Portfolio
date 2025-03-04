from django.shortcuts import render, redirect
from django.views import View
from .models import MySkill, MyQualification
from .forms import ContactForm
# Create your views here.

# index.htmlを表示する
def index(request):
    skills = MySkill.objects.all()
    qualifications = MyQualification.objects.all()
    form = ContactForm()
    context = {
        "skills": skills,
        "qualifications": qualifications,
        "form": form
    }
    return render(request, "portfolio/index.html", context)

class ContactView(View):
    def post(self, request):
        form = ContactForm(request.POST)
        if form.is_valid():
            # フォームのデータを処理する
            # ここでメールを送信するなどの処理を行う
            return redirect('portfolio_app:index')
        skills = MySkill.objects.all()
        qualifications = MyQualification.objects.all()
        context = {
            "skills": skills,
            "qualifications": qualifications,
            "form": form
        }
        return render(request, "portfolio/index.html", context)
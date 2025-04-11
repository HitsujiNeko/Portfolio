from django.shortcuts import render, redirect
from django.views import View
from .models import Profile,MySkill, MyQualification,BlogPost
from .forms import ContactForm
from django.shortcuts import get_object_or_404
# Create your views here.

# index.htmlを表示する
def index(request):
    profile=Profile.objects.first()
    skills = MySkill.objects.all()
    qualifications = MyQualification.objects.all()
    form = ContactForm()
    blog_posts = BlogPost.objects.all().order_by('-date')
    context = {
        "profile": profile,
        "skills": skills,
        "qualifications": qualifications,
        "form": form,
        'blog_posts': blog_posts, 
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
    
def blog_detail(request, pk):
    post = get_object_or_404(BlogPost, pk=pk)
    return render(request, 'portfolio/blog_detail.html', {'post': post})
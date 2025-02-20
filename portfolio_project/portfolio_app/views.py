from django.shortcuts import render
from django.views import View
# Create your views here.

# index.htmlを表示する
def index(request):
    value_message = "Hello World!"
    return render(request, "portfolio/index.html", context={"value":value_message})
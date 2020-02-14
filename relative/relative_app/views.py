from django.shortcuts import render


# Create your views here.
def index(request):
    context_dict={"text":"hello world","number":100}
    return render(request,'relative_app/index.html',context_dict)

def Relative(request):
    return render(request,'relative_app/relative_url.html')

def other(request):
    return render(request,'relative_app/other.html')

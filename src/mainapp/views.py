
from django.shortcuts import render, get_list_or_404

# Create your views here.
def index(request):
    return render(request, 'mainapp/index.html')

def testing_vue(request):
    return render(request, 'mainapp/testingvue.html')

def test_base(request):
    return render(request, 'mainapp/testbase.html')
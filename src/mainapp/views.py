
from django.shortcuts import render, get_list_or_404

# Create your views here.
def testingVue(request):
    return render(request, 'mainapp/testingVue.html')
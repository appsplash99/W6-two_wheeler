from django.shortcuts import render

# Create your views here.
def homePage(request):
    my_dict={}
    return render(request, template_name='zenful_App/home.html', context=my_dict)

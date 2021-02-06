from django.shortcuts import render

# Create your views here.


# homepage
def homePage(request):
    my_dict={}
    return render(request, template_name='zenfulApp/home.html', context=my_dict)

# aboutPage
def aboutPage(request):
    my_dict = {}
    return render(request, template_name='zenfulApp/about.html', context=my_dict)

# aboutPage
def activitiesPage(request):
    my_dict = {}
    return render(request, template_name='zenfulApp/activities.html', context=my_dict)

# aboutPage
def appsPage(request):
    my_dict = {}
    return render(request, template_name='zenfulApp/apps.html', context=my_dict)
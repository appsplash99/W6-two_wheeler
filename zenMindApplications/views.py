from django.shortcuts import render, redirect



# Create your views here.
def meditateAppPage(request):
    my_dict = {}
    return render(request, 'zenMindApplications/meditateApp.html', context=my_dict)



# Create your views here.
def priorityListAppPage(request):
    my_dict = {}
    return render(request, 'zenMindApplications/priorityListApp.html', context=my_dict)
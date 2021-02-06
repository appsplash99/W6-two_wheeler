from django.shortcuts import render
from django.contrib.auth import get_user_model

# Create your views here.

def userDataPage(request, primary_key):

    User = get_user_model()
    # database query
    User = get_user_model()
    current_user = User.objects.get(id=primary_key)

    my_dict={   'current_user':current_user,
            }
    return render(request, template_name='userDataApp/userdata.html', context=my_dict)

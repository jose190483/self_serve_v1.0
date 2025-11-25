from django.contrib.auth.decorators import login_required
from django.shortcuts import render
@login_required(login_url='login_page')
def home_view(request):

    context={
             }
    return render(request, "ss_app/home.html")
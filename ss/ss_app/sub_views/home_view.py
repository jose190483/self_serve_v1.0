from django.contrib.auth.decorators import login_required
from django.shortcuts import render

@login_required(login_url='login_page')
def home_view(request):
    context={''
             # 'parameter_definition_count':parameter_definition_count,
             # 'parameter_count':parameter_count,
             # 'systems_count':systems_count,
             # 'equipments_count':equipments_count,
             }
    return render(request, "ss_app/home.html")
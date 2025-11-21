from django.shortcuts import render
from django_smart_ratelimit.decorator import rate_limit

# Create your views here.
@rate_limit(key="ip", rate="5/m")
def index(request):
    return render(request, "index.html")
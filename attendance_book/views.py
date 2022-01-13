from django.views.decorators.csrf import csrf_exempt
from django.contrib import messages
from django.shortcuts import render, redirect

from .models import Member


@csrf_exempt
def index(request):

    if request.method == 'POST':
        name = request.POST['name']
        birthdate = request.POST['birthdate']

        result = Member.objects.filter(name=name, birthdate=birthdate)

        if result:
            messages.success(request, "의결권이 있습니다")
            return redirect('index')
            print('true')
        else:
            messages.warning(request, "의결권이 없습니다")
            return redirect('index')
            print('false')

        # return HttpResponse(template.render())
    else:
        return render(request, 'attendance_book/index.html')
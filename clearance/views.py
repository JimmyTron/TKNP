from django.shortcuts import render,redirect
from django.contrib import messages
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView
from django.contrib.auth.decorators import login_required
from .forms import ClearanceRequestForm, RequestForm
from .models import Request

@login_required
def clearance(request):
    if request.method == 'POST':
        form = ClearanceRequestForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            student = form.cleaned_data.get('student')
            messages.success(request, f'Clearance Request for {student}! was submitted successfully.')
            return redirect('Student')
    else:
        form = ClearanceRequestForm(instance=request.user)
    return render(request, 'clearance/clearance.html', {'form':form,'title':'Students Clearane Request'})

class RequestView(CreateView):
    model = Request
    form_class = RequestForm
    template_name = 'request.html'
    success_url = reverse_lazy('request')

def requests(request):
    context = {
        'title': 'Clearance Requests',
        'posts': Request.objects.all()
    }
    return render(request, 'clearance/requests.html',context)

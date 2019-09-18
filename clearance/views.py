from django.shortcuts import render,redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import ClearanceRequestForm

@login_required
def clearance(request):
    if request.method == 'POST':
        form = ClearanceRequestForm(request.POST, instance=request.user.student)
        if form.is_valid():
            form.save()
            student = form.cleaned_data.get('student')
            messages.success(request, f'Clearance Request for {student}! was submitted successfully.')
            return redirect('Student')
    else:
        form = ClearanceRequestForm(instance=request.user)
    return render(request, 'clearance/request.html', {'form':form,'title':'Students Clearane Request'})

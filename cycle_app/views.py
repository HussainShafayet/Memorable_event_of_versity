from django.shortcuts import render,redirect
from .models import Institute_info,Versity_life_cycle
from .forms import Institute_info_Form, Cycle_Form
from django.contrib import messages

# Create your views here.
def home(request):
    return render(request, 'home.html')
    
def add_institute_info(request):
    if request.method == 'POST':
        form = Institute_info_Form(request.POST, user=request.user)
        if form.is_valid():
            form = form.save(commit=False)
            form.user = request.user
            form.save()
            return redirect('/')
        else:
            context = {
                'form':form,
            }
            return render(request,'add_institute_info.html',context)
    else:
        form = Institute_info_Form(user=request.user)
        context = {
            'form':form,
        }
        return render(request, 'add_institute_info.html', context)
        


def add_cycle_info(request):
    if request.method == 'POST':
        form = Cycle_Form(request.POST, user=request.user)
        if form.is_valid():
            form = form.save(commit=False)
            form.user = request.user
            year = form.year
            year = Versity_life_cycle.objects.filter(year=year,user=request.user)
            if not year:
                form.save()
                messages.success(request,'Added Successfully')
                return redirect('/')
            else:
                sem = len(year)
                if sem == 2:
                    form=Cycle_Form(user=request.user)
                    messages.warning(request, 'Year already Added!')
                    context = {
                        'form':form,
                    }
                    return render(request, 'add_cycle_info.html',context)
                else:
                    form.save()
                    messages.success(request,'Added Successfully.')
                    return redirect('/')
    else:
        form = Cycle_Form(user=request.user)
        context = {
            'form':form,
        }
        return render(request, 'add_cycle_info.html', context)


def show_cycle_info(request, year, semester):
    value = Versity_life_cycle.objects.get(user=request.user, year=year, semester=semester)
    institute_value = Institute_info.objects.get(user=request.user)
    context = {
        'value': value,
        'institute_value':institute_value,
    }
    return render(request, 'show.html', context)
    
def all_event(request):
    event = Versity_life_cycle.objects.filter(public=True)
    institute = Institute_info.objects.filter(public=True)
    context = {
        'event': event,
        'institute':institute,
    }
    return render(request,'all_event.html',context)
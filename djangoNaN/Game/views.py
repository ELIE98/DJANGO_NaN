from django.shortcuts import render,redirect
from .forms import UserRegisterForm,UserParisForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.views.generic import ListView
from .models import Equipe,Paris

# Create your views here.


def index(request):
    context = {
        'equipes': Equipe.objects.all()
    }
    return render(request,'Game/index.html',context)



def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request,f'success')
            return redirect('login')
    else:
        form = UserRegisterForm()

    return render(request,'Game/register.html',{'form':form})





def paris(request):
        if request.method == 'POST':
            form = UserParisForm(request.POST)
            if form.is_valid():
                form.save()

                messages.success(request,f'votre paris a été enregisté')
                return redirect('index')
        else:
            form = UserParisForm()

        return render(request,'Game/paris.html',{'form':form})








@login_required
def profile():
    return render(request,'Game/index.html')


class List_equipe(ListView):
    model = Equipe
    template_name = 'Game/index.html'
    context_object_name = 'equipes'
    ordering = ['cote']

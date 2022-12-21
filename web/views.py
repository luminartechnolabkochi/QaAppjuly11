from django.shortcuts import render,redirect

# Create your views here.
from django.views.generic import CreateView,FormView,TemplateView
from .forms import LoginForm,UserRegistrationForm,QuestionForm
from django.urls import reverse_lazy
from django.contrib.auth import authenticate,login


class SignUpView(CreateView):
    template_name="register.html"
    form_class=UserRegistrationForm
    success_url=reverse_lazy("signin")

class SignInView(FormView):
    template_name="login.html"
    form_class=LoginForm
    def post(self, request,*args,**kw):
        form=LoginForm(request.POST)
        if form.is_valid():
            uname=form.cleaned_data.get("username")
            pwd=form.cleaned_data.get("password")
            usr=authenticate(request,username=uname,password=pwd)
            if usr:
                login(request,usr)
                return redirect("index")
            else:
                return render(request,self.template_name,{"form":form})

class IndexView(CreateView):
    template_name="index.html"
    form_class=QuestionForm
    success_url=reverse_lazy("index")



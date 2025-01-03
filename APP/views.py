from django.contrib.auth.forms import AuthenticationForm
from django.forms import BaseModelForm
from django.http import HttpRequest, HttpResponse
from django.shortcuts import render
from .models import *
from .forms import *
from django.views.generic.list import ListView
from django.views.generic import CreateView
from django.contrib.auth.views import LoginView, LogoutView
from django.urls import reverse_lazy, reverse
from django.contrib import messages
import markdown
import re
from django.db.models import Q
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

# import redis

# Create your views here.

# register

class RegisterView(CreateView):
    form_class = RegisterForm
    template_name = 'registration/register.html'
    success_url = reverse_lazy('APP:login')

    def form_valid(self, form: BaseModelForm) -> HttpResponse:
    
        username = form.cleaned_data.get('username')
        userEmail = form.cleaned_data.get('email')

        if User.objects.filter(username=username).exists():
            messages.error(self.request, 'Allready registered. Please Login')
            return self.form_invalid(form)
            
        else:
            form.save()
            messages.success(self.request, 'Registration successful')

            try:
                server = smtplib.SMTP('smtp.gmail.com', 587)
                server.starttls()
                server.login('jayakaraddepalli@gmail.com','vnqw yjgl krqz byje')

                message = 'Thank you'
                mes = MIMEMultipart()
                mes['Subject'] = 'Successfully Registered to My_Blogs'
                mes.attach(MIMEText(message, 'plain'))


                server.sendmail('jayakaraddepalli@gmail.com', userEmail, mes.as_string())
                server.close()

            except:
                message.error(self.request, 'Incorrect mailID')


            return super().form_valid(form)
    
    def form_invalid(self, form: BaseModelForm) -> HttpResponse:
        print('form invalid')
        return super().form_invalid(form)
    

# ==== Login ====

class LoginView(LoginView):
    form_class = LoginForm
    template_name = 'registration/login.html'
    success_url = reverse_lazy('APP:home')

    def form_valid(self, form: AuthenticationForm) -> HttpResponse:
        messages.success(self.request, 'Login successful')
        return super().form_valid(form)
    
    def form_invalid(self, form: AuthenticationForm) -> HttpResponse:
        messages.error(self.request, 'Login failed. Please try again.')
        return super().form_invalid(form)



# ==== Logout ====

class LogoutView(LogoutView):
    template_name = 'registration/logout.html'
    success_url = reverse_lazy('APP:login')

class HomeView(ListView):
    model = homeModel
    template_name = 'Home.html'
    context_object_name = 'items'

    def get_context_data(self, **kwargs: reverse_lazy):
        context = super().get_context_data(**kwargs)

        context['hashes'] = hashTagsModel.objects.all()

        return context

# ===== Category =====

class CategoryBlogs(ListView):
    template_map = {
        'Python' : ('python.html', PythonBlogsModel),
        'HTML5' : ('html5.html', HTMLBlogsModel),
        'CSS3' : ('css3.html', CSSBlogsModel),
        'JS' : ('JS.html', ),
        'Django' : ('django.html', ),
        'SQL' : ('sql.html', ),
        'MYSQL' : ('mysql.html', ),
        'ReactJs' : ('react.html', ),
        'Git' : ('git.html', ),
    }
    

    def get(self, request: HttpRequest, category) -> HttpResponse:
        template, model = self.template_map.get(category, ('github.html', None))
        data = model.objects.all() if model else None
        return render(request, template, {'data':data})
        
    
class Info(ListView):

    def get(self, request, id):
        infor = PythonBlogsModel.objects.get(id=id)
        data = TopicModel.objects.filter(id=id)

        remainingTopics = PythonBlogsModel.objects.exclude(id=id)
        # print(remainingTopics[0].id)
        # print(id)

        nextTopic = PythonBlogsModel.objects.filter(id=id+1).first()
        textContent = 'Next'

        if not nextTopic:
            nextTopic = PythonBlogsModel.objects.filter(id=id+2).first()
        if not nextTopic:
            textContent = 'Completed'


        previousTopic = PythonBlogsModel.objects.filter(id=id-1).first()
        previousText = 'Previous'

        if not previousTopic:
            previousTopic = PythonBlogsModel.objects.filter(id=id-2).first()
        if not previousTopic:
            previousText = ''

        # print(nextTopic)

        # print(remainingTopics)
        
        filtered_lines = []
        headers = []

        for item in data:
            content = markdown.markdown(item.content, extensions=['fenced_code'])
            # Find all headers and create a unique ID
            headers_in_content = re.findall(r'<h3>(.*?)</h3>', content)
            for index, header in enumerate(headers_in_content):
                section_id = f'section_{index}'
                headers.append((section_id, header))
                content = content.replace(f'<h3>{header}</h3>', f'<h3 id="{section_id}">{header}</h3>')
            filtered_lines.append(content)

        return render(request, 'infor.html', {'infor': infor, 'd': filtered_lines, 'headers': headers, 'remainingTopics':remainingTopics[id-1:id+2], 'nextTopic':nextTopic, 'textContent':textContent, 'previousTopic':previousTopic, 'previousText':previousText})
    

class HTMLInfo(ListView):

    def get(self, request, id):
        infor = HTMLBlogsModel.objects.get(id=id)
        data = HTMLTopicModel.objects.filter(id=id)

        remainingTopics = HTMLBlogsModel.objects.exclude(id=id)
        # print(remainingTopics[0].id)
        # print(id)

        nextTopic = HTMLBlogsModel.objects.filter(id=id+1).first()
        textContent = 'Next'

        if not nextTopic:
            nextTopic = HTMLBlogsModel.objects.filter(id=id+2).first()
        if not nextTopic:
            textContent = 'Completed'


        previousTopic = HTMLBlogsModel.objects.filter(id=id-1).first()
        previousText = 'Previous'

        if not previousTopic:
            previousTopic = HTMLBlogsModel.objects.filter(id=id-2).first()
        if not previousTopic:
            previousText = ''

        # print(nextTopic)

        # print(remainingTopics)
        
        filtered_lines = []
        headers = []

        for item in data:
            content = markdown.markdown(item.content, extensions=['fenced_code'])
            # Find all headers and create a unique ID
            headers_in_content = re.findall(r'<h3>(.*?)</h3>', content)
            for index, header in enumerate(headers_in_content):
                section_id = f'section_{index}'
                headers.append((section_id, header))
                content = content.replace(f'<h3>{header}</h3>', f'<h3 id="{section_id}">{header}</h3>')
            filtered_lines.append(content)

        return render(request, 'infor.html', {'infor': infor, 'd': filtered_lines, 'headers': headers, 'remainingTopics':remainingTopics[id-1:id+2], 'nextTopic':nextTopic, 'textContent':textContent, 'previousTopic':previousTopic, 'previousText':previousText})

class CSSInfo(ListView):

    def get(self, request, id):
        infor = CSSBlogsModel.objects.get(id=id)
        data = CSSTopicModel.objects.filter(id=id)

        remainingTopics = CSSBlogsModel.objects.exclude(id=id)
        # print(remainingTopics[0].id)
        # print(id)

        nextTopic = CSSBlogsModel.objects.filter(id=id+1).first()
        textContent = 'Next'

        if not nextTopic:
            nextTopic = CSSBlogsModel.objects.filter(id=id+2).first()
        if not nextTopic:
            textContent = 'Completed'


        previousTopic = CSSBlogsModel.objects.filter(id=id-1).first()
        previousText = 'Previous'

        if not previousTopic:
            previousTopic = CSSBlogsModel.objects.filter(id=id-2).first()
        if not previousTopic:
            previousText = ''

        # print(nextTopic)

        # print(remainingTopics)
        
        filtered_lines = []
        headers = []

        for item in data:
            content = markdown.markdown(item.content, extensions=['fenced_code'])
            # Find all headers and create a unique ID
            headers_in_content = re.findall(r'<h3>(.*?)</h3>', content)
            for index, header in enumerate(headers_in_content):
                section_id = f'section_{index}'
                headers.append((section_id, header))
                content = content.replace(f'<h3>{header}</h3>', f'<h3 id="{section_id}">{header}</h3>')
            filtered_lines.append(content)

        return render(request, 'infor.html', {'infor': infor, 'd': filtered_lines, 'headers': headers, 'remainingTopics':remainingTopics[id-1:id+2], 'nextTopic':nextTopic, 'textContent':textContent, 'previousTopic':previousTopic, 'previousText':previousText})
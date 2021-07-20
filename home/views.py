from django.shortcuts import render, HttpResponse, redirect
# from home.models import Contact,GeeksForm
from home.models import Contact
from blog.models import Post
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth  import authenticate,  login, logout
from .forms import GeeksForm
from .forms import InputForm
from django.core.mail import send_mail
from django.conf import settings
from django.core.mail import EmailMultiAlternatives
from django.template.loader import get_template
from django.template import Context
# from .forms import SubscribeForm
# from .forms import GeeksForm
# Create your views here.
def home(request):
    return render(request, 'home/home.html')
    # return HttpResponse('This is home ')

def contact(request):
    if request.method=="POST":
        name=request.POST['name']
        # name1 is coming from contact.html and as well as other also
        email=request.POST['email']
        phone=request.POST['phone']
        content =request.POST['content']
        
        if len(name)<2 or len(email)<3 or len(phone)<10 or len(content)<4:
            messages.error(request, "Please fill the form correctly")
        else:
            contact=Contact(namea=name, emaila=email, phonea=phone, contenta=content)
            contact.save()
            messages.success(request, "Your message has been successfully sent")
        # namea is coming from models as well as other also
        # contact=Contact(namea=name, emaila=email, phonea=phone, contenta=content)
        # contact.save()
    return render(request, "home/contact.html")


def about(request): 
    return render(request, 'home/about.html')

def search(request):
    query=request.GET['query']
    if len(query)>78:
        allPosts=Post.objects.none()
    else:
        allPostsTitle= Post.objects.filter(title__icontains=query)
        allPostsAuthor= Post.objects.filter(author__icontains=query)
        allPostsContent =Post.objects.filter(content__icontains=query)
        allPosts=  allPostsTitle.union(allPostsContent, allPostsAuthor)
    if allPosts.count()==0:
        messages.warning(request, "No search results found. Please refine your query.")
    params={'allPosts': allPosts, 'query': query}
    return render(request, 'home/search.html', params)

def handleSignUp(request):
    # form = SubscribeForm()
    if request.method=="POST":
        # Get the post parameters
        # form = SubscribeForm(request.POST)
        username=request.POST['username']
        email=request.POST['email']
        fname=request.POST['fname']
        lname=request.POST['lname']
        pass1=request.POST['pass1']
        pass2=request.POST['pass2']




         # check for errorneous input
        if len(username)<5:
            messages.error(request, " Your user name must be more than 5 characters")
            return redirect('home')

        if not username.isalnum():
            messages.error(request, " User name should only contain letters and numbers")
            return redirect('home')
        if (pass1!= pass2):
             messages.error(request, " Passwords do not match")
             return redirect('home')
        
        # Create the user
        myuser = User.objects.create_user(username, email, pass1)
        myuser.first_name= fname
        myuser.last_name= lname
        myuser.save()
        messages.success(request, " Your id  has been successfully created")
#send the mail
        print("save")
        # if email.is_valid():
        htmly = get_template('user/Email.html')
        d = {'username': username}
        subject, from_email, to = 'welcome', 'murli@gmail.com', email
        html_content = htmly.render(d)
        msg = EmailMultiAlternatives(subject, html_content, from_email, [to])
        msg.attach_alternative(html_content, "text/html")
        msg.send()
        # (below one also working fine)
        # message1 = "Your id has been successfully created"
        # recipient = email
        # subject = "Your id"
        # print(recipient)
        # send_mail(subject,
        #         message1, settings.EMAIL_HOST_USER, [recipient], fail_silently=False)
        print("manohar")
        return redirect('home')

    else:
        return HttpResponse("404 - Not found")
def handeLogin(request):
    if request.method=="POST":
        # Get the post parameters
        loginusername=request.POST['loginusername']
        loginpassword=request.POST['loginpassword']

        user=authenticate(username= loginusername, password= loginpassword)
        if user is not None:
            login(request, user)
            messages.success(request, "Successfully Logged In")
            return redirect("home")
        else:
            messages.error(request, "Invalid credentials! Please try again")
            return redirect("home")

    return HttpResponse("404- Not found") 
def handeLogout(request):
    logout(request)
    messages.success(request, "Successfully logged out")
    return redirect("home")


# creating a home view
# def home_view(request):
#     # return render(request, 'home/profile.html')
#     # context = {}
#     # initial_dict = {
#     #     "title" : "My New Title",
#     #     "description" : " A New Description",
#     #     "available":True,
#     #     "email":"abc@gmail.com"
#     # }
# 	# # form = GeeksForm(request.POST or None)
#     # form = GeeksForm(request.POST or None, initial = initial_dict)
    
# 	# context['form']= form
#     context ={}
  
#     # dictionary for initial data with 
#     # field names as keys
#     initial_dict = {
#         "title" : "My New Title",
#         "description" : " A New Description",
#         "available":True,
#         "email":"abc@gmail.com"
#     }
  
#     # add the dictionary during initialization
#     form = GeeksForm(request.POST or None, initial = initial_dict)
  
#     context['form']= form
#     return render(request, "home/profile.html", context)
# 	# return render(request, 'home/profile.html', context)


# from django.shortcuts import render




def home_view_from(request):
	context ={}

	# create object of form
	form = GeeksForm(request.POST or None, request.FILES or None)
	
	# check if form data is valid
	if form.is_valid():
		# save the form data to model
		form.save()

	context['form']= form
	return render(request, "home/profilev.html", context)



 
# Create your views here.
def home_view_m(request):
    context ={}
    context['form']= InputForm()
    return render(request, "home/mymurli.html", context)


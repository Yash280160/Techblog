from .forms import CustomUserForm
from django.contrib import messages
from django.shortcuts import render,redirect,get_object_or_404
from django.contrib import auth
from .models import Ask,Comment
from django.utils import timezone
from basic_app.forms import PostForm,CommentForm


def register(request):
	if request.method == 'POST':
		f = CustomUserForm(request.POST)

		if f.is_valid():
			f.save()
			messages.success(request,"User registered successfully!")
			return redirect('login')

	else:
		f = CustomUserForm()
		
	return render(request, 'basic_app/regis.html', {'form' : f})

def index(request):
	return render(request, 'basic_app/base.html', {})

def login(request):

	if request.method == 'POST':
		username = request.POST.get('username')
		password = request.POST.get('password')
		
		user = auth.authenticate(username = username, password = password)

		if user is not None:
			auth.login(request,user)
			return redirect('index')

		else:
			messages.error(request, "Incorrect Username or password")

	return render(request, 'basic_app/login.html', {})

def logout(request):
	auth.logout(request)
	return render(request, 'basic_app/logout.html', {})

def questions_list(request):
	ques = Ask.objects.filter(created_date__lte = timezone.now()).order_by('-created_date')
	return render(request, 'basic_app/qlist.html', {'ques' : ques})

def post(request):

	if request.method == 'POST':
		post = PostForm(request.POST)

		if post.is_valid():
			form = post.save(commit = False)
			form.author = request.user
			form.created_date = timezone.now()
			form.save()
			return redirect('ques')

	else:
		post = PostForm()
		

	return render(request,'basic_app/post_new.html', {'post' : post})

def post_detail(request,pk):
	post = get_object_or_404(Ask,pk=pk)

	return render(request, 'basic_app/post_detail.html', {'post' : post})

def add_comment_to_post(request,pk):

	post = get_object_or_404(Ask, pk=pk)
	

	if request.method == 'POST':
		form = CommentForm(request.POST)

		if form.is_valid():
			comment = form.save(commit = False)
			comment.author = request.user
			comment.post = post 
			comment.save()

			return redirect('ques')


	else:
		comment = CommentForm()


	return render(request, 'basic_app/add_comment_to_post.html', {'comment' : comment})

def comment_approve(request, pk):
	comment = get_object_or_404(Comment,pk=pk)
	comment.approve()
	return redirect('post_detail', pk=comment.post.pk)


def comment_remove(request, pk):
	comment = get_object_or_404(Comment,pk=pk)
	comment.delete()
	return redirect('post_detail', pk=comment.post.pk)













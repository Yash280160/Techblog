from .forms import CustomUserForm
from django.shortcuts import render,redirect,get_object_or_404
from django.contrib import auth
from .models import Ask,Comment,Questions,Answers
from django.utils import timezone
from basic_app.forms import PostForm,CommentForm,QuesForm,AnswerForm
from django.db.models import Q
from django.contrib import messages



def register(request):
	if request.method == 'POST':
		f = CustomUserForm(request.POST)

		if f.is_valid():
			f.save()
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

	query = request.GET.get('q')
	if query:
		ques = ques.filter(
			Q(title__icontains= query) |
			Q(text__icontains = query)).distinct() 

	return render(request, 'basic_app/qlist.html', {'ques' : ques})

def showQuestions(request):
	ques = Questions.objects.filter(created_date__lte = timezone.now()).order_by('-created_date')
	return render(request,'basic_app/ReadAnswer.html', {'ques' : ques})

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

def detailed(request,pk):
	q = get_object_or_404(Questions,pk=pk)
	answer = Answers.objects.filter(created_date__lte = timezone.now()).order_by('-created_date')
	return render(request,'basic_app/detail.html',{'q':q,'answer':answer})


def askQuestion(request):
	if request.method=='POST':
		form = QuesForm(request.POST)

		if form.is_valid():
			question = form.save(commit=False)
			question.author = request.user
			question.created_date=timezone.now()
			question.save()
			return redirect('Answer')
			

	else:
		question=QuesForm()

	return render(request,'basic_app/QnA.html',{'form':question})


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

def answer_form(request,pk):
	question = get_object_or_404(Questions,pk=pk)

	if request.method == 'POST':
		form = AnswerForm(request.POST)

		if form.is_valid():
			ans = form.save(commit=False)
			ans.created_date = timezone.now()
			ans.author = request.user 
			ans.question = question
			ans.save()

			return redirect('detail',pk=question.pk)

	else:
		ans = AnswerForm()


	return render(request,'basic_app/answer.html', {'AForm':ans} )
















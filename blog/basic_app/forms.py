from django import forms
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from basic_app.models import Ask,Comment,Questions,Answers


class CustomUserForm(forms.Form):
	
	username = forms.CharField(max_length = 15, min_length = 3, label = "Enter Username")
	email = forms.EmailField(label = "Enter email")
	github_link = forms.CharField(label = "Your Github link", max_length = 100, required = False)
	linked_link = forms.CharField(label = "Your Linked-In link", max_length = 100, required=False)
	password1 = forms.CharField(label = "Enter Password", widget = forms.PasswordInput, min_length= 8)
	password2 = forms.CharField(label = "Confirm Password", widget = forms.PasswordInput, min_length= 8)
	

	def clean_username(self):
		username = self.cleaned_data['username'].lower()
		r = User.objects.filter(username = username)

		if r.count():
			raise ValidationError("Sorry! Username already exist")
		return username

	def clean_github_link(self):
		github_link = self.cleaned_data['github_link']
		return github_link

	def clean_linked_link(self):
		linked_link = self.cleaned_data['linked_link']
		return linked_link


	def clean_email(self):
		email = self.cleaned_data['email'].lower()
		r = User.objects.filter(email = email)

		if r.count():
			raise ValidationError("Email already exist!")

		return email

	def clean_password(self):
		password1 = self.cleaned_data.get('password1')
		password2 = self.cleaned_data.get('password2')

		if(password1 and password2 and password1!=password2):
			raise ValidationError("Password does not match!")

		return password2

	def save(self, commit = True):
		user = User.objects.create_user(

			self.cleaned_data['username'],
			self.cleaned_data['email'],
			self.cleaned_data['password2'],
			self.cleaned_data['github_link'],
			self.cleaned_data['linked_link'],
			)

		return user



class PostForm(forms.ModelForm):
	class Meta():
		model = Ask
		fields = ('title', 'text',)

class CommentForm(forms.ModelForm):
	class Meta():
		model = Comment
		fields = ('text',)

class QuesForm(forms.ModelForm):
	class Meta():
		model = Questions
		fields = ('question',)

class AnswerForm(forms.ModelForm):
	class Meta():
		model = Answers
		fields = ('answer',)


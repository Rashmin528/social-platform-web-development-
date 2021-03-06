from django.contrib.auth.models import User
from django.contrib.contenttypes.models import ContentType
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.shortcuts import render, get_object_or_404, redirect
from comments.forms import CommentForm
from comments.models import Comment
from .forms import PostForm
from .models import Posts

def post_create(request):

	form = PostForm(request.POST or None, request.FILES or None)
	if form.is_valid():
		instance = form.save(commit=False)
		instance.user = request.user
		instance.save()
		return redirect('/posts/')

	context = {
		"form": form,
	}
	return render(request, "testing/post_form.html", context)

def post_detail(request, slug=None):
	
	instance = get_object_or_404(Posts, slug=slug)

	initial_data = {
			"content_type": instance.get_content_type,
			"object_id":instance.id
	}
	
	form = CommentForm(request.POST or None, initial=initial_data)
	if form.is_valid():
		c_type = form.cleaned_data.get("content_type")
		content_type = ContentType.objects.get(model=c_type)
		obj_id = form.cleaned_data.get('object_id')
		content_data = form.cleaned_data.get("content")
		parent_obj = None
		try:
			parent_id = int(request.POST.get("parent_id"))
		except:
			parent_id = None

		if parent_id:
			parent_qs = Comment.objects.filter(id=parent_id)
			if parent_qs.exists() and parent_qs.count() == 1:
				parent_obj = parent_qs.first()

		new_comment, created = Comment.objects.get_or_create(
							user = request.user,
							content_type= content_type,
							object_id = obj_id,
							content = content_data,
							parent = parent_obj,
						)
		return HttpResponseRedirect(new_comment.content_object.get_absolute_url())

	comments = instance.comments
	
	context = {
		"instance": instance,
		"comments": comments,
		"comment_form":form,
	}
	return render(request, "testing/post_detail.html", context)

def post_list(request):

	queryset_list = Posts.objects.all()

	paginator = Paginator(queryset_list, 10) # Show 25 contacts per page
	page_request_var = "page"
	page = request.GET.get(page_request_var)
	try:
		queryset = paginator.page(page)
	except PageNotAnInteger:
		# If page is not an integer, deliver first page.
		queryset = paginator.page(1)
	except EmptyPage:
		# If page is out of range (e.g. 9999), deliver last page of results.
		queryset = paginator.page(paginator.num_pages)
	
	context = {
		"object_list": queryset_list,
		"page_request_var":page_request_var
	}
	return render(request, "testing/post_list.html", context)

def post_update(request, slug=None):

	instance = get_object_or_404(Posts, slug=slug)
	form = PostForm(request.POST or None, request.FILES or None,instance=instance)
	
	if form.is_valid():
		instance = form.save(commit=False)
		instance.user = request.user
		instance.save()
		return redirect('/posts/')

	context = {
		"form":form,
	}
	return render(request, "testing/post_form.html", context)

def post_delete(request, slug=None):
	
	instance = get_object_or_404(Posts, slug=slug)
	instance.delete()
	return redirect('/posts/')

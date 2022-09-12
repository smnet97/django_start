from django.shortcuts import render, redirect, get_object_or_404
from .models import PostModel, CategoryModel
from user.models import UserModel
from .forms import PostCreateForm, PostUpdateForm
from django.db.models import Q
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.decorators import login_required

from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


@login_required
def post_create_view(request):
    form = PostCreateForm()

    if request.method == 'POST':
        form = PostCreateForm(data=request.POST, files=request.FILES)
        if form.is_valid():
            post = PostModel(
                title_uz=form.cleaned_data['title_uz'],
                title_ru=form.cleaned_data['title_ru'],
                title_en=form.cleaned_data['title_en'],
                body=form.cleaned_data['body'],
                image=form.cleaned_data['image'],
                user=request.user
            )
            post.save()
            return redirect('index')

    return render(request, 'post-create.html', context={
        'form': form
    })


def home_view(request):
    request.title = _('home page')
    default_page = 1
    page = request.GET.get('page', default_page) # {'page': 2}
    request.session['categories'] = list(CategoryModel.objects.all().values_list('id', flat=True)) # [1, 2, 3]

    paginator = Paginator(PostModel.objects.all().order_by('-id'), 4)
    try:
        items_page = paginator.page(page) # [1, 2, 3, 4, 5, 6] [ 3, 4,]
    except PageNotAnInteger:
        items_page = paginator.page(default_page)
    except EmptyPage:
        items_page = paginator.page(paginator.num_pages)
    search = request.GET.get('q', '')
    if search:
        pass
        # posts = posts.filter(Q(title__icontains=search) | Q(body__icontains=search))

    return render(request, 'index.html', context={
        'posts': items_page,
    })


def category_view(request, id):
    posts = PostModel.objects.filter(category=id)
    request.session['current_cat_id'] = id
    return render(request, 'index.html', context={
        'posts': posts
    })

def post_detail_view(request, id):
    post = PostModel.objects.get(id=id)
    post.post_view = post.post_view + 1
    post.save()
    return render(request, 'post-detail.html', context={
        'post': post
    })


@login_required
def post_delete_view(request, id):
    PostModel.objects.get(id=id).delete()
    return redirect('index')


@login_required
def update_post_view(request, id):
    instance = get_object_or_404(PostModel, id=id)
    form = PostUpdateForm(data=request.POST or None, files=request.FILES or None, instance=instance)
    if form.is_valid():
        form.save()
        return redirect('index')

    return render(request, 'post-update.html', context={
        "form": form
    })

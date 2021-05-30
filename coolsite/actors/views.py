from django.contrib.auth import logout, login
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView
from django.views.generic import ListView, DeleteView, CreateView, FormView
from django.http import HttpResponseNotFound

from django.urls import reverse_lazy
from django.shortcuts import render, redirect

from .forms import AddPostForm, RegisterUserForm, LoginUserForm, ContactForm
from .models import Actor, Category
from .utils import DataMixin, menu


class ActorHome(DataMixin, ListView):
    model = Actor
    template_name = 'actors/index.html'
    context_object_name = 'posts'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title='Главная страница')
        context_items = dict(list(context.items()) + list(c_def.items()))

        return context_items

    def get_queryset(self):
        return Actor.objects.filter(is_published=True).select_related('category')


class AddPage(LoginRequiredMixin, DataMixin, CreateView):
    form_class = AddPostForm
    template_name = 'actors/addpage.html'
    success_url = reverse_lazy('home')
    login_url = reverse_lazy('home')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title='Главная страница')
        context_items = dict(list(context.items()) + list(c_def.items()))

        return context_items


class ContactFormView(DataMixin, FormView):
    form_class = ContactForm
    template_name = 'actors/contact.html'
    success_url = reverse_lazy('home')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title='Обратная связь')
        context_items = dict(list(context.items()) + list(c_def.items()))

        return context_items

    def form_valid(self, form):
        print(form.cleaned_data)

        return redirect('home')




class ShowPost(DataMixin, DeleteView):
    model = Actor
    template_name = 'actors/post.html'
    slug_url_kwarg = 'post_slug'
    context_object_name = 'post'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title=context['post'])
        context_items = dict(list(context.items()) + list(c_def.items()))

        return context_items


class ActorCategory(DataMixin, ListView):
    model = Actor
    template_name = 'actors/index.html'
    context_object_name = 'posts'
    def get_queryset(self):
        return Actor.objects.filter(category__slug=self.kwargs['category_slug'],
                                    is_published=True).select_related('category')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)

        cat = Category.objects.get(slug=self.kwargs['category_slug'])
        c_def = self.get_user_context(title='Категория - ' + str(cat.name),
                                      category_selected=cat.id)
        context_items = dict(list(context.items()) + list(c_def.items()))

        return context_items


class RegisterUser(DataMixin, CreateView):
    form_class = RegisterUserForm
    template_name = 'actors/register.html'
    success_url = reverse_lazy('login')
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title='Регистрация')
        context_items = dict(list(context.items()) + list(c_def.items()))

        return context_items

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)

        return redirect('home')


class LoginUser(DataMixin, LoginView):
    form_class = LoginUserForm
    template_name = 'actors/login.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title='Авторизация')
        context_items = dict(list(context.items()) + list(c_def.items()))

        return context_items

    def get_success_url(self):
        return reverse_lazy('home')


def logout_user(request):
    logout(request)
    return redirect('login')


def about(request):
    actors = Actor.objects.all()

    context = {
        'menu': menu,
        'title': 'О сайте',
        'actors': actors,

    }

    return render(request, 'actors/about.html', context=context)


def page_not_found(request, exception):
    return HttpResponseNotFound('<h1>Страница не найдена</h1>')

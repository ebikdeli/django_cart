from django.shortcuts import render, HttpResponse, redirect
from django.urls import reverse
from django.views.generic.list import ListView
from django.contrib.auth.models import Group, Permission
from django.contrib.auth import get_user_model, authenticate, login, logout
from django.views.generic import FormView, CreateView
from django.urls import reverse_lazy
from django.contrib import messages
from django.forms import formset_factory
from django.db import IntegrityError
# from django.contrib.auth.decorators import permission_required
from django.contrib.auth.mixins import PermissionRequiredMixin

from shop.models import Product
from .forms import LoginForm, UserModelForm, GroupModelForm, PermissionModelForm


# def index(request):
#     return render(request, 'vitrin/templates/vitrin/index.html')


class IndexView(ListView):
    model = Product
    template_name = 'vitrin/templates/vitrin/index.html'
    context_object_name = 'products'
    paginate_by: 6
    
    """
    def get(self, request, *args, **kwargs) -> HttpResponse:
        # print('this view executed to study Simple middleware')
        # print(self.request.META)
        
        if request.user.is_authenticated:
            print(request.user.get_all_permissions())
            print(request.user.get_group_permissions())
            print(request.user.user_permissions.all())
        return super().get(request, *args, **kwargs)
    """


def simple_login(request):
    if request.method == 'POST':
        login_form = LoginForm(data=request.POST)
        if login_form.is_valid():
            user = authenticate(request,
                                username=login_form.cleaned_data['username'],
                                password=request.POST.get('password', None))
            if user:
                login(request, user)
                messages.add_message(request, messages.WARNING, f'{user.username} logged in')
                # print(redirect('vitrin:index'))
                # print(reverse('vitrin:index'))
                return redirect('vitrin:index')

            messages.add_message(request, messages.WARNING, 'User could not login')

    else:
        login_form = LoginForm()
    return render(request, 'vitrin/templates/vitrin/login_form.html', {'form': login_form})


def simple_logout(request):
    logout(request)
    messages.add_message(request, messages.SUCCESS, 'User logout from website')
    # print(reverse('vitrin:index'))
    # print(redirect('vitrin:index'))
    return redirect('vitrin:index')


class CreateUserView(FormView):
    template_name = 'vitrin/templates/vitrin/create_user.html'
    form_class = UserModelForm
    success_url = reverse_lazy('vitrin:index')

    def form_valid(self, form):
        new_user = form.save(commit=False)
        new_user.set_password(new_user.password)
        new_user.save()
        # print(new_user.username)
        print(get_user_model().objects.all())
        messages.add_message(self.request, messages.SUCCESS, f'New user {new_user} created')
        return super().form_valid(form)


class CreateGroupView(CreateView):
    model = Group
    fields = ['name']
    # If we use 'model' and 'field' in CreateView, we don't need 'form_class' anymore
    # form_class = GroupModelForm
    template_name = 'vitrin/templates/vitrin/create_group.html'
    success_url = reverse_lazy('vitrin:index')

    def form_valid(self, form):
        # JUST FOR FUN!
        # print(form.cleaned_data)
        # print(type(form))
        # group = form.save(commit=False)
        # print(group, '   ', type(group), '    ', group.name)
        self.object = form.save()
        # print(self.object, '   ', type(self.object), '    ', self.object.name)
        messages.add_message(self.request, messages.SUCCESS, f'new group {self.object.name} created')
        return super().form_valid(form)


class CreatePermissionView(CreateView):
    form_class = PermissionModelForm
    template_name = 'vitrin/templates/vitrin/create_permission.html'
    success_url = reverse_lazy('vitrin:index')

    def form_valid(self, form):
        self.object = form.save()
        messages.add_message(self.request, messages.SUCCESS, f'new permission {self.object.name} created')
        return super().form_valid(form)


class CreateUserFormset(FormView):
    # Using formset
    # template_name = 'vitrin/templates/vitrin/create_user.html'
    form_class = formset_factory(UserModelForm, extra=4)
    template_name = 'vitrin/templates/vitrin/create_user_formset.html'
    success_url = reverse_lazy('vitrin:index')

    def form_valid(self, form):
        # print(type(form), '    ', form.cleaned_data)
        for f in form:
            # print(type(f), '   ', f.cleaned_data)
            # new_user = f.save(commit=False)
            # print(new_user.username)
            try:
                f.save()
            except IntegrityError:
                messages.add_message(self.request, messages.SUCCESS, 'cant use repititve username')
                return super().form_valid(form)
        return super().form_valid(form)


"""
def create_user(request):
    print(User.objects.all())
    return HttpResponse('<h1>User!</h1>')


def create_group(request):
    print(Group.objects.all())
    return HttpResponse('<h1>Group!</h1>')


def create_permission(request):
    print(Permission.objects.all())
    return HttpResponse('<h1>Permission!</h1>')
"""
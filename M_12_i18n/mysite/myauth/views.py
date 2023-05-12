from django.contrib.auth.decorators import login_required, permission_required, user_passes_test
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.mixins import UserPassesTestMixin
from django.contrib.auth.models import User
from django.contrib.auth.views import LogoutView
from django.http import HttpRequest, HttpResponse, JsonResponse
from django.contrib.auth import authenticate, login
from django.urls import reverse_lazy, reverse
from django.views import View
from django.utils.translation import gettext_lazy, ngettext

from django.views.generic import ListView

from django.views.generic import TemplateView, CreateView, UpdateView, DetailView

from .forms import ImageForm
from .models import Profile


class HelloView(View):
    welcome_message = gettext_lazy('welcome hello world!')

    def get(self, request: HttpRequest) -> HttpResponse:
        items_str = request.GET.get('items') or 0
        items = int(items_str)
        products_line = ngettext(
            'one product',
            '{count} products',
            items,
        )
        products_line = products_line.format(count=items)
        return HttpResponse(
            f'<h1>{self.welcome_message}</h1>'
            f'<h2>{products_line}</h2>',
        )


class AboutMeView(TemplateView):
    template_name = "myauth/about-me.html"


class UserDetailsView(DetailView):
    template_name = 'myauth/user-me.html'
    model = Profile


class UpdateProfileImage(UserPassesTestMixin, UpdateView):
    def test_func(self):
        if self.request.user.is_staff:
            return True
        if self.request.user == self.get_object().user:
            return True

    model = Profile
    template_name = 'myauth/img-update.html'
    form_class = ImageForm

    def get_success_url(self):
        return reverse(
            'myauth:user_me',
            kwargs={'pk': self.object.pk}
        )

    # def form_valid(self, form):
    #     response = super().form_valid(form)
    #


class UpdateAboutMeView(UpdateView):
    model = Profile
    fields = 'bio', 'agreement_accepted', 'avatar'
    template_name = 'myauth/about-me-update.html'

    def get_success_url(self):
        return reverse(
            'myauth:about_me'
        )


class UsersListView(ListView):
    template_name = 'myauth/users-list.html'
    context_object_name = 'users'
    queryset = User.objects.all()


class RegisterView(CreateView):
    form_class = UserCreationForm
    template_name = "myauth/register.html"
    success_url = reverse_lazy("myauth:about-me")

    def form_valid(self, form):
        response = super().form_valid(form)
        Profile.objects.create(user=self.object)
        username = form.cleaned_data.get("username")
        password = form.cleaned_data.get("password1")
        user = authenticate(
            self.request,
            username=username,
            password=password,
        )
        login(request=self.request, user=user)
        return response


class MyLogoutView(LogoutView):
    next_page = reverse_lazy("myauth:login")


@user_passes_test(lambda u: u.is_superuser)
def set_cookie_view(request: HttpRequest) -> HttpResponse:
    response = HttpResponse("Cookie set")
    response.set_cookie("fizz", "buzz", max_age=3600)
    return response


def get_cookie_view(request: HttpRequest) -> HttpResponse:
    value = request.COOKIES.get("fizz", "default value")
    return HttpResponse(f"Cookie value: {value!r}")


@permission_required("myauth.view_profile", raise_exception=True)
def set_session_view(request: HttpRequest) -> HttpResponse:
    request.session["foobar"] = "spameggs"
    return HttpResponse("Session set!")


@login_required
def get_session_view(request: HttpRequest) -> HttpResponse:
    value = request.session.get("foobar", "default")
    return HttpResponse(f"Session value: {value!r}")


class FooBarView(View):
    def get(self, request: HttpRequest) -> JsonResponse:
        return JsonResponse({"foo": "bar", "spam": "eggs"})

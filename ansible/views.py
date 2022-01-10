from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, DeleteView, UpdateView, FormView, CreateView

import ansible.models
from .models import *
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth.hashers import check_password
from django.core.exceptions import ObjectDoesNotExist
from .forms import *
from django.contrib.auth.forms import UserCreationForm



# Create your views here.
def index(request):
    hosts = Host.objects.all()
    return render(request , 'ansible/index.html', context={
        'hosts': hosts,
    })


class HostCreateView(CreateView):
    model = Host
    fields = ['hostname', 'ipaddress', 'role']
    success_url = reverse_lazy('ansible:host-list')


class HostListView(ListView):
    model = Host


class HostUpdateView(UpdateView):
    model = Host
    success_url = reverse_lazy('ansible:host-list')
    fields = ['hostname', 'ipaddress', 'role']
    template_name = 'ansible/host_update.html'


class HostDeleteView(DeleteView):
    model = Host
    template_name = 'ansible/confirm_delete.html'
    success_url = reverse_lazy("ansible:host-list")


class HostGroupCreateView(CreateView):
    model = HostGroup
    fields = ['group', 'host']
    success_url = reverse_lazy('ansible:host-list')


class HostGroupListView(ListView):
    model = HostGroup


class HostGroupUpdateView(UpdateView):
    model = HostGroup
    template_name = "ansible/hostgroup_update.html"
    fields = ['group', 'host']
    success_url = reverse_lazy('ansible:hostgroup-list')


class HostGroupDeleteView(DeleteView):
    model = HostGroup
    template_name = 'ansible/confirm_delete.html'
    success_url = reverse_lazy("ansible:hostgroup-list")


class ScriptCreateView(CreateView):
    model = Script
    fields = ['script_name', 'text', 'description']
    success_url = reverse_lazy('ansible:script-list')


class ScriptListView(ListView):
    model = Script


class ScriptUpdateView(UpdateView):
    model = Script
    template_name = 'ansible/script_form.html'
    fields = ['script_name', 'text', 'description']
    success_url = reverse_lazy('ansible:script-list')


class ScriptDeleteView(DeleteView):
    model = Script
    template_name = 'ansible/confirm_delete.html'
    success_url = reverse_lazy('ansible:script-list')


class RegisterView(FormView):
    form_class = UserCreationForm
    success_url = reverse_lazy('ansible:index')
    template_name = 'ansible/register.html'

    def form_valid(self,form):
        form.save()
        return super(RegisterView, self).form_valid(form)


def operate_host(request):
    """
    操作主机函数视图
    :param request:
    :return:
    """
    hosts = Host.objects.all()
    return render(request, template_name='ansible/operate_host.html', context={'hosts': hosts})


def host_execute(request):
    """
    执行主机操作函数视图
    :param request:
    :return:
    """
    if request.method == 'GET':
        return HttpResponseRedirect(reverse_lazy('ansible:operate-host'))
    if request.method == "POST":
        context = request.POST
        # host = context['host']
        # ip = Host.objects.get(hostname=host).ipaddress
        return render(request, template_name='ansible/execute.html', context={'context': context})


def login(request):
    if request.method == 'GET':
        pass
    if request.method == 'POST':
        account = request.POST.get("account")
        password = request.POST.get("password")
        try:
            item = User.objects.get(account=account)
        except ObjectDoesNotExist:
            return HttpResponse("account does not exist.")

        if check_password(password, item.password):
            return HttpResponseRedirect(reverse_lazy('ansible:index'))
        return HttpResponse("account or password incorrect.")

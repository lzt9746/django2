from django.urls import path
from . import views


app_name = 'ansible'
urlpatterns = [
    # Inventory
    path('', views.index, name='index'),
    path('registration/', views.RegisterView.as_view(), name='registration'),
    path('inventory/hosts/', views.HostListView.as_view(), name='host-list'),
    path('inventory/host/create/', views.HostCreateView.as_view(), name='host-create'),
    path('inventory/host/update/<int:pk>/', views.HostUpdateView.as_view(), name='host-update'),
    path('inventory/host/delete/<int:pk>/', views.HostDeleteView.as_view(), name='host-delete'),
    path('inventory/hostgroups/', views.HostGroupListView.as_view(), name='hostgroup-list'),
    path('inventory/hostgroup/create/', views.HostGroupCreateView.as_view(), name='hostgroup-create'),
    path('inventory/hostgroup/update/<int:pk>', views.HostGroupUpdateView.as_view(), name='hostgroup-update'),
    path('inventory/hostgroup/delete/<int:pk>', views.HostGroupDeleteView.as_view(), name='hostgroup-delete'),
    path('inventory/scripts/', views.ScriptListView.as_view(), name='script-list'),
    path('inventory/script/create/', views.ScriptCreateView.as_view(), name='script-create'),
    path('inventory/script/update/<int:pk>', views.ScriptUpdateView.as_view(), name='script-update'),
    path('inventory/script/delete/<int:pk>', views.ScriptDeleteView.as_view(), name='script-delete'),
    # Operation
    path('operation/host', views.operate_host, name='operate-host'),
    path('operation/host/execute', views.host_execute, name='operate-host-execute'),
]
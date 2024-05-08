from django.urls import path

from .views import CommissionListView, CommissionDetailView, CommissionCreateView, JobCreateView, CommissionUpdateView, JobUpdateView, JobApplicationUpdateView


urlpatterns = [
    path('list', CommissionListView.as_view(), name="list"),
    path('detail/<int:pk>', CommissionDetailView.as_view(),
         name="commission_detail"),
    path('add', CommissionCreateView.as_view(), name="add"),
    path('detail/<int:pk>/add', JobCreateView.as_view(), name="add_job"),
    path('<int:pk>/edit', CommissionUpdateView.as_view(), name="update"),
    path('jobs/<int:pk>/edit/', JobUpdateView.as_view(), name="update_job"),
    path('commissions/<int:commission_pk>/jobs/<int:job_pk>/applications/<int:pk>/update/',
         JobApplicationUpdateView.as_view(), name="update_job_application"),

]

app_name = 'commissions'

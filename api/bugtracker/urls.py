from django.urls import path

from .views import ProjectList, ProjectDetail, IssueListView, IssueDetailView

urlpatterns = [
    path('', ProjectList.as_view()),
    path('<uuid:pk>/', ProjectDetail.as_view()),
    path('issues/', IssueListView.as_view()),
    path('issues/<uuid:pk>/', IssueDetailView.as_view()),
]

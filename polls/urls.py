from django.urls import path, include
from . import api_views

urlpatterns = [
	path("auth/", include("djoser.urls")),
	path("auth/", include("djoser.urls.authtoken")),
	path("polls/create/", api_views.CreatePollView.as_view(), name="poll_create"),
	path("polls/", api_views.ListPollsView.as_view(), name="poll_list"),
	path("polls/vote/<int:pk>/", api_views.VoteView.as_view(), name="vote"),
	path("polls/<int:pk>/", api_views.PollDetailsView.as_view(), name="poll_details"),
]

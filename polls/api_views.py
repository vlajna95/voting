from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from .permissions import IsPollAuthor
from . import models
from . import serializers


class CreatePollView(generics.CreateAPIView):
	queryset = models.Poll.objects.all()
	serializer_class = serializers.PollSerializer
	permission_classes = [IsAuthenticated]


class ListPollsView(generics.ListAPIView):
	queryset = models.Poll.objects.all()
	serializer_class = serializers.PollSerializer
	permission_classes = [IsAuthenticated]


class VoteView(generics.UpdateAPIView):
	queryset = models.Choice.objects.all()
	serializer_class = serializers.VoteSerializer
	permission_classes = [IsAuthenticated]


class PollDetailsView(generics.RetrieveUpdateDestroyAPIView):
	queryset = models.Poll.objects.all()
	serializer_class = serializers.PollDetailsSerializer
	permission_classes = [IsPollAuthor]

from rest_framework import serializers
from .models import Poll, Question, Choice


class ChoiceSerializer(serializers.ModelSerializer):
	class Meta:
		model = Choice
		fields = ["id", "choice_text"]


class QuestionSerializer(serializers.ModelSerializer):
	choices = ChoiceSerializer(many=True, required=False)

	class Meta:
		model = Question
		fields = ["id", "question_text", "choices"]

	def create(self, validated_data):
		if "choices" in validated_data:
			choices_data = validated_data.pop("choices")
			question = Question.objects.create(**validated_data)
			for choice_data in choices_data:
				choice = Choice.objects.create(question=question, **choice_data)
			return question
		return Question.objects.create(**validated_data)


class PollSerializer(serializers.ModelSerializer):
	author = serializers.HiddenField(default=serializers.CurrentUserDefault())
	questions = QuestionSerializer(many=True, required=False)

	class Meta:
		model = Poll
		fields = ["id", "title", "description", "questions", "author", "pub_date"]

	def create(self, validated_data):
		if "questions" in validated_data:
			questions_data = validated_data.pop("questions")
			poll = Poll.objects.create(**validated_data)
			for question_data in questions_data:
				if "choices" in question_data:
					choices_data = question_data.pop("choices")
					question = Question.objects.create(poll=poll, **question_data)
					for choice_data in choices_data:
						choice = Choice.objects.create(question=question, **choice_data)
			return poll
		return Poll.objects.create(**validated_data)


class VoteSerializer(serializers.ModelSerializer):
	class Meta:
		model = Choice
		fields = ["id", "question", "choice_text", "votes"] # ["votes"]
		read_only = ["id", "choice_text", "question"]

	def update(self, instance, validated_data):
		instance.votes += 1
		instance.save()
		return instance


class ChoiceWithVotesSerializer(serializers.ModelSerializer):
	class Meta:
		model = Choice
		fields = ["id", "question", "choice_text", "votes"]


class QuestionWithVotesSerializer(serializers.ModelSerializer):
	choices = ChoiceWithVotesSerializer(many=True, required=False)

	class Meta:
		model = Question
		fields = ["id", "poll", "question_text", "choices"]


class PollDetailsSerializer(serializers.ModelSerializer):
	questions = QuestionWithVotesSerializer(many=True)

	class Meta:
		model = Poll
		fields = ["id", "title", "description", "questions", "author", "pub_date"]

from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()


class Poll(models.Model):
	title = models.CharField(max_length=200, verbose_name="Naslov ankete")
	description = models.TextField(verbose_name="Opis ankete")
	author = models.ForeignKey(User, on_delete=models.CASCADE, related_name="polls", verbose_name="Autor")
	pub_date = models.DateTimeField(auto_now_add=True, verbose_name="Datum objavljivanja")

	class Meta:
		ordering = ["pub_date", "title"]
		verbose_name = "Anketa"
		verbose_name_plural = "Ankete"

	def __str__(self):
		return self.title


class Question(models.Model):
	poll = models.ForeignKey(Poll, on_delete=models.CASCADE, related_name="questions", verbose_name="Anketa")
	question_text = models.CharField(max_length=200, verbose_name="Tekst pitanja")

	class Meta:
		# ordering = ["question_text"]
		verbose_name = "Pitanje"
		verbose_name_plural = "Pitanja"

	def __str__(self):
		return self.question_text


class Choice(models.Model):
	question = models.ForeignKey(Question, on_delete=models.CASCADE, related_name="choices", verbose_name="Pitanje")
	choice_text = models.CharField(max_length=200, verbose_name="Tekst opcije")
	votes = models.IntegerField(default=0, verbose_name="Glasovi")

	class Meta:
		# ordering = ["-votes"]
		verbose_name = "Opcija"
		verbose_name_plural = "Opcije"

	def __str__(self):
		return self.choice_text

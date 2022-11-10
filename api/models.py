from django.db import models
from django.contrib.auth.models import User


class Questions(models.Model):
    title=models.CharField(max_length=250)
    description=models.CharField(max_length=250)
    image=models.ImageField(upload_to="images",null=True)
    created_date=models.DateField(auto_now_add=True)
    user=models.ForeignKey(User,on_delete=models.CASCADE)

    @property
    def question_answers(self):
        return self.answers_set.all()


    def __str__(self):
        return self.title


class Answers(models.Model):
    question=models.ForeignKey(Questions,on_delete=models.CASCADE)
    answer=models.CharField(max_length=200)
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    upvote=models.ManyToManyField(User,related_name="upvote")
    created_date=models.DateField(auto_now_add=True)

    def __str__(self):
        return self.answer

    @property
    def votecount(self):
        return self.upvote.all().count()

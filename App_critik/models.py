from django.db import models

class new_movie(models.Model):
    movie_name = models.CharField(max_length = 40)
    movie_release_year = models. IntegerField()
    movie_genre = models.CharField(max_length = 40)
    movie_director = models.CharField(max_length = 40)
    movie_protagonist = models.CharField(max_length = 40)
    movie_poster = models.CharField(max_length = 150)

class new_tvshow(models.Model):
    show_name = models.CharField(max_length = 40)
    show_release_year = models. IntegerField()
    show_director = models.CharField(max_length = 40)
    show_protagonist = models.CharField(max_length = 40)
    show_poster = models.CharField(max_length = 150)

class new_movie_review(models.Model):
    movie_score = models.IntegerField()
    favorite_movie_character = models.CharField(max_length = 30)
    movie_review = models.CharField(max_length = 250)

class new_show_review(models.Model):
    show_score = models.IntegerField()
    favorite_show_character = models.CharField(max_length = 30)
    show_review = models.CharField(max_length = 250)

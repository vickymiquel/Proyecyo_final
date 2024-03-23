from django.db import models

class new_movie(models.Model):
    movie_name = models.CharField(max_length = 60)
    movie_release_year = models. IntegerField()
    movie_genre = models.CharField(max_length = 40)
    movie_director = models.CharField(max_length = 40)
    movie_protagonist = models.CharField(max_length = 40)
    movie_poster = models.ImageField(upload_to = "posters", null=True, blank=True)
    def __str__(self):
        return f"{self.movie_release_year} - {self.movie_name}"

class new_show(models.Model):
    show_name = models.CharField(max_length = 60)
    show_release_year = models. IntegerField()
    show_genre = models.CharField(max_length = 40)
    show_director = models.CharField(max_length = 40)
    show_protagonist = models.CharField(max_length = 40)
    show_poster = models.ImageField(upload_to = "posters", null=True, blank=True)
    def __str__(self):
        return f"{self.show_release_year} - {self.show_name}"

class new_movie_review(models.Model):
    movie_score = models.IntegerField()
    favorite_movie_character = models.CharField(max_length = 30)
    movie_review = models.CharField(max_length = 250)

class new_show_review(models.Model):
    show_score = models.IntegerField()
    favorite_show_character = models.CharField(max_length = 30)
    show_review = models.CharField(max_length = 250)
    def __str__(self):
        return f"{self.show_score} - {self.show_review}"

from django.db import models

class Blog(models.Model):
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=1000)
    date = models.DateField()
    author = models.CharField(max_length=25)
    class Meta:
        db_table = "blog"

    # def __str__(self):
    #     return self.name

    # def edit_blog(self, title, description, date, author):
    #     self.title= title
    #     self.description = description
    #     self.date = date
    #     self.author = author
    #     self.save()
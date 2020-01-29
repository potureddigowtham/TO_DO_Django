from django.db import models
from django.shortcuts import redirect, reverse

Label_Choices = (
  ('primary' , 'primary'),
  ('secondary' , 'secondary'),
  ('success' , 'success'),
  ('danger' , 'danger'),
  ('warning' , 'warning'),
  ('info' , 'info')
)

class Note(models.Model):
  title = models.CharField(max_length=100)
  due_date = models.DateTimeField()
  label = models.CharField(choices=Label_Choices,max_length=10)
  finished = models.BooleanField(default=False)

  def __str__(self):
    return self.title

  def get_finish_item_url(self):
    return reverse("finish-item", kwargs={
      'id': self.id
    })

  def get_not_finish_item_url(self):
    return reverse("not-finish-item", kwargs={
      'id': self.id
    })

  def get_delete_item_url(self):
    return reverse("delete-item", kwargs={
      'id': self.id
    })


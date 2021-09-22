from django.db import models

# Create your models here.
class TodoTitile(models.Model):
    id=models.AutoField(primary_key=True)
    title_name=models.CharField(max_length=255)
    created_at=models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.title_name
    

class Task(models.Model):
    id=models.AutoField(primary_key=True)
    task_name=models.CharField(max_length=255)
    todoTitileid=models.ForeignKey(TodoTitile,on_delete=models.CASCADE)
    complete=models.BooleanField(default=False)
    created_at=models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.task_name
class Meta:
    ordering= ['complete']
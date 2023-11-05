from django.db import models
import datetime

# Create your models here.
class Task(models.Model): # By defining your data models using Django's models module, you can easily work with your database without writing raw SQL queries, making it more convenient and maintainable for building web applications.
    def __str__(self):
        return self.name
    name=models.CharField(max_length=100)
    priority=models.IntegerField()
    date=models.DateField(default=datetime.date.today)
# and after this code written you type makemigratins in cmd after open same directory  
# makemigrations command is used to create new database migration files based on the changes you have made to your Django models 
# next step is type python manage.py migrate
# migrate command is used in the command-line interface (CLI) to apply changes to your database schema
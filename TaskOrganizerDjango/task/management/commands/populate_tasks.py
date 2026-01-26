from datetime import datetime, timedelta
from task.models import Task
from django.core.management import BaseCommand
import random 

class Command(BaseCommand):
    #This will insert some duplicate tasks

    def handle(self,*args,**options):
        Title=[
            "Complete Project Documentation",
            "Fix Login Bug",
            "Design Database Schema"
        ]

        Description=[
            "Write comprehensive documentation for the new feature implementation including API endpoints, usage examples, and integration guides.",
            "Common login bugs include invalid credentials errors, account lockouts after failed attempts, expired or invisible CAPTCHA, session timeouts, and incorrect system time causing authentication failure.  Other issues involve browser cache/cookies, descriptive error messages exposing security details, and lack of HTTPS enforcement. ",
            "Database Schema Design Task Description: Design a structured database to store tasks, including fields such as task title, description, status (e.g., New, In-Progress, Completed), priority, due date, creation and update timestamps, and user or project association. Include support for task metadata, tags, and relationships like subtasks or comments. Ensure normalization, data integrity, and scalability for future extensions."
        ]

    
        for title,description in zip(Title,Description):
            status=random.choice([choice[0] for choice in Task.STATUS_CHOICES])

            duedate=datetime.now().date() + timedelta(days=random.randint(1, 30))

            Task.objects.create(title=title,description=description,status=status,duedate=duedate)

        self.stdout.write(self.style.SUCCESS("Completed inserted successfully"))
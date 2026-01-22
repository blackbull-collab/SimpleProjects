from blog.models import category, post
from django.core.management import BaseCommand


class Command(BaseCommand):
    help="This command inserts the categories data"

    def handle(self, *args, **options):


        category.objects.all().delete()

        categories=["sports","Technology","science","Art","Food"]
        

        for category_name in categories:
            category.objects.create(name=category_name)

        self.stdout.write(self.style.SUCCESS("Completed inserting data"))
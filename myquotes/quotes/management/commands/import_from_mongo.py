import json
import os
from django.core.management.base import BaseCommand
from ...models import Author, Quote  # Ensure this import is correct
from django.conf import settings


class Command(BaseCommand):
    help = "Migrate data from MongoDB export JSON files into PostgreSQL"

    def add_authors(self, authors_file_path):
        with open(authors_file_path, 'r', encoding='utf-8') as file:
            authors_data = json.load(file)
            for author_data in authors_data:
                author, created = Author.objects.get_or_create(
                    fullname=author_data['fullname'],
                    defaults={
                        'born_date': author_data.get('born_date', ''),
                        'born_location': author_data.get('born_location', ''),
                        'description': author_data.get('description', ''),
                    }
                )
                if created:
                    self.stdout.write(self.style.SUCCESS(f'Author "{author.fullname}" created.'))
                else:
                    self.stdout.write(self.style.WARNING(f'Author "{author.fullname}" already exists.'))

    def add_quotes(self, quotes_file_path):
        quotes_full_path = os.path.join(settings.BASE_DIR, quotes_file_path)
        with open(quotes_full_path, 'r', encoding='utf-8') as file:
            quotes_data = json.load(file)
            for quote_data in quotes_data:
                author_fullname = quote_data['author']
                author = Author.objects.get(fullname=author_fullname)
                quote, created = Quote.objects.get_or_create(
                    quote=quote_data['quote'],
                    defaults={'author': author}
                )
                if created:
                    self.stdout.write(self.style.SUCCESS(f'Quote "{quote.quote}" created.'))
                else:
                    self.stdout.write(self.style.WARNING(f'Quote "{quote.quote}" already exists.'))

    def handle(self, *args, **options):
        authors_file_path = os.path.join(settings.BASE_DIR, 'quotes', 'data', 'authors.json')
        quotes_file_path = os.path.join(settings.BASE_DIR, 'quotes', 'data', 'quotes.json')

        self.add_authors(authors_file_path)
        self.add_quotes(quotes_file_path)
        self.stdout.write(self.style.SUCCESS('Data migration completed successfully.'))

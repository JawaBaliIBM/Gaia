import sys, logging, traceback
sys.path.append("..")

from django.core.management.base import BaseCommand
from gaia.dao.db_client import db_client

class Command(BaseCommand):
    help = 'Create random users'

    def handle(self, *args, **kwargs):
        try:
            self.__create_articles()
            self.__create_brands()

            self.stdout.write(self.style.SUCCESS('Success create database schema!'))
        except:
            self.stdout.write(self.style.SUCCESS('Failed create database schema!'))
            traceback.print_exc()

    def __create_articles(self):
        # create database articles
        db = db_client.create_database('articles', throw_on_exist=False)
        index = db.create_query_index(
            index_name='brand-index',
            fields=['brand']
        )

    def __create_brands(self):
        # create database brands
        db = db_client.create_database('brands', throw_on_exist=False)
        index = db.create_query_index(
            index_name='name-index',
            fields=['name']
        )
        index.create()


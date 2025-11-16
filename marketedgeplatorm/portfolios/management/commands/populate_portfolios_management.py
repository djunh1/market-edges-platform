from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model
import random

from portfolios.models import Category, Portfolio, Stock, Review
from users.models import Profile, AbstractBaseUser

class Command(BaseCommand):
    help = 'Populates database with portfolios'

    def add_arguments(self, parser):
        parser.add_argument('n', type=int)

    def handle(self, *args, **options):

        '''
        Users
        '''
        User = get_user_model()

        user1 = User.objects.create_user(email="hail@caesar.com", 
                                        password="test", 
                                        username="julius_caesar")
        
        user2 = User.objects.create_user(email="test@edm.com", 
                                        password="test", 
                                        username="armin_miran")
        
        user3 = User.objects.create_user(email="test@book.com", 
                                        password="test", 
                                        username="trader_florida")
        

        profile1  = Profile.objects.order_by('?')[0]
        profile2  = Profile.objects.order_by('?')[0]
        profile3  = Profile.objects.order_by('?')[0]

        """
        # Category #
        """
        category1 = Category.objects.get(pk=1)
        category2 = Category.objects.get(pk=2)
        category4 = Category.objects.get(pk=4)
        
        """
        # Portfolio #
        """
        for i in range(options['n']):
            category = category1 

            name = 'Tonys Swing Portoflio' if random.randint(0, 1) == 0 else ('Dan Zangers portfolio' if random.randint(0, 1) == 0 else 'Stock Bee Special')
            description = 'Solid long term portfolio' if random.randint(0, 1) == 0 else ('Swing trading only' if random.randint(0, 1) == 0 else 'Via Pairoli 33')

            order = Portfolio.objects.create(
                name = name, 
                owner = profile1,
                description = description,
                category = category)

            order.save()

        """
        # Portfolio #
        """
        for i in range(options['n']):
            category = category2

            name = 'The Fast and the Turious portfolio' if random.randint(0, 1) == 0 else ('George Washingtons Portoflio' if random.randint(0, 1) == 0 else 'Notorious BIG')
            description = 'A great portoflio' if random.randint(0, 1) == 0 else ('Day trading mostly.  Not sure how to update this...' if random.randint(0, 1) == 0 else 'Du')

            order = Portfolio.objects.create(
                name = name, 
                owner = profile2,
                description = description,
                category = category)

            order.save()

        """
        # Portfolio #
        """
        for i in range(options['n']):
            category = category2

            name = 'Dougs Swing Portoflio' if random.randint(0, 1) == 0 else ('Pradeeps 9m EP' if random.randint(0, 1) == 0 else 'Wu tang ifnancial')
            description = 'Long term portfolio with long term prospects' if random.randint(0, 1) == 0 else ('Swing trading mostly, with some investment' if random.randint(0, 1) == 0 else 'When is a dip coming?')

            order = Portfolio.objects.create(
                name = name, 
                owner = profile3,
                description = description,
                category = category)

            order.save()
           
from django.core.management.base import BaseCommand
import random

from portfolios.models import Portfolio, Stock

class Command(BaseCommand):
    help = 'Populates database with stocks'

    def add_arguments(self, parser):
        parser.add_argument('n', type=int)

    def handle(self, *args, **options):
        
        """
        # Portfolio #
        """
        portfolio1 = Portfolio.objects.order_by('?')[0]
        portfolio2 = Portfolio.objects.order_by('?')[0]
        portfolio3 = Portfolio.objects.order_by('?')[0]


        """
        # Stock with first portfolio
        """
        for i in range(options['n']):
            
            portfolio = portfolio1 

            ticker_name = 'NVDA' if i == 0 else ('TSLA' if i == 1 else ('KLAC' if i == 2 else ('AAPL' if i == 3 else 'GOOG')))
            company_name = 'Nvidia' if i == 0 else ('Tesla' if i == 1 else ('KLA Coporation' if i == 2 else ('Unoriginal apple' if i == 3 else 'Google Inc')))
            sector = 'Electronic Technologuy' if i == 0 else ('Customer Discretionairy' if i == 1 else ('Semiconductors' if i == 2 else ('Who cares' if i == 3 else 'Censorship')))
           
            stock = Stock.objects.create(
                ticker = ticker_name,
                company_name =company_name,
                sector = sector,
                portfolio = portfolio
                )
            stock.save()

        """
        # Stock with 2nd portfolio
        """
        for i in range(options['n']):
            
            portfolio = portfolio2

            ticker_name = 'TGLS' if i == 0 else ('ANET' if i == 1 else ('TRMB' if i == 2 else ('TDOC' if i == 3 else 'MNMD')))
            company_name = 'Technaglass' if i == 0 else ('Arista Networks' if i == 1 else ('Trimble' if i == 2 else ('teledoc' if i == 3 else 'Mind mend')))
            sector = 'GLass?' if i == 0 else ('Electronic Technology' if i == 1 else ('Industrials' if i == 2 else ('Healthcare' if i == 3 else 'biotech')))
           
            stock = Stock.objects.create(
                ticker = ticker_name,
                company_name =company_name,
                sector = sector,
                portfolio = portfolio
                )
            stock.save()

        """
        # Stock with 3nd portfolio
        """
        for i in range(options['n']):
            
            portfolio = portfolio3

            ticker_name = 'SHOP' if i == 0 else ('UBER' if i == 1 else ('GTAT' if i == 2 else ('SDRL' if i == 3 else 'SLCA')))
            company_name = 'Shopify' if i == 0 else ('Uber' if i == 1 else ('GT Advanced technologies' if i == 2 else ('seadrill' if i == 3 else 'US Silica holdings')))
            sector = 'etf' if i == 0 else ('Electronic Technology' if i == 1 else ('Bankrupt' if i == 2 else ('energy' if i == 3 else 'energy')))
           
            stock = Stock.objects.create(
                ticker = ticker_name,
                company_name =company_name,
                sector = sector,
                portfolio = portfolio
                )
            stock.save()
       
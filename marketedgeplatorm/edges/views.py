from datetime import datetime, timedelta

from django.shortcuts import render, redirect

from api.service.stock_bar_service import StockBarService

import api.helpers.clients as helper_clients

def edges(request):




    context = {'edge': "test"}


    return render(request, 'edges/home.html', context)


def daily_odds(request):
    end_date = datetime.now().date()
    start_date = end_date - timedelta(days=90)  # 3 months ago (approximately)

    context = {
        'default_start_date': start_date.strftime('%Y-%m-%d'),
        'default_end_date': end_date.strftime('%Y-%m-%d')
    }




    if request.method == 'POST':
        stock_ticker = request.POST.get('ticker', '').strip().upper()
        start_date = request.POST.get('start_date', '')
        end_date = request.POST.get('end_date', '')

        stock_api_client = helper_clients.FmpAPIClient(stock_ticker)
        stock_price_data = stock_api_client.get_stock_data()

        stock_service = StockBarService(start_date, end_date, stock_ticker)
        hit_matrix_json = stock_service.generate_weekday_hit_matrix_response(stock_price_data)

        context = {'stock_ticker': stock_ticker, 'json': hit_matrix_json}
        return render(request, 'edges/daily_odds.html', context)

    return render(request, 'edges/daily_odds.html', context)

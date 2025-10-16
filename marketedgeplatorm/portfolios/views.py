from django.core import paginator
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.shortcuts import render, redirect

from django.http import HttpResponse
from .models import Portfolio, Tag, Stock
from .forms import PortfolioForm, ReviewForm, StockForm
from .utils import searchPortfolios, paginatePortfolios



@login_required(login_url="login")
def portfolios(request):
    portfolios, search_query = searchPortfolios(request)
    custom_range, portfolios = paginatePortfolios(request, portfolios, 15)

    context = {'portfolios': portfolios, 'search_query': search_query, 'custom_range': custom_range}
    return render(request, 'portfolios/portfolios.html', context)

@login_required(login_url="login")
def portfolio(request, pk):
    portfolioObj = Portfolio.objects.get(id=pk)
    form = ReviewForm()
    stockForm = StockForm()
    ownPortfolio = (portfolioObj.owner == request.user.profile)

    stockList = portfolioObj.stock_set.all()

    if request.method == 'POST':
        form = ReviewForm(request.POST)
        # stockForm = StockForm(request.POST)
        review = form.save(commit=False)
        review.portfolio = portfolioObj
        review.owner = request.user.profile
        review.save()

        #portfolioObj.getVoteCount

        messages.success(request, 'Comment successfully posted.')
        return redirect('portfolio', pk=portfolioObj.id)
    return render(request, 'portfolios/portfolio.html', {'portfolio': portfolioObj, 
                                                         'form': form, 
                                                         'stocklist': stockList,
                                                         'stockform': stockForm,
                                                         'owner': ownPortfolio})

@login_required(login_url="login")
def stock(request, pk):
    return HttpResponse('Caesar')

@login_required(login_url="login")
def createPortfolio(request):
    profile = request.user.profile
    portfolio_form = PortfolioForm()
    
    if request.method == 'POST':
        newtags = request.POST.get('newtags').replace(',',  " ").split()
        portfolio_form = PortfolioForm(request.POST)
        if portfolio_form.is_valid():
            portfolio = portfolio_form.save(commit=False)
            portfolio.owner = profile
            portfolio.save()

            for tag in newtags:
                tag, created = Tag.objects.get_or_create(name=tag)
                portfolio.tags.add(tag)

            return redirect('account')
    context = {'form': portfolio_form}
    return render(request, 'portfolios/portfolio_form.html', context)

@login_required(login_url="login")
def updatePortfolio(request, pk):
    profile = request.user.profile
    portfolio = profile.portfolio_set.get(id=pk) # Good test that another user can not get this set
    portfolio_form  = PortfolioForm(instance=portfolio)

    if request.method == 'POST':
        newtags = request.POST.get('newtags').replace(',',  " ").split()

        portfolio_form = PortfolioForm(request.POST, instance=portfolio)
        if portfolio_form.is_valid():
            portfolio = portfolio_form.save()
            for tag in newtags:
                tag, created = Tag.objects.get_or_create(name=tag)
                portfolio.tags.add(tag)

            return redirect('account')

    context = {'form': portfolio_form , 'portfolio': portfolio}
    return render(request, "portfolios/portfolio_form.html", context)

@login_required(login_url="login")
def deletePortfolio(request, pk):
    portfolio = Portfolio.objects.get(id=pk)
    if request.method == 'POST':
        portfolio.delete()
        return redirect('account')
    
    context = {'object': portfolio}
    return render(request, 'delete_template.html', context)  

@login_required(login_url="login")
def addStock(request, pk):
    portfolio = Portfolio.objects.get(id=pk)
    if request.method == 'POST':
        stock_form = StockForm(request.POST, portfolio)
        if stock_form.is_valid():
            stock = stock_form.save(commit=False)
            stock.portfolio = portfolio
            stock.save()


    return redirect('portfolio', pk=portfolio.id)

    
@login_required(login_url="login")
def deleteStock(request, pk):
    referer_url = request.META.get('HTTP_REFERER')
    stock = Stock.objects.get(id=pk)
    if request.method == 'POST':
        stock.delete()
    return redirect(referer_url)
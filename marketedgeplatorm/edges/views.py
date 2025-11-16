from django.shortcuts import render, redirect


def edges(request):

    context = {'edge': "test"}
    return render(request, 'edges/home.html', context)
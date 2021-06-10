from django.shortcuts import render


def base_view_form(request):
    return render(request, 'base.html', {})

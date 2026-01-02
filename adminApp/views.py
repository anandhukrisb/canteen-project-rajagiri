from django.shortcuts import render


def admin_page(request):
    return render(request, 'AdminDashboard.html')

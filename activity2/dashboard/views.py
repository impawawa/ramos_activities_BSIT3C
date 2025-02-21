from django.shortcuts import render

def index(request):
    return render(request, "pages/base.html")  # Ensure this path matches your actual template
def report_view(request):  
    return render(request, 'pages/report.html')
def settings_view(request):  
    return render(request, 'pages/settings.html')
def index(request):
    data = [
        {"title": "Users", "count": 150},
        {"title": "Orders", "count": 320},
        {"title": "Revenue", "count": "12,450"},
    ]
    return render(request, "pages/base.html", {"data": data})

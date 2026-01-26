from django.shortcuts import render

def custom_page_404_not_found(request,exception):
    return render(request, "custom_404_page.html", status=404)
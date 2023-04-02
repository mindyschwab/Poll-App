from django.shortcuts import render


# Create your views here.

# Home view
def home(request):
  # Include an .html file extension - unlike when rendering EJS templates
  return render(request, 'home.html')
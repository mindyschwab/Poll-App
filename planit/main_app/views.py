from django.shortcuts import render


# Create your views here.

# Home view
def home(request):
  return render(request, 'home.html')

def about(request):
  return render(request, 'about.html')

def events_index(request):
  # We pass data to a template very much like we did in Express!
  return render(request, 'events/index.html', {
    'events': events
  })
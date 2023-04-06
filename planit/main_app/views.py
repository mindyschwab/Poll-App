from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from .models import Event, Group, Poll
<<<<<<< HEAD
from .forms import PollForm
=======
from .forms import CreatePollForm
>>>>>>> 4537714 (added forms for polls)

# Create your views here.
events = []

# *************** Basic Views ****************


def home(request):
    return render(request, 'home.html')


def about(request):
    return render(request, 'about.html')

# *************** Events Views ****************


def events_index(request):
    events = Event.objects.all()
    # events = Event.filter(user=request.user)
    # We pass data to a template very much like we did in Express!
    return render(request, 'events/index.html', {
        'events': events
    })


def events_detail(request, event_id):
    event = Event.objects.get(id=event_id)
    return render(request, 'events/detail.html', {
        'event': event
    })


class EventCreate(CreateView):
    model = Event
    fields = ['name', 'who', 'what', 'where', 'when', 'why']
    success_url = '/events/'

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


class EventUpdate(UpdateView):
    model = Event
    fields = ['name', 'who', 'what', 'where', 'when', 'why']


class EventDelete(DeleteView):
    model = Event
    success_url = '/events/'

# *************** Group Views ****************


class GroupList(ListView):
    model = Group

    def user(request):
        context = {'request': request, }
        return render(request, 'group_list.html', context)


class GroupDetail(DetailView):
    model = Group


class GroupCreate(CreateView):
    model = Group
    fields = '__all__'


class GroupUpdate(UpdateView):
    model = Group
    fields = '__all__'


class GroupDelete(DeleteView):
    model = Group
    success_url = '/groups/'


def assoc_group(request, event_id, group_id):
    Event.objects.get(id=event_id).groups.add(group_id)
    return redirect('home')
    # delete line above and uncomment line below to redirect to events details page once created
    # return redirect('detail', event_id=event_id)


def remove_group(request, event_id, group_id):
    Event.objects.get(id=event_id).groups.remove(group_id)
    return redirect('home')
    # delete line above and uncomment line below to redirect to events details page once created
    # return redirect('detail', event_id=event_id)return redirect('detail', event_id=event_id)


def signup(request):
    error_message = ''
    if request.method == 'POST':
        # This is how to create a 'user' form object
        # that includes the data from the browser
        form = UserCreationForm(request.POST)
        if form.is_valid():
            # This will add the user to the database
            user = form.save()
            # This is how we log a user in via code
            login(request, user)
            return redirect('index')
        else:
            error_message = 'Invalid sign up - try again'
    # A bad POST or a GET request, so render signup.html with an empty form
    form = UserCreationForm()
    context = {'form': form, 'error_message': error_message}
    return render(request, 'registration/signup.html', context)


# *************** Poll Views ****************

class PollCreate(CreateView):
    model = Poll
    fields = ['question', 'choice_one', 'choice_two', 'choice_three']
    success_url = '/polls_detail/'

# def polls_create(request, event_id):
#     form = PollForm(request.POST)
#     if form.is_valid():
#         new_poll = form.save(commit=False)
#         new_poll.event_id = event_id
#         new_poll.save()
#         return redirect('detail', event_id=event_id)

# def add_poll(request, event_id):
#     if request.method == 'POST':
#         form = CreatePollForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect('detail', event_id=event_id)
#     else:
#         form = CreatePollForm()
#     return render(request, 'polls/create.html', {
#     def form_valid(self, form):
#         form.instance.user = self.request.user
#         return super().form_valid(form)
    
#     def assoc_poll(request, event_id, poll_id):
#         Event.objects.get(id=event_id).polls.add(poll_id)
#         return redirect('home')
        # delete line above and uncomment line below to redirect to events details page once created
        # return redirect('detail', event_id=event_id)
     
class PollDetail(DetailView):
    model = Poll

class PollUpdate(UpdateView):
    model = Poll
    fields = '__all__'

class PollDelete(DeleteView):
    model = Poll
    success_url = '/events/'
def polls_detail(request, poll_id):
    poll = Poll.objects.get(id=poll_id)
    return render(request, 'polls/detail.html', {
        'poll': poll
    })

def add_poll(request, event_id):
    if request.method == 'POST':
        form = CreatePollForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('detail', event_id=event_id)
    else:
        form = CreatePollForm()
    return render(request, 'polls/create.html', {

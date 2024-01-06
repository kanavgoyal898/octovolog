from django.shortcuts import render

posts = [
    {
        'author' : 'John Doe',
        'title' : 'Test Post 00',
        'content' : 'Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.',
        'date_posted' : 'April 6, 2024'
    },
    {
        'author' : 'Jane Doe',
        'title' : 'Test Post 01',
        'content' : 'Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.',
        'date_posted' : 'June 22, 2024'

    }
]

# Create your views here.
def home(request):
    context = {'title' : 'Home', 'posts' : posts}
    return render(request, 'blog/home.html', context)

def about(request):
    context = {'title' : 'About'}
    return render(request, 'blog/about.html', context)
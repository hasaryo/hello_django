from django.shortcuts import render

# Create your views here.

def home(request):
    context = {
            'text' : 'Home empty.',
            'title' : 'Home -'
}
    return render(
        request, 
        'home/home.html',
        context,
    )

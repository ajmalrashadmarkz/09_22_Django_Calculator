from django.shortcuts import render,redirect
from django.views.generic import TemplateView
from .forms import HomeForm

# Create your views here.
class HomePage(TemplateView):
    template_name = 'templatesviews/home.html'
    #template_name = 'aboutus.html'


    #def get(self, request, *args, **kwargs):
        #return render(request, "aboutus.html")

    def get(self, request, *args, **kwargs):
        form = HomeForm()
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        form = HomeForm(request.POST)
        if form.is_valid():
            text = form.cleaned_data['num1']
            text2 = form.cleaned_data['num2']
            if 'add' in request.POST:
                result = text + text2
            elif 'sub' in request.POST:
                result = text - text2
            elif 'mul' in request.POST:
                result = text * text2
            elif 'div' in request.POST:
                result = text / text2

            form = HomeForm()
            # return redirect ('home:home')

        args = {'form': form, 'result': result}
        return render(request, self.template_name, args)

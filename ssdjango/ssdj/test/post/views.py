from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader


# Create your views here.
# ~ from django.http import https
# ~ def post(request):
    # ~ return HttpResponse("Hello world! index")

'''def post(request):
  template = loader.get_template('ss1.html')
  return HttpResponse(template.render())
'''


from .models import Members

# ~ def post(request):
  # ~ mymembers = Members.objects.all().values()
  # ~ output = ""
  # ~ for x in mymembers:
    # ~ output += x["firstname"]
  # ~ return HttpResponse(output)


def post(request):
	mymembers = Members.objects.all().values()
	template = loader.get_template('ss2.html')
	context = {'mymembers': mymembers}
	return HttpResponse(template.render(context, request))
def add(request):
  template = loader.get_template('add.html')
  return HttpResponse(template.render({}, request))

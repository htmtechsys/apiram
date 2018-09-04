import json
from django.shortcuts import render
from django.core.serializers import serialize
from django.http import JsonResponse,HttpResponse
from django.views.generic import View
from cfeapi.mixins import JsonResponseMixin
from updates.models import Update

#def detail_view(request):
    #return render()#return Json data xml

def json_example_view(request):
    data={
    "count":1000,
    "content":"some new content"
    }
    json_data=json.dumps(data)
    #return JsonResponse(data)
    return HttpResponse(json_data,content_type='application/json')

class JsonCBV(View):
    def get(self,request,*args,**kwargs):
        data={
        "count":1000,
        "content":"some new content"
        }
        return JsonResponse(data)

class JsonCBV2(JsonResponseMixin,View):
    def get(self,request,*args,**kwargs):
        data={
        "count":10,
        "content":"some new content 1"
        }
        return self.render_to_json_response(data)

class SerializedDetailView(View):
    def get(self,request,*args,**kwargs):
        obj = Update.objects.get(id=3)
        #data = serialize("json", [obj,], fields = ('user', 'content'))
        json_data = obj.serialize()
        return HttpResponse(json_data,content_type='application/json')

class SerializedListView(View):
   def get(self,request,*args,**kwargs):
       #qs=Update.objects.all()
       #data=serialize("json",qs,fields=('user','content'))
       #print(data)
       #json_data=data
       json_data=Update.objects.all().serialize()
       return HttpResponse(json_data,content_type='application/json')

import json
from rest_framework.decorators import api_view
from django.http import HttpResponse




@api_view()
def getstudents(request):
   list= {
   "cn":[{"name":"lap tob","number":3},{"name":"Iphone","number":1},{"name":"Television","number":1},{"name":"samsung A12","number":1}],
   "hc":[{"name":"lap tob","y":3},{"name":"Iphone","y":1},{"name":"Televisions","y":1},{"name":"samsung A12","y":1}]

   }





   return HttpResponse(json.dumps(list,default=lambda o:o.__dict__),content_type="application/json")

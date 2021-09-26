import requests
from rest_framework.response import Response
from rest_framework.views import APIView

yandex = {"api_url": "https://api.rasp.yandex.net/v3.0/",
          "api_key": "93488be9-8831-4e68-b934-afd8de8f5500"}


class YandexAPIView(APIView):
    def get(self, request):

        req = request.GET['query_type']
        lng = request.GET['lng']
        lat = request.GET['lat']
        distance = request.GET['distance']

        url = yandex['api_url'] + req

        params = {'apikey': yandex['api_key'],
                  'lat': lat,
                  'lng': lng,
                  'distance': distance}
        if req == 'nearest_stations/':
            params.update({'limit': request.GET['limit']})
        result = requests.get(url, params=params)
        data = result.json()
        return Response(data)




from django.shortcuts import render
from .serializers import DataSerializer
from .Risk_1 import Risk_R_Area
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import AllowAny


@api_view(["GET"])
def get_list( request):
    data = Risk_R_Area
    output = []
    for key, values in data.items():
        temp = {}
        for i, val in enumerate(values):
            temp[f'a{i+1}'] = round(val * 100, 2)
        output.append({key: temp})  
    serialized_data = DataSerializer(output, many=True)
    return Response(serialized_data.data, status=status.HTTP_200_OK)

@api_view(["GET"])
def get_details(request, city_name):
    data = Risk_R_Area
    
    if city_name not in data:
        return Response({"message": "City not found"}, status=status.HTTP_404_NOT_FOUND)

    city_data = {}
    for i, val in enumerate(data[city_name]):
        city_data[f'a{i+1}'] = round(val * 100, 2)
    serialized_data = DataSerializer({city_name: city_data})
    return Response(serialized_data.data, status=status.HTTP_200_OK)



    
    # def get_details(self , request , city_name):
        
    #     output = Risk_R_Area.get(city_name = Risk_R_Area.keys())
    #     serialized_data = DataSerializer(output, many=False)
        

        

# class MyAPIView(APIView):
#     def get(self, request):
#         my_dict = Risk_R_Area

#         new_dict = {}
#         for key in my_dict:
#             values_list = my_dict[key]
#             new_values_list = [{'a{}'.format(i+1): value} for i, value in enumerate(values_list)]
#             new_dict[key] = new_values_list

#         result_dict = {}
#         for key, values_list in new_dict.items():
#             result_dict[key.replace(' ', '_')] = dict(zip(range(1, len(values_list)+1), values_list))

#         serializer = MySerializer(data=result_dict)
#         serializer.is_valid()
#         return Response(serializer.data)



# def make_dict(data):
#     new_dict = {}
#     for i, val in enumerate(data):
#         key = f'a{i+1}'
#         new_dict[key] = val

#     data[key] = new_dict
#     data_dic.append(new_dict)
#     print (data_dic)
        

# class GetAllData(APIView):
#     def get(self, request, format=None):
#         global data_dic
#         data= Risk_R_Area
#         # print(data) 
#         data_dic = []
#         make_dict(data)
#         query = data_dic
#         serializer = DataSerializer(query, many=True).data
     
#         return Response(serializer, status=status.HTTP_200_OK)
    
    




        
# def GetapiView(request):
#    #result = subprocess.run(['python', 'my_project/scripts/my_script.py'], stdout=subprocess.PIPE)
#     result = Risk_R_Area
#     context = {"api" : result}

   
#     return render (request , "API/api.html" ,context )
    




# Create your views here.

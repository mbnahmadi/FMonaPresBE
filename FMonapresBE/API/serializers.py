# from rest_framework import serializers, viewsets
# from .Risk_1 import Risk_R_Area
from rest_framework import serializers

class ValueSerializer(serializers.Serializer):
    a1 = serializers.FloatField()
    a2 = serializers.FloatField()
    a3 = serializers.FloatField()
    a4 = serializers.FloatField()
    a5 = serializers.FloatField()
    

class DataSerializer(serializers.Serializer):
    values = ValueSerializer()

    def to_representation(self, instance):
        return instance
    
    def to_internal_value(self, data):
        return {key: {'values': ValueSerializer(values).data} for key, values in data.items()}


# class MySerializer(serializers.Serializer):
#     Ardebil = serializers.DictField()
#     Bushehr = serializers.DictField()
#     Chahar_Mahall_and_Bakhtiari = serializers.DictField()
#     East_Azarbaijan = serializers.DictField()
#     Esfahan = serializers.DictField()
#     Fars = serializers.DictField()
#     Gilan = serializers.DictField()
#     Golestan = serializers.DictField()
#     Hamadan= serializers.DictField()
#     Hormozgan = serializers.DictField()
#     Ilam = serializers.DictField()
#     Kermanshah = serializers.DictField()
#     Kerman= serializers.DictField()
#     Khuzestan= serializers.DictField()
#     Kohgiluyeh_and_Buyer_Ahmad= serializers.DictField()
#     Kordestan= serializers.DictField()
#     Lorestan= serializers.DictField()
#     Markazi= serializers.DictField()
#     Mazandaran= serializers.DictField()
#     North_Khorasan= serializers.DictField()
#     Qazvin= serializers.DictField()
#     Qom= serializers.DictField()
#     Razavi_Khorasan= serializers.DictField()
#     Semnan= serializers.DictField()
#     Sistan_and_Baluchesta= serializers.DictField()
#     South_Khorasan= serializers.DictField()
#     Tehran= serializers.DictField()
#     West_Azarbaijan= serializers.DictField()
#     Yazd= serializers.DictField()
#     Zanjan= serializers.DictField()


    
    
    
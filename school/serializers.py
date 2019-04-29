# -*- coding: utf-8 -*-
# @Time    : 2019/4/29 17:34
# @Author  : Langu
# @Email   : xblinux06@gmail.com


from rest_framework import serializers
from school.models import School


class SchoolSerializer(serializers.ModelSerializer):
    country = serializers.SerializerMethodField()

    class Meta:
        model = School
        # fields = '__all__'
        fields = ('id', 'name', 'address','country', 'updated', 'created')

    def get_country(self,obj):

        return "cn"






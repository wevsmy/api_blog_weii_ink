import json

import requests
from django.contrib.auth.models import User, Group
from django.http import JsonResponse
from rest_framework import viewsets
from rest_framework.views import APIView

from api.models import UserSerializer, GroupSerializer


# ViewSets define the view behavior.
class UserViewSet(viewsets.ModelViewSet):
    """
    retrieve:
        Return a user instance.

    list:
        Return all users, ordered by most recently joined.

    create:
        Create a new user.

    delete:
        Remove an existing user.

    partial_update:
        Update one or more fields on an existing user.

    update:
        Update a user.
    """

    queryset = User.objects.all()
    serializer_class = UserSerializer


class GroupViewSet(viewsets.ModelViewSet):
    """
    retrieve:
        Return a group instance.

    list:
        Return all groups, ordered by most recently joined.

    create:
        Create a new group.

    delete:
        Remove an existing group.

    partial_update:
        Update one or more fields on an existing group.

    update:
        Update a group.
    """

    queryset = Group.objects.all()
    serializer_class = GroupSerializer


# Create your views here.
class GetMessageView(APIView):
    # get 请求
    def get(self, request):
        # 获取参数数据
        get = request.GET
        # 获取参数 a
        a = get.get('a')
        print(a)
        # 返回信息
        d = {
            'status': 200,
            'message': 'success',
            'data': get
        }
        return JsonResponse(d)


class GetIssuesComments(APIView):
    # get 请求
    # 获取评论数量
    def get(self, request):
        # 获取参数数据
        get = request.GET
        # 获取参数 a
        a = get.get('a')
        print(a)
        user = "wevsmy"
        repo = "wevsmy.github.io"
        client_id = "ded8625909c20b7ae2f7"
        client_secret = "c9ba27c5047486b4e2e0f8c3001aae33bc15374a"
        url = "https://api.github.com/repos/{}/{}/issues?client_id={}&client_secret={}".format(user, repo, client_id,
                                                                                               client_secret)
        ret = requests.get(url=url, timeout=30)
        if ret.status_code == 200:
            jsonData = json.loads(ret.content.decode("utf-8"))
            print(jsonData, type(jsonData))
            d = {
                'status': ret.status_code,
                'message': 'success',
                'data': jsonData
            }
            return JsonResponse(d)
        else:
            d = {
                'status': ret.status_code,
                'message': 'error',
                'data': []
            }
            return JsonResponse(d)

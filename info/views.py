from info.models import Info
from rest_framework import views,response,viewsets, status , permissions
from . import serializers
from role_manager.permissions import HasGroupRolePermission

class InfoView(viewsets.ModelViewSet):
    queryset = Info.objects.all()
    serializer_class = serializers.InfoSeriaizers    
    permission_classes = [permissions.IsAuthenticated , HasGroupRolePermission]

    def create(self, request, *args, **kwargs):
        data=request.data
        user={}
        user['first_name'] = data.get('firstName')
        user['last_name'] = data.get('lastName')
        user['phone'] = data.get('phone')
        user['email'] = data.get('email')
        user['username'] = data.get('nationalcode')
        data['userName'] = data.get('nationalcode')
        user['password'] = data.pop('password')
        user['re_password'] = data.pop('re_password')
        data['user'] = user
        serializer = self.get_serializer(data=data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return response.Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)
    
    def get_serializer_context(self):
        return {
            'request': self.request,
            'format': self.format_kwarg,
            'view': self,
            'groups': 'client'
        }


from rest_framework import viewsets
from mantix_pro.models.user import User
from mantix_pro.serializer import UserSerializer

from mantix_pro.models.status import Status

from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth.hashers import check_password

class UserView(viewsets.ModelViewSet):
    serializer_class = UserSerializer
    queryset = User.objects.all()
    
    @action(detail=True, methods=['post'])
    def activar_desactivar(self, request, pk=None, acc=None):
        try:
            user = self.get_object()
            mensaje =  ""
            if user.status.id == 1:
                user.status = Status.objects.get(id=2)
                mensaje = f'user {user.user_name} {user.user_apellido} desactivado correctamente'
            elif user.status.id == 2:
                user.status = Status.objects.get(id=1)
                mensaje = f'user {user.user_name} {user.user_apellido} activado correctamente'
            user.save()
        except Exception as ex:
            mensaje =  f'Exeption: {ex}'
        finally:
            return Response({'mensaje': mensaje})

    @action(detail=True, methods=['post'])
    def ObtenerTokenAuth(self, request):
        
        email = request.data.get('user_email')
        password = request.data.get('user_password')
        if not email or not password:
            return Response({'error': 'Debes proporcionar un correo electrónico y una contraseña.'}, status=status.HTTP_400_BAD_REQUEST)
        
        user = authenticate(email, password)
        
        if user is not None:
            refresh = RefreshToken.for_user(user)
            access_token = str(refresh.access_token)
            return Response({'access_token': access_token}, status=status.HTTP_200_OK)
        else:
            return Response({'error': 'Credenciales inválidas'}, status=status.HTTP_401_UNAUTHORIZED)
    
    @action(detail=True, methods=['GET'])
    def ObtenerOwners(self, request):
        try:
            user = User.objects.filter(is_owner = 'S', status = 1)
            serializer = self.get_serializer(user, many=True)
            
            return Response(serializer.data, status=status.HTTP_200_OK)
            
        except Exception as ex:
            mensaje =  f'Exeption: {ex}'
            return Response({'mensaje': mensaje}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    
def authenticate(email, password):
    try:
        user = User.objects.get(user_email = email)
        if user and check_password(password, user.user_password):
            return user
    except User.DoesNotExist:
        pass
    return None
    
      
  
        
        

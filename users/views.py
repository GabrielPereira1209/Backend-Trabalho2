from rest_framework import status, permissions
from rest_framework.decorators import api_view, permission_classes

# views para autenticação e perfil de usuário
from rest_framework import status, permissions
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth import authenticate
from .serializers import UserSerializer, RegisterSerializer
from .models import User

# endpoint de registro de usuário
@api_view(['POST'])
@permission_classes([permissions.AllowAny])
def register(request):
    serializer = RegisterSerializer(data=request.data)
    serializer.is_valid(raise_exception=True)
    user = serializer.save()
    return Response(UserSerializer(user).data, status=status.HTTP_201_CREATED)

# endpoint de login
@api_view(['POST'])
@permission_classes([permissions.AllowAny])
def login(request):
    email = request.data.get('email')
    password = request.data.get('password')
    user = authenticate(request, email=email, password=password)
    if not user:
        return Response({'detail':'Credenciais inválidas'}, status=status.HTTP_400_BAD_REQUEST)
    refresh = RefreshToken.for_user(user)
    return Response({'access_token': str(refresh.access_token), 'user': UserSerializer(user).data})

# endpoint para obter dados do usuário logado
@api_view(['GET'])
@permission_classes([permissions.IsAuthenticated])
def me(request):
    return Response(UserSerializer(request.user).data)

# endpoint para atualizar perfil
@api_view(['PUT'])
@permission_classes([permissions.IsAuthenticated])
def update_profile(request):
    user = request.user
    serializer = UserSerializer(user, data=request.data, partial=True)
    serializer.is_valid(raise_exception=True)
    serializer.save()
    return Response(serializer.data)

# endpoint para trocar senha
@api_view(['POST'])
@permission_classes([permissions.IsAuthenticated])
def change_password(request):
    user = request.user
    current_password = request.data.get('current_password')
    new_password = request.data.get('new_password')
    if not user.check_password(current_password):
        return Response({'detail':'Senha atual incorreta'}, status=status.HTTP_400_BAD_REQUEST)
    user.set_password(new_password)
    user.save()
    return Response({'detail':'Senha alterada'})

# endpoint para recuperação de senha
@api_view(['POST'])
def forgot_password(request):
    email = request.data.get('email')
    try:
        user = User.objects.get(email=email)
        # em um app real, enviaria email
        return Response({'detail':'Se o email existir, instruções foram enviadas.'})
    except User.DoesNotExist:
        return Response({'detail':'Se o email existir, instruções foram enviadas.'})

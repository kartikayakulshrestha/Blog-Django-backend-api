
from rest_framework.pagination import PageNumberPagination
from rest_framework.viewsets import ModelViewSet
import datetime
from rest_framework import viewsets,status
from api.models import User,Blog,likes,comments,userV2
from rest_framework.response import Response
from rest_framework.decorators import action
from api.serializers import UserSerializer,BlogSerializer,likerSerializer,commentsSerializer,userv2Serializer

class CustomPagination(PageNumberPagination):
    page_size = 5 
    page_query_param = 'page'
    page_size_query_param = 'page_size'
    max_page_size = 100
class BlogPagination(PageNumberPagination):
    page_size = 10
    page_query_param = 'page'
    page_size_query_param = 'page_size'
    max_page_size = 1000
class UserViewSet(viewsets.ModelViewSet):
    queryset=User.objects.all()
    serializer_class=UserSerializer
    
    @action(detail=True,methods=['get'])
    def blogs(self,request,pk=None):
        
        try:
            user=User.objects.get(pk=pk)
        
            blogs=Blog.objects.filter(author=user)
            blog_serializer=BlogSerializer(
                blogs,
                many=True,
                context={'request':request}
            )
            return Response(blog_serializer.data)
        except Exception as e:
            print(e)
            return Response([])
    @action(detail=False,methods=['get'])
    def logout(self,request):
        if request.COOKIES['sessionid']:
            response=Response({'message':'logged out'})
            response.delete_cookie('sessionid')
            return response
            
    @action(detail=False,methods=['post'])
    def login(self,request):
        
        try:
            user=User.objects.get(email=request.data['email'])
            
           
            if user.password == request.data['password']:
                
                response=Response({'message':"Logged in"})
                
                response.set_cookie('sessionid',str(user.pk)+" " +str(user.email),expires=datetime.datetime.utcnow() + datetime.timedelta(days=1),secure=True)
                print(response)
                return response
            else:
                return Response({'message':"Wrong Password"})
        except Exception as e:
            print(e)
            return Response({'message':"do not exist "})
        
class BlogViewSet(viewsets.ModelViewSet):

    queryset=Blog.objects.all()
    
    serializer_class=BlogSerializer
    pagination_class = BlogPagination
    
    @action(detail=True,methods=['post','get'])
    def comments(self,request,pk=None):
        if request.method=="GET":
            try:
                paginator = CustomPagination()
                comment=comments.objects.filter(blog_id=int(pk),commenter_id=int(request.COOKIES['sessionid'][0]))
                paginated_comments = paginator.paginate_queryset(comment, request)
                serializer = commentsSerializer(paginated_comments, many=True)
                return paginator.get_paginated_response(serializer.data)
            except Exception as e:
                print(e)
                return Response([])
        elif request.method == "POST":
            
            try:
                
                cookie=request.COOKIES['sessionid']
                
                if request.data['text']:
                    if cookie:
                        cookies=cookie.split(" ")

                        user =User.objects.get(pk=int(cookies[0]))
                    
                        if user.email==cookies[1]:
                       
                            
                            comment=comments.objects.create(blog_id=Blog.objects.get(pk=int(pk)),commenter_id=user,text=request.data['text'])
                            commentser=commentsSerializer(comment)
                        
                        return Response(commentser.data)
            except Exception as e:
                print(e)
                return Response({'error': str(e)}, status=400)


    @action(detail=True,methods=['post','get'])
    def like(self,request,pk=None):
        
        if request.method == "GET":
            try:
                
                like=likes.objects.get(blog_id=Blog.objects.get(pk=pk))
                return Response(likerSerializer(like).data)
            except Exception as e:
                return Response([])
        elif request.method == "POST":
            try:
                # Your logic to handle listing likes or adding likes to multiple blog posts
                cookie=request.COOKIES['sessionid']
                
                if cookie:
                    cookies=cookie.split(" ")

                    user =User.objects.get(pk=int(cookies[0]))
                    
                    if user.email==cookies[1]:
                        #now like table will add a record blog_id , liker_id ,create_at
                        
                        like,created=likes.objects.get_or_create(blog_id=Blog.objects.get(pk=int(pk)),liker_id=user)
                        if created==False:
                            like.delete()
                            

                        likeser=likerSerializer(like)
                        
                    return Response(likeser.data)
            except Exception as e:
                print(e)
                return Response({'error': str(e)}, status=400)
    
# version 2

class userv2ViewSet(viewsets.ModelViewSet):
    queryset=userV2.objects.all()
    serializer_class=userv2Serializer

    
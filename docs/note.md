使用pip install pillow 失败：

        apt-get install python-dev python-setuptools
        apt-get install libjpeg-dev zlib1g-dev libpng12-dev
        pip install pillow
        
登录xadmin

    首先需要创建一个超级用户 python manage.py createsuperuser 
    
GenericViewSet(viewset)
    GenericAPIView
        APIView
            View
mixin
    CreateModelMixin
    ListModelMixin
    UpdateModelMixin
    DestroyModelMixin
    RetrieveModelMixin
    

使用django-cors-headers解决跨域问题
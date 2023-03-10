


from unicodedata import name
from django.urls import path

from .views import home,services,technology,blog,aboutus,contactus,aiml,odoo,python,robotic,\
    BusinessConsulting,BusinessIntelligence,hire,pwa,AI,RPA,PythonTechnology,Django,Golang,Flutter,\
    ReactJs,Contactdata,Blog_1,Blog_2,Blog_3,NewsLetter,oddocrm,aimlblog,Oddofuture

from .views import home,services,technology,blog,aboutus,contactus,aiml,odoo,python,robotic,BusinessConsulting,BusinessIntelligence,hire,pwa,AI,RPA,PythonTechnology,Django,Golang,Flutter,ReactJs,Contactdata,Blog_1,Blog_2,Blog_3,NewsLetter,oddocrm,aimlblog,Oddofuture


urlpatterns = [ 
    path('',home,name='home'),
    path('services',services,name='services'),
    path('technology',technology,name='technology'),
    path('blog',blog,name='blog'),
    path('aboutus',aboutus,name='aboutus'),
    path('contactus',contactus,name='contactus'),
    path('aiml',aiml,name='aiml'),
    path('odoo',odoo,name='odoo'),
    path('python',python,name='python'),
    path('robotic',robotic,name='robotic'),
    path('consulting',BusinessConsulting,name='consulting'),
    path('bi',BusinessIntelligence,name='bi'),
    path('hire',hire,name='hire'),
    path('pwa',pwa,name='pwa'),
    path('ai',AI,name='ai'),
    path('rpa',RPA,name='rpa'),
    path('python-tech',PythonTechnology,name='pythontech'),
    path('django',Django,name='django'),
    path('golang',Golang,name='golang'),
    path('flutter',Flutter,name='flutter'),
    path('react',ReactJs,name='react'),

    path('contactformdata',Contactdata,name='contactformdata'),
    path('blog-1',Blog_1,name='blog-1'),
    path('blog-2',Blog_2,name='blog-2'),
    path('blog-3',Blog_3,name='blog-3'),
    path('newsletter',NewsLetter,name='newsletter'),
    path('oddocrm',oddocrm,name='oddocrm'),
    path('aimlblog',aimlblog,name='aimlblog'),
    path('oddofuture',Oddofuture,name='oddofuture')
    # path('receivedata',receivedata,name='receivedata')
  


]

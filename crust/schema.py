import graphene
from graphene_django  import DjangoObjectType

from crust.models import Cuisine


class CuisineType(DjangoObjectType):
    class Meta:
        model = Cuisine
        fields =("id", "name")
       

class Query(graphene.ObjectType):
    
    all_cuisine = graphene.List(CuisineType)  

    def resolve_all_cuisine(root, info):
        return Cuisine.objects.all() 

        

schema =graphene.Schema(query=Query)   



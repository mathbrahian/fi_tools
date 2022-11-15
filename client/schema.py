import graphene
from graphene_django import DjangoObjectType
from client.models import Client as ClientModel

class Client(DjangoObjectType):
    class Meta:
        model = ClientModel

class Query(graphene.ObjectType):
    clients = graphene.List(Client)
    def resolve_clients(self, info):
        return ClientModel.objects.all()

schema = graphene.Schema(query=Query)
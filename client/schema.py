import graphene
from graphene_django import DjangoObjectType
from client.models import Client as Client

class ClientType(DjangoObjectType):
    class Meta:
        model = Client

class UpdateClientInput(graphene.InputObjectType):
    name = graphene.String(required=False)
    email = graphene.String(required=False)
    direction = graphene.String(required=False)
    phone_number = graphene.String(required=False)

class CreateClientInput(graphene.InputObjectType):
    name = graphene.String(required=True)
    email = graphene.String(required=True)
    direction = graphene.String(required=True)
    phone_number = graphene.String(required=True)

class CreateClient(graphene.Mutation):
    class Arguments:
        client_data = ClientInput(required=True)

    client = graphene.Field(ClientType)

    def mutate(root, info, client_data=None):
        client = Client(**client_data)
        client.save()
        return CreateClient(client=client)

class Mutation(graphene.ObjectType):
    create_client = CreateClient.Field()

class Query(graphene.ObjectType): 
    client = graphene.Field(ClientType)
    clients = graphene.List(ClientType)
    def resolve_clients(self, info):
        return Client.objects.all()

schema = graphene.Schema(query=Query, mutation=Mutation)
import graphene
from graphene_django import DjangoObjectType
from products.models import Product


class ProductType(DjangoObjectType):
    class Meta:
        model = Product
        fields = ("id", "name", "created_date")

class Query(graphene.ObjectType):
    all_products = graphene.List(ProductType)

    def resolve_all_products(root, info):
        return Product.objects.all()


class CreateProduct(graphene.Mutation):
    class Arguments:
        name = graphene.String()

    ok = graphene.Boolean()
    product = graphene.Field(ProductType)

    def mutate(root, info, name):
        product = Product(name=name)
        ok = False
        try:
            product.save()
            ok = True
        except:
            pass

        return CreateProduct(product=product, ok=ok)

class Mutations(graphene.ObjectType):
    create_product = CreateProduct.Field()

schema = graphene.Schema(query=Query, mutation=Mutations)
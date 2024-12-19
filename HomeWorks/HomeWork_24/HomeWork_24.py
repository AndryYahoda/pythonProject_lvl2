from peewee import *

db = SqliteDatabase('store.db')


class BaseModel(Model):
    class Meta:
        database = db


class Buyer(BaseModel):
    id = AutoField(primary_key=True)
    name = CharField()
    email = CharField(unique=True)


class Seller(BaseModel):
    id = AutoField(primary_key=True)
    name = CharField()
    contact = CharField()


class Product(BaseModel):
    id = AutoField(primary_key=True)
    name = CharField()
    price = DecimalField(max_digits=10, decimal_places=2)
    manufacture_date = DateField()
    seller = ForeignKeyField(Seller, backref='products')


class Purchase(BaseModel):
    id = AutoField(primary_key=True)
    buyer = ForeignKeyField(Buyer, backref='purchases')
    product = ForeignKeyField(Product, backref='purchases')
    quantity = IntegerField()


db.connect()
db.create_tables([Buyer, Seller, Product, Purchase])

buyers = [
    {'name': 'Олексій', 'email': 'olexiy@gmail.com'},
    {'name': 'Марія', 'email': 'maria@gmail.com'},
    {'name': 'Іван', 'email': 'ivan@gmail.com'},
    {'name': 'Олена', 'email': 'olena@gmail.com'},
    {'name': 'Дмитро', 'email': 'dmytro@gmail.com'}
]
Buyer.insert_many(buyers).execute()

sellers = [
    {'name': 'TechStore', 'contact': 'techstore@example.com'},
    {'name': 'GadgetZone', 'contact': 'gadgetzone@example.com'}
]
Seller.insert_many(sellers).execute()

products = [
    {'name': 'Смартфон', 'price': 15000.00, 'manufacture_date': '2023-01-15', 'seller': 1},
    {'name': 'Ноутбук', 'price': 45000.00, 'manufacture_date': '2022-11-10', 'seller': 1},
    {'name': 'Навушники', 'price': 2500.00, 'manufacture_date': '2023-06-20', 'seller': 2},
    {'name': 'Планшет', 'price': 20000.00, 'manufacture_date': '2023-03-05', 'seller': 2},
    {'name': 'Смарт-годинник', 'price': 8000.00, 'manufacture_date': '2023-08-01', 'seller': 1}
]
Product.insert_many(products).execute()

purchases = [
    {'buyer': 1, 'product': 1, 'quantity': 3},
    {'buyer': 2, 'product': 2, 'quantity': 1},
    {'buyer': 3, 'product': 3, 'quantity': 5},
    {'buyer': 4, 'product': 1, 'quantity': 2},
    {'buyer': 5, 'product': 4, 'quantity': 1}
]
Purchase.insert_many(purchases).execute()

popular_product = (Product
                   .select(Product, fn.SUM(Purchase.quantity).alias('total_sales'))
                   .join(Purchase)
                   .group_by(Product)
                   .order_by(fn.SUM(Purchase.quantity).desc())
                   .first())
if popular_product:
    print(f"Найпопулярніший товар: {popular_product.name} (Продано: {popular_product.total_sales} одиниць)")

expensive_product = Product.select().order_by(Product.price.desc()).first()
if expensive_product:
    print(f"Найдорожчий товар: {expensive_product.name} (Ціна: {expensive_product.price} грн)")

newest_product = Product.select().order_by(Product.manufacture_date.desc()).first()
if newest_product:
    print(f"Найновіший товар: {newest_product.name} (Дата виробництва: {newest_product.manufacture_date})")

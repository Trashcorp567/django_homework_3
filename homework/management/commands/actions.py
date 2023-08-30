from django.core.management.base import BaseCommand
from homework.models import Category, Product


class Command(BaseCommand):

    def handle(self, *args, **options):
        # Удаляем старые данные
        Category.objects.all().delete()
        Product.objects.all().delete()

        # Создаем новые данные
        category1 = Category.objects.create(name='Фото и видео', description='Объективы')
        category2 = Category.objects.create(name='Техника', description='Электронная техника')

        product1 = Product.objects.create(name='Объектив Canon EF50mm', description='Для фото', category=category1, price=29640)
        product2 = Product.objects.create(name='Ноутбук Acer Aspire', description='Мощный ноутбук', category=category2, price=29999)
        product3 = Product.objects.create(name='Ноутбук HONOR', description='В основе устройства лежит двухъядерный процессор', category=category2, price=49999)

        self.stdout.write(self.style.SUCCESS(''))

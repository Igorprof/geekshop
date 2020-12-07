from django.shortcuts import render

# Create your views here.
def index(request):
    context = {
        'title': 'GeekShop - главная'
    }
    return render(request, 'mainapp/index.html', context)

def products(request):
    folder_images = 'vendor/img/products'
    context = {
        'title': 'GeekShop - продукты',
        'product_list':[
            {'img_src': f'{folder_images}/Adidas-hoodie.png',  
            'name': 'Худи черного цвета с монограммами adidas Originals', 
            'price': '6 090,00 руб.', 
            'description': 'Мягкая ткань для свитшотов. Стиль и комфорт – это образ жизни.'},
            {'img_src': f'{folder_images}/Adidas-hoodie.png', 
            'name': 'Худи черного цвета с монограммами adidas Originals', 
            'price': '6 090,00 руб.', 
            'description': 'Мягкая ткань для свитшотов. Стиль и комфорт – это образ жизни.'},
            {'img_src': f'{folder_images}/Blue-jacket-The-North-Face.png', 
            'name': 'Синяя куртка The North Face', 
            'price': '23 725,00 руб.', 
            'description': 'Гладкая ткань. Водонепроницаемое покрытие. Легкий и теплый пуховый наполнитель.'},
            {'img_src': f'{folder_images}/Brown-sports-oversized-top-ASOS-DESIGN.png', 
            'name': 'Коричневый спортивный oversized-топ ASOS DESIGN', 
            'price': '3 390,00 руб.', 
            'description': 'Материал с плюшевой текстурой. Удобный и мягкий.'},
            {'img_src': f'{folder_images}/Black-Nike-Heritage-backpack.png', 
            'name': 'Черный рюкзак Nike Heritage', 
            'price': '2 340,00 руб.', 
            'description': 'Плотная ткань. Легкий материал.'},
            {'img_src': f'{folder_images}/Black-Dr-Martens-shoes.png', 
            'name': 'Черные туфли на платформе с 3 парами люверсов Dr Martens 1461 Bex', 
            'price': '13 590,00 руб.', 
            'description': 'Гладкий кожаный верх. Натуральный материал.'},
            {'img_src': f'{folder_images}/Dark-blue-wide-leg-ASOs-DESIGN-trousers.png', 
            'name': 'Темно-синие широкие строгие брюки ASOS DESIGN', 
            'price': '2 890,00 руб.', 
            'description': 'Легкая эластичная ткань сирсакер Фактурная ткань.'},
        ]
    }
    return render(request, 'mainapp/products.html', context)
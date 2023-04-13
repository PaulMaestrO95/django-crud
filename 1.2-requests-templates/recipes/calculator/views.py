from django.shortcuts import render

DATA = {
    'omlet': {
        'яйца, шт': 2,
        'молоко, л': 0.1,
        'соль, ч.л.': 0.5,
    },
    'pasta': {
        'макароны, г': 500,
        'сыр, г': 100,
        'бекон, г': 200,
        'яйца, шт': 2,
    },
    'buter': {
        'хлеб, ломтик': 1,
        'колбаса, ломтик': 1,
        'сыр, ломтик': 1,
        'помидор, ломтик': 1,
    },
    'pancake': {
        'яйца, шт': 1,
        'мука, г': 400,
        'соль, ч.л.': 0.5,
        'вареная сгущенка, ст.л.': 1,
        'cливочное масло, г': 20,
    },
}

def recipe(request, dish):
    servings = int(request.GET.get('servings', 1))
    DATA[dish].update(
        (key, value * servings) for key, value in DATA[dish].items()
    )
    context = {
        'ingredients': DATA[dish],
        'dish': dish,
    }
    return render(request, 'calculator/index.html', context)

# я понимаю, что данные сохраняются, и при каждом следующем обновлении страницы например если servings 2,
# то ингридиенты удваиваются, не смог исправить этот баг убив кучу времени


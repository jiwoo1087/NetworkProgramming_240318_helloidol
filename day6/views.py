from django.http import HttpResponse
from django.shortcuts import render

group = {
    'categories': [
        {
            'group_name': "So let's go see the stars",
            'name': 'Smoothie',
            'img_src': 'day6/images/Smoothie.png',
        },
        {
            'group_name': "So let's go see the stars",
            'name': 'Coffe',
            'img_src': 'day6/images/Coffe.png',
        },
        {
            'group_name': "So let's go see the stars",
            'name': 'Tea',
            'img_src': 'day6/images/Tea.png',
        },
        {
            'group_name': "So let's go see the stars",
            'name': 'Food',
            'img_src': 'day6/images/Food.png',
        }
    ],
    'Smoothie' : [
        {
            'group_name': "So let's go see the stars",
            'name': 'mango',
            'img_src': 'day6/images/mango.png',
        },
        {
            'group_name': "So let's go see the stars",
            'name': 'yogurt',
            'img_src': 'day6/images/yogurt.png',
        },
        {
            'group_name': "So let's go see the stars",
            'name': 'cloud',
            'img_src': 'day6/images/cloud.png',
        },
        {
            'group_name': "So let's go see the stars",
            'name': 'peach',
            'img_src': 'day6/images/peach',
        }
    ]
}

# 멤버리스트 보기
def show_멤버리스트(request):
    context = group  # {'categories' : [{카테고리1}, {카테고리2}]}
    return render(request, template_name='day6/멤버리스트.html', context=context)

# 특정 멤버 보기
def show_멤버(request, 멤버):
    member = list(filter(lambda m: 멤버 in m['name'], group['categories']))[0]
    context = {
        'group_name': member['group_name'],
        'name': member['name'],
        'img_src': member['img_src'],
        'categories': group['categories']  # categories를 추가
    }
    return render(request, "day6/멤버.html", context=context)

def show_메뉴(request, 멤버):
    member = list(filter(lambda m: 멤버 in m['name'], group['categories']))[0]
    context = {
        'group_name': member['group_name'],
        'name': member['name'],
        'img_src': member['img_src'],
        'categories': group['categories']  # categories를 추가
    }
    return render(request, template_name='day6/메뉴.html', context=context)
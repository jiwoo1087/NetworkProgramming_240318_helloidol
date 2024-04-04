from django.http import HttpResponse
from django.shortcuts import render


group = {
    'members':[
        {
            'group_name':'day6',
            'name':'도운',
            'img_src':'day6/images/도운.jpg',
        },
        {
            'group_name':'day6',
            'name':'원필',
            'img_src':'day6/images/원필.jpg',
        },
        {
            'group_name':'day6',
            'name':'youngk',
            'img_src':'day6/images/youngk.jpg',
        },
        {
            'group_name':'day6',
            'name':'성진',
            'img_src':'day6/images/성진.jpg',
        }
    ]
}



# def show_도운(request):
#     context = list(filter(lambda member: '도운' in member['name'], group['members']))[0]
#     return render(request, "day6/멤버.html", context=context);

# def show_원필(request):
#     context = list(filter(lambda member: '원필' in member['name'], group['members']))[0]
#     return render(request, "day6/멤버.html", context=context);
#
# def show_youngk(request):
#     context = list(filter(lambda member: 'youngk' in member['name'], group['members']))[0]
#     return render(request, "day6/멤버.html", context=context);
#
# def show_성진 (request):
#     context = list(filter(lambda member: '성진' in member['name'], group['members']))[0]
#     return render(request, "day6/멤버.html", context=context);

def show_멤버(request, 멤버):
    context = list(filter(lambda member: 멤버 in member['name'], group['members']))[0]
    return render(request, "day6/멤버.html", context=context);
# Create your views here.

def show_멤버리스트(request):
    context = group     #{'members' : [{멤버1}, {멤버2}]}
    return render(request, template_name='day6/멤버리스트.html', context=context)
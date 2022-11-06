from django.shortcuts import render

from popup.models import HubriseOrder, HubriseOrderItem, HubriseOrderItemOption


def popup(request):

    if request.htmx:
        id = request.GET.get('id')
        test = HubriseOrder.objects.get(id=id)
        datafiltre1 = HubriseOrderItem.objects.filter(
            HubriseOrderId=test)
        datafiltre2 = HubriseOrderItemOption.objects.filter(
            HubriseOrderItemId=datafiltre1[0])
        print(datafiltre2)
        context = {
            'show1': datafiltre1,
            'test': test,
            'show2': datafiltre2
        }
        return render(request, 'popup/partials/htmx_show_popup.html', context=context)

    context = {
        'shows': HubriseOrder.objects.all(),
        'show1': HubriseOrderItem.objects.all()
    }
    return render(request, 'popup/popup.html', context=context)

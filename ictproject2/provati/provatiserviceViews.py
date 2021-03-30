from django.shortcuts import render


def picl_service(request):
    return render(request,"piclservice/picl_service.html")

def picl_service_bill(request):
    return render(request,"statement/service_bill.html")

def picl_product_bill(request):
    return render(request,"statement/picl_product_bill.html")
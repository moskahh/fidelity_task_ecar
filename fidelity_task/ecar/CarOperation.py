from django.shortcuts import render, redirect
import datetime
from .models import Employee, Car
from django.contrib import messages

def show(request):
    # Car.objects.create(car_number='qwe', user_id=123789, car_brand='宝马', car_color='red', car_type='轿车')
    Carall = Car.objects.all()
    for car in Carall: #car is a dictionary
        car.employee_name = Employee.objects.get(sid=car.user_id).name
    return render(request, 'showcar.html', {'car': Carall})

def add(request):
    if request.POST:
        # return add information from addCar.html
        csid = request.POST.get("c_number") #addemployee.html name
        cuserid = request.POST.get("c_userid")
        cbrand = request.POST.get("c_brand")
        ccolor = request.POST.get("c_color")
        ctype = request.POST.get("c_type")

        #若添加的车辆信息对应员工信息不在employee表内，则禁止添加，并弹出alert
        # print(list(Employee.objects.filter(sid=cuserid)))
        if not list(Employee.objects.filter(sid=cuserid)):
            messages.success(request, "员工信息不存在")
            return redirect('/addCar/')
        # add information into Database
        Car.objects.create(car_number=csid,user_id=cuserid, car_brand=cbrand,car_color=ccolor,car_type=ctype)
        return redirect('/showCar/')  # 重定向urls
    return render(request, 'addCar.html')

def delete(request,cid):

    Car.objects.get(c_id=cid).delete()
    return redirect('/showCar/')  # 重定向urls

def edit(request,cid):
    #修改员工信息函数
    if request.POST:
        #点击修改按钮后，需要更新数据库内的值
        # cnumber = request.POST.get("c_number") # editcar.html name
        # cuserid = request.POST.get("c_userid")
        cbrand = request.POST.get("c_brand")
        ccolor = request.POST.get("c_color")
        ctype = request.POST.get("c_type")
        Car.objects.filter(c_id=cid).update(car_brand=cbrand,car_color=ccolor,car_type=ctype)
        return redirect('/showCar/')
    Cardata = Car.objects.get(c_id=cid)
    brand_all = ["奔驰", "宝马", "奥迪", "林肯", "丰田", "保时捷", "其他"]
    color_all = ["red", "white", "black", "pink", "grey", "blue", "others"]
    type_all = ["轿车", "SUV", "面包车", "越野车", "其他"]
    return render(request, 'editcar.html', {"car": Cardata, "brand_all": brand_all, "color_all": color_all, "type_all": type_all})

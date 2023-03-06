from django.shortcuts import render, redirect
import datetime
from .models import Employee,Car
def show(request):
    # Employee.objects.create(sid=202306,name='username', phone='123456',department='aa',ifcar=True)
    employeeall = Employee.objects.all()

    for employee in employeeall:
        ifcar = list(Car.objects.filter(user_id=employee.sid)) #返回在车辆信息表里是否有该员工信息，若有则为该员工添加属性
        if ifcar: #若员工存在对应车辆信息
            employee.ifcar = True
        else:
            employee.ifcar = False
    return render(request, 'showemployee.html', {'employeeall': employeeall})

def edit(request,sid):
    #修改员工信息函数
    if request.POST:
        #点击修改按钮后，需要更新数据库内的值

        ename = request.POST.get("t_name") # editemployee.html name
        ephone = request.POST.get("t_phone")
        edepartment = request.POST.get("t_apartment")
        ebirthday = request.POST.get("t_birthday")
        # eifcar = request.POST.get("t_ifcar")

        Employee.objects.filter(sid=sid).update(name=ename, phone=ephone,department=edepartment,birthday=ebirthday) #,ifcar=eifcar
        return redirect('/showEmployee/')
    Employeedata = Employee.objects.get(sid=sid)
    Employeedata.birthday = str(Employeedata.birthday) #March 04, 2023 - 21:45:17
    department = ["数据部门 ", "开发部门", "咨询部门", "人力资源管理部门", "后勤部门", "算法部门"]
    return render(request, 'editemployee.html', {"employee": Employeedata, "department_all": department})

def delete(request,sid):
    Employee.objects.get(sid=sid).delete()
    if list(Car.objects.filter(user_id=sid)):
        Car.objects.filter(user_id=sid).delete() #将删除员工的对应车辆信息删除
    return redirect('/showEmployee/') #重定向urls

def add(request):
    if request.POST:
        esid = request.POST.get("t_id") #addemployee.html name
        ename = request.POST.get("t_name")
        ephone = request.POST.get("t_phone")
        edepartment = request.POST.get("t_apartment")
        ebirthday = request.POST.get("t_birthday")
        '''
        cardata = Car.objects.filter(user_id=esid)
        if cardata:
            eifcar = False
        else:
            eifcar = True
        # eifcar = request.POST.get("t_ifcar")
        '''


        Employee.objects.create(sid=esid,name=ename, phone=ephone,department=edepartment,birthday=ebirthday)  #,ifcar=eifcar
        return redirect('/showEmployee/')  # 重定向urls
    return render(request, 'addemployee.html')

def findcar(request,id):
    '''
    若员工有车，显示对应车辆的信息
    :param request:
    :param id:
    :return:
    '''
    cardata = Car.objects.filter(user_id = id)
    for car in cardata: #car is a dictionary
        car.employee_name = Employee.objects.get(sid=car.user_id).name
        # employee_data=Employee.objects.get(sid=id)
    return render(request, 'showcar.html', {'car': cardata})

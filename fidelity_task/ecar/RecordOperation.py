from django.shortcuts import render, redirect
import datetime
from .models import Records
from datetime import timedelta
from django.contrib import messages

def show(request):
    # Employee.objects.create(sid=202306,name='username', phone='123456',department='aa',ifcar=True)
    recordall = Records.objects.all()
    current_time = datetime.datetime.now() #当前时间 .strftime("%Y-%m-%d_%H:%M:%S")
    for record in recordall:
        if record.out_time is None:
            stay_seconds = timedelta.total_seconds(current_time-record.enter_time)
            s = int(stay_seconds)
            hours, remainder = divmod(s, 3600)
            minutes, seconds = divmod(remainder, 60)
            staytime = '{:02}:{:02}:{:02}'.format(int(hours), int(minutes), int(seconds))

            record.stay_time = staytime
        else:
            stay_seconds = timedelta.total_seconds(record.out_time - record.enter_time)
            s = int(stay_seconds)
            hours, remainder = divmod(s, 3600)
            minutes, seconds = divmod(remainder, 60)
            staytime = '{:02}:{:02}:{:02}'.format(int(hours), int(minutes), int(seconds))

            # staytime = stay_seconds.strftime('%H:%M:%S')
            record.stay_time = staytime
            # record.stay_time = record.out_time - record.enter_time

    return render(request, 'showrecords.html', {'recordall': recordall})

def carenter(request):
    if request.POST:

        # current_time = datetime.datetime.now().strftime("%Y-%m-%d_%H:%M:%S") #当前时间
        car_number = request.POST.get("enter_car_number") #addemployee.html name
        Records.objects.create(car_number=car_number, out_time=None)
        return redirect('/showRecord/')
    return render(request, 'entercar.html')

def carleave(request):
    if request.POST:
        car_number = request.POST.get("leave_car_number")
        if not list(Records.objects.filter(car_number=car_number)):
            messages.success(request, "不存在车辆进出记录")
            return redirect('/carLeave/')
        leave_sid = Records.objects.filter(car_number=car_number).last().sid  #若数据库中有多条该车牌号信息，选择最后一条信息的sid并以此更新
        Records.objects.filter(sid=leave_sid).update(out_time=datetime.datetime.now())
        return redirect('/showRecord/')
    return render(request, 'leavecar.html')

def delete(request,sid):
    Records.objects.get(sid=sid).delete()
    return redirect('/showRecord/')  # 重定向urls
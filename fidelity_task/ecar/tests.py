# Create your tests here.
from django.test import TestCase
from .models import Employee,Car,Records


# Create your tests here.
class ModelTest(TestCase):  # 创建ModelTest类，继承django.test.TestCase测试类。

    def setUp(self) -> None:
        Employee.objects.create(sid=202316, name='testemployee1', phone=15698521542, department='开发部门', birthday='2022-01-13')
        Car.objects.create(car_number='辽B1111C', user_id=202316, car_brand='宝马',car_color='red',car_type='轿车')
        Records.objects.create(car_number='辽B1111C')

    def test_Employee_models(self):
        result = Employee.objects.get(sid=202316)
        self.assertEqual(result.name, 'testemployee1')
        self.assertEqual(str(result.birthday), '2022-01-13')
        self.assertEqual(result.phone, '15698521542')
        # self.assertTrue(result.status)

    def test_Car_models(self):
        result = Car.objects.get(car_number='辽B1111C')
        self.assertEqual(result.user_id, 202316)
        # self.assertFalse(result.sign)

    def test_Records_models(self):
        result = Records.objects.get(car_number='辽B1111C')
        self.assertEqual(result.out_time, None)

    def test_delete_employee(self):
        em = Employee.objects.get(sid=202316)
        em.delete()
        em_ret = Employee.objects.filter(sid=202316)
        self.assertEqual(len(em_ret), 0)  #判断员工对应信息是否删除


    def test_delete_car(self):
        car = Car.objects.get(car_number="辽B1111C")
        car.delete()
        car_ret = Car.objects.filter(car_number="辽B1111C")
        self.assertEqual(len(car_ret), 0)  #判断车辆信息是否删除

    def test_update_employee(self):
        em = Employee.objects.get(sid=202316)
        em.name = "testupdate1"
        em.phone = "13256486563"
        em.department = "咨询部门"
        em.birthday = '1999-02-13'
        em.save()
        change = Employee.objects.get(sid=202316)
        self.assertEqual(change.name, "testupdate1")
        self.assertEqual(change.phone, "13256486563")
        self.assertEqual(change.department, "咨询部门")
        self.assertEqual(str(change.birthday), '1999-02-13')

    def test_update_car(self):
        car = Car.objects.get(car_number="辽B1111C")
        car.car_number = "辽A1653O"
        car.car_brand = "林肯"
        car.save()
        change = Car.objects.get(car_number="辽A1653O")
        self.assertEqual(change.car_brand, "林肯")
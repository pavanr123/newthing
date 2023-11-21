from django.db import models

# Create your models here.



class Employeesdetails(models.Model):
    employee_id = models.CharField(max_length=100)
    employee_name = models.CharField(max_length=100)
    gender = models.CharField(max_length=100)
    date_of_birth = models.CharField(max_length=100)
    department = models.CharField(max_length=100)
    designation = models.CharField(max_length=100)
    bank = models.CharField(max_length=100)
    ifsc_code = models.CharField(max_length=100)
    pan_card_number = models.CharField(max_length=100)
    uan_number = models.CharField(max_length=100)
    pf_number = models.CharField(max_length=100)
    paid_days = models.CharField(max_length=100)
    paid_leaves = models.CharField(max_length=100)
    date_of_jioning = models.CharField(max_length=100)
    account_number = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    basic = models.IntegerField(default=0)
    house_rent_allowances = models.IntegerField(default=0)
    medical_allowance = models.IntegerField(default=0)
    conveyance = models.IntegerField(default=0)
    special_allowance = models.IntegerField(default=0)
    phone_allowance = models.IntegerField(default=0)
    travel_allowance = models.IntegerField(default=0)
    employee_referral_scheme = models.IntegerField(default=0)
    bonus = models.IntegerField(default=0)
    professional_tax = models.IntegerField(default=0)
    provident_fund = models.IntegerField(default=0)
    t_d_s = models.IntegerField(default=0)
    loss_of_pay = models.IntegerField(default=0)
    def __str__(self):
        return self.employee_name






# class Employeedetails(models.Model):
#     employee_id = models.CharField(max_length=100)
#     employee_name = models.CharField(max_length=100)
#     gender = models.CharField(max_length=100)
#     date_of_birth = models.CharField(max_length=100)
#     department = models.CharField(max_length=100)
#     designation = models.CharField(max_length=100)
#     bank = models.CharField(max_length=100)
#     ifsc_code = models.CharField(max_length=100)
#     pan_card_number = models.CharField(max_length=100)
#     uan_number = models.CharField(max_length=100)
#     pf_number = models.CharField(max_length=100)
#     paid_days = models.CharField(max_length=100)
#     paid_leaves = models.CharField(max_length=100)
#     date_of_jioning = models.CharField(max_length=100)
#     account_number = models.CharField(max_length=100)
#     location = models.CharField(max_length=100)

#     def __str__(self):
#         return self.employee_name



# class Earnings(models.Model):
#     basic = models.IntegerField(default=0)
#     house_rent_allowances = models.IntegerField(default=0)
#     medical_allowance = models.IntegerField(default=0)
#     conveyance = models.IntegerField(default=0)
#     special_allowance = models.IntegerField(default=0)
#     phone_allowance = models.IntegerField(default=0)
#     salary_arrears = models.IntegerField(default=0)
#     employee_referral_scheme = models.IntegerField(default=0)
#     bonus = models.IntegerField(default=0)


# class Deductions(models.Model):
#     professional_tax = models.IntegerField(default=0)
#     provident_fund = models.IntegerField(default=0)
#     t_d_s = models.IntegerField(default=0)
#     loss_of_pay = models.IntegerField(default=0)


    

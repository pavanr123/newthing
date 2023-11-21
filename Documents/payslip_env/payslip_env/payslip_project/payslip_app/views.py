import calendar
from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render ,HttpResponse,redirect
from .models import Employeesdetails

# Create your views here.


def login(request):
    return render(request,'login.html')


def home(request):
    return render(request,'home.html')


def edit(request,id):
    emp = Employeesdetails.objects.get(id=id)
    return render(request,'edit.html',{"emp":emp})


def update(request,id):
    employee_id = request.POST['employee_id']
    employee_name = request.POST['employee_name']
    gender = request.POST['gender']
    date_of_birth = request.POST['date_of_birth']
    department = request.POST['department']
    designation = request.POST['designation']
    bank = request.POST['bank']
    ifsc_code = request.POST['ifsc_code']
    pan_card_number = request.POST['pan_card_number']
    uan_number = request.POST['uan_number']
    pf_number =  request.POST['pf_number']
    paid_days =  request.POST['paid_days']
    paid_leaves =  request.POST['paid_leaves']
    date_of_jioning =  request.POST['dateofjoining']
    account_number =  request.POST['account_number']
    location =  request.POST['location']
    basic =  request.POST['basic']
    # gross_deductions = request.POST['gross_deductions']

    emp = Employeesdetails.objects.get(id=id)

    emp.employee_id = employee_id
    emp.employee_name=employee_name
    emp.gender=gender
    emp.date_of_birth=date_of_birth
    emp.department=department
    emp.designation=designation
    emp.bank=bank
    emp.ifsc_code=ifsc_code
    emp.pan_card_number=pan_card_number
    emp.uan_number=uan_number
    emp.pf_number=pf_number
    emp.paid_days=paid_days
    emp.paid_leaves=paid_leaves
    emp.date_of_jioning=date_of_jioning
    emp.account_number=account_number
    emp.location=location
    emp.basic=basic
    # emp.gross_deductions=gross_deductions

    emp.save()
    return redirect("/get")
    

def view(request):
    emps = Employeesdetails.objects.all()
    result = {
        'emps': emps
    }
    return render(request ,'view.html',result)


def view_all(request):
    emps = Employeesdetails.objects.all()
    result = {
        'emps':emps
    }
    return render(request,'view_all.html',result)


def add(request):
    if request.method == 'POST':
        employee_id = request.POST['employee_id']
        employee_name = request.POST['employee_name']
        gender = request.POST['gender']
        date_of_birth = request.POST['date_of_birth']
        department = request.POST['department']
        designation = request.POST['designation']
        bank = request.POST['bank']
        ifsc_code = request.POST['ifsc_code']
        pan_card_number = request.POST['pan_card_number']
        uan_number = request.POST['uan_number']
        pf_number =  request.POST['pf_number']
        paid_days =  request.POST['paid_days']
        paid_leaves =  request.POST['paid_leaves']
        date_of_joining =  request.POST['dateofjoining']
        account_number =  request.POST['account_number']
        location =  request.POST['location']
        basic =  request.POST['basic']
        house_rent_allowances = request.POST['house_rent_allowances']
        medical_allowance = request.POST['medical_allowance']
        conveyance = request.POST['conveyance']
        special_allowance = request.POST['spical_allowance']
        phone_allowance = request.POST['phone_allowance']
        travel_allowance = request.POST['travel_allowance']
        employee_referral_scheme = request.POST['e_r_s']
        bonus = request.POST['bonus']
        professional_tax = request.POST['professional_tax']
        provident_fund = request.POST['provident']
        t_d_s = request.POST['t_d_s']
        loss_of_pay = request.POST['loss_of_pay']
        add_emp = Employeesdetails(employee_id = employee_id,employee_name=employee_name,gender=gender,date_of_birth=date_of_birth,department=department,designation=designation,
                                   bank=bank,ifsc_code=ifsc_code,pan_card_number=pan_card_number,uan_number=uan_number,pf_number=pf_number,
                                   paid_days=paid_days,paid_leaves=paid_leaves,date_of_jioning=date_of_joining,account_number=account_number,location=location,basic=basic,
                                   house_rent_allowances=house_rent_allowances,medical_allowance=medical_allowance,conveyance=conveyance,special_allowance=special_allowance,phone_allowance=phone_allowance,
                                   salary_arrears=travel_allowance,employee_referral_scheme=employee_referral_scheme,bonus=bonus,professional_tax=professional_tax,provident_fund=provident_fund,
                                   t_d_s=t_d_s,loss_of_pay=loss_of_pay)
        add_emp.save()
        return redirect("/get")
    elif request.method == "GET":
        return render(request,'add_emp.html')
    else:
        return HttpResponse("ERROR")
    # return render(request,'add_emp.html')

from django.shortcuts import render
from .models import Employeesdetails  # Import your model

def filter(request):
    if request.method == 'POST':
        name = request.POST['employee_name']
        month = request.POST['month']
        month_name = list(calendar.month_name).index(month.capitalize())
        _, total_days = calendar.monthrange(2023, month_name)
        absent_days = int(request.POST['absent'])
        # paid_leaves = int(request.POST.get('absent', 0))       
        emps = Employeesdetails.objects.all()
        if name:
            emps = emps.filter(employee_name=name)

        # # Calculate loss of pay
        # paid_leaves = int(request.POST.get('absent', 0))
        # loss_of_pay = (gross_earnings / total_days) * paid_leaves

        # Fetch the necessary data from the database
        # Assuming Employeesdetails model has fields for the earnings and deductions
        data = Employeesdetails.objects.filter(employee_name=name).values('basic', 'house_rent_allowances', 'medical_allowance', 'conveyance', 'special_allowance', 'phone_allowance', 'travel_allowance', 'employee_referral_scheme', 'bonus', 'professional_tax', 'provident_fund', 't_d_s').first()

        basic = data['basic']
        house_rent_allowances = data['house_rent_allowances']
        medical_allowance = data['medical_allowance']
        conveyance = data['conveyance']
        special_allowance = data['special_allowance']
        phone_allowance = data['phone_allowance']
        travel_allowance = data['travel_allowance']
        employee_referral_scheme = data['employee_referral_scheme']
        bonus = data['bonus']
        professional_tax = data['professional_tax']
        provident_fund = data['provident_fund']
        t_d_s = data['t_d_s']
        loss_of_pay = round((basic / total_days) * absent_days)
        gross_earning = basic + house_rent_allowances+ medical_allowance + conveyance + special_allowance + phone_allowance + travel_allowance + employee_referral_scheme + bonus
        gross_deductions = professional_tax + provident_fund + t_d_s + loss_of_pay
        net_pay = gross_earning - gross_deductions

        result = {
            'emps': emps,
            'month': month,
            'total_days': total_days,
            'absent': absent_days,
            'loss_of_pay': loss_of_pay,
            'net_pay': net_pay,
            'gross_earning': gross_earning,
            'gross_deductions': gross_deductions,

        }
        return render(request,'one_emp.html', result)

    elif request.method == 'GET':
        return render(request, 'filter_emp.html')

    return HttpResponse("ERROR")

# def convert_html_to_pdf(request):
#     if request.method == 'POST':
#         html_content = request.POST.get('html_content')  # Get the HTML content from the form submission

#         # # Create a file-like buffer to receive the PDF data
#         # buffer = BytesIO()

#         # # Convert HTML to PDF
#         # pisa.CreatePDF(html_content, dest=buffer)

#         # Get the PDF content from the buffer
#         pdf = buffer.getvalue()

#         # Close the buffer
#         buffer.close()

#         # Set the appropriate response headers
#         response = HttpResponse(content_type='application/pdf')
#         response['Content-Disposition'] = 'attachment; filename="converted_pdf.pdf"'

#         # Write the PDF content to the response
#         response.write(pdf)
#         return response

#     return render(request, 'one_emp.html')

































# def convert_html_to_pdf(request):
#     if request.method == 'POST':
#         html_content = request.POST.get('html_content')  # Get the HTML content from the form submission

#         # Generate a unique filename for the PDF
#         output_path = '/path/to/output.pdf'
#         # output_path = os.path.join(BASE_DIR, 'pdfs', 'output.pdf')


#         # Convert the HTML content to PDF using pdfkit
#         pdfkit.from_string(html_content, output_path)

#         # Optionally, you can return the PDF file as a response
#         with open(output_path, 'rb') as file:
#             response = HttpResponse(file.read(), content_type='application/pdf')
#             response['Content-Disposition'] = 'attachment; filename="converted_pdf.pdf"'
#             return response

#     return render(request, 'one_emp.html')
        

    #     return render(request, 'one_emp.html', result)

    # elif request.method == 'GET':
    #     return render(request, 'filter_emp.html')
    # else:
    #     return HttpResponse("ERROR")

# def calculate_components(request):
#     gross_package = 140000

#     # Calculate individual components
#     house_rent_allowances = gross_package * 0.25
#     medical_allowance = 15000  
#     conveyance = 8000  
#     phone_allowance = 2000  
#     travel_allowance = gross_package * 0.05 
#     special_allowance = gross_package - ( house_rent_allowances +  medical_allowance + conveyance + phone_allowance + travel_allowance)

#     # Create a string with the calculated values
#     result = f"HRA: {house_rent_allowances}\nMedical: { medical_allowance}\nConveyance: {conveyance}\nPhone: {phone_allowance}\nTravel: {travel_allowance}\nSpecial Allowance: {special_allowance}"

#     return HttpResponse(result)








































































































# def filter(request):
#     if request.method == 'POST':
#         name = request.POST['employee_name']
#         month = request.POST['month']
#         month_name = list(calendar.month_name).index(month.capitalize())
#         _, total_days = calendar.monthrange(2023, month_name)
#         absent_days = request.POST['absent']
#         emps = Employeesdetails.objects.all()
#         if name:
#             emps = emps.filter(employee_name=name)

#         # Calculate loss of pay
#         gross_earnings =  15000
#         paid_leaves = int(request.POST.get('absent', 0))
#         loss_of_pay = (gross_earnings / total_days) * paid_leaves

#         # Calculate the earnings
#         basic = 15000
#         hra =0
#         medical_allowance = 0
#         conveyance = 0  
#         special_allowance = 0  
#         phone_allowance = 0  
#         salary_arrears = 0 
#         employee_referral_scheme = 0  
#         bonus = 0  
#         gross_earning = basic + hra + medical_allowance + conveyance + special_allowance + phone_allowance + salary_arrears + employee_referral_scheme + bonus
#         net_pay = gross_earning - loss_of_pay

#         # Calculate the deductions
#         professional_tax = 0 
#         provident_fund = 0 
#         tds = 0  
#         gross_deductions = professional_tax + provident_fund + tds + loss_of_pay
#         result = {
#             'emps': emps,
#             'month': month,
#             'total_days': total_days,
#             'absent': absent_days,
#             'loss_of_pay': loss_of_pay,
#             'net_pay': net_pay,
#             'gross_earning': gross_earning,
#             'gross_deductions': gross_deductions,
#         }

#         return render(request, 'one_emp.html', result)

#     elif request.method == 'GET':
#         return render(request, 'filter_emp.html')
#     else:
#         return HttpResponse("ERROR")


















































































# def filter(request):
#     loss_of_pay = 0
#     net_pay=0
#     if request.method == 'POST':
#         # Existing code for filtering employee details
#         name = request.POST['employee_name']
#         month = request.POST['month']
#         month_name = list(calendar.month_name).index(month.capitalize())
#         _, total_days = calendar.monthrange(2023, month_name)
#         absent_days = request.POST['absent']
#         emps = Employeesdetails.objects.all()
#         if name:
#             emps = emps.filter(employee_name=name)
#         result = {
#             'emps': emps,
#             'month': month,
#             'total_days': total_days,
#             'absent': absent_days,
#             'loss_of_pay': loss_of_pay,
#             'net_pay': net_pay,
#         }

#         # Calculate loss of pay
#         gross_earnings = 15000
#         paid_leaves = int(request.POST.get('absent', 0))
#         loss_of_pay = (gross_earnings / total_days) * paid_leaves
#         result['loss_of_pay'] = loss_of_pay
        
#         return render(request, 'one_emp.html', result)

#     elif request.method == 'GET':
#         return render(request, 'filter_emp.html')
#     else:
#         return HttpResponse("ERROR")

































































    
 
# def filter(request):
#     if request.method == 'POST':
#         # id = request.POST['employee_id']
#         name = request.POST['employee_name']
#         month = request.POST['month']
#         month_name = list(calendar.month_name).index(month.capitalize())
#         _, total_days = calendar.monthrange(2023, month_name)
#         absent_days = request.POST['absent']
#         emps = Employeesdetails.objects.all()
#         # if id:
#         #     emps = emps.filter(employee_id = id)
#         if name:
#             emps = emps.filter(employee_name = name)
#         result = {
#         'emps': emps,
#         'month':month,
#         'total_days':total_days,
#         'absent': absent_days
#           }
#         return render(request,'one_emp.html',result)
#     elif request.method == 'GET':
#         return render(request ,'filter_emp.html')
#     else:
#         return HttpResponse("ERROR")   
    








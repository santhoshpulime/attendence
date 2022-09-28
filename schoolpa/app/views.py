from django.shortcuts import render,redirect
from .models import student,classroom,attendance
from django.http import HttpResponse,JsonResponse
from django.contrib.auth.models import User,auth
import vonage




def home(request):
	if request.user.username != 'school12':
		return redirect('login')
	classes = classroom.objects.all()
	return render(request,'home.html',{'cla':classes})




#students page class wise
def students_page(request,pk):
	students = student.objects.filter(studentclass=pk)
	student_class = student.objects.filter(studentclass=pk).first()
	print(student_class)
	return render(request,'students.html',{'stu':students,'stu_class':student_class.studentclass})




#showing students
def showstudents(request):
	if request.method == 'POST':
		cla = request.POST.get('cla')
		students = student.objects.filter(studentclass=cla)
		return JsonResponse({'students':list(students.values())})

	return JsonResponse({'status':'working'})


#send message 
def sendmsg(request):
	if request.method == 'POST':
		sid = request.POST.get('sid')
		print(sid)
		s_number = student.objects.filter(id=sid).first()
		pn = '91'+s_number.phonenumber
		print(pn)
		#sending sms to student number 
		client = vonage.Client(key="fae90bb8", secret="pG2ujU58elWVMRRK")
		sms = vonage.Sms(client)

		responseData = sms.send_message(
   		 {
        	"from": "Vonage APIs",
        	"to": "917893895732",
        	"text": "A text message sent using the Nexmo SMS API",
    	}
		)

		if responseData["messages"][0]["status"] == "0":


    			print("Message sent successfully.")
		else:
    			print(f"Message failed with error: {responseData['messages'][0]['error-text']}")
		return JsonResponse({'status':'sms sent..'})
	return JsonResponse({'status':' sms sent'})




#student attendance
def student_attendance(request):
	if request.method == 'POST':
		sid = request.POST.get('sid')
		a_value = request.POST.get('attendance_value')
		s_name = student.objects.filter(id=sid).first()
		print(s_name.studentname)

		data = attendance(studentname=s_name.studentname,pre_abs=a_value)
		data.save()
		return JsonResponse({'status':'attendance saved..'})
	return JsonResponse({'status':'hii..'})


#create student 
def create_student(request):

	return render(request,'createstudent.html')


def create_student_ajax(request):
	if request.method == 'POST':
		studentname = request.POST.get('studentname')
		rollnumber = request.POST.get('rollnumber')
		phonenumber = request.POST.get('phonenumber')
		studentclass = request.POST.get('student_class')
		data = student(
			studentname=studentname,
			rollnumber=rollnumber,
			phonenumber=phonenumber,
			studentclass=studentclass
			)
		data.save()
		return JsonResponse({'status':'saved'})
	return JsonResponse({'status':'hi'})


#login
def login(request):
	
	if request.method == 'POST':
		username = request.POST['username']
		password = request.POST['password']
		userdata = auth.authenticate(username=username,password=password)
		if userdata is not None:
			auth.login(request,userdata)

			return redirect('/')
		else:
			
			return redirect('login')
	return render(request,'login.html')
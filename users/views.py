import dotenv
dotenv.load_dotenv()
import os
API_KEY = os.environ.get('API_KEY')
token=os.environ.get('token')
time_api_key=os.environ.get('time_api_key')
from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.contrib import messages
from .forms import UserRegistrationForm
from users.models import data_collected
import time 
import datetime
from django.utils.timezone import make_aware
import requests
import json
from django.views.decorators.csrf import csrf_exempt,csrf_protect
from django.db import connection
from django.contrib.auth import logout

def count_username_instances(username):
    with connection.cursor() as cursor:
        cursor.execute("SELECT COUNT(*) FROM users_data_collected WHERE userid = %s", [username])
        count = cursor.fetchone()[0]
    return count
def get_last_login_date(userid):
    with connection.cursor() as cursor:
        cursor.execute(
            "SELECT start_date FROM users_data_collected WHERE userid = %s ORDER BY id DESC LIMIT 1",
            [userid]
        )
        row = cursor.fetchone()
        last_login_time = row[0] if row else None
    return last_login_time

from django.contrib.auth.views import LogoutView

# class CustomLogoutView(LogoutView):
    # def dispatch(self, request, *args, **kwargs):
    #     # Print a statement when the user logs out
    #     print("User logged out:", request.user.username)
    #     uid = request.session.get('uid')
    #     print("UID value:", uid)
    #     del request.session['uid']
    #     current_datetime = datetime.datetime.now()
    #     end_date = current_datetime.date()
    #     # print("the end date is ",end_date)
        
    #     obj = data_collected.objects.get(UID=uid)

    #     # Update the end_date field with the new value
    #     obj.end_date = end_date

    #     # Save the changes to the database
    #     obj.save()
    #     print("NEW STUFF------------")
    #     second_last_instance = data_collected.objects.filter(userid=request.user.username).order_by('-id')[1]
    #     second_last_instance.prev_date=end_date
    #     second_last_instance.save()
    #     obj = data_collected.objects.get(UID=uid)
    #     # obj.period=int(obj.prev_date-end_date)
    #     date_difference = (obj.prev_date - end_date).days
    #     # int(date_difference)
    #     print(date_difference)
    #     # print(type(int(date_difference)))

    #     obj.period=date_difference

    #     obj.save()
    #     print(end_date)
    #     print("data is updated ")
    #     return super().dispatch(request, *args, **kwargs)
class CustomLogoutView(LogoutView):
    def dispatch(self, request, *args, **kwargs):
        # Print a statement when the user logs out
        print("User logged out:", request.user.username)
        uid = request.session.get('uid')
        print("UID value:", uid)
        del request.session['uid']
        current_datetime = datetime.datetime.now()
        end_date = current_datetime.date()
        
        # Filter the queryset based on the UID
        objects_with_uid = data_collected.objects.filter(UID=uid)

        if objects_with_uid.exists():
            obj = objects_with_uid.first()  # Use the first object in the queryset
            # Update the end_date field with the new value
            obj.end_date = end_date
            # Save the changes to the database
            obj.save()

            print("NEW STUFF------------")
            second_last_instance = data_collected.objects.filter(userid=request.user.username).order_by('-id')[1]
            second_last_instance.prev_date = end_date
            second_last_instance.save()

            obj = data_collected.objects.get(UID=uid)
            date_difference = (obj.prev_date - end_date).days
            print(date_difference)
            print("data updated")
        else:
            print("No object found with UID:", uid)

        return super().dispatch(request, *args, **kwargs)

@csrf_exempt
def home(request):
  

    
        
    if request.user is not None :
            obj11=datetime.datetime.now()
            time_stamp=str(make_aware(obj11).hour)+"H"+str(make_aware(obj11).minute)+"M"
            date_stamp=str(make_aware(obj11).day)+"D"+str(make_aware(obj11).month)+"M"+str(make_aware(obj11).year)+"Y"
            print("asdasdasdasdsadasdsa",date_stamp)
            uid=str(request.user)+"UID"+time_stamp+"DD"+date_stamp
            print(uid)
            request.session['uid'] = uid
            total_start=time.time()
            #username start--------------------
            user_start=time.time()
            print("User: ", request.user)
            username=request.user
            instance_count = int(count_username_instances(username))+1
            print("total instance of the user is ",instance_count)
            last_login_date = get_last_login_date(username)
            print("the last login date",last_login_date)
            # uid=username+"UID"+current_time

            # print("uidasdasdasdasdasd",uid)
            user_end=time.time()
            totaltime_user=user_end-user_start
    #username end-------------------------------------
            #lang----------------start-----------
            lang_start=time.time()
            lang=request.META['HTTP_ACCEPT_LANGUAGE']
            # print(lang)
            lang_end=time.time()
            lang_totaltime=lang_end-lang_start
             #-------------lang end---------------
             #getting date and time ----------------------
            naive_datetime = datetime.datetime.now()
            naive_datetime.tzinfo  # None

            # settings.TIME_ZONE  # 'UTC'
            aware_datetime = make_aware(naive_datetime)
            aware_datetime.tzinfo  # <UTC>

            print("the real ip of the user",request.client_ip)
            
            start_timezone = time.time()

            local_timezone = datetime.datetime.now(datetime.timezone.utc).astimezone().tzinfo
            # print("Timezone of the user is --> ",local_timezone)
            # printing date and time 
            # print("Date Time: ",aware_datetime)
            # print('date time -----',naive_datetime.date())
            # print('date time -----',naive_datetime.time())
               #time collected 
           
            end_timezone = time.time()
            final_timezone=end_timezone-start_timezone
            print(final_timezone)

            #timezone done------------------------


             # getting ip-----------------------------------
            start_ip = time.time()

            
        


          

            ip1 = requests.get("https://api64.ipify.org/?format=json").json().get('ip')
            ip2 = requests.get("https://api-bdc.net/data/client-ip").json().get('ipString')
            ip3 = requests.get('https://ipapi.co/ip/').text.strip()

            ip_address = max(ip1, ip2, ip3) if ip1 == ip2 == ip3 else "All three values are different" if len({ip1, ip2, ip3}) == 3 else ip1
       
           
#             ip_address=print(request.META['REMOTE_ADDR'])

            print('the ip address-------',ip_address)
            end_ip = time.time()
            final_ip = print(end_ip-start_ip)
            #final ip=----------------



            #location start ----------------------
            # getting location from the ip 

            
          
            # response = requests.get(f'https://ipapi.co/{ip_address}/json/').json()
            


            #browser start----------------------------

            ua_starttime = time.time()

            browser_ua = request.user_agent.browser
            system_ua = request.user_agent.os
            ua_endtime = time.time()
            ua_totaltime = ua_endtime - ua_starttime

            webgl = ''
            canvas_hash = ''
            browser_version = ''
            user_agent = ''
            OS = ''
            screen_res_height = ''
            screen_res_width = ''
            # latitude=''
            if request.method == 'POST':
                latitude=None
                longitude=None
                data = json.loads(request.body.decode('utf-8'))
                # print(type(data),data)
                webgl = data['data']['webgl']
                webgl_total_time = data['data']['webgl_total_time']
                canvas_hash = data['data']['canvas_hash']
                canvas_total_time = data['data']['canvas_total_time']
                plugins = data['data']['plugins']
                plugins_totaltime = data['data']['plugins_totaltime']
                browser_fonts = data['data']['browser_fonts']
                browser_fonts_totaltime = data['data']['browser_fonts_totaltime']
                browser_version = data['data']['browser_version']
                browser_version_total_time = data['data']['browser_version_total_time']
                user_agent = data['data']['userAgent']
                useragent_total_time = data['data']['useragent_total_time']
                OS = data['data']['OS']
                os_plat_total_time = data['data']['os_plat_total_time']
                screen_res_height = data['data']['screen_res_height']
                screen_res_width = data['data']['screen_res_width']
                screen_res_total_time = data['data']['screen_res_total_time']
                device_type_final = data['data']['device_type_final']
                latitude=data['data']['latitude']
                longitude=data['data']['longitude']
           
                time_url="https://api.ipgeolocation.io/ipgeo?apiKey={0}&ip={1}".format(time_api_key,request.client_ip)
                # time_url="https://api.ipgeolocation.io/ipgeo?apiKey={0}&ip={1}".format(time_api_key,"122.180.223.178")
                res=requests.get(time_url).json()
                print(time_url)
                current_time = res['time_zone']['current_time']
                print(current_time)
                parsed_time = datetime.datetime.strptime(current_time, "%Y-%m-%d %H:%M:%S.%f%z")
                time_only = parsed_time.time()
                print("Date only:", parsed_time.date())
                print("Time only:", time_only)
                date = datetime.datetime.strptime(str(parsed_time.date()), "%Y-%m-%d")
                day_name = date.strftime("%A") 
                print(day_name) 

            
                time_zone=None
                if latitude is not None and longitude is not None:
                    location_start=time.time()

                    print("collected from getCurrentLocation",latitude,longitude)
                    url = "https://api.geoapify.com/v1/geocode/reverse?lat={0}&lon={1}&format=json&apiKey={2}".format(latitude,longitude,API_KEY)
                    res=requests.get(url).json()
                    print(url)
                    # print("using geolocay->",res)
                    city=res['results'][0]['city']
                    # print(city)
                    country=res['results'][0]['country']
                    region=res['results'][0]['state']
                    location_final = str(res['results'][0]['country'])+str(res['results'][0]['state'])+str(res['results'][0]['city'])
                    time_zone = res.get('results', [{}])[0].get('timezone', {}).get('name')
                    lat_long=str(latitude)+":"+str(longitude)
                
                else:
                    url="https://ipinfo.io/{0}?token={1}".format(request.client_ip,token) 
                    # url="https://ipinfo.io/{0}?token={1}".format("34.82.78.16",token) 
                    print(url)
                    res=requests.get(url).json()
                    print(res)
                    city = res['city']
                    region = res['region']
                    country = res['country']
                    lat_long = res['loc']
                    print("user denied access latlong inside-->",lat_long)
                    location_final=str(res['country'])+"-"+str(res['region'])+"-"+str(res['city'])
                    time_zone = res['timezone']
                
                    # "ip": ip_address,
                    # city= response.get("city")
                
                    
                    # country= response.get("country_name")
                    # print(data)
                   
              
                total_end=time.time()
                print("user denied access latlong outside -->",lat_long)
                # csrf_token = csrf.get_token(request)
                    # print(request.META)
                browser_final=str(browser_ua.family)+"-"+str(browser_ua.version_string)
                OS=str(system_ua.family)+"-"+str(system_ua.version_string)
                    # print(ip_address)
                login_status='NFE'
                screen_size=str(screen_res_height)+":"+str(screen_res_width)
                overall_totaltime=total_end-total_start
                data=data_collected(UID=uid,prev_date=last_login_date,login_count=instance_count,login_status=login_status,start_week=day_name,screen_size=screen_size,Os=OS,system_type=device_type_final,userid=username,latlong=lat_long,browser=browser_final,location=location_final,webgl=webgl,canvas=canvas_hash,ip=request.client_ip,language=lang,login_time=str(parsed_time.time()),start_date=str(parsed_time.date()),time_zone=time_zone,rtt=overall_totaltime)
                data.save()
    return render(request, 'users/home.html')

def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()

            messages.success(request, f'Your account has been created. You can log in now!')    
            return redirect('login')
    else:
        form = UserRegistrationForm()

    context = {'form': form}
    return render(request, 'users/register.html', context)
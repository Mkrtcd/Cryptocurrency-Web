# Cryptocurrency-Web
How to run? On Linux (Mac) machine, first cd into the corresponding directory, look for manage.py file, python3 manage.py runserver 0.0.0.0:8000. Open you browser and open webpage http://127.0.0.1:8000. Currently only two page was created, http://127.0.0.1:8000/homepage/ and http://127.0.0.1:8000.

If the above command doesnt work, try pip3 install django first. 

For html (UI design), please put all html file under templates folder. 

Please pay attention to version control

If you run the django project, there might be a error occuring, due to the missing of secret key. Please use the secret key provided, copy and paste to the corresponding variable in settings.py 

PLEASE REMOVE THE SECRET KEY FROM setting.py BEFORE EACH COMMIT. 

M. Lai
2022/03/05
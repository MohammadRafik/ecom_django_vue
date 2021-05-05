#### eCommerce website made with django and vue.js hosted on an AWS EC2 instance inside a docker container


## How to set up
please note the commands below are for the bash shell on linux, you will need to make some changes to the commands to make it work on windows
1. get python version 3.7 (it does not work on some other python versions so make sure its 3.7),and make sure you also have pip
2. clone the project `git clone https://github.com/MohammadRafik/ecom_django_vue.git`
3. redirect path to ecom_django_vue `cd ecom_django_vue`
4. create a virtual environment `python3 -m venv env`
5. activate the virtual env `source env/bin/activate`
6. run `pip3 install -r requirements.txt`
now you need to run a local server using django, so do this:
7. run `python3 src/manage.py runserver`
on a browser if you go to 127.0.0.1:8000 you should be able to see the site now

to also setup the front-end with webpacks and generate a new bundled js file follow the steps below:
1. make sure you are in the correct path as the steps before, you should be in `ecom_django_vue`
2. run `npm install`
3. run `./node_modules/.bin/webpack --config ./webpack.config.js`
this will create a new app.js file and replace the old one. its located at ./src/assets/bundles/app.js

to see the deployment version go to the [deployment branch](https://github.com/MohammadRafik/ecom_django_vue/tree/deployment)

gif demo: 

![](ecom_demo.gif)

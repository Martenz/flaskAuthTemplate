see https://www.digitalocean.com/community/tutorials/how-to-add-authentication-to-your-app-with-flask-login

create the virtualenv:
```
python
sudo apt install -y python3-venv
mkdir environments
cd environments
python -m venv my_env
source my_env/bin/activate
```

Enable apache2 proxypass
```   
sudo a2enmod proxy
sudo a2enmod proxy_http
sudo a2enmod proxy_balancer
sudo a2enmod lbmethod_byrequests

```

Example of apache conf file with proxypass:

```
<VirtualHost *:80>
	ServerName mydomain.com
    ProxyPreserveHost On

    ProxyPass / http://127.0.0.1:5000/
    ProxyPassReverse / http://127.0.0.1:5000/

</VirtualHost>

```


To enable the service file edit the flask_app.service with the correct paths, then:

```
cp flask_app.service /etc/systemd/system/flask_app.service
systemctl enable flask_app.service 
systemctl daemon-reload
systemctl start flask_app.service
```


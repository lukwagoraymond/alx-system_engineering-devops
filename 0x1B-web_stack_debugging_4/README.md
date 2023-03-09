# 0x1B. Web stack debugging #4

## Resources:books:
Read or watch:
* [NGINX Access Logs and Error Logs](https://www.digitalocean.com/community/tutorials/nginx-access-logs-error-logs)
* [How to set nginx max open files?](https://stackoverflow.com/questions/27849331/how-to-set-nginx-max-open-files)
* [Understanding /etc/security/limits.conf file](https://www.thegeekdiary.com/understanding-etc-security-limits-conf-file-to-set-ulimit/)

---
## Learning Objectives:bulb:
What you should learn from this project:

---

### [0. Sky is the limit, let's bring that limit higher](./0-the_sky_is_the_limit_not.pp)
* In this web stack debugging task, we are testing how well our web server setup featuring Nginx is doing under pressure and it turns out it’s not doing well: we are getting a huge amount of failed requests. 


### [1. User limit](./1-user_limit.pp)
* Change the OS configuration so that it is possible to login with the holberton user and open a file without any error message.

---

## Author
* **Raymond Lukwago** - [lukwagoraymond](https://github.com/raymondlukwago)

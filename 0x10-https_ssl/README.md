# 0x10. HTTPS SSL

## Resources:books:
Read or watch:
* [What is HTTPS?](https://www.instantssl.com/http-vs-https)
* [What are the 2 main elements that SSL is providing](https://www.sslshopper.com/why-ssl-the-purpose-of-using-ssl-certificates.html)
* [HAProxy SSL termination on Ubuntu16.04](https://devops.ionos.com/tutorials/install-and-configure-haproxy-load-balancer-on-ubuntu-1604/)
* [SSL termination](https://en.wikipedia.org/wiki/TLS_termination_proxy)
* [Bash function](https://tldp.org/LDP/abs/html/complexfunct.html)
* [How To Use Certbot Standalone Mode to Retrieve Let's Encrypt SSL Certificates on Ubuntu 16.04](https://www.digitalocean.com/community/tutorials/how-to-use-certbot-standalone-mode-to-retrieve-let-s-encrypt-ssl-certificates-on-ubuntu-16-04)


---

## man or help
* awk
* dig

---

## Learning Objectives:bulb:
What you should learn from this project:

* What is HTTPS SSL 2 main roles
* What is the purpose encrypting traffic
* What SSL termination means

---

### [0. World wide web](./0-world_wide_web)
* Configure your domain zone so that the subdomain www points to your load-balancer IP (lb-01).
Let’s also add other subdomains to make our life easier, and write a Bash script that will display information about subdomains.


### [1. HAproxy SSL termination](./1-haproxy_ssl_termination)
* “Terminating SSL on HAproxy” means that HAproxy is configured to handle encrypted traffic, unencrypt it and pass it on to its destination.


### [2. No loophole in your website traffic](./100-redirect_http_to_https)
* A good habit is to enforce HTTPS traffic so that no unencrypted traffic is possible. Configure HAproxy to automatically redirect HTTP traffic to HTTPS.

---

## Author
* **Raymond Lukwago** - [lukwagoraymond](https://github.com/lukwagoraymond)

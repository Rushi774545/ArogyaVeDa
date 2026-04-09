# Comprehensive Deployment Guide: ArogyaVeda (Secure Subpath Deployment)

This guide provides the final, verified instructions to deploy the ArogyaVeda platform (Django + React) to an Azure VM at `arogyaveda.duckdns.org` with full HTTPS/SSL.

---

## 1. Prerequisites (Azure VM & DuckDNS)
- **VM IP**: `4.186.26.113`
- **Domain**: `arogyaveda.duckdns.org` (Pointed to IP)
- **DuckDNS Token**: `5c15c08c-4400-40f4-9baa-e4b9e9de2200`

---

## 2. Server Setup (Ubuntu 22.04+)

```bash
# 1. Core dependencies
sudo apt update && sudo apt upgrade -y
sudo apt install python3-pip python3-venv nginx snapd -y

# 2. Node.js 20 & PM2
curl -fsSL https://deb.nodesource.com/setup_20.x | sudo -E bash -
sudo apt install -y nodejs
sudo npm install pm2 -g

# 3. Certbot via Snap (Latest Version)
sudo snap install --classic certbot
sudo ln -sf /snap/bin/certbot /usr/bin/certbot
```

---

## 3. Backend Deployment (Django)

```bash
cd /home/azureuser/ArogyaVeDa/ArogyaVeda

# 1. Setup Environment
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt gunicorn

# 2. Run Gunicorn via PM2 (120s timeout for model loading)
pm2 start "venv/bin/gunicorn --bind 127.0.0.1:8000 --timeout 120 ArogyaVeda.wsgi" --name "arogyaveda-backend"
pm2 save
```

---

## 4. Frontend Deployment (React)

Ensure `vite.config.js` has `base: '/frontend/'` and `App.jsx` has `basename="/frontend"`.

```bash
cd /home/azureuser/ArogyaVeDa/ArogyaVeda/frontend
npm install
npm run build
```

---

## 5. SSL Security (Certbot DNS-01)

We use DNS-01 challenge with DuckDNS hooks to secure the site without needing port 80/443 for validation.

### A. Create Auth Hook (`/usr/local/bin/duckdns-auth.sh`)
```bash
#!/bin/bash
TOKEN="YOUR_TOKEN"
curl -s "https://www.duckdns.org/update?domains=arogyaveda&token=$TOKEN&txt=$CERTBOT_VALIDATION"
sleep 30
```

### B. Obtain Certificate
```bash
sudo certbot certonly --manual --preferred-challenges dns \
  --manual-auth-hook /usr/local/bin/duckdns-auth.sh \
  --manual-cleanup-hook /usr/local/bin/duckdns-cleanup.sh \
  -d arogyaveda.duckdns.org --non-interactive --agree-tos --email webmaster@arogyaveda.duckdns.org
```

---

## 6. Nginx Configuration (HTTPS)

```nginx
server {
    listen 80;
    server_name arogyaveda.duckdns.org;
    return 301 https://$host$request_uri;
}

server {
    listen 443 ssl;
    server_name arogyaveda.duckdns.org;

    ssl_certificate /etc/letsencrypt/live/arogyaveda.duckdns.org/fullchain.pem;
    ssl_certificate_key /etc/letsencrypt/live/arogyaveda.duckdns.org/privkey.pem;

    # 1. Frontend Subpath
    location /frontend/ {
        alias /home/azureuser/ArogyaVeDa/ArogyaVeda/frontend/dist/;
        index index.html;
        try_files $uri $uri/ /frontend/index.html;
    }

    # 2. Backend API (Nginx strips /backend/ and proxies to Gunicorn)
    location /backend/ {
        proxy_pass http://127.0.0.1:8000/;
        proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_addr;
        proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
        proxy_set_header X-Forwarded-Proto $scheme;
    }

    # Redirect root to frontend
    location / {
        return 301 https://arogyaveda.duckdns.org/frontend/;
    }
}
```

---

## 7. Verification

- **Frontend**: `https://arogyaveda.duckdns.org/frontend/`
- **Admin**: `https://arogyaveda.duckdns.org/backend/admin/`

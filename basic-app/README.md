# Basic app

## Quickstart

```bash
docker compose up --build [-d]

docker compose down
```

Run with Nginx as load balancer:

```bash
docker compose -f docker-compose.lb.yml up --build [-d]

docker compose -f docker-compose.lb.yml down
```

## `systemd` service

See [shiny-basic-app.service](shiny-basic-app.service)

```bash
# Create dir where you want to put your apps
mkdir -p /opt/shiny_apps

# Copy app
cp -r basic-app /opt/shiny_apps/my_app

# Add service file tp systemd dir
cp shiny-basic-app.service /etc/systemd/system/shiny-app.service

# Setup virtual env
cd /opt/shiny_apps
uv init
uv add -r my_app/requirements.txt

# Reload daemon
systemctl daemon-reload

# Start service
systemctl start shiny-app
systemctl status shiny-app
```

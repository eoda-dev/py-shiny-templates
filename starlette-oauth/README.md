# Use Starlette to secure your Shiny App

```bash
shiny create -g eoda-dev/py-shiny-templates -t starlette-oauth

cd starlette-oauth

uv init
uv add -r requirements.txt

# Add .env file with the following content
GITLAB_CLIENT_ID=your-client-id
GITLAB_CLIENT_SECRET=your-client-secret

uvicorn app:app
```

Then navigate to [http://localhost:8000](http://localhost:8000) and login with your GitLab credentials.

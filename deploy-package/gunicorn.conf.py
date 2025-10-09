# Gunicorn configuration for Azure App Service
import os

# Server socket - Azure provides PORT environment variable
bind = f"0.0.0.0:{os.environ.get('PORT', 8000)}"

# Worker processes
workers = 1
worker_class = "uvicorn.workers.UvicornWorker"

# Logging
loglevel = "info"
accesslog = "-"
errorlog = "-"

# Timeout settings
timeout = 120
keepalive = 2
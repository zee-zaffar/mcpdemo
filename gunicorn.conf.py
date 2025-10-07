# Gunicorn configuration for Azure App Service
import os

# Server socket
bind = f"0.0.0.0:{os.environ.get('PORT', 8000)}"

# Worker processes
workers = 1
worker_class = "uvicorn.workers.UvicornWorker"

# Logging
loglevel = "info"
accesslog = "-"
errorlog = "-"
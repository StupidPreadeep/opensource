# middleware.py

from fastapi import Request
import logging
import time

logger = logging.getLogger(__name__)

class RequestInitTimeMiddleware:
    def __init__(self, app):
        self.app = app

    async def __call__(self, scope, receive, send):
        request = Request(scope, receive)
        start_time = time.time()

        # Store the start time in the request state
        scope['app_state'] = {
            'request_start_time': start_time
        }

        async def send_wrapper(response):
            # Calculate request processing time
            end_time = time.time()
            duration_ms = (end_time - start_time) * 1000

            # Log the request initiation time
            logger.info(f"Request {request.url.path} initiated in {duration_ms:.2f} ms")

            await send(response)

        await self.app(scope, receive, send_wrapper)

import time
from django.http import JsonResponse

# Store requests temporarily in memory (reset when server restarts)
VISITOR_REQUESTS = {}

def rate_limit(max_requests=5, timeframe=60):  # 5 requests per 60 seconds
    def decorator(view_func):
        def wrapper(request, *args, **kwargs):
            ip = get_client_ip(request)
            now = time.time()

            if ip not in VISITOR_REQUESTS:
                VISITOR_REQUESTS[ip] = []

            # Filter timestamps to only keep those within the timeframe
            VISITOR_REQUESTS[ip] = [t for t in VISITOR_REQUESTS[ip] if now - t < timeframe]

            if len(VISITOR_REQUESTS[ip]) >= max_requests:
                return JsonResponse(
                    {
                        "error": "Too many requests. Please try again later."
                    },
                    status=429
                )

            VISITOR_REQUESTS[ip].append(now)
            return view_func(request, *args, **kwargs)
        return wrapper
    return decorator

def get_client_ip(request):
    """Utility to get the client's IP address from the request"""
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')
    return ip

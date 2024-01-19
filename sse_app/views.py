import time
from django.http import StreamingHttpResponse

def sse_stream(request):
    def event_stream():
        # Send an initial message to the client
        yield "data: Initial message\n\n"
        time.sleep(1)  # Add a delay for demonstration purposes

        # Send periodic updates to the client
        for i in range(5):
            yield f"data: Update {i}\n\n"
            time.sleep(5)

    response = StreamingHttpResponse(event_stream(), content_type='text/event-stream')
    response['Cache-Control'] = 'no-cache'
    return response


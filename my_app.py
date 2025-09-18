import http.server
import random
import time
from prometheus_client import start_http_server, Counter, Gauge, Summary, Histogram

# Metrics from all examples
REQUEST_COUNT = Counter('app_requests_count', 'total app http request count', ['app_name', 'endpoint'])
RANDOM_COUNT = Counter('app_random_count', 'increment counter by random value')
REQUEST_INPROGRESS = Gauge('app_requests_inprogress', 'number of application requests in progress')
REQUEST_LAST_SERVED = Gauge('app_last_served', 'Time the application was last served.')
REQUEST_RESPOND_TIME_SUMMARY = Summary('app_response_latency_seconds', 'Response latency in seconds')
REQUEST_RESPOND_TIME_HISTOGRAM = Histogram('app_response_latency_seconds_histogram', 
                                          'Response latency in seconds histogram', 
                                          buckets=[0.1, 0.5, 1, 2, 3, 4, 5, 10])

APP_PORT = 8000
METRICS_PORT = 8001

class HandleRequests(http.server.BaseHTTPRequestHandler):

    @REQUEST_INPROGRESS.track_inprogress()
    @REQUEST_RESPOND_TIME_SUMMARY.time()
    @REQUEST_RESPOND_TIME_HISTOGRAM.time()
    def do_GET(self):
        # Increment request count with labels
        REQUEST_COUNT.labels('prom_python_app', self.path).inc()
        
        # Increment random counter
        random_val = random.random() * 10
        RANDOM_COUNT.inc(random_val)
        
        # Simulate processing time (sleep)
        time.sleep(7)
        
        # Send response
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()
        self.wfile.write(bytes("<html><head><title>First Application</title></head><body style='color: #333; margin-top: 30px;'><center><h2>Welcome to our first Prometheus-Python application.</center></h2></body></html>", "utf-8"))
        self.wfile.close()
        
        # Set last served time
        REQUEST_LAST_SERVED.set_to_current_time()

if __name__ == "__main__":
    # Start metrics server
    start_http_server(METRICS_PORT)
    
    # Start application server
    server = http.server.HTTPServer(('0.0.0.0', APP_PORT), HandleRequests)
    print(f"Application server running on port {APP_PORT}")
    print(f"Metrics server running on port {METRICS_PORT}")
    server.serve_forever()

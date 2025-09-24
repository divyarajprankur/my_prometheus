# My Prometheus Demo

A hands-on repository to learn and experiment with **Prometheus monitoring**, including Python applications, exporters, alerting rules, and dashboards.  
This project demonstrates how to expose metrics from a Python app and configure Prometheus + Alertmanager to monitor them.

---

## 📂 Repository Structure

```text
my_prometheus/
│
├── my_app.py              # Example Python web app exposing Prometheus metrics
├── boilerplate.py          # Utility / setup scaffolding for metrics
│
├── counter.py              # Counter metric example
├── gauge.py                # Gauge metric example
├── histogram.py            # Histogram metric example
├── summary.py              # Summary metric example
│
├── prometheus.yml          # Prometheus main configuration file
├── alertmanager.yml        # Alertmanager configuration
├── alertmanager.yml.bkp2   # Backup of Alertmanager config
├── cloudwatchexporter.yml  # Example config for AWS CloudWatch exporter
│
├── rules.yml               # Generic Prometheus alerting rules
├── webrules.yml            # Web app–related alerting rules
├── linuxrules.yml          # Linux host monitoring rules
├── windowsrules.yml        # Windows host monitoring rules
````

---

## 🚀 Getting Started

### 1. Clone the Repository

```bash
git clone https://github.com/divyarajprankur/my_prometheus.git
cd my_prometheus
```

### 2. Install Dependencies

Make sure you have Python 3.8+ and `pip` installed.
Install requirements:

```bash
pip install prometheus-client flask
```

### 3. Run the Example App

Start the sample Python app (exposes metrics at `http://localhost:8000/metrics`):

```bash
python my_app.py
```

### 4. Run Prometheus

Download Prometheus (if not already installed):
👉 [https://prometheus.io/download/](https://prometheus.io/download/)

Start Prometheus using the provided config:

```bash
./prometheus --config.file=prometheus.yml
```

### 5. Run Alertmanager

Download Alertmanager:
👉 [https://prometheus.io/download/#alertmanager](https://prometheus.io/download/#alertmanager)

Start it with:

```bash
./alertmanager --config.file=alertmanager.yml
```

---

## 📊 Metrics Exposed

Each file demonstrates a different **Prometheus metric type**:

* **Counter** (`counter.py`) → counts events (e.g., requests served).
* **Gauge** (`gauge.py`) → tracks a value that can go up and down (e.g., memory usage).
* **Histogram** (`histogram.py`) → measures request durations, latencies, etc.
* **Summary** (`summary.py`) → similar to histogram, but supports quantiles.

---

## 🔔 Alerting Rules

* `rules.yml` → General alerts
* `webrules.yml` → Web app–specific alerts
* `linuxrules.yml` → Linux system monitoring
* `windowsrules.yml` → Windows system monitoring

These rules can be customized and plugged into `prometheus.yml`.

---

## ☁️ Exporters

* `cloudwatchexporter.yml` → Example config for scraping AWS CloudWatch metrics.

You can adapt this to integrate cloud metrics into your Prometheus stack.

---

## 🛠️ Roadmap / To-Do

* [ ] Add Docker support (Prometheus, Alertmanager, Python app)
* [ ] Create Grafana dashboards
* [ ] Write unit tests for metric endpoints
* [ ] Expand documentation with real-world use cases

---

## 📜 License

This project is for **educational and demo purposes**.
Feel free to fork, adapt, and use it in your learning journey with Prometheus.

```

---

Would you like me to also create a **docker-compose.yml** so you can run Prometheus + Alertmanager + your Python app in one go? That way, users just need `docker-compose up`.
```

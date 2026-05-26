# AI Network Troubleshooter

AI Network Troubleshooter is a full-stack cybersecurity and network analysis platform that automates packet capture analysis, identifies networking issues, and generates AI-powered troubleshooting reports.

The platform enables users to upload PCAP files, analyze network traffic, identify potential security concerns, and generate professional PDF reports for investigation and documentation.

Built to simulate the workflow of Network Support Engineers, Security Analysts, and Technical Support Engineers working with enterprise networking environments.

---

## Features

### Packet Analysis

- Upload and analyze PCAP files
- Protocol distribution analysis
- Packet count statistics
- Top talkers identification
- DNS query extraction

### Network Troubleshooting

- TCP handshake analysis
- Failed connection detection
- Severity assessment
- Root cause identification

### Advanced Network Intelligence

- Top destination ports
- TLS version analysis
- HTTP host extraction
- User-Agent extraction

### AI-Powered Diagnostics

- Automated root cause analysis
- Security observations
- Troubleshooting recommendations
- Severity classification

### Reporting

- Analysis history
- Persistent PostgreSQL storage
- PDF report generation
- Case review workflow

---

# Dashboard

The dashboard provides:

### Network Overview

- Total packets
- Protocol count
- Failed TCP connections
- Severity level

### Traffic Analysis

- Protocol distribution chart
- Top talkers chart
- Top ports analysis

### Application Intelligence

- DNS queries
- HTTP hosts
- User agents

### Security Analysis

- Potential issues
- AI diagnostic report

---

# Architecture

```text
                +----------------+
                | React Frontend |
                +-------+--------+
                        |
                        v
                +----------------+
                | FastAPI Backend|
                +-------+--------+
                        |
         +--------------+--------------+
         |                             |
         v                             v

 +---------------+        +----------------------+
 | PCAP Analyzer |        | AI Diagnostics Engine|
 +-------+-------+        +----------+-----------+
         |                           |
         +------------+--------------+
                      |
                      v

             +----------------+
             | PostgreSQL DB |
             +----------------+

                      |
                      v

             +----------------+
             | PDF Reporting |
             +----------------+
```

---

# Technology Stack

## Frontend

- React
- Vite
- Tailwind CSS
- React Router
- Axios
- Recharts

## Backend

- FastAPI
- SQLAlchemy
- PostgreSQL
- JWT Authentication

## Network Analysis

- TShark
- Wireshark
- PyShark

## Artificial Intelligence

- OpenAI GPT

## Reporting

- ReportLab

---

# Example Workflow

### 1. Upload Packet Capture

Upload a `.pcap` file through the dashboard.

### 2. Network Analysis

The platform automatically extracts:

- Protocols
- Top talkers
- DNS activity
- TCP handshake statistics
- TLS information
- HTTP hosts
- User agents

### 3. AI Diagnostic Report

The AI engine generates:

- Root cause summary
- Security observations
- Troubleshooting recommendations
- Severity assessment

### 4. Save Analysis

Results are stored in PostgreSQL for future review.

### 5. Export Report

Generate a professional PDF report for documentation and investigation.

---

# Screenshots

## Dashboard

```markdown
![Dashboard1](screenshots/dashboard1.png)
```
```markdown
![Dashboard2](screenshots/dashboard2.png)
```

## AI Report

```markdown
![AI-Report](screenshots/aireport.png)
```

## Analysis History

```markdown
![History](screenshots/history.png)
```

## PDF Report

```markdown
![PDF Report](screenshots/report.png)
```

---

# Installation

## Clone Repository

```bash
git clone https://github.com/YOUR_USERNAME/ai-network-troubleshooter.git

cd ai-network-troubleshhoter
```

---

## Backend Setup

```bash
cd backend

python -m venv venv

source venv/bin/activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

---

## PostgreSQL Setup

Login:

```bash
sudo -u postgres psql
```

Create database:

```sql
CREATE DATABASE ai_network_troubleshooter;
```

Create user:

```sql
CREATE USER aiuser WITH PASSWORD 'password';
```

Grant permissions:

```sql
GRANT ALL PRIVILEGES ON DATABASE ai_network_troubleshooter TO aiuser;
```

Exit:

```sql
\q
```

---

## Environment Variables

Create:

```text
backend/.env
```

Add:

```env
DATABASE_URL=postgresql://aiuser:password@localhost/ai_network_troubleshooter

OPENAI_API_KEY=your_openai_api_key
```

---

## Initialize Database

```bash
python -m app.db.init_db
```

---

## Start Backend

```bash
uvicorn app.main:app --reload
```

Swagger:

```text
http://localhost:8000/docs
```

---

## Frontend Setup

Open a new terminal:

```bash
cd frontend

npm install

npm run dev
```

Frontend:

```text
http://localhost:5173
```

---

# Project Structure

```text
ai-network-troubleshhoter/

├── backend/
│   ├── app/
│   │   ├── api/
│   │   ├── ai/
│   │   ├── analyzers/
│   │   ├── core/
│   │   ├── db/
│   │   ├── models/
│   │   └── services/
│   │
│   ├── uploads/
│   ├── reports/
│   └── requirements.txt
│
├── frontend/
│   ├── src/
│   │   ├── components/
│   │   ├── pages/
│   │   └── assets/
│   │
│   └── package.json
│
└── README.md
```

---

# Sample Analysis Output

```json
{
  "packet_count": 1194,
  "protocols": {
    "TCP": 541,
    "TLSv1.3": 419,
    "DNS": 36
  },
  "top_ports": [
    ["443", 460],
    ["80", 4]
  ],
  "http_hosts": [
    "example.com",
    "neverssl.com"
  ]
}
```

---

# Use Cases

### Network Troubleshooting

- Connectivity issues
- Failed TCP connections
- DNS troubleshooting

### Security Analysis

- Port scanning detection
- Suspicious traffic identification
- Network reconnaissance analysis

### Technical Support

- Root cause analysis
- Incident investigation
- Customer issue documentation

---

# Future Enhancements

- Threat Detection Engine
- Live Packet Capture
- Clickable Historical Analyses
- Docker Deployment
- Cloud Deployment
- Advanced Threat Hunting Features

---

# Skills Demonstrated

This project demonstrates:

- TCP/IP Analysis
- Network Troubleshooting
- Packet Capture Analysis
- FastAPI Development
- PostgreSQL Database Design
- React Frontend Development
- AI Integration
- Security Analysis
- Root Cause Investigation
- Technical Reporting
- REST API Development

---


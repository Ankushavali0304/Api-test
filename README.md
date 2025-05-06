# 📘 API Testing Framework – README

## 📂 Project Overview

This repository contains a structured API testing framework using:
- `Pytest` for test execution
- `Allure` for generating detailed reports
- Custom utilities for API handling, logging, and validations

---

## 🏗️ Project Structure

```
project-root/
│
├── tests/
│   ├── user/
│   │   └── test_create_user.py
│   │   └── test_get_user.py
│   ├── jobs/
│   │   └── test_job_status.py
│   └── conftest.py
│
├── utils/
│   └── api_client.py
│   └── validators.py
│
├── logs/
│   └── logger.py
│
├── config/
│   └── config.yaml
│   └── env_handler.py
│
├── reports/
│
└── pytest.ini

```

---

## ⚙️ Setup Instructions

### 🔹 1. Clone the Repository
```bash
git clone https://github.com/your-org/datom-api-tests.git
cd datom-api-tests
```

### 🔹 2. Create & Activate Virtual Environment
```bash
python -m venv venv
venv\Scripts\activate   # On Windows
# or
source venv/bin/activate  # On macOS/Linux
```

### 🔹 3. Install Dependencies
```bash
pip install -r requirements.txt
```

---

## 🧪 Running Tests

### ✅ Run All Tests with Allure Results
```bash
pytest --alluredir=reports/allure-results
```

### 📊 Generate Allure HTML Report
```bash
allure generate reports/allure-results -o reports/allure-report --clean
allure open reports/allure-report
```

> If `allure` command not found, [download Allure CLI](https://docs.qameta.io/allure/#_installing_a_commandline) and add it to your system path.

---

## 🛠 Configuration

Update `config/config.yaml` with your environment-specific details:
```yaml
base_url: "https://api.example.com"
auth_token: "Bearer your_token_here"
```

---

## 📋 Logging

All logs are saved in the `logs/api_test.log` file. You can configure the logger in `utils/logger.py` or `logs/logger.py`.

---

## 📌 Best Practices

- Group APIs by feature in the `tests/` folder
- Keep utility and validation functions in `utils/`
- Log every request and response
- Use `conftest.py` to manage fixtures and configs

---

## 🧼 Cleaning Up

To remove old report data:
```bash
rm -rf reports/allure-results/*
rm -rf reports/allure-report/*
```

---

## 🙋 Support

For any issues or suggestions, feel free to raise an issue or contact the QA team.
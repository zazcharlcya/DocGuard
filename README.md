<div align="center">

[![RU](https://img.shields.io/badge/🇷🇺-Русский-dc3545?style=for-the-badge)](#-русский)&nbsp;&nbsp;[![EN](https://img.shields.io/badge/🇬🇧-English-0d6efd?style=for-the-badge)](#-english)

<br/>

<img src="https://img.shields.io/badge/🛡_DocGuard-DLP%20System-0d0d0d?style=for-the-badge&labelColor=0d0d0d&color=6f42c1" alt="DocGuard" height="40"/>

<br/><br/>

[![Telegram](https://img.shields.io/badge/Telegram-%40skreamdead-0d0d0d?style=for-the-badge&logo=telegram&logoColor=26A5E4&labelColor=0d0d0d)](https://t.me/skreamdead)
[![GitHub](https://img.shields.io/badge/GitHub-zazcharlcya-0d0d0d?style=for-the-badge&logo=github&logoColor=white&labelColor=0d0d0d)](https://github.com/zazcharlcya)

<br/>

[![Python](https://img.shields.io/badge/Python-3.10+-0d0d0d?style=for-the-badge&logo=python&logoColor=3776AB&labelColor=0d0d0d)](https://python.org)
[![Flask](https://img.shields.io/badge/Flask-3.1-0d0d0d?style=for-the-badge&logo=flask&logoColor=white&labelColor=0d0d0d)](https://flask.palletsprojects.com)
[![Bootstrap](https://img.shields.io/badge/Bootstrap-5-0d0d0d?style=for-the-badge&logo=bootstrap&logoColor=7952B3&labelColor=0d0d0d)](https://getbootstrap.com)
[![SQLite](https://img.shields.io/badge/SQLite-3-0d0d0d?style=for-the-badge&logo=sqlite&logoColor=44a8d8&labelColor=0d0d0d)](https://sqlite.org)
[![License](https://img.shields.io/badge/License-CC%20BY--NC%204.0-0d0d0d?style=for-the-badge&logo=creativecommons&logoColor=EF9421&labelColor=0d0d0d)](https://creativecommons.org/licenses/by-nc/4.0/)

</div>

---

## 🇷🇺 Русский

### О проекте

**DocGuard** — веб-система класса DLP (Data Loss Prevention) для автоматического анализа документов на наличие конфиденциальной информации. Система обрабатывает файлы форматов `.txt`, `.docx` и `.pdf`, извлекает чувствительные данные и классифицирует документы с помощью набора правил и байесовского классификатора.



---

### ✨ Возможности

- 📧 **Email-детектор** — находит все адреса электронной почты в документе
- 📞 **Детектор телефонов** — распознаёт российские номера в форматах `+7` и `8` (с пробелами, скобками, дефисами)
- 💳 **Детектор банковских карт** — находит номера карт с валидацией по **алгоритму Луна** (отсеивает случайные числа)
- 🔑 **Детектор ключевых слов** — ищет маркеры секретности: `пароль`, `логин`, `password`, `секретно`, `конфиденциально` и др.
- 🤖 **Байесовский классификатор** — ML-классификация документов по обучающей выборке
- 📊 **Дашборд** — статистика проверок в реальном времени
- 🕓 **История проверок** — журнал всех сканирований с детальным просмотром
- 📥 **Отчёты** — скачать текстовый отчёт по любой проверке
- 📁 **Мультиформатность** — поддержка `.txt`, `.docx`, `.pdf`

---

### 🛠 Технологии

| Компонент | Технология |
|-----------|-----------|
| Backend | Python 3.10+, Flask 3.1 |
| База данных | SQLite + SQLAlchemy ORM |
| Миграции | Flask-Migrate (Alembic) |
| Frontend | Bootstrap 5, Bootstrap Icons |
| ML | Наивный байесовский классификатор (TF-IDF) |
| PDF | pdfplumber |
| DOCX | python-docx |
| Тесты | unittest |

---

### 🏗 Архитектура

```
docguard/
├── app.py                        # Flask-приложение, роуты
├── models.py                     # ORM-модели (Document, ScanResult)
├── scanner/
│   ├── base/                     # Абстрактные классы
│   ├── context/                  # AnalysisContext — контекст анализа
│   ├── pipeline/                 # ScannerPipeline — конвейер сканеров
│   ├── scanners/
│   │   ├── email_scanner.py      # Детектор email-адресов
│   │   ├── phone_scanner.py      # Детектор телефонных номеров
│   │   ├── card_scanner.py       # Детектор карт + алгоритм Луна
│   │   └── keyword_scanner.py    # Детектор ключевых слов
│   ├── results/                  # Датаклассы результатов
│   └── services/
│       └── file_scanner.py       # Чтение TXT / DOCX / PDF
├── classifier/
│   └── naive_bayes_classifier.py # Байесовский классификатор
├── templates/                    # Jinja2 шаблоны
├── tests/                        # Unit-тесты
├── migrations/                   # Alembic-миграции БД
└── requirements.txt
```

---

### 🚀 Установка и запуск

#### 1. Клонировать репозиторий

```bash
git clone https://github.com/zazcharlcya/DocGuard.git
cd DocGuard
```

#### 2. Создать виртуальное окружение

```bash
python -m venv venv

# Windows
venv\Scripts\activate

# Linux / macOS
source venv/bin/activate
```

#### 3. Установить зависимости

```bash
pip install -r requirements.txt
```

#### 4. Запустить

```bash
python app.py
```

Открыть в браузере: **http://127.0.0.1:5000**

> База данных и папка `uploads/` создаются автоматически при первом запуске.

---

### 🧪 Тесты

```bash
python -m unittest discover tests -v
```

---

### 💡 Как работает классификация

1. Файл загружается, текст извлекается (TXT / DOCX / PDF)
2. Конвейер сканеров проверяет текст на email, телефоны, карты и ключевые слова
3. Если что-то найдено → документ **конфиденциальный** (правила)
4. Если ничего не найдено → запускается байесовский классификатор по обучающей выборке
5. Результат сохраняется в БД и отображается в истории

---

<div align="center">

**[⬆ Наверх](#)**

[![Telegram](https://img.shields.io/badge/Telegram-@skreamdead-2CA5E0?style=flat-square&logo=telegram&logoColor=white)](https://t.me/skreamdead)
[![GitHub](https://img.shields.io/badge/GitHub-zazcharlcya-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/zazcharlcya)

</div>

---

## 🇬🇧 English

### About

**DocGuard** is a web-based DLP (Data Loss Prevention) system for automated sensitive data detection in documents. It processes `.txt`, `.docx`, and `.pdf` files, extracts confidential information using a scanner pipeline, and classifies documents with rule-based detection and a Naïve Bayes classifier.

Built as part of an industrial internship project.

---

### ✨ Features

- 📧 **Email detector** — finds all email addresses in the document
- 📞 **Phone detector** — recognizes Russian phone numbers in `+7` and `8` formats (with spaces, parentheses, dashes)
- 💳 **Bank card detector** — finds card numbers validated by the **Luhn algorithm** (filters out random digit sequences)
- 🔑 **Keyword detector** — looks for secrecy markers: `password`, `login`, `secret`, `confidential` and others
- 🤖 **Naïve Bayes classifier** — ML-based document classification using a training dataset
- 📊 **Dashboard** — real-time scan statistics
- 🕓 **Scan history** — full log of all scans with detailed view
- 📥 **Reports** — download a text report for any scan result
- 📁 **Multi-format** — supports `.txt`, `.docx`, `.pdf`

---

### 🛠 Tech Stack

| Component | Technology |
|-----------|-----------|
| Backend | Python 3.10+, Flask 3.1 |
| Database | SQLite + SQLAlchemy ORM |
| Migrations | Flask-Migrate (Alembic) |
| Frontend | Bootstrap 5, Bootstrap Icons |
| ML | Naïve Bayes classifier (TF-IDF) |
| PDF parsing | pdfplumber |
| DOCX parsing | python-docx |
| Testing | unittest |

---

### 🏗 Architecture

```
docguard/
├── app.py                        # Flask app, routes
├── models.py                     # ORM models (Document, ScanResult)
├── scanner/
│   ├── base/                     # Abstract base classes
│   ├── context/                  # AnalysisContext
│   ├── pipeline/                 # ScannerPipeline
│   ├── scanners/
│   │   ├── email_scanner.py      # Email detector
│   │   ├── phone_scanner.py      # Phone number detector
│   │   ├── card_scanner.py       # Card detector + Luhn algorithm
│   │   └── keyword_scanner.py    # Keyword detector
│   ├── results/                  # Result dataclasses
│   └── services/
│       └── file_scanner.py       # TXT / DOCX / PDF reader
├── classifier/
│   └── naive_bayes_classifier.py # Naïve Bayes classifier
├── templates/                    # Jinja2 templates
├── tests/                        # Unit tests
├── migrations/                   # Alembic DB migrations
└── requirements.txt
```

---

### 🚀 Installation & Setup

#### 1. Clone the repository

```bash
git clone https://github.com/zazcharlcya/DocGuard.git
cd DocGuard
```

#### 2. Create a virtual environment

```bash
python -m venv venv

# Windows
venv\Scripts\activate

# Linux / macOS
source venv/bin/activate
```

#### 3. Install dependencies

```bash
pip install -r requirements.txt
```

#### 4. Run

```bash
python app.py
```

Open in browser: **http://127.0.0.1:5000**

> The database and `uploads/` folder are created automatically on first run.

---

### 🧪 Running Tests

```bash
python -m unittest discover tests -v
```

---

### 💡 How Classification Works

1. File is uploaded and text is extracted (TXT / DOCX / PDF)
2. The scanner pipeline checks the text for emails, phones, card numbers, and keywords
3. If anything is found → document is marked **CONFIDENTIAL** (rule-based)
4. If nothing is found → the Naïve Bayes classifier runs on the training dataset
5. Result is saved to the database and shown in scan history

---

<div align="center">

**[⬆ Back to top](#)**

[![Telegram](https://img.shields.io/badge/Telegram-@skreamdead-2CA5E0?style=flat-square&logo=telegram&logoColor=white)](https://t.me/skreamdead)
[![GitHub](https://img.shields.io/badge/GitHub-zazcharlcya-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/zazcharlcya)

</div>

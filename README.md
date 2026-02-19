# 💰 Expense Tracker

[![Python 3.8+](https://img.shields.io/badge/python-3.8%2B-blue)](https://www.python.org/downloads/)
[![Streamlit](https://img.shields.io/badge/streamlit-latest-FF4B4B?logo=streamlit)](https://streamlit.io)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Build Status](https://img.shields.io/badge/build-passing-brightgreen)](https://github.com/chaturvedikhyati/Expense_Tracker)
[![GitHub Stars](https://img.shields.io/github/stars/chaturvedikhyati/Expense_Tracker?style=flat)](https://github.com/chaturvedikhyati/Expense_Tracker)

A lightweight, modular expense management application built with Streamlit. Track, analyze, and visualize your spending patterns with a clean, intuitive interface.

---

## 🚀 Highlights

- **Modular Architecture** — Clean separation of concerns with dedicated modules for business logic, storage, and analytics
- **Separation of Concerns** — UI layer, business logic, storage, and visualization are independently managed
- **Testable Business Logic** — Core expense management functions are decoupled and thoroughly testable
- **Lightweight & Extensible** — Minimal dependencies, easy to customize and extend with new features
- **Analytics-Driven Insights** — Built-in spending analysis, category breakdowns, and trend visualization
- **CSV-Based Storage** — Simple, portable data persistence without database overhead

---

## 📋 Overview

Expense Tracker simplifies personal finance management by providing:

- **Quick Expense Logging** — Add expenses on-the-fly with category tagging
- **Spending Analysis** — Visualize spending patterns by category, date range, and trends
- **Data Persistence** — Automatic CSV-based storage for reliable data retention
- **Interactive Dashboards** — Real-time charts and statistics powered by Streamlit

The application is designed for individuals who want to understand their spending habits without complexity.

---

## 🏗 Architecture Flow

```
┌─────────────────────────────────────────┐
│         User (Browser UI)               │
└──────────────┬──────────────────────────┘
               │
               ▼
┌─────────────────────────────────────────┐
│   Streamlit UI Layer (app.py)           │
│   - Form inputs                         │
│   - Navigation                          │
│   - Display management                  │
└──────────────┬──────────────────────────┘
               │
               ▼
┌─────────────────────────────────────────┐
│   Business Logic (expense_manager.py)   │
│   - Add/edit/delete expenses            │
│   - Category management                 │
│   - Data validation                     │
└──────────────┬──────────────────────────┘
               │
               ▼
┌─────────────────────────────────────────┐
│   Storage Layer (storage.py)            │
│   - CSV read/write operations           │
│   - Data serialization                  │
└──────────────┬──────────────────────────┘
               │
               ▼
┌─────────────────────────────────────────┐
│   CSV Data File (expenses.csv)          │
└──────────────┬──────────────────────────┘
               │
               ▼
┌─────────────────────────────────────────┐
│   Analysis Layer (analysis.py)          │
│   - Aggregations & calculations         │
│   - Statistics generation               │
│   - Trend computation                   │
└──────────────┬──────────────────────────┘
               │
               ▼
┌─────────────────────────────────────────┐
│   Visualization Layer (visualization.py)│
│   - Chart generation                    │
│   - UI component rendering              │
└──────────────┬──────────────────────────┘
               │
               ▼
┌─────────────────────────────────────────┐
│   Rendered Dashboard in Streamlit       │
└─────────────────────────────────────────┘
```

---

## 🛠 Tech Stack

### Frontend
- **Streamlit** — Interactive web UI framework
- **Plotly/Altair** — Data visualization & charting

### Backend & Logic
- **Python 3.8+** — Core application language
- **Pandas** — Data manipulation & analysis

### Storage
- **CSV** — Lightweight, portable data format

### Tools & DevOps
- **Git/GitHub** — Version control
- **Pytest** — Testing framework
- **Streamlit Cloud / Render / Railway / Docker** — Deployment platforms

---

## 📦 Installation

### Prerequisites
- Python 3.8 or higher
- pip package manager

### Step 1: Clone the Repository

```bash
git clone https://github.com/chaturvedikhyati/Expense_Tracker.git
cd Expense_Tracker
```

### Step 2: Create a Virtual Environment

```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

### Step 3: Install Dependencies

```bash
pip install -r requirements.txt
```

### Step 4: Run the Application

```bash
streamlit run app.py
```

The application will open in your browser at `http://localhost:8501`

---

## 📁 Folder Structure

```
Expense_Tracker/
├── app.py                  # Streamlit UI entry point
├── main.py                 # Alternative entry point / utilities
├── requirements.txt        # Python dependencies
├── README.md               # Project documentation
├── .gitignore              # Git ignore rules
│
├── src/                    # Source modules
│   ├── expense_manager.py  # Core business logic
│   ├── storage.py          # CSV storage operations
│   ├── analysis.py         # Data analysis functions
│   └── visualization.py    # Chart & UI components
│
└── tests/                  # Unit and integration tests
    ├── test_expense_manager.py
    ├── test_storage.py
    └── test_analysis.py
```

---

## 🧪 Testing

The project includes unit tests for core business logic, storage operations, and analysis functions.

### Run Tests

```bash
pytest
```

### Test Coverage

Tests verify:
- Expense creation, update, and deletion
- CSV persistence and data integrity
- Analytics calculations and aggregations
- Edge cases and error handling

---

## 🌍 Deployment

### Streamlit Cloud (Recommended)

1. Push your repository to GitHub
2. Visit [Streamlit Cloud](https://streamlit.io/cloud)
3. Click **"New app"** and connect your GitHub repo
4. Select the branch and `app.py` as the main file
5. Click **Deploy**

### Alternative Platforms

- **Render** — Free tier available, supports Python apps
- **Railway** — Simple deployment with auto-scaling
- **Docker** — Containerize with a custom Dockerfile for flexibility

---

## 📊 Usage

### Adding an Expense

1. Open the app in your browser
2. Navigate to **"Add Expense"**
3. Enter amount, category, date, and description
4. Click **Save**

### Viewing Analytics

1. Go to **"Analytics"** section
2. View spending by category, time period, or trends
3. Download reports as needed

### Managing Expenses

1. Open **"Manage Expenses"**
2. Edit or delete existing entries
3. Search by category or date range

---

## 🗺 Roadmap

- [ ] Multi-user support with authentication
- [ ] Budget limits and alerts
- [ ] Recurring expense templates
- [ ] Export reports (PDF, Excel)
- [ ] Mobile-responsive design
- [ ] Data encryption for sensitive information
- [ ] Integration with banking APIs
- [ ] Advanced forecasting and recommendations

---

## 🤝 Contributing

Contributions are welcome! Please follow these guidelines:

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/your-feature`)
3. Commit your changes (`git commit -m "Add your feature"`)
4. Push to the branch (`git push origin feature/your-feature`)
5. Open a Pull Request with a clear description

Please ensure:
- Code follows PEP 8 style guidelines
- Tests pass before submitting
- Documentation is updated as needed

---

## 📄 License

This project is licensed under the **MIT License** — see the [LICENSE](LICENSE) file for details.

You are free to use, modify, and distribute this project for personal or commercial purposes.

---

## 🚧 Project Status

**Actively Maintained** — This project is under active development. Bug reports and feature requests are encouraged.

---

## 👤 Author

**Khyati Chaturvedi**

- GitHub: [@chaturvedikhyati](https://github.com/chaturvedikhyati)
- Repository: [Expense Tracker](https://github.com/chaturvedikhyati/Expense_Tracker)

---

## 💬 Feedback & Support

Found a bug or have a suggestion? Please open an [issue](https://github.com/chaturvedikhyati/Expense_Tracker/issues) on GitHub.

For questions or discussions, feel free to start a [discussion](https://github.com/chaturvedikhyati/Expense_Tracker/discussions).

---

**Made with ❤️ for better financial awareness**

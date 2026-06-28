# 🌍 AtmosIQ

**Real-Time Air Quality Intelligence Powered by AI**

AtmosIQ is an intelligent air quality dashboard built with Python and Streamlit that helps users understand current environmental conditions through live AirNow data, interactive visualizations, and an AI-powered assistant.

Instead of simply displaying an Air Quality Index (AQI), AtmosIQ transforms environmental data into actionable insights that help people make informed decisions about outdoor activities, health, and daily planning.

---

## 🚀 Features

### 🌎 Live Air Quality Monitoring

* Retrieve real-time AQI data using the AirNow API
* Search by any valid U.S. ZIP code
* Display the official AirNow reporting area
* Automatically detect the local time for the selected location

### 📊 Interactive Dashboard

* Dynamic AQI Hero Card
* AQI Risk Gauge
* AQI Risk Levels Guide
* Current pollutant information
* Air quality category display
* Reporting station location
* Local time display

### 🤖 AtmosIQ AI Assistant

Ask natural language questions like:

* Is it safe to run outside today?
* Should I wear a mask?
* Can my kids play outside?
* Is today good for hiking?
* What is AQI?
* What is PM2.5?
* Who is AtmosIQ?

AtmosIQ provides personalized recommendations based on the user's current air quality conditions.

### 💡 Quick Questions

Interactive buttons allow users to instantly ask common air quality questions without typing.

### 🔄 Reset Dashboard

Reset the application to perform a new air quality search without refreshing the page.

---

# 🛠 Technologies Used

* Python
* Streamlit
* Plotly
* AirNow API
* HTML/CSS
* Session State Management

---

# 📁 Project Structure

```
AtmosIQ/

├── api/
│   └── airnow.py
│
├── services/
│   ├── chatbot.py
│   ├── recommendation.py
│   ├── timezone_service.py
│   └── location.py
│
├── ui/
│   ├── dashboard.py
│   ├── charts.py
│   ├── cards.py
│   ├── sidebar.py
│   └── styles.py
│
├── utils/
│   └── formatting.py
│
├── app.py
├── config.py
├── requirements.txt
└── README.md
```

---

# 📦 Installation

Clone the repository:

```bash
git clone https://github.com/YOUR_USERNAME/AtmosIQ.git
```

Navigate into the project:

```bash
cd AtmosIQ
```

Create a virtual environment:

```bash
python -m venv venv
```

Activate the virtual environment:

### Windows

```bash
venv\Scripts\activate
```

### macOS/Linux

```bash
source venv/bin/activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Run the application:

```bash
streamlit run app.py
```

---

# 🌤 Example Workflow

1. Enter a U.S. ZIP code.
2. Retrieve live air quality data.
3. Review the AQI dashboard.
4. Explore the AQI Risk Gauge.
5. Understand today's AQI category.
6. Ask AtmosIQ questions about today's conditions.
7. Receive personalized recommendations.

---

# 🎯 Project Goals

AtmosIQ was designed to make environmental data easier to understand by combining:

* Real-time air quality monitoring
* Data visualization
* Artificial intelligence
* User-centered interface design

The objective is to help users make healthier, data-informed decisions based on current environmental conditions.

---

# 🚧 Future Improvements

* Historical AQI trends
* Air quality forecasting
* Weather integration
* Interactive AQI maps
* User profiles
* Favorite locations
* Mobile optimization
* Push notifications
* AI conversation memory
* Health recommendations based on user preferences

---

# 📄 License

This project is intended for educational and portfolio purposes.

---

## 👨‍💻 Developer

Built by **Drequan Walker and Amina Jobarteh**

Passionate about building AI-powered software that transforms complex data into meaningful, everyday insights.

import streamlit as st
import mysql.connector
from datetime import datetime, timedelta
import requests

# Připojení k MySQL databázi
mydb = mysql.connector.connect(
  host="localhost",
  user="yourusername",
  password="yourpassword",
  database="yourdatabase"
)
mycursor = mydb.cursor()

# Funkce pro získání statistik z MySQL databáze
def get_statistics(period: str) -> dict:
    periods = {'h': 'hour', 'd': 'day', 'w': 'week', 'm': 'month'}
    if period.lower() not in periods:
        st.error("Invalid period. Use 'h' for hour, 'd' for day, 'w' for week, 'm' for month.")
        return {}
    
    if period.lower() == 'h':
        time_window_start = datetime.now() - timedelta(hours=1)
        time_window_end = datetime.now()
    elif period.lower() == 'd':
        time_window_start = datetime.now() - timedelta(days=1)
        time_window_end = datetime.now()
    elif period.lower() == 'w':
        time_window_start = datetime.now() - timedelta(weeks=1)
        time_window_end = datetime.now()
    elif period.lower() == 'm':
        time_window_start = datetime.now() - timedelta(days=30)
        time_window_end = datetime.now()

    sql = f"SELECT COUNT(*) FROM urls WHERE scan_date BETWEEN '{time_window_start}' AND '{time_window_end}';"
    mycursor.execute(sql)
    total_scans = mycursor.fetchone()[0]

    sql = f"SELECT COUNT(*) FROM urls WHERE scan_date BETWEEN '{time_window_start}' AND '{time_window_end}' AND positives > 0;"
    mycursor.execute(sql)
    total_positives = mycursor.fetchone()[0]

    return {'total_scans': total_scans, 'total_positives': total_positives}

# Funkce pro analýzu URL pomocí VirusTotal API
def analyze_url_vt(url: str) -> dict:
    api_key = "4306e6a729417cbccf06ca445316d2179c6ece234a3f7ec486e70f506ac0429e"
    vt_url = f"https://www.virustotal.com/api/v3/urls"
    headers = {"x-apikey": api_key}
    data = {"url": url}
    response = requests.post(vt_url, headers=headers, json=data)
    if response.status_code == 200:
        return response.json()
    else:
        st.error("Error analyzing URL with VirusTotal API")
        return {}

def main():
    st.title("URL Analyzer")
    st.header("Analyze URL")
    url_input = st.text_input("Enter URL:")
    if st.button("Analyze"):
        vt_response = analyze_url_vt(url_input)
        scan_id = vt_response["data"]["id"]
        vt_url = f"https://www.virustotal.com/api/v3/analyses/{scan_id}"
        headers = {"x-apikey": "your_virustotal_api_key"}
        response = requests.get(vt_url, headers=headers)
        if response.status_code == 200:
            vt_analysis = response.json()
            positives = vt_analysis["data"]["attributes"]["stats"]["malicious"]
            sql = "INSERT INTO urls (url, scan_date, positives) VALUES (%s, %s, %s)"
            val = (url_input, datetime.now(), positives)
            mycursor.execute(sql, val)
            mydb.commit()
            st.write({"url": url_input, "analysis": vt_analysis})
        else:
            st.error("Error analyzing URL with VirusTotal API")

    st.header("Statistics")
    period_input = st.selectbox("Select period:", ['h', 'd', 'w', 'm'])
    if st.button("Get Statistics"):
        stats = get_statistics(period_input)
        st.write(stats)

if __name__ == "__main__":
    main()
# LiveLogic Auto-Wake Automation

This directory contains a Selenium-based automation script designed to keep the **LiveLogic** virtual interview platform running continuously on Streamlit Community Cloud. 

Because Streamlit automatically puts apps to sleep after a period of inactivity, this GitHub Actions workflow prevents downtime by periodically simulating a user visit, checking the page state, and clicking the "Yes, get this app back up!" button if the platform has gone idle.

## 📂 Repository Structure

* `wake_app.py`: The core Python script that initializes a headless Chrome browser, navigates to the LiveLogic URL, and interacts with the DOM to wake the app.
* `.github/workflows/wake.yml`: The GitHub Actions configuration file that schedules the script to run automatically every 4 hours.
* `requirements.txt`: Contains the necessary Python dependencies (`selenium` and `webdriver-manager`).

## 🚀 How It Works

1. **Scheduled Trigger:** GitHub Actions triggers the `wake.yml` workflow every 4 hours using a cron job (`0 */4 * * *`).
2. **Environment Setup:** The workflow spins up an Ubuntu runner, installs Python 3.10, and installs the dependencies from `requirements.txt`.
3. **Execution:** The `wake_app.py` script runs in a headless environment. 
4. **Interaction:** If the Streamlit sleeping screen is detected, Selenium locates the wake-up button via XPath and clicks it. If the app is already awake, the script simply times out safely and closes the browser.

## ⚙️ Setup & Customization

If you are forking or adapting this code, ensure you update the target URL in `wake_app.py`:

```python
# Replace with your actual Streamlit app URL
APP_URL = "[https://livelogic.streamlit.app/](https://livelogic.streamlit.app/)"
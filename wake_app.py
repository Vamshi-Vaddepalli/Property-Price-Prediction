"""
Visits a Streamlit Community Cloud app with a real (headless) browser.
If the app is asleep, it detects the wake-up button and clicks it,
then waits for the app to finish loading.
"""
from playwright.sync_api import sync_playwright

APP_URL = "https://property-price-prediction-gurgaon.streamlit.app/"
WAKE_BUTTON_TEXT = "Yes, get this app back up!"

def main():
    with sync_playwright() as p:
        browser = p.chromium.launch()
        page = browser.new_page()
        print(f"Visiting {APP_URL} ...")
        page.goto(APP_URL, timeout=60000)

        # Give the page a moment to render the sleep screen, if present
        page.wait_for_timeout(3000)

        try:
            wake_button = page.get_by_text(WAKE_BUTTON_TEXT, exact=False)
            if wake_button.count() > 0:
                print("App is asleep — clicking wake-up button...")
                wake_button.first.click()
                # Streamlit apps can take a minute or two to spin back up
                page.wait_for_timeout(60000)
                print("Wake-up triggered and waited for app to spin up.")
            else:
                print("App was already awake — no action needed.")
        except Exception as e:
            print(f"Could not find/click wake button (app likely already awake): {e}")

        browser.close()

if __name__ == "__main__":
    main()

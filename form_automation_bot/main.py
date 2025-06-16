from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
import time


def check_x_account_exists(login_input: str) -> dict:
    result = {"input": login_input, "exists": None, "profile_url": None, "error": None}

    chrome_options = Options()

    chrome_options.add_argument("--headless")  
    chrome_options.add_argument("--disable-blink-features=AutomationControlled")
    chrome_options.add_experimental_option("excludeSwitches", ["enable-automation"])
    chrome_options.add_experimental_option('useAutomationExtension', False)

    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)

    try:
        driver.get("https://twitter.com/login")
        wait = WebDriverWait(driver, 20)


        user_input = wait.until(EC.presence_of_element_located((By.NAME, "text")))
        user_input.send_keys(login_input)
        user_input.send_keys(Keys.RETURN)
        time.sleep(3)

        page_source = driver.page_source.lower()


        if "couldn’t find your account" in page_source or "не вдалося знайти ваш обліковий запис" in page_source:
            result["exists"] = False
            return result


        suspicious_texts = [
            "unusual login attempts", "confirm your identity",
            "незвичні спроби входу", "підтвердьте свою особу",
            "введіть ваш номер телефону", "we’ve detected unusual"
        ]
        if any(txt in page_source for txt in suspicious_texts):
            result["exists"] = True
            result["error"] = "Twitter вимагає підтвердження через підозрілу активність"
            return result


        try:
            wait.until(EC.presence_of_element_located((By.NAME, "password")))
            result["exists"] = True
            if "@" not in login_input and not login_input.startswith("+"):
                result["profile_url"] = f"https://twitter.com/{login_input}"
            return result
        except:
            pass

        if "something went wrong" in page_source or "щось пішло не так" in page_source:
            result["error"] = "Twitter тимчасово недоступний або блокує запит"
            return result

        result["error"] = "Невизначена ситуація. Можливо, Twitter блокує запити."
        return result

    except Exception as e:
        result["error"] = f"Помилка: {str(e)}"
        return result
    finally:
        driver.quit()


if __name__ == "__main__":
    login_input = input("Введіть email, телефон або username: ").strip()
    result = check_x_account_exists(login_input)

    print("\n--- Результат ---")

    if result["exists"] is True:
        print("✅ Акаунт існує")
        if result["profile_url"]:
            print(f"🔗 Посилання: {result['profile_url']}")
        if result["error"]:
            print(f"⚠️ Увага: {result['error']}")

    elif result["exists"] is False:
        print("❌ Акаунт не знайдено")

    else:
        if result["error"] == "Невизначена ситуація. Можливо, Twitter блокує запити.":
            print("❌ Акаунт не знайдено")
        else:
            print(f"⚠️ Помилка: {result['error']}")

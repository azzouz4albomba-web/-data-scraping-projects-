from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# إعداد متصفح Chrome
options = webdriver.ChromeOptions()
options.add_argument("--headless") # تشغيل المتصفح في الخلفية
driver = webdriver.Chrome(options=options)

url = 'https://www.365scores.com/ar'
driver.get(url)

try:
    # الانتظار حتى تظهر عناصر المباريات (تغيير الـ Selector حسب هيكل الصفحة)
    # نستخدم WebDriverWait للتعامل مع تحميل البيانات الديناميكي
    wait = WebDriverWait(driver, 15)
    matches = wait.until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, 'div.match-card')))

    for match in matches[:5]: # استخراج أول 5 مباريات كمثال
        print(match.text)
        print("-" * 20)

except Exception as e:
    print(f"Error: {e}")

finally:
    driver.quit()

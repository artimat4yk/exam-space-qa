from selenium.webdriver.common.by import By          
from selenium.webdriver.common.keys import Keys
from pages.base_page import BasePage

class MainPage(BasePage):
    """Главная страница консоли Outerspace."""

    # Локаторы — "адреса" элементов на странице
    CONSOLE_CONTAINER = (By.CSS_SELECTOR, "[data-test-id='console-container']")
    OUTPUT_AREA = (By.CSS_SELECTOR, "[data-test-id='console-output']")
    COMMAND_INPUT = (By.CSS_SELECTOR, "[data-test-id='command-input']")
    PROMPT_SYMBOL = (By.CSS_SELECTOR, "[data-test-id='prompt-symbol']")
    CONSOLE_TITLE = (By.CSS_SELECTOR, "[data-test-id='console-title']")

    def __init__(self, driver):
        super().__init__(driver)  # Вызываем конструктор родительского класса BasePage
        self.url = "https://exam.space-qa.site/" 

    def open_main_page(self):
        """Открыть главную страницу."""
        self.open(self.url)

    def send_command(self, command):
        """Ввести команду в поле ввода и отправить её (нажатием Enter)."""
        input_element = self.find_element(self.COMMAND_INPUT)
        input_element.clear()
        input_element.send_keys(command)
        input_element.send_keys(Keys.RETURN)

    def get_output_text(self):
        """Получить весь текст из области вывода."""
        return self.get_text(self.OUTPUT_AREA)

    def wait_for_output_contains(self, text, timeout=10):
        """Ожидать, пока в выводе появится заданный текст."""
        return self.wait.until(
            lambda driver: text in self.get_text(self.OUTPUT_AREA)
        )
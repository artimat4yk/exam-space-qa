import pytest
from pages.main_page import MainPage

class TestConsole:

    def test_console_title(self, driver):
        """Проверяем, что заголовок консоли соответствует ожидаемому."""
        main_page = MainPage(driver)
        main_page.open_main_page()
        title = main_page.get_text(main_page.CONSOLE_TITLE)
        assert "Outerspace Command Line Interface" in title, \
            f"Заголовок '{title}' не соответствует ожидаемому"

    def test_help_command(self, driver):
        """Проверяем, что команда help выводит список доступных команд."""
        main_page = MainPage(driver)
        main_page.open_main_page()
        main_page.send_command("help")
        assert main_page.wait_for_output_contains("BEHOLD! The sacred commandments"), \
            "Команда help не вывела ожидаемый текст"

    def test_unknown_command(self, driver):
        """Проверяем, что неизвестная команда выдает сообщение об ошибке."""
        main_page = MainPage(driver)
        main_page.open_main_page()
        main_page.send_command("unknown_command_123")
        assert main_page.wait_for_output_contains("Unknown command"), \
            "Неизвестная команда не вывела сообщение об ошибке"
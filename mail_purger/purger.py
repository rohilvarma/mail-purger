import imaplib
from printStatus import printStatus


class Purger:
    def __init__(self) -> None:
        self.__imap_host = "imap.gmail.com"
        self.__imap_user = "rohilvarma96@gmail.com"
        self._is_logged_in = False

    def __update_login_status(self) -> None:
        self._is_logged_in = not self._is_logged_in

    def _select_folder(self, folder_name: str) -> None:
        self.__imap.select(folder_name)
        printStatus.done("{} folder selected".format(folder_name))

    def _open_connection(self) -> None:
        try:
            self.__imap = imaplib.IMAP4_SSL(self.__imap_host)
            printStatus.running("Logging in")
            self.__imap.login(self.__imap_user, self.__imap_pass)
            self.__update_login_status()
            printStatus.updateDone("Login Successful", True)
        except Exception:
            printStatus.updateFailed("Login Failed!")

    def __del__(self) -> None:
        if self._is_logged_in:
            self.__imap.logout()
            self.__update_login_status()
            printStatus.done("Logged Out Successfully.")

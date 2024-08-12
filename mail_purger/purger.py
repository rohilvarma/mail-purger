import imaplib  # noqa: D100
from os import environ

from dotenv import load_dotenv
from printStatus import printStatus


class Purger:
    """Represents a mail purger.

    This class is responsible for establishing a connection to the mail server,
    selecting the folder to purge, and logging out of the mail server.

    Attributes
    ----------
        __imap_host (str): The IMAP host.
        __imap_user (str): The IMAP user.
        __imap_pass (str): The IMAP password.
        is_logged_in (bool): The login status.

    Methods
    -------
        open_connection(): Establish a secure connection to the IMAP server using SSL.
        select_folder(folder_name): Determine a folder on the IMAP server.
        __del__(): Log out of the IMAP server and update the login status.

    """

    def __init__(self) -> None:
        """Initialize a Purger object.

        Initialize the IMAP host, user, and password, and set the login status to False.

        :return: None
        :rtype: None
        """
        load_dotenv(override=True)
        self.__imap_host = "imap.gmail.com"
        self.__imap_user = "rohilvarma96@gmail.com"
        self.__imap_pass = environ.get("APP_KEY")
        self.is_logged_in = False

    def __update_login_status(self) -> None:
        self.is_logged_in = not self.is_logged_in

    def select_folder(self, folder_name: str) -> None:
        """Determine a folder on the IMAP server.

        :param folder_name: The name of the folder to select.
        :type folder_name: str
        :return: None
        :rtype: None
        """
        self.__imap.select(folder_name)
        printStatus.done(f"'{folder_name}' folder selected")

    def open_connection(self) -> None:
        """Establish a secure connection to the IMAP server using SSL.

        :return: None
        :rtype: None
        """
        try:
            self.__imap = imaplib.IMAP4_SSL(self.__imap_host)
            printStatus.running("Logging in")
            self.__imap.login(self.__imap_user, self.__imap_pass)
            self.__update_login_status()
            printStatus.updateDone("Login Successful", progressbar=True)
        except imaplib.IMAP4.error:
            printStatus.updateFailed("Login Failed!")

    def __del__(self) -> None:
        """Log out of the IMAP server and update the login status once the application encounters some error or application reaches end of state.

        :return: None
        :rtype: None
        """
        if self.is_logged_in:
            self.__imap.logout()
            self.__update_login_status()
            printStatus.done("Logged Out Successfully.")

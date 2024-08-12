"""Mail Purger.

This is the entry point module for the Mail Purger application.

This module is responsible for initializing the Mail Purger application,
establishing a connection to the mail server, and selecting the folder to
purge based on the provided command-line argument.

"""

from sys import argv

from purger import Purger


def main() -> None:
    """Entry point of the Mail Purger application.

    Initializes the mail purger, establishes a connection to the mail server,
    and selects the folder to purge based on the provided command-line argument.

    :return: None
    :rtype: None
    """
    mail_purger = Purger()
    mail_purger.open_connection()
    if mail_purger.is_logged_in:
        try:
            folder_name = argv[1]
        except IndexError:
            folder_name = "Inbox"
        mail_purger.select_folder(folder_name)


if __name__ == "__main__":
    main()

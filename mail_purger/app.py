from sys import argv
from purger import Purger

def main() -> None:
    mail_purger = Purger()
    mail_purger._open_connection()
    
    if mail_purger._is_logged_in:
        try:
            folder_name = argv[1]
        except IndexError:
            folder_name = "Inbox"
        mail_purger._select_folder(folder_name)
    

if __name__ == "__main__":
    main()
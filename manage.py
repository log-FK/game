from modules.window import main_window
from modules.app import app
def main():
    try:
        main_window.show()
        app.exec()
    except Exception as eror:
        print(eror)
if __name__ == "__main__":
    main()
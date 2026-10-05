from modules.window import window
from modules.app import app
def main():
    try:
        window.show()
        app.exec()
    except Exception as eror:
        print(eror)
if __name__ == "__main__":
    main()
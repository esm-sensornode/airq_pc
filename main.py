import ec_sense
from guizero import App, Text


# touch display_size = 800x480 px
app = App(title="AirQ v1.0 ", layout="grid", visible=True, bg="white")

text = Text(app, text="hello world")


# run as main application
if __name__ == "__main__":
    app.display()

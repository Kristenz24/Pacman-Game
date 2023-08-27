from kivy.config import Config
Config.set('graphics', 'resizable', 0)


from kivy.app import App
from kivy.uix.screenmanager import Screen
from kivy.properties import ObjectProperty
from kivy.uix.image import Image
from kivy.core.window import Window
from kivy.uix.button import Button
from kivy.clock import Clock
from kivy.core.audio import SoundLoader


Window.size = (800, 600)
Window.borderless = False

def stop_app(instances): # <---- (function na kapag cinall, mas-stop yung app)
    PacmanApp().stop()

#mga song na nakastored sa isang variable
Enter = SoundLoader.load("Enter.mp3")  # click sfx
Decisive = SoundLoader.load("DecisiveBattle.mp3")  # sound for scene one
Street = SoundLoader.load("StreetBrawlin.mp3")  # sound for scene two

Decisive.volume = 0.3
Street.volume = 0.3

Decisive.loop = True
Street.loop = True

class members(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.members_page = Image(source="members.png",
                                  pos= (self.center_x - 50, self.center_y - 20))
        self.add_widget(self.members_page)

        self.exit_button = Button(size_hint=(None, None),
                                  size=(80, 80),
                                  pos=(self.center_x + 685, self.center_y + 485),
                                  background_normal="exit_button.png")
        self.exit_button.bind(on_press=self.remove)
        self.add_widget(self.exit_button)
        Enter.play()

    def remove(self, instances):
        self.parent.remove_widget(self)
        Enter.play()

class Background(Screen):
    cloud_texture = ObjectProperty(None)
    floor_texture = ObjectProperty(None)
    vines_texture = ObjectProperty(None)
    vines2_texture = ObjectProperty(None)

    Decisive.play()

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self.exit_button = Button(size_hint=(None, None),
                                  size=(90, 90),
                                  pos=(self.center_x + 670, self.center_y + 474),
                                  background_normal="exit_button.png")
        self.exit_button.bind(on_press=stop_app)
        self.add_widget(self.exit_button)

        self.members_button = Button(size_hint=(None, None),
                                  size=(100, 90),
                                  pos=(self.center_x + 600, self.center_y + 474),
                                  background_normal="members_button.png",
                                  background_down="members_button.png")
        self.members_button.bind(on_press=self.open_members)
        self.add_widget(self.members_button)

        self.start_button = Button(
            size_hint=(None, None),
            size=(110, 110),
            pos=(self.center_x + 301.9, self.center_y + 125),
            background_normal='PacmanGame-StartButton.png')
        self.start_button.bind(on_press=self.on_button_click)
        self.add_widget(self.start_button)

        # To Create Textures
        self.cloud_texture = Image(source="PacmanGame-Cloud.png").texture
        self.cloud_texture.wrap = "repeat" #para mag repeat yung mga pics
        self.cloud_texture.uvsize = (3, -1) #yung size at spacing yung mga pics, 3

        self.floor_texture = Image(source="PacmanGame-Ground.png").texture
        self.floor_texture.wrap = "repeat"
        self.floor_texture.uvsize = (6, -1)

        self.vines_texture = Image(source="Vines.png").texture
        self.vines_texture.wrap = "repeat"
        self.vines_texture.uvsize = (6, -1)

        self.vines2_texture = Image(source="Vines2.png").texture
        self.vines2_texture.wrap = "repeat"
        self.vines2_texture.uvsize = (6, -1)

    def open_members(self, instances):
            mem = members()
            self.parent.add_widget(mem)

    def scroll_textures(self, time_passed):
        # yung speed nung pag-scroll nung mga pic sa background
        self.cloud_texture.uvpos = (
            (self.cloud_texture.uvpos[0] + time_passed / 5.0) % Window.width, self.cloud_texture.uvpos[1])
        self.floor_texture.uvpos = (
            (self.floor_texture.uvpos[0] + time_passed * 2) % Window.width, self.floor_texture.uvpos[1])
        self.vines_texture.uvpos = (
            (self.vines_texture.uvpos[0] + time_passed / 2) % Window.width, self.vines_texture.uvpos[1])
        self.vines2_texture.uvpos = (
            (self.vines2_texture.uvpos[0] + time_passed / 3) % Window.width, self.vines2_texture.uvpos[1])

        # pag execute nung upper code
        texture = self.property('cloud_texture')
        texture.dispatch(self)
        texture = self.property('floor_texture')
        texture.dispatch(self)
        texture = self.property('vines_texture')
        texture.dispatch(self)
        texture = self.property('vines2_texture')
        texture.dispatch(self)

    def on_button_click(self, instances):
        Decisive.stop()
        QOne = QuestionOne()
        self.parent.add_widget(QOne)
        self.parent.remove_widget(self)
        Enter.play()

class QuestionOne(Screen): #<---- (first question)
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        Street.play()
        self.exit_button = Button(size_hint=(None, None),
                                  size=(90, 90),
                                  pos=(self.center_x + 670, self.center_y + 474),
                                  background_normal="exit_button.png")
        self.exit_button.bind(on_press=stop_app)
        self.add_widget(self.exit_button)

        self.next_button = Button(size_hint=(None, None),
                                  size=(90, 90),
                                  pos=(self.center_x + 670, self.center_y + 415),
                                  background_normal="next_button.png")
        self.next_button.bind(on_press=self.on_button_click)
        self.add_widget(self.next_button)

    def on_button_click(self, instance):
        Qtwo = QuestionTwo()
        self.parent.add_widget(Qtwo)
        self.parent.remove_widget(self)
        Enter.play()

class QuestionTwo(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.exit_button = Button(size_hint=(None, None),
                                  size=(90, 90),
                                  pos=(self.center_x + 670, self.center_y + 474),
                                  background_normal="exit_button.png")
        self.exit_button.bind(on_press=stop_app)
        self.add_widget(self.exit_button)


        self.next_button = Button(size_hint=(None, None),
                                  size=(90, 90),
                                  pos=(self.center_x + 670, self.center_y + 415),
                                  background_normal="next_button.png")
        self.next_button.bind(on_press=self.on_button_click)
        self.add_widget(self.next_button)

    def on_button_click(self, instance):
        Qthree = QuestionThree()
        self.parent.add_widget(Qthree)
        self.parent.remove_widget(self)
        Enter.play()

class QuestionThree(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.exit_button = Button(size_hint=(None, None),
                                  size=(90, 90),
                                  pos=(self.center_x + 670, self.center_y + 474),
                                  background_normal="exit_button.png")
        self.exit_button.bind(on_press=stop_app)
        self.add_widget(self.exit_button)

        self.next_button = Button(size_hint=(None, None),
                                  size=(90, 90),
                                  pos=(self.center_x + 670, self.center_y + 415),
                                  background_normal="next_button.png")
        self.next_button.bind(on_press=self.on_button_click)
        self.add_widget(self.next_button)

    def on_button_click(self, instance):
        Qfour = QuestionFour()
        self.parent.add_widget(Qfour)
        self.parent.remove_widget(self)
        Enter.play()

class QuestionFour(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.exit_button = Button(size_hint=(None, None),
                                  size=(90, 90),
                                  pos=(self.center_x + 670, self.center_y + 474),
                                  background_normal="exit_button.png")
        self.exit_button.bind(on_press=stop_app)
        self.add_widget(self.exit_button)

        self.next_button = Button(size_hint=(None, None),
                                  size=(90, 90),
                                  pos=(self.center_x + 670, self.center_y + 415),
                                  background_normal="next_button.png")
        self.next_button.bind(on_press=self.on_button_click)
        self.add_widget(self.next_button)

    def on_button_click(self, instance):
        Qfive = QuestionFive()
        self.parent.add_widget(Qfive)
        self.parent.remove_widget(self)
        Enter.play()

class QuestionFive(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.exit_button = Button(size_hint=(None, None),
                                  size=(90, 90),
                                  pos=(self.center_x + 670, self.center_y + 474),
                                  background_normal="exit_button.png")
        self.exit_button.bind(on_press=stop_app)
        self.add_widget(self.exit_button)

class PacmanApp(App):
    def on_start(self):                        #the frame rate: 60 per second
        Clock.schedule_interval(self.root.ids.background.scroll_textures, 1 / 60)

if __name__ == '__main__':
    PacmanApp().run()
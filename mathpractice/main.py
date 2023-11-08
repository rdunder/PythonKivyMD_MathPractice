
#       Kivy moduless
from kivymd.app import MDApp
from kivy.lang import Builder
from kivy.clock import Clock

#       General modules
import random


#       Main app class
class MainApp(MDApp):

    #   Building main interface
    def build(self):
        self.theme_cls.primary_palette = 'DeepPurple'
        return Builder.load_file('MathPractice_withDrawer.kv')

    calc = []
    calc_list = []

    #   Focusing the text inut
    def focusTextInput(self, dt):
        self.root.ids.input_text.focus = True

    #   Starting a new game
    def start_game(self, game):
        self.root.ids.feedback.text = ''

        if game == 'plus':
            self.menu_choice = 'plus'
            l = [1,2,3,4,5]
            self.calc_list = [[x,y, x+y] for x in l for y in l] 
            
            self.calc = random.choice(self.calc_list)
            self.root.ids.input_text.hint_text = f'{self.calc[0]} + {self.calc[1]}'
            Clock.schedule_once(self.focusTextInput, 0.5)


        elif game == 'multiply':
            self.menu_choice = 'multiply'
            l = [2, 3, 4, 5, 6, 7, 8, 9]        
            self.calc_list = [[x,y,x*y] for x in l for y in l]

            self.calc = random.choice(self.calc_list)
            self.root.ids.input_text.hint_text = f'{self.calc[0]} * {self.calc[1]}'
            Clock.schedule_once(self.focusTextInput, 0.5)


    def answerCalc(self):
        if len(self.calc_list) < 1:
            return
        try:
            user_answer = int(self.root.ids.input_text.text)
        except:
            self.root.ids.input_text.text = ''
            Clock.schedule_once(self.focusTextInput, 0.5)
            return

        prev_calc = self.root.ids.input_text.hint_text
        answer = self.calc[2]
        
        if int(user_answer) == answer:
            self.root.ids.feedback.text = 'RÄTT !'

        else:
            self.root.ids.feedback.text = f'! {prev_calc} = {answer}'


        self.calc = random.choice(self.calc_list)
        self.root.ids.input_text.hint_text = f'{self.calc[0]} + {self.calc[1]}'
        self.root.ids.input_text.text = ''
        Clock.schedule_once(self.focusTextInput, 0.5)


if __name__ == '__main__':
    MainApp().run()
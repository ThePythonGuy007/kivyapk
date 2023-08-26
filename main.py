from kivy.properties import ObjectProperty
from kivy.app import App
from kivy.uix.widget import Widget
from kivy.lang import Builder
from kivy.core.window import Window

#set window size/App size
Window.size = (400,550)


# to load design .kv files
Builder.load_file('design.kv')



class MyLayout(Widget):


    # CLEAR BUTTON
    def clear(self):
        self.ids.calc_input.text='0'

    #Create a button pressing function
    def button_press(self,button):
        #create variable to contain textbox var
        already = self.ids.calc_input.text

        if "Error" in already:
            already = ''

        if already == '0':
            self.ids.calc_input.text = ''
            self.ids.calc_input.text = f'{button}'

        else:
            self.ids.calc_input.text = f'{already}{button}'



    def inverse(self):
        already = self.ids.calc_input.text
        if '-' in already:
            self.ids.calc_input.text =f'{already.replace("-","")}'

        else:
            self.ids.calc_input.text = f'-{already}'




    def remove(self):
        already = self.ids.calc_input.text
        already = already[:-1]
        self.ids.calc_input.text = already

        if self.ids.calc_input.text== '':
            self.ids.calc_input.text = '0'



    def dot(self):
        already = self.ids.calc_input.text

        num_list = already.split('+')

        if "+" in already and "." not in num_list[-1]:
            already = f'{already}.'
            self.ids.calc_input.text = already
        elif "." in already:
            pass

        else:
        #add decimal
            already = f'{already}.'

            #output
            self.ids.calc_input.text = already


    def math_sign(self,sign):
        already = self.ids.calc_input.text

        #adding plus sign to textbox
        self.ids.calc_input.text = f'{already}{sign}'


    def equal(self):
        try:
            already = self.ids.calc_input.text


            answer = eval(already)
            self.ids.calc_input.text = str(answer)
        except:
            self.ids.calc_input.text = 'Error'







class Calculator(App):
    def build(self):
        return MyLayout()


if __name__ == "__main__":
    Calculator().run()
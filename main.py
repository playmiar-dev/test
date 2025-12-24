# -*- coding: utf-8 -*-
import re
from kivy.app import App
from kivy.lang import Builder
from kivy.properties import StringProperty
from kivy.core.window import Window

# Optional: set a fixed size when running on desktop
# Window.size = (360, 640)

KV = """
#:import dp kivy.metrics.dp

<CalcButton@Button>:
    font_size: '20sp'
    size_hint: (1, 1)
    background_normal: ''
    background_color: (0.13, 0.13, 0.16, 1)
    color: (1, 1, 1, 1)
    bold: False

BoxLayout:
    orientation: 'vertical'
    padding: dp(12)
    spacing: dp(8)

    TextInput:
        id: display
        text: app.display_text
        font_size: '28sp'
        size_hint_y: None
        height: dp(64)
        multiline: False
        readonly: True
        background_normal: ''
        background_color: (0.06, 0.06, 0.08, 1)
        foreground_color: (1, 1, 1, 1)
        cursor_blink: False

    GridLayout:
        cols: 4
        spacing: dp(6)
        size_hint_y: None
        height: dp(320)

        CalcButton:
            text: 'C'
            background_color: (0.72, 0.18, 0.18, 1)
            on_press: app.clear()

        CalcButton:
            text: 'DEL'
            background_color: (0.45, 0.20, 0.20, 1)
            on_press: app.backspace()

        CalcButton:
            text: '('
            on_press: app.append_char('(')

        CalcButton:
            text: ')'
            on_press: app.append_char(')')

        CalcButton:
            text: '7'
            on_press: app.append_char('7')
        CalcButton:
            text: '8'
            on_press: app.append_char('8')
        CalcButton:
            text: '9'
            on_press: app.append_char('9')
        CalcButton:
            text: '÷'
            on_press: app.append_char('/')

        CalcButton:
            text: '4'
            on_press: app.append_char('4')
        CalcButton:
            text: '5'
            on_press: app.append_char('5')
        CalcButton:
            text: '6'
            on_press: app.append_char('6')
        CalcButton:
            text: '×'
            on_press: app.append_char('*')

        CalcButton:
            text: '1'
            on_press: app.append_char('1')
        CalcButton:
            text: '2'
            on_press: app.append_char('2')
        CalcButton:
            text: '3'
            on_press: app.append_char('3')
        CalcButton:
            text: '-'
            on_press: app.append_char('-')

        CalcButton:
            text: '0'
            on_press: app.append_char('0')
        CalcButton:
            text: '.'
            on_press: app.append_char('.')
        CalcButton:
            text: '+'
            on_press: app.append_char('+')
        CalcButton:
            text: '='
            background_color: (0.20, 0.45, 0.25, 1)
            on_press: app.evaluate()
"""

class CalcApp(App):
    display_text = StringProperty("")

    def build(self):
        return Builder.load_string(KV)

    def append_char(self, ch):
        # Prevent two operators in a row (basic hygiene)
        if self.display_text and ch in '+-*/' and self.display_text[-1] in '+-*/':
            self.display_text = self.display_text[:-1] + ch
            return
        # Limit length to keep UI clean
        if len(self.display_text) >= 64:
            return
        self.display_text += ch

    def clear(self):
        self.display_text = ""

    def backspace(self):
        self.display_text = self.display_text[:-1]

    def _sanitize(self, expr):
        # Replace unicode operators with python ones
        expr = expr.replace('×', '*').replace('÷', '/')
        # Only allow digits, operators, parentheses, dot, space
        if not re.fullmatch(r'[0-9\+\-\*/\(\)\.\s]*', expr):
            raise ValueError("Invalid characters")
        return expr

    def evaluate(self):
        expr = self.display_text.strip()
        if not expr:
            return
        try:
            safe_expr = self._sanitize(expr)
            # Evaluate safely: only arithmetic
            result = eval(safe_expr, {"__builtins__": {}}, {})
            # Convert floats like 5.0 to 5
            if isinstance(result, float) and result.is_integer():
                result = int(result)
            self.display_text = str(result)
        except Exception:
            self.display_text = "خطا"

if __name__ == "__main__":
    CalcApp().run()
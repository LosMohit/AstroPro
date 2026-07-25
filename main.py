from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.scrollview import ScrollView
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.popup import Popup
from engine.prediction import Prediction
from database.database import save_user, save_daily_forecast


class CalendarPopup(Popup):
    def __init__(self, user_id, **kwargs):
        super().__init__(**kwargs)
        self.title = "AstroAI Pro - Yearly Astrology Calendar"
        self.size_hint = (0.9, 0.9)

        # Main layout inside popup
        content_layout = BoxLayout(orientation="vertical", padding=10, spacing=10)

        # Scrollable area for the yearly grid
        scroll = ScrollView()
        grid_layout = BoxLayout(orientation="vertical", size_hint_y=None, spacing=5)
        grid_layout.bind(minimum_height=grid_layout.setter("height"))

        engine = Prediction()
        calendar_data = engine.generate_yearly_calendar("2026-01-01")

        for day in calendar_data:
            date_str = day["date"]
            status = day["status"]
            pro_text = day["pro"]
            con_text = day["con"]

            # Row layout for each day
            row = BoxLayout(size_hint_y=None, height=40, spacing=10)
            lbl_date = Label(text=date_str, size_hint_x=0.3)
            lbl_status = Label(text=status, size_hint_x=0.4)

            btn_detail = Button(text="Details", size_hint_x=0.3)
            btn_detail.bind(
                on_press=lambda x, d=date_str, s=status, p=pro_text, c=con_text: self.show_details(
                    d, s, p, c
                )
            )

            row.add_widget(lbl_date)
            row.add_widget(lbl_status)
            row.add_widget(btn_detail)

            grid_layout.add_widget(row)
            save_daily_forecast(user_id, date_str, status, pro_text, con_text)

        scroll.add_widget(grid_layout)
        content_layout.add_widget(scroll)

        close_btn = Button(text="Close", size_hint_y=None, height=50)
        close_btn.bind(on_press=self.dismiss)
        content_layout.add_widget(close_btn)

        self.content = content_layout

    def show_details(self, date_str, status, pro_text, con_text):
        detail_layout = BoxLayout(orientation="vertical", padding=15, spacing=10)
        detail_layout.add_widget(Label(text=f"Date: {date_str}", bold=True))
        detail_layout.add_widget(Label(text=f"Status: {status}"))
        detail_layout.add_widget(Label(text=f"Pro: {pro_text}"))
        detail_layout.add_widget(Label(text=f"Con: {con_text}"))

        popup = Popup(
            title="Forecast Details", content=detail_layout, size_hint=(0.8, 0.6)
        )
        detail_layout.add_widget(
            Button(text="Back", size_hint_y=None, height=40, on_press=popup.dismiss)
        )
        popup.open()


class AstroApp(App):
    def build(self):
        self.title = "AstroAI Pro"

        # Main Home Screen Layout
        layout = BoxLayout(orientation="vertical", padding=20, spacing=20)

        title_label = Label(
            text="Welcome to AstroAI Pro",
            font_size=24,
            bold=True,
            size_hint_y=None,
            height=60,
        )
        layout.add_widget(title_label)

        btn_calendar = Button(
            text="Open Yearly Calendar",
            size_hint_y=None,
            height=60,
            background_color=(0.2, 0.6, 0.8, 1),
        )
        btn_calendar.bind(on_press=self.open_calendar_popup)
        layout.add_widget(btn_calendar)

        return layout

    def open_calendar_popup(self, instance):
        user_id = save_user("Sample User", "1995-05-15", "10:30", "New York")
        popup = CalendarPopup(user_id)
        popup.open()


if __name__ == "__main__":
    AstroApp().run()

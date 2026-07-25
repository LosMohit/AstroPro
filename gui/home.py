import customtkinter as ctk
from database.database import save_user, save_daily_forecast
from engine.prediction import Prediction


class CalendarWindow(ctk.CTkToplevel):
    def __init__(self, parent, user_id):
        super().__init__(parent)
        self.geometry("750x600")
        self.title("AstroAI Pro - Yearly Astrology Calendar")
        self.user_id = user_id

        self.engine = Prediction()

        title = ctk.CTkLabel(
            self, text="Interactive Astrology Calendar Grid", font=("Arial", 22, "bold")
        )
        title.pack(pady=15)

        self.scroll_frame = ctk.CTkScrollableFrame(self, width=680, height=450)
        self.scroll_frame.pack(padx=20, pady=10, fill="both", expand=True)

        self.load_full_year_grid()

    def load_full_year_grid(self):
        calendar_data = self.engine.generate_yearly_calendar("2026-01-01")

        for day in calendar_data:
            date_str = day["date"]
            status = day["status"]
            pro_text = day["pro"]
            con_text = day["con"]

            if "Good" in status or "Excellent" in status or "Productive" in status:
                color = "green"
            elif "Caution" in status:
                color = "orange"
            else:
                color = "darkred"

            card = ctk.CTkFrame(self.scroll_frame, fg_color="gray20", corner_radius=8)
            card.pack(fill="x", pady=4, padx=5)

            lbl_date = ctk.CTkLabel(
                card, text=date_str, font=("Arial", 13, "bold"), width=100, anchor="w"
            )
            lbl_date.pack(side="left", padx=10, pady=8)

            lbl_status = ctk.CTkLabel(
                card,
                text=status,
                font=("Arial", 12),
                text_color=color,
                width=160,
                anchor="w",
            )
            lbl_status.pack(side="left", padx=10, pady=8)

            btn_details = ctk.CTkButton(
                card,
                text="View Pros & Cons",
                width=130,
                fg_color="#3b82f6",
                command=lambda d=date_str, s=status, p=pro_text, c=con_text: self.show_day_details(
                    d, s, p, c
                ),
            )
            btn_details.pack(side="right", padx=10, pady=8)

            save_daily_forecast(self.user_id, date_str, status, pro_text, con_text)

    def show_day_details(self, date_str, status, pro_text, con_text):
        detail_dialog = ctk.CTkToplevel(self)
        detail_dialog.geometry("400x300")
        detail_dialog.title(f"Forecast for {date_str}")

        ctk.CTkLabel(
            detail_dialog, text=f"Date: {date_str}", font=("Arial", 16, "bold")
        ).pack(pady=10)
        ctk.CTkLabel(
            detail_dialog,
            text=f"Overall Status: {status}",
            font=("Arial", 14),
            text_color="cyan",
        ).pack(pady=5)
        ctk.CTkLabel(
            detail_dialog,
            text=f"(+) Pro Advantage:\n{pro_text}",
            text_color="lightgreen",
            wraplength=350,
            justify="left",
        ).pack(pady=10)
        ctk.CTkLabel(
            detail_dialog,
            text=f"(-) Potential Challenge:\n{con_text}",
            text_color="salmon",
            wraplength=350,
            justify="left",
        ).pack(pady=10)


class HomePage:
    def __init__(self, root):
        self.root = root
        self.frame = ctk.CTkFrame(self.root)
        self.frame.pack(fill="both", expand=True)

        title = ctk.CTkLabel(
            self.frame, text="Welcome to AstroAI Pro", font=("Arial", 22, "bold")
        )
        title.pack(pady=30)

        btn_open_calendar = ctk.CTkButton(
            self.frame, text="Open Yearly Calendar", command=self.open_calendar
        )
        btn_open_calendar.pack(pady=20)

    def open_calendar(self):
        user_id = save_user("Sample User", "1995-05-15", "10:30", "New York")
        CalendarWindow(self.root, user_id)

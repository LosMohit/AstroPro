import random
from datetime import datetime, timedelta

class Prediction:
    def __init__(self):
        pass

    def generate(self):
        return {
            "overall": random.randint(40, 100),
            "career": random.choice(["Excellent", "Good", "Average", "Weak"]),
            "finance": random.choice(["Excellent", "Good", "Average", "Weak"]),
            "love": random.choice(["Excellent", "Good", "Average", "Weak"]),
            "health": random.choice(["Excellent", "Good", "Average"]),
            "lucky_number": random.randint(1, 9),
            "lucky_color": random.choice(["Blue", "Green", "White", "Purple"]),
        }

    def generate_yearly_calendar(self, start_date_str="2026-01-01"):
        """Generates daily pros, cons, and statuses for an entire 365-day year."""
        start_date = datetime.strptime(start_date_str, "%Y-%m-%d")
        statuses = ["Good Day", "Highly Productive", "Caution Advised", "Not so good", "Excellent Energy"]
        
        pool_pros = [
            "High mental clarity", "Great alignment for financial growth", 
            "Favorable for starting new projects", "Strong interpersonal connections"
        ]
        pool_cons = [
            "Prone to minor miscommunications", "Avoid impulsive purchases", 
            "Watch out for sudden fatigue", "Emotional turbulence possible"
        ]

        yearly_data = []
        for i in range(365):
            current_date = start_date + timedelta(days=i)
            yearly_data.append({
                "date": current_date.strftime("%Y-%m-%d"),
                "status": random.choice(statuses),
                "pro": random.choice(pool_pros),
                "con": random.choice(pool_cons)
            })
        return yearly_data
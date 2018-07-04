"""
Program opens the browser and play a music video to simulate a disruption and provoke a break from work
"""

import time
import webbrowser

total_breaks = 3
break_count = 0
delay = 10

print("This program started on "+time.ctime())

while break_count < total_breaks:
    time.sleep(delay)
    webbrowser.open("https://www.youtube.com/watch?v=jP0AuScHhGU&start_radio=1&list=RDjP0AuScHhGU")
    break_count += 1
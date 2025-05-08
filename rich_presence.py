from pypresence import Presence
import time
import random 

CLIENT_ID="1369991638126166087"
rpc = Presence(CLIENT_ID)
rpc.connect()

states = [
    "Samir hits another tree, again !",
    "Full throttle",
    "When in doubt, go Flat-Out !",
    "Flat-Out !",
    "Not listening to the calls",
    "Breaking the car",
    "Hoping the car survives",
    "Taking a shortcut",
    "Pulling the handbrake",
    "In the air, again...",
    "The road? What road?",
    "Too much speed, not enough grip",
    "The co-driver says left 4, it was a left 2...'",
    "It's not crashing, it's creative driving",
    "That was supposed to be a drift",
    "Taking on gravel like a pro",
    "Hoping the handbrake holds up",
    "One more corner... or maybe not",
    "Flat-out into the unknown",
]

start_time = time.time()

rpc.update(
    state=random.choice(states),
    details="Richard Burns Rally (Rallysimfans)",
    start=start_time
)

print("Rich Presence for Richard Burn Rally activated. Ctrl+C to quit.")

while True:
    rpc.update(
        state=random.choice(states),
        details="Richard Burns Rally (Rallysimfans)",
        start=start_time
    )
    time.sleep(120)
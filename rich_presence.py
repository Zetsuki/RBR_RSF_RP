from pypresence import Presence
import time

CLIENT_ID="1369991638126166087"
rpc = Presence(CLIENT_ID)
rpc.connect()

rpc.update(
    state="In a race",
    details="Richard Burns Rally (Rallysimfans)",
    start=time.time()
)

print("Rich Presence for Richard Burn Rally activated. Ctrl+C to quit.")
while True:
    time.sleep(60)
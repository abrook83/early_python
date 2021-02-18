### 8.9 Messages ###

# msgs = ['how ya goin?','where ya garn?','can i come too?']

# def send_msg(msgs):
#     for msg in msgs:
#         print(f"Hey, {msg}")

# send_msg(msgs)


### 8.10 Sending Messages ###

# msgs = ['how ya goin?','where ya garn?','can i come too?']
# sent = []

# def send_msg(msgs):
#     while msgs:
#         sending = msgs.pop()
#         print(f"Sending '{sending}'")
#         sent.append(sending)

# print("\n")
# send_msg(msgs)

# print(f"\nMsgs: {msgs}")
# print(f"Sent: {sent}")


### 8.11 Archived Messages ###


msgs = ['how ya goin?','where ya garn?','can i come too?']
sent = []

def send_msg(msgs):
    while msgs:
        sending = msgs.pop()
        print(f"Sending '{sending}'")
        sent.append(sending)

print("\n")
send_msg(msgs[:])           # adding [:] creates a copy of the list

print(f"\nMsgs: {msgs}")
print(f"Sent: {sent}")
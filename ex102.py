# Write a program to read through the mbox-short.txt and figure out the
# distribution by hour of the day for each of the messages. You can pull the
# hour out from the 'From ' line by finding the time and then splitting the
# string a second time using a colon.
# From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008
# Once you have accumulated the counts for each hour, print out the counts,
# sorted by hour as shown below:
name = input("Enter file:")
if len(name) < 1 : name = "mbox-short.txt"
fhand = open(name)
counts = 0
hrs = dict()
for line in fhand:
    if not line.startswith('From'): continue    #skip lines not beginning w/ 'From'
    words = line.split()                        # split lines into words
    time = words[5:6]                # extract time
    for hr in time:
        hr = (hr[:2])                    # extract hour
        hrs[hr] = hrs.get(hr,0) + 1       # add hr to hrs dictionary, count up 1.
for k,v in sorted(hrs.items()):    # for each comma-seperated entry in hrs, sort, and -
    print(k,v)                      # print those items.

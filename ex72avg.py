# Use the file name mbox-short.txt as the file name
fname = input("Enter file name: ")
fh = open(fname,'r')
count = 0
tot = 0
for line in fh:
# for each line that doesn't start with... continue
    if not line.startswith("X-DSPAM-Confidence:") : continue
    count = count + 1
# take data after the 20th char., then rstrip to remove the white space from RHS
    num = float(line[20:].rstrip())
# as tot starts at 0, with each new one num, add it to tot
    tot = tot + num
# divide the lot by the sum to get the average!
avg = tot / count
print("Average spam confidence:",avg)

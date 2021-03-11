N = int(input('Enter width dimension: '))
M = 3 * N

patt = '.|.'
for i in range(1,N,2):      # every second number in the range
    patts = i * patt
    dashes_per_side = int((M - len(patts)) / 2)
    line = f"{'-' * dashes_per_side}{patts}{'-' * dashes_per_side}"
    print(line)

msg = 'WELCOME'
cline_dashes = int((M - len(msg)) / 2)
print(f"{cline_dashes * '-'}{msg}{cline_dashes * '-'}")

for i in reversed(range(1,N,2)):      # every second number in the range
    patts = i * patt
    dashes_per_side = int((M - len(patts)) / 2)
    line = f"{'-' * dashes_per_side}{patts}{'-' * dashes_per_side}"
    print(line)

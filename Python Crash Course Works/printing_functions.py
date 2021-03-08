
def print_models(unprinted, printed):
    while unprinted:                    # while there is still items in 'unprinted'
        curr_job = unprinted.pop()          # pop the last design out of the list 'unprinted' and call it 'curr_job'
        print(f"\nPrinting {curr_job}...")     
        printed.append(curr_job)            # add 'curr_job' in to 'printed' to show completion

def display(printed):
    print("\nThe following print jobs have been completed:")
    for finished in printed:
        print(f"\t- {finished}")


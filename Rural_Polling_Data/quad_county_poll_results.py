import os
import csv

votes_cast = []
candidates = []


csvpath = os.path.join('Resources', 'election_data.csv')
out_path = os.path.join('quad_county_poll_results.txt')

with open(csvpath, 'r') as csvfile:


    csvreader = csv.reader(csvfile)
    next(csvreader, None)

    for row in csvreader:
        votes_cast.append(row[0])
        candidates.append(row[2])
        
    #Calculating Amount and Names of Candidates    
    name_of_candidates = set(candidates)
    num_of_candidates = len(name_of_candidates)

    #Function calc total votes each candidate
    def total_vote_received(candidate):
        total_votes = candidates.count(candidate)
        return(total_votes)

    #Function calc percentage each candidate
    def percentage_vote_received(candidate):
        percentage_votes = candidates.count(candidate) / len(candidates)
        as_percent = "{:.3%}".format(percentage_votes)
        return(as_percent)

    total_vote_set = [total_vote_received('Khan'), total_vote_received("Correy"), total_vote_received("Li"), total_vote_received("O'Tooley")]
    winner_winner = max(total_vote_set)

    def winner_calc():
        if winner_winner == total_vote_received('Correy'):
            print("Correy")
        elif winner_winner == total_vote_received('Li'):
            print("Li")
        elif winner_winner == total_vote_received("O'Tooley"):
            print("O'Tooley")
        else:
            return('Khan')

    print("Election Results")
    print("-------------------------")
    print("Total Votes: " + str(len(votes_cast)))
    print("  -------------------------")
    print("Candidates: " + str(name_of_candidates))
    print("-------------------------")
    print("Khan: " + str(percentage_vote_received('Khan')) + " (" + str(total_vote_received('Khan')) + ")") 
    print("Correy: " + str(percentage_vote_received('Correy')) + " (" + str(total_vote_received('Correy')) + ")")
    print("Li: " + str(percentage_vote_received('Li')) + " (" + str(total_vote_received('Li')) + ")")
    print("O'Tooley: " + str(percentage_vote_received("O'Tooley")) + " (" + str(total_vote_received("O'Tooley")) + ")")
    print("-------------------------")
    print("Winner: " + str(winner_calc()))


    with open(out_path, "w") as file:

        file.write("Election Results" + "\n")
        file.write("-------------------------" + "\n")
        file.write("Total Votes: " + str(len(votes_cast)) + "\n")
        file.write("  -------------------------" + "\n")
        file.write("Candidates: " + str(name_of_candidates) + "\n")
        file.write("-------------------------" + "\n")
        file.write("Khan: " + str(percentage_vote_received('Khan')) + " (" + str(total_vote_received('Khan')) + ")" + "\n")
        file.write("Correy: " + str(percentage_vote_received('Correy')) + " (" + str(total_vote_received('Correy')) + ")" + "\n")
        file.write("Li: " + str(percentage_vote_received('Li')) + " (" + str(total_vote_received('Li')) + ")" + "\n")
        file.write("O'Tooley: " + str(percentage_vote_received("O'Tooley")) + " (" + str(total_vote_received("O'Tooley")) + ")" + "\n")
        file.write("-------------------------" + "\n")
        file.write("Winner: " + str(winner_calc()) + "\n")
        



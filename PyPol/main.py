import os
import csv

fpath = os.path.join("PyPol",
                     "resources/election_data.csv")

voter_id = []
candidate_dict = {}

with open(fpath, 'r', newline='')as file:
    csv_read = csv.reader(file)
    next(csv_read)
    for row in csv_read:
        voter_id.append(row[0])

        # making dictionary
        if row[2] in candidate_dict:
            candidate_dict[row[2]] += 1
        else:
            candidate_dict[row[2]] = 1

total_vote = len(voter_id)

# sorting dictionary by using .items() method and sorted() function
candidate_dict_sorted = sorted(
    candidate_dict.items(),
    key=lambda kv: kv[1],
    reverse=True)
winner_name = candidate_dict_sorted[0][0]

# printing results in console as well as in text file
with open("PyPol_Results.txt", '+w') as f:
    print("Election Results")
    print("-------------------------")
    print(f"Total Votes:{total_vote}")
    print("------------------------")
    f.write("Election Results\n")
    f.write("-------------------------\n")
    f.write(f"Total Votes:{total_vote}\n")
    f.write("------------------------\n")

    # unpacking dictionary in tuples by .items() method and printing results
    for name, votecount in candidate_dict.items():
        percentage_of_vote = round((votecount/total_vote)*100, 3)
        print(f"{name}:{percentage_of_vote}% ({votecount})")
        f.write(f"{name}:{percentage_of_vote}% ({votecount})\n")

    print("------------------------")
    print(f"winner: {winner_name}")
    print("-------------------------")
    f.write("------------------------\n")
    f.write(f"winner: {winner_name}\n")
    f.write("-------------------------\n")

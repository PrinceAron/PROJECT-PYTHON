## 🏆 THE PROJECT: The Starfleet Recruitment Center

def get_eligible_candidates(candidates,min_age=18):
    eligible = []
    for candidate in candidates:
        if candidate["age"]  >= min_age:
            eligible.append(candidate)
    return eligible

how_many = int(input("Please Enter How many applicant: "))
applicants = []

for register in range(how_many):
    while True:

        job_seeker = {
            "name": input("Please Enter Your Name: "), 
            "age": int(input("Please Enter Your Age: ")),
        }
        
        applicants.append(job_seeker)


accepted = get_eligible_candidates(applicants)

print(f"Name: {job_seeker['name']}")
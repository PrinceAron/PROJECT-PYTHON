# The Airport Customs Scanner PERFECT
prohibited_items = ["knife", "explosives", "liquids"]

security_log = []

for i in range(2):
    passenger = {}
    passenger["name"] = input("Enter your name: ")
    passenger["passport_country"] = input("Enter your passport country: ")
    suitcase = []
    for x in range(3):
        item = input("Enter Item inside at suitcase: ").lower().strip()
        suitcase.append(item)
        passenger["suitcase"] = suitcase
    security_log.append(passenger)

for validity in security_log:
    cleared = True

    for check in validity["suitcase"]:
        if check in prohibited_items:
            cleared = False

    if cleared:
        validity["Result"] = "PASSED"
    else:
        validity["Result"] = "DETENTION!!!"

for final in security_log:
    print(final)
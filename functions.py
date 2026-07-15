import random
import json

def train(number):
    guess1 = random.randint(2, 11)
    with open("logs.json", "r") as file:
        # protocol for no prior data
        if file.read() == "[]":
            final_guess = guess1
            question_if_correct = input(f"does {final_guess} come after {number}? (y/n)")
            if question_if_correct == "y":
                correct = True
            elif question_if_correct == "n":
                correct = False
            file.seek(0)
            with open("logs.json", "r") as file:
                data = json.load(file)
            # safety code for when something else then "y" or "n" is the input
            try:
                data.append({
                    "input": number,
                    "output": final_guess,
                    "correct": correct
                })
            except NameError:
                data.append({
                    "input": number,
                    "output": final_guess,
                    "correct": None
                })
            # end of safety code
            file.seek(0)
            with open("logs.json", "w") as file:
                json.dump(data, file)
        # end of protocol for no data
        else:
            file.seek(0)
            data = json.load(file)
            selection = []
            for item in data:
                if item["input"] == number:
                    selection.append(item)
            if selection == []:
                final_guess = guess1
                question_if_correct = input(f"does {final_guess} come after {number}? (y/n)")
                if question_if_correct == "y":
                    correct = True
                elif question_if_correct == "n":
                    correct = False
                # safety code for when something else then "y" or "n" is the input
                try:
                    data.append({
                        "input": number,
                        "output": final_guess,
                        "correct": correct
                    })
                except NameError:
                    data.append({
                        "input": number,
                        "output": final_guess,
                        "correct": None
                    })
                # end of safety code
                file.seek(0)
                with open("logs.json", "w") as file:
                    file.seek(0)
                    json.dump(data, file)
            for item in selection:
                if item["correct"] == True:
                    final_guess = item["output"]
                    question_if_correct = input(f"does {final_guess} come after {number}? (y/n)")
                    if question_if_correct == "y":
                        correct = True
                    elif question_if_correct == "n":
                        correct = False
                        item["correct"] = False
                        # safety code for when something else then "y" or "n" is the input
                        try:
                            data.append({
                            "input": number,
                            "output": final_guess,
                            "correct": correct
                            })
                        except NameError:
                            data.append({
                               "input": number,
                                "output": final_guess,
                                "correct": None
                            })
                        # end of safety code
                        file.seek(0)
                        with open("logs.json") as file:
                            json.dump(data, file)
                    # safety code for when something else then "y" or "n" is the input
                    try:
                        data.append({
                        "input": number,
                            "output": final_guess,
                            "correct": correct
                        })
                    except NameError:
                        data.append({
                            "input": number,
                            "output": final_guess,
                            "correct": None
                        })
                    # end of safety code
                    with open("logs.json", "w") as file:
                        json.dump(data, file)

def logs():
    with open("logs.json", "r") as file:
        file.seek(0)
        logs = json.load(file)
        return logs

def addlogstollm(logsToadd):
    with open(logsToadd, "r") as file:
        newlogs = json.load(file)
    with open("logs.json", "r") as file:
        file.seek(0)
        mainlogs = json.load(file)
    print(f"""
        These are the new logs:
        {newlogs}
    """)
    isNotcorruptAnswer = input("Are these logs correct? (y/n)")
    if isNotcorruptAnswer == "y":
        isNotcorrupt = True
    elif isNotcorruptAnswer == "n":
        isNotcorrupt = False
        print("shutting down...")
        exit()
    for item in newlogs:
        if isNotcorrupt:
            mainlogs.append(item)
        else:
            print("shutting down...")
            exit()


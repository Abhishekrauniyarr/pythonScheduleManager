
import pandas as pd
from datetime import datetime


t = {
    "Time": [],
    "Activities": []
}


def day_schedule(Time, Activity):
    t["Time"].append(Time)
    t["Activities"].append(Activity)
    df = pd.DataFrame(t)
    return df


def add(day):
    reset_dict()
    print(f"\n--- CREATING SCHEDULE: {day.upper()} ---")

    while True:
        print("\nEnter 'stop' to finish adding entries.")
        time = input("Enter time: ")
        if time.lower() == "stop":
            break
        activity = input("Enter activity: ")
        if activity.lower() == "stop":
            break
        day_schedule(time, activity)

    if not t["Time"]:
        print("\nNo schedule entries added!")
        return
    fun = pd.DataFrame(t)
    fun.to_csv(f"schedule/{day}.csv", index=False)

    print(f"\nSchedule for {day.upper()} saved successfully!")


def reset_dict():
    for key in t:
        t[key].clear()


while True:

    print("""
    ══════════════════════════════
        WEEKLY SCHEDULE MANAGER
    ══════════════════════════════
    Select a day:
    1. Monday
    2. Tuesday
    3. Wednesday
    4. Thursday
    5. Friday
    6. Saturday
    7. Sunday
    8. Today
    9. Exit
    ══════════════════════════════
    """)

    day_user = int(input("Select day: "))

    if day_user == 9:
        print("\nExiting Schedule Manager. Goodbye!")
        exit()

    if day_user == 1:
        day = "monday"
    elif day_user == 2:
        day = "tuesday"
    elif day_user == 3:
        day = "wednesday"
    elif day_user == 4:
        day = "thursday"
    elif day_user == 5:
        day = "friday"
    elif day_user == 6:
        day = "saturday"
    elif day_user == 7:
        day = "sunday"
    elif day_user == 8:
        day = datetime.now().strftime("%A").lower()
    else:
        print("\nInvalid day selection! Please try again.")
        continue

    while True:
        print(f"""
        ══════════════════════════════
            {day.upper()} SCHEDULE
        ══════════════════════════════
        1. Add Data
        2. Edit Data
        3. View Data
        4. Remove Data
        5. Back to Day Selection
        ══════════════════════════════
        """)

        feature_user = int(input("Select an option: "))

        if feature_user == 5:
            reset_dict()
            break

        # to add
        if feature_user == 1:
            add(day)

        # to edit data
        elif feature_user == 2:
            fun = pd.read_csv(f"schedule/{day}.csv")
            print("\n--- CURRENT SCHEDULE ---")
            print(fun)

            print("""
            Select a column to edit:
            1. Time
            2. Activities
            """)

            edit_choice = int(input("Select column: "))
            if edit_choice in [1, 2]:
                line = int(input("Enter entry number to edit: "))
                if line < 1 or line > len(fun):
                    print("Invalid entry number!")
                    continue

                # for time
                if edit_choice == 1:
                    new_time = input("Enter new time: ")
                    fun.at[line - 1, "Time"] = new_time

                # for activity
                elif edit_choice == 2:
                    new_activity = input("Enter new activity: ")
                    fun.at[line - 1, "Activities"] = new_activity

                print("\n--- UPDATED SCHEDULE ---")
                print(fun)
                fun.to_csv(f"schedule/{day}.csv", index=False)
                print("\nChanges saved successfully!")

            else:
                print("Invalid column selection!")

        # to view
        elif feature_user == 3:
            fun = pd.read_csv(f"schedule/{day}.csv")
            print(f"\n--- {day.upper()} SCHEDULE ---")
            print(fun)

        # to delete
        elif feature_user == 4:
            fun = pd.read_csv(f"schedule/{day}.csv")
            print("\n--- CURRENT SCHEDULE ---")
            print(fun)

            line = int(input("Enter entry number to remove: "))

            if line < 1 or line > len(fun):
                print("Invalid entry number!")
                continue

            fun = fun.drop(line - 1).reset_index(drop=True)
            print("\n--- UPDATED SCHEDULE ---")
            print(fun)
            fun.to_csv(f"schedule/{day}.csv", index=False)
            print("\nEntry removed successfully!")

        else:
            print("Invalid option! Please try again.")

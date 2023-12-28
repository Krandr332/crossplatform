import random

def tv_plot():
    print("\tTVPLOT")
    print("\tCREATIVE COMPUTING")
    print("\tMORRISTOWN, NEW JERSEY")
    print("\n\n\n")
    print("THIS PROGRAM AUTOMATICALLY COMES UP WITH TELEVISION")
    print("SHOWS GUARANTEED TO APPEAL TO THE MASSES AND WIN")
    print("HIGH NEILSEN RATINGS.\n")

    print("HERE IS THE FIRST PLOT:")
    generate_plot()

def generate_plot():
    plot_type = choose_option(["PROGRAM", "REPORT", "SPECIAL", "SERIES", "STORY"])
    print("\n")
    generate_character(plot_type)
    generate_trait()
    generate_occupation()
    generate_success()
    generate_activity()
    generate_resolution()

    another = input("\nANOTHER (YES OR NO): ").upper()
    if another == "NO":
        print("\nO.K.  HOPE YOU HAVE A SUCCESSFUL TV SHOW!!")
        return
    else:
        generate_plot()

def choose_option(options):
    option_index = random.randint(0, len(options) - 1)
    return options[option_index]

def generate_character(plot_type):
    character_type = choose_option(["SWINGING", "BRILLIANT", "SALTY", "HILARIOUS", "SENSITIVE", "DODDERING", "HENPECKED", "DEDICATED", "THOUGHTFUL", "HEAVY"])
    print(f"{plot_type} IS ABOUT A {character_type} {choose_option(['GIRL COWHAND', 'LITTLE BOY', 'SCIENTIST', 'LAWYER', 'TOWN MARSHALL', 'DENTIST', 'BUS DRIVER', 'JUNGLE MAN', 'SECRET AGENT', 'COLLIE'])} WHO IS {choose_option(['A WHIZ', 'A FLOP', 'MEDIOCRE', 'A SUCCESS', 'A DISASTER'])} AT", end=" ")

def generate_trait():
    print(f"{choose_option(['SOLVING CRIMES', 'ROPING COWS', 'COOKING HEALTH FOOD', 'PITCHING WOO', 'PROTECTING ECOLOGY', 'HELPING CHILDREN', 'TWO-FISTED DRINKING', 'FIGHTING FIRES', 'HERDING ELEPHANTS', 'WINNING RACES'])} AND WHO ", end="")

def generate_occupation():
    print(f"{choose_option(['RECOVERS THE JEWELS', 'FOILS THE SPIES', 'DESTROYS THE CITY', 'FINDS LOVE', 'SAVES THE ANIMALS', 'CONFESSES', 'DISCOVERS THE SECRET', 'STOPS THE FLOOD', 'HELPS THE DOG', 'MAKES THE SACRIFICE'])}.\n\n")

def choose_option(options):
    option_index = random.randint(0, len(options) - 1)
    return options[option_index]

def generate_success():
    return choose_option(['A WHIZ', 'A FLOP', 'MEDIOCRE', 'A SUCCESS', 'A DISASTER'])

def generate_activity():
    return choose_option(['SOLVING CRIMES', 'ROPING COWS', 'COOKING HEALTH FOOD', 'PITCHING WOO', 'PROTECTING ECOLOGY', 'HELPING CHILDREN', 'TWO-FISTED DRINKING', 'FIGHTING FIRES', 'HERDING ELEPHANTS', 'WINNING RACES'])

def generate_resolution():
    return choose_option(['RECOVERS THE JEWELS', 'FOILS THE SPIES', 'DESTROYS THE CITY', 'FINDS LOVE', 'SAVES THE ANIMALS', 'CONFESSES', 'DISCOVERS THE SECRET', 'STOPS THE FLOOD', 'HELPS THE DOG', 'MAKES THE SACRIFICE'])

if __name__ == "__main__":
    tv_plot()

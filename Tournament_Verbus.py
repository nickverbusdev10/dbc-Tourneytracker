'''
REQ

Participants and their starting slots should be represented by an array.
Do not put a value for empty in a slot.
Participant names are a single string. Do not put first and last names in separate values.
There will be at least 1 loop and at least 1 function.

order of things


functions

    AddPlayer

    RemovePlayer

    ListofPlayers

    NameSeparate?

    NameSort?

    NameTitle-er
        
        to regulate string entries



initialize variables

    tournament array list name thing

    Separtated_Names_Alphabetical?


THE START


input
    
    How many players?



loop- --while people are still being entered--

#access ui though input

input

UI
    Add player

        specific slot

    Remove player

        both name and slot number required

    List of players/player select?

        ordered based on slots

        additional inputs to sort alphabetically or by position?
    
    Finish

        end while loop

-loop
    

list_design

list of players (List)[
    list of player info (List_Element)[
        Name(s),slot_number
    ]
]


'''

#functions

#intialize list with slot already given

def Add_Player(Name, Slot, List):

    Slot_Number = int(Slot)

    if List[Slot_Number] == [None,Slot_Number]:

        List[Slot_Number] = [Name, Slot_Number]

    else:

        print (f"This slot is occupied by {List[i][0]} please select a different slot\n")

    return List



def Remove_Player(Name, Slot, List):

    Slot_Number = int(Slot)

    if List[Slot_Number] == [Name,Slot_Number]:

        List[Slot_Number][0] = None
        #the [0] is the name spot

    else:

        print("The given information did not match a player. Please try again\n")
    
    return List



def List_of_Players(Slot_Count, List):
    
    New_List = [None] * Slot_Count 

    for i in range(Slot_Count):

        New_List [i] = List[i][0]
    
    return New_List



#name title-er
def NT(Name):

    New_Name = Name.title()

    return New_Name



def Name_Breaker_Upper(List_Element):

    record_index=int(List_Element[1])

    if List_Element == [None,record_index]:

        Two_Names = [None,None, record_index]



    else:
        
        Two_Names = List_Element[0].split(" ")

        Two_Names.append(record_index)
    #This keeps the slot number  from Name_List

    return Two_Names



def Name_Sort_Surname_Alphabetically(List):
    
    length = len(List)

    Temp_List = [None] * length

    Sorted_List = Temp_List

    Finished_List = [None] * length

    for i in range(length):

        Temp_List[i] = List [i][1]
        # the last name will be in the name list --first slot of input -- in the second element, and will all be title cased

        if Temp_List[i] == None:

            Temp_List[i] = "zNo Participant"
    
    Sorted_List = sorted(Temp_List)

    for i in range(length):
    #looping the sorted loop 
        
        for j in range(length):
        #loop the list
           
            if Sorted_List[i] ==  List[j][1]:
            #compare

                truth_check=True

                for k in range(i):

                    truth_check=True

                    if List[j] == Finished_List[k]:
                    # if List[j] already exists in Finished_List then it won't go in

                        truth_check=False

                        break
                        # pop out of j loop pre write
                    
                if truth_check == False:

                    continue

                Finished_List[i] = List[j]

                break
                # pop out of j loop
    
    return Finished_List



'''
commence building program
'''


Player_Count=input("How many players in your tournament?\n")

Player_Count = int(Player_Count)

Tournament = True

Tournament_List = [None]*Player_Count

Tournament_Name_Split_List = [None]*Player_Count

for i in range(Player_Count):

    Tournament_List[i] = [None, i]

while Tournament == True:

    print("To add a player type \'1\'\nTo Remove a player type \'2\'\nTo view participants type\'3\'\nTo quit type \'0\'\n")

    x=input("Please respond here\n")

    x=int(x)

    if x == 1:

        A_Slot = input(f"Name a slot in which you want to place the player. Please choose from 0 to {Player_Count-1}\n")

        A_Name = input("Please give a name First Last with one space between First Last\n")

        A_Name = NT(A_Name)

        Tournament_List = Add_Player(A_Name,A_Slot,Tournament_List)

    elif x == 2:

        print("To remove a player, you must supply the name and slot of the player\n")

        Another_Name = input("Give me the name, First Last, of the player you would like to remove with exactly one space between First Last\n")

        Another_Name= NT(Another_Name)

        Another_Slot = input("Give me the slot in which the player is placed\n")

        Remove_Player(Another_Name,Another_Slot,Tournament_List)


    elif x == 3:


        print("You can see participants by seating or in alphabetical order. Type O for seating order or A for alphabetical order. Type anything else to return to the menu\n")

        petty_input=input("Select an input\n")

        if petty_input == "O" or petty_input == "o":

            for i in range(Player_Count):

                print(f"{Tournament_List[i]}\n")

        # I know that this is inefficient but my mind is tired
        if petty_input == "A" or petty_input == "a":

            for i in range(Player_Count):

                Tournament_Name_Split_List[i] = Name_Breaker_Upper(Tournament_List[i])

            Alpha_List = Name_Sort_Surname_Alphabetically(Tournament_Name_Split_List)

            for i in range(Player_Count):

                print(f"{Alpha_List[i]}\n")



    elif x == 0:

        Tournament = False



    else:

        print("Please select a valid input\n")
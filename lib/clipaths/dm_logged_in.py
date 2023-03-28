def dm_logged_in(session,currentUser):
    logged_in = True
    while logged_in:
        option = input('''
Choose:
1) Add Player
2) Show Player
3) Log out
''')
        if option == "Add Player" or option == "1":
            player_name = input("Who are you adding? ")
            currentUser.add_player(session,player_name)
        else:
            print("invalid")
    pass
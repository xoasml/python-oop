class Player:

    def __init__(self, name, team):
        self.name = name
        self.xp = 1500
        self.team = team

    def introduce(self):
        print(f"Hello! I'm {self.name},  play for {self.team}")


class Team:
    def __init__(self, team_name):
        self.team_name = team_name
        self.players = []

    def add_player(self, player_name):
        new_player = Player(player_name, self.team_name)
        self.players.append(new_player)

    def remove_player(self, player_name):
        for player in self.players:
            if player.name == player_name:
                self.players.remove(player)
                break

    def show_players(self):
        for player in self.players:
            player.introduce()

    def show_total_xp(self):
        total_xp = 0
        for player in self.players:
            total_xp += player.xp

        print(f"total XP : {total_xp}")


t1 = Team("T1")
geng = Team("GenG")

t1.add_player("Taehoon")
t1.add_player("Faker")

t1.remove_player("Taehoon")

t1.show_players()
t1.show_total_xp()





from master_deck import master_deck
import random


class Bohnanza:
    def __init__(self, n_players: int) -> None:
        self.n_players = n_players
        self.deck = self.create_deck()
        self.players = {}
        self.round = 0

    def filter_deck(self, deck: list, to_remove: list) -> list:
        """
        Remove specified beans from a provided deck

        Args:
            - deck (list): List of cards representing the deck
            - to_remove (list): List of bean types to remove from a deck
        """
        filtered_deck = []
        for card in deck:
            if card in to_remove:
                continue
            else:
                filtered_deck.append(card)
        return filtered_deck

    def create_deck(self) -> None:
        """
        Create a game deck, accounting for number of players and beans to remove
        """
        # for 3 players, remove cocoa beans
        if self.n_players == 3:
            deck = self.filter_deck(deck=master_deck, to_remove=["cocoa"])
        # for 4 or 5 players, remove coffee beans
        elif self.n_players in [4, 5]:
            deck = self.filter_deck(deck=master_deck, to_remove=["coffee"])
        # for 6 or 7 players, remove coca and garden
        elif self.n_players in [6, 7]:
            deck = self.filter_deck(deck=master_deck, to_remove=["cocoa", "garden"])
        else:
            raise ValueError(f"{self.n_players} players not currently supported.")
        return deck

    def deal(self):
        """
        Deal each player 5 cards to start the game
        """
        # create player instances
        for i in range(self.n_players):
            # if there are less than 3 players, start everyone with 3 fields
            if self.n_players <= 3:
                field = {"field_a": [], "field_b": [], "field_c": []}
            # otherwise start with 2
            else:
                fields = {"field_a": [], "field_b": [], "field_c": None}
            # create each player's dictionary
            self.players[f"player_{i}"] = {"hand": [], "fields": fields, "harvest": []}
        # shuffle the deck
        random.shuffle(self.deck)
        # deal each player 5 cards
        for i in range(5):
            for j in range(self.n_players):
                self.players[f"player_{j}"]["hand"].append(self.deck.pop())

from schedule import *
from metrics import *


class Print:

    @staticmethod
    def printSlots(schedule: Schedule):
        print("\n***Slots:")
        for gameId, slot in schedule.slots.items():
            ids = [player for player in slot.players]
            s = [f"{item:3d}" for item in ids]
            str = ''.join(s)
            print(f"Slot {gameId:2d}: {str}")

    @staticmethod
    def printOpponentsMatrix(schedule: Schedule):
        m = Metrics(schedule)
        matrix = m.calcOpponentsMatrix()

        print("\n*** Opponents matrix:")
        for playerId in range(len(matrix)):
            line = matrix[playerId]
            s = ''.join([f"{v:3d}" for v in line])
            print(f"{playerId:2d}: {s}")

    def printPairsHistogram(schedule : Schedule):
        m = Metrics(schedule)               
        matrix = m.calcOpponentsMatrix()
        
        pairs = {}
        for val in range(schedule.numAttempts + 1):
            pairs[val] = 0

        for playerId in range(len(matrix)):
            line = matrix[playerId]
            for opponentId in range(playerId):
                numGames = line[opponentId]
                pairs[numGames] += 1

        print("\n*** Pairs histogram:")
        for numGames, count in pairs.items():
            if count > 0:
                print(f"{numGames:2d} : {count:3d} pairs")
    
    @staticmethod
    def printGames(schedule: Schedule):
        print("\n***Games:")
        for game in schedule.games:
            ids = [player.id for player in game.players]
            s = [f"{item:3d}" for item in ids]
            str = ''.join(s)
            print(f"Game {game.id:2d}: {str}")

    @staticmethod
    def printScheduleByGames(schedule : Schedule):
        print("\n*** Schedule by games:")
        for round in schedule.rounds:
            print(f"\nRound: {round.id + 1}")
            for game in round.games:
                ids = [player.id for player in game.players]
                s = [f"{item:3d}" for item in ids]
                str = ''.join(s)
                print(f"Game {game.id:2d}: {str}")



    @staticmethod
    def printSeats(schedule: Schedule):
        m = Metrics(schedule)
        print("\n*** Seats matrix:")
        for playerId in range(schedule.configuration.numPlayers):
            seats = m.calcPlayerSeatsHistogram(playerId)
            s = ''.join([f"{v:3d}" for v in seats])
            print(f"{playerId:2d}: {s}")

import unittest
from schedule_factory import *
from schedule import *
from player import *
from game import *

class TestScheduleFactory(unittest.TestCase):
    def test_factory_simple(self):
        '''Simple schedule: 10 players, just 1 game'''

        numPlayers = 10
        participants = Participants(Participants.generateNames(numPlayers))

        conf = Configuration(numPlayers, numTables = 1, numRounds = 1, numGames = 1, numAttempts = 1)
        s = ScheduleFactory.createInitialSchedule(conf, participants)
        self.assertTrue(s.isValid())

    def test_factory_simple_bad(self):
        '''Bad schedule: 11 players, just 1 game'''

        numPlayers = 11
        participants = Participants(Participants.generateNames(numPlayers))

        conf = Configuration(numPlayers, numTables = 1, numRounds = 1, numGames = 1, numAttempts = 1)
        s = ScheduleFactory.createInitialSchedule(conf, participants)
        self.assertFalse(s.isValid())

    def test_factory_rounds2_players10_attempts2(self):
        '''Simple 2-round schedule: 10 players 2 attempts per player'''

        numPlayers = 10
        participants = Participants(Participants.generateNames(numPlayers))

        conf = Configuration(numPlayers, numTables = 1, numRounds = 2, numGames = 2, numAttempts = 2)
        s = ScheduleFactory.createInitialSchedule(conf, participants)
        self.assertTrue(s.isValid())

    def test_factory_rounds2_players20_attempts1(self):
        '''Simple 2-round schedule: 20 players 1 attempts per player'''

        numPlayers = 20
        participants = Participants(Participants.generateNames(numPlayers))

        conf = Configuration(numPlayers, numTables = 1, numRounds = 2, numGames = 2, numAttempts = 1)
        s = ScheduleFactory.createInitialSchedule(conf, participants)
        self.assertTrue(s.isValid())

    def test_factory_tables1_players12(self):
        '''Classic mini-tournament schedule'''

        numPlayers = 12
        participants = Participants(Participants.generateNames(numPlayers))

        conf = Configuration(numPlayers, numTables = 1, numRounds = 6, numGames = 6, numAttempts = 5)
        s = ScheduleFactory.createInitialSchedule(conf, participants)
        self.assertTrue(s.isValid())

    def test_factory_tables2_players20(self):
        '''Full schedule for 2 tables'''

        numPlayers = 20
        participants = Participants(Participants.generateNames(numPlayers))
        conf = Configuration(numPlayers, numTables = 2, numRounds = 10, numGames = 20, numAttempts = 10)

        s = ScheduleFactory.createInitialSchedule(conf, participants)
        self.assertTrue(s.isValid())

    def test_factory_tables2_players25(self):
        '''Not-full schedule for 2 tables (VaWaCa-2017)'''

        numPlayers = 25
        participants = Participants(Participants.generateNames(numPlayers))

        conf = Configuration(numPlayers, numTables = 2, numRounds = 10, numGames = 20, numAttempts = 8)
        s = ScheduleFactory.createInitialSchedule(conf, participants)
        self.assertTrue(s.isValid())

    def test_factory_tables3_players30(self):
        '''Full schedule for 3 tables'''

        numPlayers = 30
        participants = Participants(Participants.generateNames(numPlayers))

        conf = Configuration(numPlayers, numTables = 3, numRounds = 10, numGames = 30, numAttempts = 10)
        s = ScheduleFactory.createInitialSchedule(conf, participants)
        self.assertTrue(s.isValid())

    def test_factory_tables3_players33(self):
        '''Not-full schedule for 3 tables (11 rounds by 10 attempts per player)'''

        numPlayers = 33
        participants = Participants(Participants.generateNames(numPlayers))

        conf = Configuration(numPlayers, numTables = 3, numRounds = 11, numGames = 33, numAttempts = 10)
        s = ScheduleFactory.createInitialSchedule(conf, participants)
        self.assertTrue(s.isValid())

    def test_factory_tables3_players35(self):
        '''Not-full schedule for 3 tables with not all tables at the last round (12 rounds by 10 attempts per player)'''

        numPlayers = 35
        participants = Participants(Participants.generateNames(numPlayers))

        conf = Configuration(numPlayers, numTables = 3, numRounds = 12, numGames = 35, numAttempts = 10)
        s = ScheduleFactory.createInitialSchedule(conf, participants)
        self.assertTrue(s.isValid())

if __name__ == '__main__':
    unittest.main()
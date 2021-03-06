import json
import os.path

from schedule import *

def saveSchedule(schedule: Schedule, fname: str):
    jsonDict = schedule.toJson()
    jsonStr = json.dumps(jsonDict, indent=2)

    home = os.path.expanduser("~")
    filename = os.path.join(home, fname)
    print(f"Saving schedule to: {filename}")
    with open(filename, "w") as f:
        f.write(jsonStr)

def saveParticipants(participants : Participants, fname : str):
    jsonDict = participants.toJson()
    jsonStr = json.dumps(jsonDict, indent=2)

    home = os.path.expanduser("~")
    filename = os.path.join(home, fname)
    print(f"Saving participants to: {filename}")
    with open(filename, "w") as f:
        f.write(jsonStr)

def loadSchedule(fname: str) -> Schedule:
    home = os.path.expanduser("~")
    filename = os.path.join(home, fname)
    print(f"Loading schedule from: {filename}")
    with open(filename, "r") as f:
        s = f.read()
    d = json.loads(s)

    s = Schedule.fromJson(d)
    s.generateSlotsFromGames()
    return s

def loadParticipants(fname: str) -> Participants:
    home = os.path.expanduser("~")
    filename = os.path.join(home, fname)
    print(f"Loading participants from: {filename}")
    with open(filename, "r") as f:
        s = f.read()
    d = json.loads(s)

    participants = Participants.fromJson(d)
    return participants
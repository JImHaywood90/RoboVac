from homeassistant.components.vacuum import VacuumEntityFeature
from .base import RoboVacEntityFeature, RobovacCommand


class T2320:
    homeassistant_features = (
        VacuumEntityFeature.BATTERY
        | VacuumEntityFeature.CLEAN_SPOT
        | VacuumEntityFeature.FAN_SPEED
        | VacuumEntityFeature.LOCATE
        | VacuumEntityFeature.PAUSE
        | VacuumEntityFeature.RETURN_HOME
        | VacuumEntityFeature.SEND_COMMAND
        | VacuumEntityFeature.START
        | VacuumEntityFeature.STATE
        | VacuumEntityFeature.STOP
        | VacuumEntityFeature.MAP
    )
    robovac_features = RoboVacEntityFeature.CLEANING_TIME | RoboVacEntityFeature.CLEANING_AREA | RoboVacEntityFeature.DO_NOT_DISTURB | RoboVacEntityFeature.AUTO_RETURN | RoboVacEntityFeature.ROOM | RoboVacEntityFeature.ZONE | RoboVacEntityFeature.BOOST_IQ | RoboVacEntityFeature.MAP | RoboVacEntityFeature.CONSUMABLES
    commands = {
        RobovacCommand.START_PAUSE: 2,
        RobovacCommand.DIRECTION: {
            "code": 3,
            "values": ["forward", "back", "left", "right"],
        },
        RobovacCommand.MODE: {
            "code": 5,
            "values": ["auto", "SmallRoom", "Spot", "Edge", "Nosweep"],
        },
        RobovacCommand.STATUS: 15,
        RobovacCommand.RETURN_HOME: 101,
        RobovacCommand.FAN_SPEED: {
            "code": 102,
            "values": ["Pure","Standard","Turbo","Max"],
        },
        RobovacCommand.LOCATE: 103,
        RobovacCommand.BATTERY: 104,
        RobovacCommand.ERROR: 106,
        # These commands need codes adding
        # RobovacCommand.CLEANING_AREA: 0,
        # RobovacCommand.CLEANING_TIME: 0,
        # RobovacCommand.AUTO_RETURN: 0,
        # RobovacCommand.DO_NOT_DISTURB: 0,
        # RobovacCommand.BOOST_IQ: 0,
        # RobovacCommand.CONSUMABLES: 0,
    }

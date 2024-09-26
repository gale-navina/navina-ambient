from enum import Enum


class RecordingStatus(str, Enum):
    INITIALIZED = "initialized"
    ACTIVE = "active"
    PAUSED = "paused"
    ENDED = "ended"
    ERROR = "error"


class RecordingAction(str, Enum):
    INITIALIZE = "initialize"
    START = "start"
    PAUSE = "pause"
    RESUME = "resume"
    STOP = "stop"


class ProcessingStatus(str, Enum):
    ACTIVE = "active"
    PAUSED = "paused"
    COMPLETED = "completed"
    FINALIZING = "finalizing"
    ERROR = "error"

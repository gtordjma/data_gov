from enum import Enum


class FileStepStatus(Enum):
    PENDING = 'pending'
    RUNNING = 'running'
    FINISHED = 'finished'
    ERROR = 'error'

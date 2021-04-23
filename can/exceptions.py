"""
There are several specific :class:`Exception` classes to allow user
code to react to specific scenarios related to CAN busses::

    Exception (Python standard library)
     +-- ...
     +-- CanError (python-can)
         +-- CanBackendError
         +-- CanInitializationError
         +-- CanOperationError
         +-- CanTimeoutError

Keep in mind that some functions and methods may raise different exceptions.
For example, validating typical arguments and parameters might result in a
:class:`ValueError`. This should be documented for the function at hand.
"""


class CanError(Exception):
    """Base class for all CAN related exceptions."""


class CanBackEndError(CanError):
    """Indicates an error related to the backend (e.g. driver/OS/library).

    Example scenarios:
      - The interface does not exist
      - The interface is unsupported on the current platform
      - The driver is not present or has the wrong version
    """


class CanInitializationError(CanError):
    """Indicates an error the occurred while initializing a :class:`can.BusABC`.

    Example scenarios:
      - Try to open a non-existent device and/or channel
      - Try to use an invalid setting, which is ok by value, but not ok for the interface
      - The device or other resources are already used
    """


class CanOperationError(CanError):
    """Indicates an error while in operation.

    Example scenarios:
      - A call to a library function results in an unexpected return value
      - An invalid message was received
      - The driver rejected a message that was meant to be sent
      - Cyclic redundancy check (CRC) failed
      - A message remained unacknowledged
    """


class CanTimeoutError(CanError, TimeoutError):
    """Indicates the timeout of an operation.

    Example scenarios:
      - Some message could not be sent after the timeout elapsed
      - No message was read within the given time
    """

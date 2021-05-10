# import pyautogui
# import time
import windows


def open_inventory(local=True, max_attempts=100):
    """
    Opens the inventory provided. If not "local" then remote (using "F" key)
    :param max_attempts: (Number) Maximum times to attempt to open inventory
    :param local: (boolean) open local or remote? (Default=True)
    :return: (boolean) true on success, false on failed after max_attempts
    TODO: implement this
    """
    # as this is a placeholder, we always return true as if it succeeded
    return True


def close_inventory(max_attempts=100):
    """
    Close the currently accessed inventory
    :param max_attempts: (Number) - Max times to attempt to close inventory
    :return: (boolean) false on failed after max_attempts
    TODO: implement this
    """
    return True


def toggle_command_palette(force_open=0):
    """
    Toggles the command palette or sets the given state if "open" is passed
    Example: Open command palette if not already open: input.toggle_command_palette(force_open=True)
    TODO: implement this
    :param force_open: (boolean) if defined, only toggle if state does not match this
    :return: boolean
    """
    # As this is currently a placeholder, we're always going to "pretend" it succeeded
    if windows.is_inventory_open():
        if not close_inventory():
            raise Exception("Failed to close inventory")

    if force_open == 0:
        return True  # Pretend we opened the palette
    else:
        if windows.is_command_palette_open(returns=True) != force_open:
            return True  # Pretend we opened the palette

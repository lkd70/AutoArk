import pyautogui
import time


def is_ark_active():
    """
    :return: bool - True if ark is the active window
    """
    return pyautogui.getActiveWindow().title == "Ark: Survival Evolved"


def wait_for_ark_active(maximum_attempts=100):
    """
    :param maximum_attempts: Attempts before failing - Default: 100
    :return: (boolean) - true once ark is active, false if maximum attempts exceeded
    """
    for x in range(1, maximum_attempts):
        time.sleep(0.1)
        if is_ark_active():
            return True
    return False


def is_inventory_open(returns=True):
    """
    Check if the Ark window shows that an inventory is open
    TODO: implement this
    :param returns: (boolean) - since this is a placeholder this defines the return value
    :return: (boolean)
    """
    return returns


def is_command_palette_open(returns=True):
    """
    Check if the command palette ("tab") is open
    TODO: implement this
    :param returns: (boolean) - Since this is a placeholder this defines the return value
    :return: (boolean)
    """
    return returns

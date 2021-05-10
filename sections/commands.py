import input


def __enter_command(command):
    """
    ;param command: Defines the command we wish to type
    :return: bool - true on success, false if entering command failed
    """
    # Ensure the command palette is open, opening it if needed:
    if not input.toggle_command_palette(force_open=True):
        raise Exception("Failed to ensure the command palette is opened")
    # TODO:Type the 'command' here
    return True


def set_fps(fps=10):
    """
    Sets the desired FPS through the command palette
    :param fps: (Number) FPS desired (Default=10)
    :return: (Boolean) success?
    """
    return __enter_command("t.maxfps=" + str(fps))


def set_gamma(gamma=""):
    """
    Sets gamma to the given value, if not value is provided, default gamma is set
    :param gamma: (String) - (defaults to default gamma)
    :return: (boolean) - success?
    """
    return __enter_command("gamma " + gamma)


def disconnect():
    """
    Disconnects from the current Ark server
    :return: (boolean) - success?
    """
    return __enter_command("disconnect")


def reconnect():
    """
    Reconnects to the currently connected server (disconnect and connect again)
    :return: (boolean) - success?
    """
    return __enter_command("reconnect")


def connect(ip="127.0.0.1", port="7777"):
    """
    Connects to the given IP and PORT (Ark server)
    :param ip: IP address of the desired server - (Default: 127.0.0.1)
    :param port: Game Port of the desired server - (Default: 7777)
    :return: (boolean) - command sent successfully? (Does not check if server connected)
    """
    return __enter_command("open " + ip + ":" + port)


def toggle_display_fps():
    """
    Shows or hides the FPS display in the top corner of the screen
    :return: (boolean) success?
    """
    return __enter_command("stat fps")

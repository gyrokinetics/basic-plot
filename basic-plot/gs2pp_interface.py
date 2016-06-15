"""
.. function:: gs2pp_interface
   :platform: Unix
   :synopsis: Interface used by gs2pp to interact with package.

"""

def gs2pp_interface(command, function, options):
    """
    Controls the behaviour of basic-plot following the gs2pp package guidelines

    Parameters
    ----------

    command : str
        One of the commands defined by the gs2pp package.
    function : str, optional
        A package specific function call.
    options : dict, optional
        Dictionary of options passed directly from the user.
    """



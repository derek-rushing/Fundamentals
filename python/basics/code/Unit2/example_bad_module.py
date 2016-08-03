"""
This module is meant to be written as a very basic what not to do when writing
your module.
"""

class doesntUseProperCasing_AmongOtherThings():
    """
    This class should follow pep8 specifications for naming, and should inherit
    from object. It also doesn't define an __init__ function which is bad
    practice even if unnecessary.
    """

    def someFunction(self):
        """
        Doesn't follow naming convention, and defines another function inside
        of it. In general you should never define a function inside of another
        function unless you can't do what you need otherwise. Privatize the
        inner function instead.
        """

        def some_sub_function():
            """
            This function is fine, but why is it in another function instead of
            being a private function of the class?
            """
            pass

        some_sub_function()
    def bad_spacing(self, param):
        """
        Need a line of space between functions.
        :param param: Naming should be less generic and hopefully give some idea
                      of what the type might be.
        """
        return param # Single line comments should be above the line, not on it

def foo():
    # No doc is a no-no
    print("Unexpected Consequences")

foo() # <- This shouldn't be called here. It's bad form for you to call a
      #    function in a module someone will import without a great reason to.

if __name__ == "__main__":
    # Don't combine scripts and modules. If this might get imported, then why
    # do we have it as a script as well? You aren't saving any trees by tossing
    # everything in 1 file.
    print "I'm a bad module, but don't worry cause I still work" # <- Wrap your print statements with () as that works in both
                                                                 #    Python 2 and 3. Also we are past 80 characters which is
                                                                 #    specified in the pep. (I actually break this all the time because 80 is a little archaic. Break when it makes sense not because you have to worry about someone else's 11" monitor)
from datetime import datetime

class Date:
    def __init__(self):
        """
        Initializes the object by setting the current date and time.

        Parameters:
            self: The object instance.

        Returns:
            None
        """
        self.date = datetime.now()
        
    def getNow(self):
        """
        Get the current date and time.

        Returns:
            datetime: The current date and time.
        """
        return self.date

    def getCurrentYear(self):
        """
        Get the current year.

        Returns:
            int: The current year.
        """
        return self.date.year

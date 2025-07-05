class YCNBCError(Exception):
    """Base exception for ycnbc errors."""
    pass


class DataNotFoundError(YCNBCError):
    """Exception raised when expected data is not found on the page."""
    pass


class ParsingError(YCNBCError):
    """Exception raised when there is an issue parsing the page content."""
    pass

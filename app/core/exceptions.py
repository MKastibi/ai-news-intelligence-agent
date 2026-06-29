class ConfigError(Exception):
    """Raised when required configuration is missing or invalid."""


class APIError(Exception):
    """Raised when an external API call fails."""


class ValidationError(Exception):
    """Raised when input data fails validation."""

import dataclasses
import enum
import logging
import os
from typing import Union

logger = logging.getLogger(__name__)


class Theme(enum.Enum):
    """
    Enumeration for fixed themes represented in the application.
    """

    # These are mapped in `_THEME_MAP` to their respective colors.
    purple = "purple"
    light = "light"
    green = "green"
    red = "red"
    beige = "beige"
    pink = "pink"
    blue = "blue"
    warm_cold = "warm_cold"


@dataclasses.dataclass
class ThemeColors:
    """
    Representation of the colors for a given theme, these values represent hex values such as #FFFFFF and will be mapped
    into the stylesheet at runtime.
    """

    primary: str
    secondary: str


class Stylesheet:
    """
    Class representing a dynamically variable stylesheet that is retrievable using different, constant themes.

    .. note::

        If you are only interested in the default stylesheet, you can use the classmethod `stylesheet` instead:

        >>> style_sheet: str = Stylesheet.get(Theme.purple)
        >>> my_widget.setStylesheet(style_sheet)

    Usage:

    >>> stylesheet = Stylesheet("path/to/the/qss")
    >>> stylesheet_str = stylesheet.get(Theme.purple)
    """

    _PRIMARY_COLOR_KEY = "@@primary_color@@"
    _SECONDARY_COLOR_KEY = "@@secondary_color@@"

    _DEFAULT_STYLESHEET = os.path.join(os.path.dirname(__file__), "style.qss")

    def __init__(self, theme_filepath: str):
        self.theme_filepath = theme_filepath

    @classmethod
    def stylesheet(cls, theme: Theme) -> str:
        instance = cls(cls._DEFAULT_STYLESHEET)
        return instance.get(theme)

    @staticmethod
    def get_colors(theme: Theme) -> ThemeColors:
        """
        Retrieve the colors for the given theme. Defaulting to `Theme.light`.
        """
        try:
            return _THEME_MAP[theme]
        except KeyError:
            # Default to light when no appropriate theme is present
            logger.warning(f"No known color scheme present for theme {str(theme)}, reverting to {str(Theme.light)}")
            return _THEME_MAP[Theme.light]

    def get(self, theme: Union[str, Theme]) -> str:
        """
        Retrieve the stylesheet, remapping any variable colors to the given theme. If the given theme is not found,
        the function defaults to `Theme.light`.

        :param theme: The theme to get the stylesheet as.
        :returns: The stylesheet as a string.
        """

        if isinstance(theme, str):
            try:
                theme = Theme(theme)
            except ValueError:
                logger.warning(f"Unknown theme {theme} passed, reverting to {str(Theme.light)}.")
                theme = Theme.light

        contents = open(self.theme_filepath, "r").readlines()
        colors = self.get_colors(theme)

        for i, line in enumerate(contents):
            if self._PRIMARY_COLOR_KEY in line:
                contents[i] = line.replace(self._PRIMARY_COLOR_KEY, colors.primary)
            elif self._SECONDARY_COLOR_KEY in line:
                contents[i] = line.replace(self._SECONDARY_COLOR_KEY, colors.secondary)

        return "\n".join(contents)


# Global map describing the mapping of themes to their respective color hex codes.
_THEME_MAP = {
    Theme.purple: ThemeColors(primary="#272849", secondary="#B3B9F7"),
    Theme.light: ThemeColors(primary="#DCE2F0", secondary="#50586C"),
    Theme.green: ThemeColors(primary="#2C5F2D", secondary="#FFE77A"),
    Theme.red: ThemeColors(primary="#A4193D", secondary="#FFDFB9"),
    Theme.beige: ThemeColors(primary="#755139", secondary="#F2EDD7"),
    Theme.pink: ThemeColors(primary="#F96167", secondary="#FCE77D"),
    Theme.blue: ThemeColors(primary="#00203F", secondary="#ADEFD1"),
    Theme.warm_cold: ThemeColors(primary="#08BDBD", secondary="#F21B3F"),
}

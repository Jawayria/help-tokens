"""
Django app for linking to help pages with short tokens.
"""

from .context_processor import context_processor

__version__ = '1.1.2'

default_app_config = 'help_tokens.apps.HelpTokensConfig'  # pylint: disable=invalid-name

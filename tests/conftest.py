"""pytest fixtures for ntt.

W0621:redefined-outer-name
  Pylint warns on fixtures (env_path) used as parameter of other
  fixtures (sample_path_in).
"""
# pylint: disable=W0621

from pathlib import Path

import dotenv
import pytest


@pytest.fixture(scope="session")
def env_path():
    """Get the path of the .env file.

    Returns:
        _type_: Path
    """
    ev_path = dotenv.find_dotenv()

    if len(ev_path) == 0:
        raise FileNotFoundError(
            "No .env file found for environment variables"
            )

    return Path(ev_path).parent


@pytest.fixture(scope="session")
def env_dict():
    """Load all .env environment variables in a dictionnary.

    Returns:
        _type_: OrderedDict with variables names as keys and values
    """
    return dotenv.dotenv_values()


@pytest.fixture(scope="session")
def sample_path_in(env_path, env_dict):
    """Get PATH_IN variable from .env file.

    Args:
        env_path (Path): .env containing folder
        env_dict (OrderedDict): environment variables defined in .env

    Raises:
        FileExistsError: If PATH_IN folder does not exist
        UnboundLocalError: If PATH_IN environment variable is not defined

    Returns:
        Path: PATH_IN path
    """
    if 'PATH_IN' in env_dict:
        path_in = env_path / env_dict.get('PATH_IN')

        if not path_in.exists():
            raise FileExistsError(f"{path_in} does not exist")
    else:
        raise UnboundLocalError(
            "Environment variable PATH_IN not defined in .env file"
            )

    return path_in


@pytest.fixture(scope="session")
def sample_path_out(env_path, env_dict):
    """Get PATH_OUT variable from .env file.

    Args:
        env_path (Path): .env containing folder
        env_dict (OrderedDict): environment variables defined in .env

    Raises:
        UnboundLocalError: If PATH_OUT environment variable is not defined

    Returns:
        Path: PATH_OUT path
    """

    if 'PATH_OUT' in env_dict:
        path_out = env_path / env_dict.get('PATH_OUT')

        if not path_out.exists():
            path_out.mkdir()
    else:
        raise UnboundLocalError(
            "Environment variable PATH_OUT not defined in .env file"
            )

    return path_out

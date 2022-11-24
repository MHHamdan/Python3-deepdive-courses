# posts

from .posts import *
from .post import * # relative import .... 

__all_ = (posts.__all__ +
          post.__all__)
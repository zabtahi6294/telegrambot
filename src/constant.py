from utils import create_keyboards
from types import SimpleNamespace



KEYS = SimpleNamespace (**dict(
    Audiowithoutnoises = 'Audio without any background noises',
    Audiowithnoises = 'Audio with background noises',
    KEYBACK = 'Back'
))

KEYBOARDS = SimpleNamespace (**dict(
    main=create_keyboards ([KEYS.Audiowithoutnoises, KEYS.Audiowithnoises]),
    back=create_keyboards ([KEYS.KEYBACK])
))


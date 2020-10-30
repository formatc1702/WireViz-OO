class Part:
    ignore_in_bom: bool = False
    pn: Optional[str]
    mpn: Optional[str]
    manufacturer: Optional[str]

class BomEntry:
    part: Part
    qty: UnitDim
    qty_multiplier: TBD

class UnitDim:
    amount: Union[int, float]  # e.g. 1.2
    unit: str                  # e.g. 'm'

class ColorScheme:
    name: str                    # e.g. 'DIN' for DIN 47100
    color_sequence: List[Color]  # e.g. [WH, BN, GN, YE, ...]

class Image:
    pass  # as already implemented

class Color:
    name: str  # e.g. 'RD', 'rt', 'red'
    hex: str   # e.g. '#FF0000'

class TBD:
    pass  # just a placeholder

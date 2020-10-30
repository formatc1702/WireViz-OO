class Connector(Part):
    pins: List[Pin]
    loops: Optional[List[Loop]]
    image: Optional[Image]

class Pin(Part):
    id: str
    label: Optional[str]
    color: Optional[str]

class Loop:
    pin_from: str
    pin_to: str
    wire: Wire

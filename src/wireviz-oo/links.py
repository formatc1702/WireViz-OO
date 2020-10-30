# Connections should not get passed full objects (risking recursion),
# but rather IDs of the components and their respective ports to be linked.

class Connection:
    # defines the classic connection from connector, via conductor, to connector
    source: Endpoint  # from is a Python keyword
    via: Endpoint
    destination:  Endpoint

class MatePin:
    # defines a mechanical mate from one pin to another
    # see WireViz feature/mate+autogenerate branch
    source: Endpoint
    destination: Endpoint
    shape: str

class MateComponent:
    # defines a mechanical mate from one connector to another
    # see WireViz feature/mate+autogenerate branch
    source: Designator
    destination: Designator
    shape: str

class Endpoint:
    id: Designator
    port: int

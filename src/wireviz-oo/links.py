# Connections should not get passed full objects (risking recursion),
# but rather IDs of the components and their respective ports to be linked.

class Connection:
    # defines the classic connection from connector, via conductor, to connector
    from_id:   Any
    from_port: Any
    via_id:    Any
    via_port:  Any
    to_id:     Any
    to_port:   Any

class MatePin:
    # defines a mechanical mate from one pin to another
    # see WireViz feature/mate+autogenerate branch
    from_id:   Any
    from_port: Any
    to_id:     Any
    to_port:   Any
    shape: str

class MateComponent:
    # defines a mechanical mate from one connector to another
    # see WireViz feature/mate+autogenerate branch
    from_id: Any
    to_name: Any
    shape: str

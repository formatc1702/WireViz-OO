class Conductor(Part):
    id: str
    label: str

class Wire(Conductor):
    gauge: UnitDim

class Tube(Conductor):
    diameter: UnitDim

class TwistedPair:
    members: List[Wire]
    twist_rate: UnitDim

class Group:
    # May be used to group cables/conductors into bundles
    # or wires within a cable.
    # Allows nested groups.
    members: List[Union[
        Cable,
        Group,
        TwistedPair,
        Conductor]]

class ShieldedGroup(Group):
    shield_type: TBD

class Cable(Part):
    id: str
    members: List[Union[
        ShieldedGroup,
        TwistedPair,
        Wire]]
    color_code: Optional[ColorCode]
    pass

# TODO: define a representation/object/syntax for defining
# - cut lenghts
# - strip lengths
# - ...

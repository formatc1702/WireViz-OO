# WireViz-OO

## What this repository is for

- To attempt to create a structured, object-oriented approach to represent the entities found in [WireViz](https://github.com/formatc1702/WireViz):
  - Connectors and pins
  - Cables, wires, and generalizations thereof
  - Connections between these
    - Electrical connections
    - Mechanical mates
- To discuss these features separate from the [main WireViz repository](https://github.com/formatc1702/WireViz)

In the initial stage, the aim is just to collect ideas and build a [non-functional] skeleton of how these elements could be represented.

## What this repository is *not yet* for

- Building working Python Dataclasses
  - In the beginning, not every possible attribute needs to be listed; only the ones needed to define the overall relationships between different classes.
  Detailing can happen over time.
  - Omitting the `@dataclass` decorator for every class reduces noise.
  - Some open points may be marked with `TBD` or other, non-functional references.
- Discussions about the YAML Syntax
  - First, a good internal data representation needs to be found.
  - Afterwards, we can think of how a user might input this data without requiring deep nesting and other complications. A lot of the data structure might get auto-generated, auto-filled and copied internally.
  - The aim would be to not change the existing WireViz syntax too much for simple cases, while adding finer control for more complex projects that cannot be currently represented in WireViz.
- Discussions about rendering the graphical output
  - Rendering multiple nested groups, bundles, etc. might be tricky. But again: first we need to define, what combinations are actually needed.

## What this repository is *definitely not* for

- Discussing general WireViz issues, feature requests, bug reports, etc.
  Please keep these in the [original repo](https://github.com/formatc1702/WireViz/issues).
- This is not a fork of WireViz. It is a separate discussion platform for the issues mentioned above, with the hope of inspiring a future refactoring of WireViz.

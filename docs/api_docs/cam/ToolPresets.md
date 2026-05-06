# ToolPresets
Namespace: adsk.cam
Inherits: Base
Since: April 2023

ToolPresets represents a collection of ToolPreset. It provides access and allows the manipulation like removing and extending the list.

**Accessed from:** Tool.presets

## Methods

### add() -> ToolPreset
Creates and inserts a new Preset at the end of the Preset collection of the owning Tool. The new Preset will have the same values as the owning Tool.
- **Returns** (ToolPreset): Returns the newly created Preset

### [static] classType() -> string
Static function that all classes support that returns the type of the class as a string. The returned string matches the string returned by the objectType property. For example if you have a reference to an object and you want to check if it's a SketchLine you can use myObject.objectType == fusion.SketchLine.classType().
- **Returns** (string): Returns a string indicating the type of the object.

### item(index: uinteger) -> ToolPreset
Get Preset by index.
- **index** (uinteger): Index of the Preset in the owning Tool that should be returned.
- **Returns** (ToolPreset): Returns Preset at by given index, null otherwise

### itemsByName(name: string) -> ToolPreset
Search presets by name. Returns all presets for which the name matches the given pattern. Compare is case insensitive and characters * and ? are used for wild-card matching.
- **name** (string): Name of the Preset to search for. The string can define a pattern with wild-card matching. '*' represents an arbitrary sequence including the empty sequence and '?' represents one arbitrary character.
- **Returns** (ToolPreset): Returns all presets with matching name.

### remove(index: uinteger) -> boolean
Remove Preset by index from the owning Tool.
- **index** (uinteger): Index of the Preset in the Tool that should be removed.
- **Returns** (boolean): Returns true for successful deletion, false otherwise

## Properties

### count : uinteger [read-only]
The number of Presets of the owning Tool.

### isValid : boolean [read-only]
Indicates if this object is still valid, i.e. hasn't been deleted or some other action done to invalidate the reference.

### objectType : string [read-only]
This property is supported by all objects in the API and returns a string that contains the full name (namespace::objecttype) describing the type of the object.

It's often useful to use this in combination with the classType method to see if an object is a certain type. For example: if obj.objectType == adsk.core.Point3D.classType():

## Samples
- **Manufacturing Workflow API Sample**: Manufacturing Workflow API Sample
This sample script starts by creating a simple component which is then used to describe a milling workflow. It creates a setup, a few operations, pick some tools from a Fusion sample tool library using loops and queries and ends up post-processing the operations out using an NC Program.

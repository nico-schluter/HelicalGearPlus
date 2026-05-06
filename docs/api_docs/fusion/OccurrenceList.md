# OccurrenceList
Namespace: adsk.fusion
Inherits: Base
Since: August 2014

Provides a list of occurrences.

**Accessed from:** BaseComponent.allOccurrences, BaseComponent.allOccurrencesByComponent, BaseComponent.occurrencesByComponent, Component.allOccurrences, Component.allOccurrencesByComponent, Component.occurrencesByComponent, FlatPatternComponent.allOccurrences, FlatPatternComponent.allOccurrencesByComponent, FlatPatternComponent.occurrencesByComponent, Occurrence.childOccurrences, Occurrences.asList, RigidGroup.occurrences

## Methods

### [static] classType() -> string
Static function that all classes support that returns the type of the class as a string. The returned string matches the string returned by the objectType property. For example if you have a reference to an object and you want to check if it's a SketchLine you can use myObject.objectType == fusion.SketchLine.classType().
- **Returns** (string): Returns a string indicating the type of the object.

### item(index: uinteger) -> Occurrence
Returns the specified occurrence using an index into the collection.
- **index** (uinteger): The index of the occurrence within the collection to return. The first item has an index of 0.
- **Returns** (Occurrence): Returns the specified occurrence or null in the case of an invalid index.

### itemByName(name: string) -> Occurrence
Returns the specified occurrence using the name of the occurrence.
- **name** (string): The name of the occurrence to return.
- **Returns** (Occurrence): Returns the occurrence or null if an invalid name was specified

## Properties

### count : uinteger [read-only]
Returns the number of occurrences in the collection.

### isValid : boolean [read-only]
Indicates if this object is still valid, i.e. hasn't been deleted or some other action done to invalidate the reference.

### objectType : string [read-only]
This property is supported by all objects in the API and returns a string that contains the full name (namespace::objecttype) describing the type of the object.

It's often useful to use this in combination with the classType method to see if an object is a certain type. For example: if obj.objectType == adsk.core.Point3D.classType():

## Samples
- **Assembly traversal using recursion API Sample**: Traverses the entire structure of the currently open assemlby using a recursive function and displays the result in a message box. This will match the occurrence structure seen in the browser.
- **Create Setups From Hole Recognition API Sample**: This sample script demonstrates how to create a correctly oriented setup using Hole Recognition functionality.
The Fusion Manufacturing Extension is required for Hole Recognition.
The script starts by opening a sample model from the CAM Samples folder via its URN. The model comprises a 3 way coupling containing holes in various orientations and mounted on a fixture. A reference setup is created for the model using a simple stock mode and offsets. The Hole Recognition feature of the Fusion Manufacturing Extension creates 5 hole groups containing 11 holes between them. For each unique hole group vector captured, a new setup is created and its orientation transformed to match the vector.
- **Get Volume of Active Design API Sample**: Traverses through the active design and totals the volume of every body within the design.
- **Set Vise Origin As Setup WCS Origin API Sample**: This sample script demonstrates how to define our setup WCS origin relative to our vise origin from either a component, a sketch point or a joint origin.
The Work Coordinate System is a reference point set in our CAM workspace and on our machine. All machine coordinates are drawn from the WCS. This script demonstrates defining the WCS by each of 4 alternative methods:
Setup by default with no origin defined.
Setup using vise origin as WCS origin.
Setup using a sketch point as WCS origin.
Setup using a joint origin as WCS origin.

# GraphNodeProperties
Namespace: adsk.volume
Inherits: Base
Since: May 2025

A collection of properties of a graph node.

**Accessed from:** GraphNode.properties

## Methods

### [static] classType() -> string
Static function that all classes support that returns the type of the class as a string. The returned string matches the string returned by the objectType property. For example if you have a reference to an object and you want to check if it's a SketchLine you can use myObject.objectType == fusion.SketchLine.classType().
- **Returns** (string): Returns a string indicating the type of the object.

### item(index: uinteger) -> GraphNodeProperty
Function that returns the specified property using an index into the collection.
- **index** (uinteger): The index of the item within the collection to return. The first item in the collection has an index of 0.
- **Returns** (GraphNodeProperty): Returns the specified item or null if an invalid index was specified.

### itemByName(propertyName: string) -> GraphNodeProperty
Returns the property with the specified internal name.
- **propertyName** (string): The id of the property.
- **Returns** (GraphNodeProperty): Returns the specified property or null in the case where there is no property with the specified id.

## Properties

### count : uinteger [read-only]
The number of items in the collection.

### isValid : boolean [read-only]
Indicates if this object is still valid, i.e. hasn't been deleted or some other action done to invalidate the reference.

### objectType : string [read-only]
This property is supported by all objects in the API and returns a string that contains the full name (namespace::objecttype) describing the type of the object.

It's often useful to use this in combination with the classType method to see if an object is a certain type. For example: if obj.objectType == adsk.core.Point3D.classType():

## Samples
- **Volumetric Custom Feature API Sample**: Demonstrates how to create a Volumetric Custom Feature using the API for graph creation.


To run the sample script, have a document open in Fusion’s DESIGN workspace. This script will create a component with a box by sketching then extruding that sketch. It will then use that box as a boundary body and create a Volumetric Custom Feature.


The script will the create a gyroid lattice using the Volumetric Model API with the appropriate Graphs, Nodes and Connections for a minimal example. Finally, the script will convert that Volumetric Model to Mesh using the API and the VolumetricModelToMeshFeature.

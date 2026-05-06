# BRepCell
Namespace: adsk.fusion
Inherits: Base
Since: June 2015

Object that represents an existing BRepCell.

**Accessed from:** BRepCells.item

## Methods

### [static] classType() -> string
Static function that all classes support that returns the type of the class as a string. The returned string matches the string returned by the objectType property. For example if you have a reference to an object and you want to check if it's a SketchLine you can use myObject.objectType == fusion.SketchLine.classType().
- **Returns** (string): Returns a string indicating the type of the object.

## Properties

### cellBody : BRepBody [read-only]
Returns a BRepBody that represents this cell. This is a transient B-Rep body.

### isSelected : boolean [read-write]
Gets and sets whether the cell is selected. For a Trim feature a selected cell is removed, whereas for a boundary fill feature, a selected cell is kept and used in the feature operation.

### isValid : boolean [read-only]
Indicates if this object is still valid, i.e. hasn't been deleted or some other action done to invalidate the reference.

### objectType : string [read-only]
This property is supported by all objects in the API and returns a string that contains the full name (namespace::objecttype) describing the type of the object.

It's often useful to use this in combination with the classType method to see if an object is a certain type. For example: if obj.objectType == adsk.core.Point3D.classType():

### sourceTools : ObjectCollection [read-only]
Returns the tools that we're using in the definition of this cell.

## Samples
- **boundaryFillFeatures.add**: Demonstrates the boundaryFill.add method. To use this sample you need to have two existing overlapping bodies. You'll be prompted to select the bodies when running the script.
- **Boundary Fill Feature API Sample**: Demonstrates creating a new boundary fill feature.
- **Trim Feature API Sample**: Demonstrates creating a new trim feature.

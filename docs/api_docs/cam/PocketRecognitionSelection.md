# PocketRecognitionSelection
Namespace: adsk.cam
Inherits: CurveSelection
Since: July 2023

Pocket type curve selection. It searches for pockets matching the criteria on the selected bodies The result of the value property call may contain duplicates. See also RecognizedPockets for the ability to analyze the pockets

**Accessed from:** CurveSelections.createNewPocketRecognitionSelection

## Methods

### [static] classType() -> string
Static function that all classes support that returns the type of the class as a string. The returned string matches the string returned by the objectType property. For example if you have a reference to an object and you want to check if it's a SketchLine you can use myObject.objectType == fusion.SketchLine.classType().
- **Returns** (string): Returns a string indicating the type of the object.

## Properties

### areHolesIncluded : boolean [read-write]
Flag to interpret holes as pockets.

### error : string [read-only]
Gets the last warning string encountered after the selection was applied to a parent.

### hasError : boolean [read-only]
Gets if errors were encountered when applying the selection to a a parent.

### hasWarning : boolean [read-only]
Gets if warnings were encountered when applying the selection to a parent.

### inputGeometry : array [read-write]
Get or set the value of the input geometry. If the value originates from a component instead of an occurrence, or an occurrence outside of the CAM environment, then the subpath is checked against the CAM model tree. For some child classes, this may be the same as the value property, but might also consist of fewer elements. Valid elements depend on the capabilities of the derived class. An exception is thrown if the matching fails or the given entity does not match the expected type.

### isSetupModelSelected : boolean [read-write]
Flag to include all B-Rep bodies set as the setup models.

### isValid : boolean [read-only]
Indicates if this object is still valid, i.e. hasn't been deleted or some other action done to invalidate the reference.

### maximumCornerRadius : double [read-write]
The largest corner radius that can appear in a pocket to machine.

### maximumPocketDepth : double [read-write]
The deepest pocket (measured from top to bottom) to machine.

### minimumCornerRadius : double [read-write]
The smallest corner radius that can appear in a pocket to machine.

### minimumHoleDiameter : double [read-write]
Lower bound for the diameter for the hole detection. It can only be set if areHoldeIncluded is set to true.

### minimumPocketDepth : double [read-write]
The shallowest pocket (measured from top to bottom) to machine.

### objectType : string [read-only]
This property is supported by all objects in the API and returns a string that contains the full name (namespace::objecttype) describing the type of the object.

It's often useful to use this in combination with the classType method to see if an object is a certain type. For example: if obj.objectType == adsk.core.Point3D.classType():

### value : array [read-only]
Returns the resulting value of the selection. In general, this returns the input selection, but child classes can override the return value if needed. Refer to the child classes comments for further details. The collection may contain duplicates. For OperationInputs, the return value may not be the same as for Operations, as additional geometry selected by child classes is not evaluated for OperationInputs.

### warning : string [read-only]
Gets the last warning string encountered after the selection was applied to a parent.

## Samples
- **Hole and Pocket Recognition API Sample**: This sample script demonstrates three different methods for feature recognition: one for holes and two for pockets.
The script starts by creating a simple component which is then used to demonstrate the three methods. After the features are recognised they are coloured and milling and drilling operations are created for each feature.
RecognizedHoleGroup returns a list of BRepFaces that can be used as selections for the drilling operation. RecognizedPocket also return some BRepFaces but it needs additional processing before the output can be used for creating machining operations.
The sample script demonstrates a couple of different methods, including finding the pocket BRepFaces and creating sketches from the recognized pockets.
This script works only if the Manufacturing Extension is active.

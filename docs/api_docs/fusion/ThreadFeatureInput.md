# ThreadFeatureInput
Namespace: adsk.fusion
Inherits: Base
Since: January 2015

This class defines the methods and properties that pertain to the definition of a thread feature.

**Accessed from:** ThreadFeatures.createInput

## Methods

### [static] classType() -> string
Static function that all classes support that returns the type of the class as a string. The returned string matches the string returned by the objectType property. For example if you have a reference to an object and you want to check if it's a SketchLine you can use myObject.objectType == fusion.SketchLine.classType().
- **Returns** (string): Returns a string indicating the type of the object.

## Properties

### inputCylindricalFace : BRepFace [read-write]
Gets and sets the threaded face. In the case where there are multiple faces, only the first one is returned. Setting this results in a thread being applied to only a single face. It is recommended that you use the inputCylindricalfaces property in order to have full access to the collection of faces to be threaded.

### inputCylindricalFaces : ObjectCollection [read-write]
Gets and sets the cylindrical input faces.

### isFullLength : boolean [read-write]
Gets and sets if this thread is the full length of the cylinder. It defaults to true.

### isModeled : boolean [read-write]
Gets and sets if the thread is physical or cosmetic thread. A value of true indicates a physical thread. It defaults to false.

### isRightHanded : boolean [read-write]
This function is retired. See more information in the 'Remarks' section below.

Gets and sets if the thread is right or left-handed thread. A value of true indicates a right-handed thread. It defaults to true.

### isValid : boolean [read-only]
Indicates if this object is still valid, i.e. hasn't been deleted or some other action done to invalidate the reference.

### objectType : string [read-only]
This property is supported by all objects in the API and returns a string that contains the full name (namespace::objecttype) describing the type of the object.

It's often useful to use this in combination with the classType method to see if an object is a certain type. For example: if obj.objectType == adsk.core.Point3D.classType():

### targetBaseFeature : BaseFeature [read-write]
When creating a feature that is owned by a base feature, set this property to the base feature you want to associate the new feature with. By default, this is null, meaning it will not be associated with a base feature.

Because of a current limitation, if you want to create a feature associated with a base feature, you must set this property AND call the startEdit method of the base feature, create the feature, and then call the finishEdit method of the base feature. The base feature must be in an "edit" state to be able to add any additional items to it.

### threadInfo : ThreadInfo [read-write]
Gets and sets the information that defines the thread.

### threadLength : ValueInput [read-write]
Gets and sets the thread length. It is only used in the case where the isFullLength property is false.

### threadLocation : ThreadLocations [read-write]
Gets and sets which end of the cylinder the thread is measured from when it's not full length. The thread position and length can be measured from either the "low" or "high" end. You can determine the low and high end by using the Cylinder associated with the cylindrical BRepFace the thread is being added to. The BRepFace.geometry which will return a Cylinder object. The axis property of the Cylinder is a vector and the high end of the cylinder is at the far end of the cylinder with respect to the axis vector.

This property is only used in the case where the isFullLength property is false and is otherwise ignored. It defaults to creating a thread at the high end.

### threadOffset : ValueInput [read-write]
Gets and sets the thread offset. The offset is the distance along the axis of the cylinder from the edge to the start of the thread. It is only used in the case where the isFullLength property is false. Returns nothing in the case where the feature is non-parametric.

## Samples
- **Thread Feature API Sample**: Demonstrates creating a new thread feature.

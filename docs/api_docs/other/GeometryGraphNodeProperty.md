# GeometryGraphNodeProperty
Namespace: adsk.volume
Inherits: GraphNodeProperty
Since: May 2025

A property value that represents a link to a geometric object.

## Methods

### [static] classType() -> string
Static function that all classes support that returns the type of the class as a string. The returned string matches the string returned by the objectType property. For example if you have a reference to an object and you want to check if it's a SketchLine you can use myObject.objectType == fusion.SketchLine.classType().
- **Returns** (string): Returns a string indicating the type of the object.

## Properties

### beamNetwork : BeamNetwork [read-write]
Set the value of the property. The value should be a BeamNetwork object, which defines the geometry by defining vertices, beams and radii of the beams.

### customSDFCallbackID : string [read-write]
The ID of a custom Signed Distance Field callback object registered with CustomSDFCallbackRegistry. Setting this will override any CAD geometry set previously.

### description : string [read-only]
Returns the description of this property. This description is localized and can change based on the current language.

### isValid : boolean [read-only]
Indicates if this object is still valid, i.e. hasn't been deleted or some other action done to invalidate the reference.

### name : string [read-only]
Gets the internal name of the property.

### objectType : string [read-only]
This property is supported by all objects in the API and returns a string that contains the full name (namespace::objecttype) describing the type of the object.

It's often useful to use this in combination with the classType method to see if an object is a certain type. For example: if obj.objectType == adsk.core.Point3D.classType():

### value : array [read-write]
Get or set the value of the property. This should be one or more CAD geometry objects, such as a BREP or mesh bodies, faces or sketch curves. Setting this will override any value set by customSDFCallbackID.

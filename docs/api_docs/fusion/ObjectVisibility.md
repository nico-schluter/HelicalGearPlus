# ObjectVisibility
Namespace: adsk.fusion
Inherits: Base
Since: November 2025

An object that provides control over which objects are displayed in the graphics window. This is the equivalent of the "Object Visibility" settings in the Display Settings drop-down in the navigation toolbar at the bottom of the Fusion graphics window.

**Accessed from:** Design.objectVisibility, FlatPatternProduct.objectVisibility, WorkingModel.objectVisibility

## Methods

### [static] classType() -> string
Static function that all classes support that returns the type of the class as a string. The returned string matches the string returned by the objectType property. For example if you have a reference to an object and you want to check if it's a SketchLine you can use myObject.objectType == fusion.SketchLine.classType().
- **Returns** (string): Returns a string indicating the type of the object.

## Properties

### isAllObjectsVisible : boolean [read-write]
Sets if all objects are visible or hidden. When setting this property it will set the value of all other properties of this object to true or false. When getting this property, if it is true, then all other properties are true. If false, one or more other properties are false.

### isJointOriginAxesVisible : boolean [read-write]
Gets and sets if the axes lines shown in the glyphs for joint origins in all components, local or referenced by this design, are visible in the graphics window.

### isJointOriginsVisible : boolean [read-write]
Gets and sets if the glyphs for joint origins in all components, local or referenced by this design, are visible in the graphics window.

### isJointsVisible : boolean [read-write]
Gets and sets if the glyphs for joints in all components, local or referenced by this design, are visible.

### isOriginAxesVisible : boolean [read-write]
Gets and sets if the origin construction axes of all components, local or referenced by this design, are visible in the graphics window.

### isOriginPlanesVisible : boolean [read-write]
Gets and sets if the origin construction planes of all components, local or referenced by this design, are visible in the graphics window.

### isOriginPointsVisible : boolean [read-write]
Gets and sets if the origin construction points of all components, local or referenced by this design, are visible in the graphics window.

### isSketchesVisible : boolean [read-write]
Gets and sets if the sketches in all components, local or referenced by this design, are visible in the graphics window.

### isUserWorkAxesVisible : boolean [read-write]
Gets and sets if the user created construction axes of all components, local or referenced by this design, are visible in the graphics window.

### isUserWorkPlanesVisible : boolean [read-write]
Gets and sets if the user created construction planes of all components, local or referenced by this design, are visible in the graphics window.

### isUserWorkPointsVisible : boolean [read-write]
Gets and sets if the user created construction points of all components, local or referenced by this design, are visible in the graphics window.

### isValid : boolean [read-only]
Indicates if this object is still valid, i.e. hasn't been deleted or some other action done to invalidate the reference.

### objectType : string [read-only]
This property is supported by all objects in the API and returns a string that contains the full name (namespace::objecttype) describing the type of the object.

It's often useful to use this in combination with the classType method to see if an object is a certain type. For example: if obj.objectType == adsk.core.Point3D.classType():

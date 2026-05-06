# AreaProperties
Namespace: adsk.fusion
Inherits: Base
Since: March 2016

The Area properties of a sketch profile or planar surface.

**Accessed from:** Design.areaProperties, FlatPatternProduct.areaProperties, Profile.areaProperties, WorkingModel.areaProperties

## Methods

### [static] classType() -> string
Static function that all classes support that returns the type of the class as a string. The returned string matches the string returned by the objectType property. For example if you have a reference to an object and you want to check if it's a SketchLine you can use myObject.objectType == fusion.SketchLine.classType().
- **Returns** (string): Returns a string indicating the type of the object.

### getCentroidMomentsOfInertia(ixx: double, iyy: double, izz: double, ixy: double, iyz: double, ixz: double) -> boolean
Method that returns the moments of inertia about the centroid. Unit for returned values is kg*cm^2.
- **ixx** (double): Output Double that returns the XX partial moment.
- **iyy** (double): Output Double that returns the YY partial moment.
- **izz** (double): Output Double that returns the ZZ partial moment.
- **ixy** (double): Output Double that returns the XY partial moment.
- **iyz** (double): Output Double that returns the YZ partial moment.
- **ixz** (double): Output Double that returns the XZ partial moment.
- **Returns** (boolean): Returns true if successful

### getMomentsOfInertia(ixx: double, iyy: double, izz: double, ixy: double, iyz: double, ixz: double) -> boolean
Method that, for a sketch, returns the moments of inertia about the sketch origin. For a planar face, this method returns the moments about the world coordinate system origin. Unit for returned values is kg*cm^2.
- **ixx** (double): Output Double that returns the XX partial moment.
- **iyy** (double): Output Double that returns the YY partial moment.
- **izz** (double): Output Double that returns the ZZ partial moment.
- **ixy** (double): Output Double that returns the XY partial moment.
- **iyz** (double): Output Double that returns the YZ partial moment.
- **ixz** (double): Output Double that returns the XZ partial moment.
- **Returns** (boolean): Returns true if successful

### getPrincipalAxes(xAxis: Vector3D, yAxis: Vector3D) -> boolean
Method that returns the principal axes.
- **xAxis** (Vector3D): The output Vector3D object that indicates the direction of the x axis.
- **yAxis** (Vector3D): The output Vector3D object that indicates the direction of the y axis.
- **Returns** (boolean): Returns true if successful

### getPrincipalMomentsOfInertia(i1: double, i2: double, i3: double) -> boolean
Method that returns the moments of inertia about the principal axes. Unit for returned values is kg*cm^2.
- **i1** (double): Output Double that specifies the first moment of inertia.
- **i2** (double): Output Double that specifies the second moment of inertia.
- **i3** (double): Output Double that specifies the third moment of inertia.
- **Returns** (boolean): Returns true if successful

### getRadiusOfGyration(kxx: double, kyy: double, kzz: double) -> boolean
Method that returns the radius of gyration about the principal axes. Unit for returned values is cm.
- **kxx** (double): Output Double that returns the X partial radius of gyration.
- **kyy** (double): Output Double that returns the Y partial radius of gyration.
- **kzz** (double): Output Double that returns the Z partial radius of gyration.
- **Returns** (boolean): Returns true if successful

## Properties

### accuracy : CalculationAccuracy [read-only]
Returns the accuracy that was used for the calculation.

### area : double [read-only]
Gets the area in the square centimeters.

### centroid : Point3D [read-only]
Gets the centroid where the units are centimeters. The Location is relative to the sketch origin for a profile or relative to the world coordinate system for a planar face.

### isValid : boolean [read-only]
Indicates if this object is still valid, i.e. hasn't been deleted or some other action done to invalidate the reference.

### objectType : string [read-only]
This property is supported by all objects in the API and returns a string that contains the full name (namespace::objecttype) describing the type of the object.

It's often useful to use this in combination with the classType method to see if an object is a certain type. For example: if obj.objectType == adsk.core.Point3D.classType():

### perimeter : double [read-only]
Gets the perimeter in centimeters. The perimeter is the sum of the length of all the curves or edges of the profile or planar surface

### rotationToPrincipal : double [read-only]
Gets the angle of rotation of the principal axes.

## Samples
- **API Sample for AreaProperties**: Demonstrates how to use AreaProperties
- **Patch Feature API Sample**: Demonstrates creating a new patch feature.

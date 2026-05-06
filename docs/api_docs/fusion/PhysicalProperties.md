# PhysicalProperties
Namespace: adsk.fusion
Inherits: Base
Since: September 2015

The physical properties of a Component, Occurrence or BRepBody

**Accessed from:** BRepBody.getPhysicalProperties, BRepBody.physicalProperties, Component.getPhysicalProperties, Component.physicalProperties, Design.physicalProperties, FlatPatternComponent.getPhysicalProperties, FlatPatternComponent.physicalProperties, FlatPatternProduct.physicalProperties, Occurrence.getPhysicalProperties, Occurrence.physicalProperties, WorkingModel.physicalProperties

## Methods

### [static] classType() -> string
Static function that all classes support that returns the type of the class as a string. The returned string matches the string returned by the objectType property. For example if you have a reference to an object and you want to check if it's a SketchLine you can use myObject.objectType == fusion.SketchLine.classType().
- **Returns** (string): Returns a string indicating the type of the object.

### getPrincipalAxes(xAxis: Vector3D, yAxis: Vector3D, zAxis: Vector3D) -> boolean
Method that returns the principal axes.
- **xAxis** (Vector3D): The output Vector3D object that indicates the direction of the x axis.
- **yAxis** (Vector3D): The output Vector3D object that indicates the direction of the y axis.
- **zAxis** (Vector3D): The output Vector3D object that indicates the direction of the z axis.
- **Returns** (boolean): Returns true if successful

### getPrincipalMomentsOfInertia(i1: double, i2: double, i3: double) -> boolean
Method that returns the moments of inertia about the principal axes. Unit for returned values is kg*cm^2.
- **i1** (double): Output Double that specifies the first moment of inertia.
- **i2** (double): Output Double that specifies the second moment of inertia.
- **i3** (double): Output Double that specifies the third moment of inertia.
- **Returns** (boolean): Returns true if successful

### getRadiusOfGyration(kx: double, ky: double, kz: double) -> boolean
Method that returns the radius of gyration about the principal axes. Unit for returned values is cm.
- **kx** (double): Output Double that returns the X partial radius of gyration.
- **ky** (double): Output Double that returns the Y partial radius of gyration.
- **kz** (double): Output Double that returns the Z partial radius of gyration.
- **Returns** (boolean): Returns true if successful

### getRotationToPrincipal(rx: double, ry: double, rz: double) -> boolean
Gets the rotation from the world coordinate system of the target to the principal coordinate system.
- **Returns** (boolean): Returns true if successful

### getXYZMomentsOfInertia(xx: double, yy: double, zz: double, xy: double, yz: double, xz: double) -> boolean
Method that gets the moment of inertia about the world coordinate system. Unit for returned values is kg*cm^2.
- **xx** (double): Output Double that returns the XX partial moment.
- **yy** (double): Output Double that returns the YY partial moment.
- **zz** (double): Output Double that returns the ZZ partial moment.
- **xy** (double): Output Double that returns the XY partial moment.
- **yz** (double): Output Double that returns the YZ partial moment.
- **xz** (double): Output Double that returns the XZ partial moment.
- **Returns** (boolean): Returns true if successful

## Properties

### accuracy : CalculationAccuracy [read-only]
Returns the accuracy that was used for the calculation.

### area : double [read-only]
Gets the area in square centimeters.

### centerOfMass : Point3D [read-only]
Returns the center of mass position

### density : double [read-only]
Gets the density in kilograms per cubic centimeter.

### isValid : boolean [read-only]
Indicates if this object is still valid, i.e. hasn't been deleted or some other action done to invalidate the reference.

### mass : double [read-only]
Gets the mass in kilograms.

### objectType : string [read-only]
This property is supported by all objects in the API and returns a string that contains the full name (namespace::objecttype) describing the type of the object.

It's often useful to use this in combination with the classType method to see if an object is a certain type. For example: if obj.objectType == adsk.core.Point3D.classType():

### volume : double [read-only]
Gets the volume in the cubic centimeters.

## Samples
- **Get Physical Properties API Sample**: Script that demonstrates getting physical properties using the API. When this script is run it will create a new document, build a simple model, and get the various physical properties from the model.

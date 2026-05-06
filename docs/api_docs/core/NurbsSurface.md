# NurbsSurface
Namespace: adsk.core
Inherits: Surface
Since: August 2014

Transient NURBS surface. A transient NURBS surface is not displayed or saved in a document. A transient NURBS surface is used as a wrapper to work with raw NURBS surface information. A transient NURBS surface is bounded by it's natural boundaries and does not support the definition of arbitrary boundaries. A NURBS surface is typically obtained from a BREPFace object, which does have boundary information. They are created statically using the create method of the NurbsSurface class.

**Accessed from:** NurbsSurface.copy, NurbsSurface.create

## Methods

### [static] classType() -> string
Static function that all classes support that returns the type of the class as a string. The returned string matches the string returned by the objectType property. For example if you have a reference to an object and you want to check if it's a SketchLine you can use myObject.objectType == fusion.SketchLine.classType().
- **Returns** (string): Returns a string indicating the type of the object.

### copy() -> NurbsSurface
Creates and returns an independent copy of this NurbsSurface object.
- **Returns** (NurbsSurface): Returns a new NurbsSurface object that is a copy of this NurbsSurface object.

### create(degreeU: integer, degreeV: integer, controlPointCountU: integer, controlPointCountV: integer, controlPoints: Point3D[], knotsU: double[], knotsV: double[], weights: double[], propertiesU: NurbsSurfaceProperties, propertiesV: NurbsSurfaceProperties) -> NurbsSurface
Creates a transient NURBS surface object.
- **degreeU** (integer): The degree in the U direction.
- **degreeV** (integer): The degree in the V direction.
- **controlPointCountU** (integer): The number of control points in the U direction.
- **controlPointCountV** (integer): The number of control points in the V direction.
- **controlPoints** (Point3D[]): An array of surface control points. The length of this array must be controlPointCountU * controlPointCountV.
- **knotsU** (double[]): The knot vector for the U direction.
- **knotsV** (double[]): The knot vector for the V direction.
- **weights** (double[]): An array of weights that corresponds to the control points of the surface.
- **propertiesU** (NurbsSurfaceProperties): The properties (NurbsSurfaceProperties) of the surface in the U direction.
- **propertiesV** (NurbsSurfaceProperties): The properties (NurbsSurfaceProperties) of the surface in the V direction.
- **Returns** (NurbsSurface): Returns the new NurbsSurface object or null if the creation failed.

### getData(degreeU: integer, degreeV: integer, controlPointCountU: integer, controlPointCountV: integer, controlPoints: Point3D[], knotsU: double[], knotsV: double[], weights: double[], propertiesU: NurbsSurfaceProperties, propertiesV: NurbsSurfaceProperties) -> boolean
Gets the data that defines the NURBS surface.
- **degreeU** (integer): The output degree in the U direction.
- **degreeV** (integer): The output degree in the V direction.
- **controlPointCountU** (integer): The output number of control points in the U direction.
- **controlPointCountV** (integer): The output number of control points in the V direction.
- **controlPoints** (Point3D[]): An output array of surface control points.
- **knotsU** (double[]): The output knot vector for the U direction.
- **knotsV** (double[]): The output knot vector for the V direction.
- **weights** (double[]): An output array of weights that corresponds to the control points of the surface.
- **propertiesU** (NurbsSurfaceProperties): The output properties (NurbsSurfaceProperties) of the surface in the U direction.
- **propertiesV** (NurbsSurfaceProperties): The output properties (NurbsSurfaceProperties) of the surface in the V direction.
- **Returns** (boolean): Returns true if successful.

### set(degreeU: integer, degreeV: integer, controlPointCountU: integer, controlPointCountV: integer, controlPoints: Point3D[], knotsU: double[], knotsV: double[], weights: double[], propertiesU: NurbsSurfaceProperties, propertiesV: NurbsSurfaceProperties) -> boolean
Sets the data that defines the NURBS surface.
- **degreeU** (integer): The degree in the U direction.
- **degreeV** (integer): The degree in the V direction.
- **controlPointCountU** (integer): The number of control points in the U direction.
- **controlPointCountV** (integer): The number of control points in the V direction.
- **controlPoints** (Point3D[]): An array of surface control points.
- **knotsU** (double[]): The knot vector for the U direction.
- **knotsV** (double[]): The knot vector for the V direction.
- **weights** (double[]): An array of weights that corresponds to the control points of the surface.
- **propertiesU** (NurbsSurfaceProperties): The properties (NurbsSurfaceProperties) of the surface in the U direction.
- **propertiesV** (NurbsSurfaceProperties): The properties (NurbsSurfaceProperties) of the surface in the V direction.
- **Returns** (boolean): Returns true if successful

### transformBy(matrix: Matrix3D) -> boolean
Updates this surface by transforming it with a given input matrix.
- **matrix** (Matrix3D): A 3D matrix that defines the transform to apply to the surface.
- **Returns** (boolean): Returns true if the transform was successful.

## Properties

### controlPointCountU : integer [read-only]
Gets the number of control points in the U direction.

### controlPointCountV : integer [read-only]
Gets the number of control points in the V direction.

### controlPoints : array [read-only]
Gets an array of control points from the surface.

### degreeU : integer [read-only]
Gets the degree in the U direction.

### degreeV : integer [read-only]
Gets the degree in the V direction.

### evaluator : SurfaceEvaluator [read-only]
Returns the surface evaluator.

### isValid : boolean [read-only]
Indicates if this object is still valid, i.e. hasn't been deleted or some other action done to invalidate the reference.

### knotCountU : integer [read-only]
Gets the knot count in the U direction.

### knotCountV : integer [read-only]
Gets thekKnot count in the V direction.

### knotsU : array [read-only]
Get the knot vector from the U direction.

### knotsV : array [read-only]
Get the knot vector from the V direction

### objectType : string [read-only]
This property is supported by all objects in the API and returns a string that contains the full name (namespace::objecttype) describing the type of the object.

It's often useful to use this in combination with the classType method to see if an object is a certain type. For example: if obj.objectType == adsk.core.Point3D.classType():

### propertiesU : NurbsSurfaceProperties [read-only]
Gets the properties (NurbsSurfaceProperties) of the surface in the U direction.

### propertiesV : NurbsSurfaceProperties [read-only]
Gets the properties (NurbsSurfaceProperties) of the surface in the V direction.

### surfaceType : SurfaceTypes [read-only]
Returns the surface type.

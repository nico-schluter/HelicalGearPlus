# CustomGraphicsCoordinates
Namespace: adsk.fusion
Inherits: Base
Since: September 2017

Represents coordinates that are used to define vertices in custom graphics.

**Accessed from:** CustomGraphicsCoordinates.create, CustomGraphicsLines.coordinates, CustomGraphicsMesh.coordinates, CustomGraphicsPointSet.coordinates

## Methods

### [static] classType() -> string
Static function that all classes support that returns the type of the class as a string. The returned string matches the string returned by the objectType property. For example if you have a reference to an object and you want to check if it's a SketchLine you can use myObject.objectType == fusion.SketchLine.classType().
- **Returns** (string): Returns a string indicating the type of the object.

### create(coordinates: double[]) -> CustomGraphicsCoordinates
Static method that creates a CustomGraphicsCoordinates object which can be used as input to various custom graphics methods.
- **coordinates** (double[]): An array of doubles where the values are the x, y, z components of each coordinate where the unit of measure is centimeters.
- **Returns** (CustomGraphicsCoordinates): Returns the created CustomGraphicsCoordinates object or null in the case of failure.

### getColor(index: integer) -> Color
Gets the color assigned to the coordinate at the specified index.
- **index** (integer): The index of the color to return. The first color has an index of 0.
- **Returns** (Color): Returns the color associated with the index. Can also return null in the case where there is no color assigned.

### getCoordinate(index: integer) -> Point3D
Gets the coordinate at the specified index.
- **index** (integer): The index of the coordinate to return. The first coordinate has an index of 0.
- **Returns** (Point3D): Returns the coordinate as a Point3D object.

### setColor(index: integer, color: Color) -> boolean
Sets the color of the coordinate at the specified index.
- **index** (integer): The index of the coordinate to set. The first coordinate has an index of 0.
- **color** (Color): The color value as a Color object.
- **Returns** (boolean): Returns true if setting the color was successful.

### setCoordinate(index: integer, coordinate: Point3D) -> boolean
Sets the coordinate at the specified index.
- **index** (integer): The index of the coordinate to set. The first coordinate has an index of 0.
- **coordinate** (Point3D): The coordinate value as a Point3D object.
- **Returns** (boolean): Returns true if setting the coordinate was successful.

## Properties

### colors : array [read-write]
Gets and sets the colors associated with the coordinate data. This is used when a mesh is displayed using per-vertex coloring. The color at each vertex is represented by four values where they are the red, green, blue, and alpha values. This should contain the same number of colors as vertices.

### coordinateCount : integer [read-only]
Returns the number of coordinates defined in the CustomGraphicsCoordinates object.

### coordinates : array [read-write]
Gets and sets the coordinate data associated with this CustomGraphicsCoordinates object. This data represents the x, y, z components of the coordinates where the unit of measure is centimeters.

### isValid : boolean [read-only]
Indicates if this object is still valid, i.e. hasn't been deleted or some other action done to invalidate the reference.

### objectType : string [read-only]
This property is supported by all objects in the API and returns a string that contains the full name (namespace::objecttype) describing the type of the object.

It's often useful to use this in combination with the classType method to see if an object is a certain type. For example: if obj.objectType == adsk.core.Point3D.classType():

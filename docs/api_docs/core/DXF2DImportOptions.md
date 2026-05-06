# DXF2DImportOptions
Namespace: adsk.core
Inherits: ImportOptions
Since: November 2015

Defines that a 2D DXF Import to create sketches (based on layers in the DXF file) is to be performed and specifies the various options.

**Accessed from:** ImportManager.createDXF2DImportOptions

## Methods

### [static] classType() -> string
Static function that all classes support that returns the type of the class as a string. The returned string matches the string returned by the objectType property. For example if you have a reference to an object and you want to check if it's a SketchLine you can use myObject.objectType == fusion.SketchLine.classType().
- **Returns** (string): Returns a string indicating the type of the object.

## Properties

### filename : string [read-write]
Gets and sets the filename or URL of the file to be imported.

### isCreateControlPointSplines : boolean [read-write]
When set to true, if there are any splines in the DXF they will be created as control point splines. Otherwise they will be created as fixed splines that cannot be edited. The default for this property is false, to create fixed splines.

### isSingleSketchResult : boolean [read-write]
Gets and sets if importing the DXF file should create a new sketch for each layer or if the entire contents of the DXF file should be merged into a single layer. If true a single sketch will be created. If false a new sketch for each layer will be created where the sketch name will be the name of the layer. The default value for this property is false, resulting in a sketch for each layer.

### isValid : boolean [read-only]
Indicates if this object is still valid, i.e. hasn't been deleted or some other action done to invalidate the reference.

### isViewFit : boolean [read-write]
Specifies if the camera should be adjusted to fit the geometry of the import. This defaults to true, which will cause a change in the current view. Setting this to false will leave the view as-is and just import the geometry.

### layers : array [read-write]
Gets and sets the names of the layers that will be imported. When the DXF2DImportOptions object is first created, the array returned is a list of all the layers in the DXF file. By default, all layers will be imported. You can set the property using a new array that contains the names of only those layers you want to import.

### objectType : string [read-only]
This property is supported by all objects in the API and returns a string that contains the full name (namespace::objecttype) describing the type of the object.

It's often useful to use this in combination with the classType method to see if an object is a certain type. For example: if obj.objectType == adsk.core.Point3D.classType():

### planarEntity : Base [read-write]
Gets and sets the construction plane or planar face that defines the plane that the resulting sketches will be created on.

### position : Point2D [read-write]
Gets and sets the X,Y offset position for the origin of the imported DXF data relative to the sketch origin. This defaults to (0,0) in a newly created DXF2DImportOptions object.

### results : ObjectCollection [read-only]
Returns a collection of Sketch objects. A sketch is created for each layer in the DXF file that contains 2D geometry. Any 3D geometry contained in the DXF file is ignored. The names of the resulting sketches correspond to the layer names in the DXF file. Currently, the only way to get a single sketch as a result is to supply a DXF file that only has 2D geometry on a single layer.

## Samples
- **Import Manager API Sample**: Demonstrates how to import different formats to Fusion document

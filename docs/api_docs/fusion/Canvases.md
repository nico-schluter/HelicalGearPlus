# Canvases
Namespace: adsk.fusion
Inherits: Base
Since: May 2023

Provides access to the Canvases in a component and provides the functionality to add new Canvases.

**Accessed from:** BaseComponent.canvases, Component.canvases, FlatPatternComponent.canvases

## Methods

### add(input: CanvasInput) -> Canvas
Creates a new canvas. Use the createInput method to first create an input object and set the available options. Then, pass that input object to the add method to create the canvas.
- **input** (CanvasInput): The CanvasInput object that defines the required information needed to create a new canvas. A CanvasInput object is the logical equivalent to the command dialog when creating a canvas. It provides access to the various options when creating a canvas. Calling the add method and passing in the CanvasInput is the equivalent to clicking the OK button on the dialog to create the canvas.
- **Returns** (Canvas): Returns the newly created Canvas object.

### [static] classType() -> string
Static function that all classes support that returns the type of the class as a string. The returned string matches the string returned by the objectType property. For example if you have a reference to an object and you want to check if it's a SketchLine you can use myObject.objectType == fusion.SketchLine.classType().
- **Returns** (string): Returns a string indicating the type of the object.

### createInput(imageFilename: string, planarEntity: Base) -> CanvasInput
Creates a new CanvasInput object. A CanvasInput object is the logical equivalent to the command dialog when creating a canvas. It provides access to the various options when creating a canvas. Calling the add method and passing in the CanvasInput is the equivalent to clicking the OK button on the dialog to create the canvas.
- **imageFilename** (string): The full filename to the image to use for the canvas. PNG, JPEG, and TIFF files are supported.
- **planarEntity** (Base): A planar BRepFace or a Construction plane to create the canvas on. If the canvas is being created in a base feature or in a direct modeling design, this can be a Plane object.
- **Returns** (CanvasInput): Returns a CanvasInput object or null in the case of failure.

### item(index: uinteger) -> Canvas
Returns the specified canvas using an index into the collection.
- **index** (uinteger): The index of the item within the collection to return. The first item in the collection has an index of 0.
- **Returns** (Canvas): Returns the specified item or null if an invalid index was specified.

### itemByName(name: string) -> Canvas
Returns the specified canvas using the name of the canvas.
- **name** (string): The name of the canvas as seen in the browser and timeline.
- **Returns** (Canvas): Returns the specified Canvas, if it exists. Otherwise it returns null.

## Properties

### count : uinteger [read-only]
Returns the number of canvases in the component.

### isValid : boolean [read-only]
Indicates if this object is still valid, i.e. hasn't been deleted or some other action done to invalidate the reference.

### objectType : string [read-only]
This property is supported by all objects in the API and returns a string that contains the full name (namespace::objecttype) describing the type of the object.

It's often useful to use this in combination with the classType method to see if an object is a certain type. For example: if obj.objectType == adsk.core.Point3D.classType():

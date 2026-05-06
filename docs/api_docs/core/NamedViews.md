# NamedViews
Namespace: adsk.core
Inherits: Base
Since: September 2023

Collection that provides access to all of the existing named views associated with a Product and supports the creation of new named views.

**Accessed from:** CAM.namedViews, Design.namedViews, Drawing.namedViews, FlatPatternProduct.namedViews, Product.namedViews, WorkingModel.namedViews

## Methods

### add(camera: Camera, name: string) -> NamedView
Creates a new named view.
- **camera** (Camera): The camera that defines the view. To create a named view for the active viewport you can get a camera from the active viewport and provide it as input to this method.
- **name** (string): The name of the named view. This must be unique with respect to other named views in the product. This is optional and if not provided a default unique name will be generated.

This is an optional argument whose default value is "".
- **Returns** (NamedView): Returns the newly created NamedView object or fails if invalid input was provided.

### [static] classType() -> string
Static function that all classes support that returns the type of the class as a string. The returned string matches the string returned by the objectType property. For example if you have a reference to an object and you want to check if it's a SketchLine you can use myObject.objectType == fusion.SketchLine.classType().
- **Returns** (string): Returns a string indicating the type of the object.

### item(index: uinteger) -> NamedView
Returns the specified named view using an index into the collection. The four standard named views ("TOP", "FRONT", "RIGHT", and "HOME") are not accessible through this method. For the predefined view use the properties on this collection that provide direct access to the specific named view.
- **index** (uinteger): The index of the named view within the collection to return. The first item in the collection has an index of 0.
- **Returns** (NamedView): Returns the specified named view or an error if an invalid index was specified.

### itemByName(name: string) -> NamedView
Returns the specified named view using the name of the named view. The four standard named views ("TOP", "FRONT", "RIGHT", and "HOME") are not accessible through this method. For the predefined view use the properties on this collection that provide direct access to the specific named view.
- **name** (string): The name of the named view within the collection to return.
- **Returns** (NamedView): Returns null if the specified name was not found.

## Properties

### count : uinteger [read-only]
Returns the number of named views associated with the product. The four standard named views ("TOP", "FRONT", "RIGHT", and "HOME") are not included in this count. Only user-created named view are counted.

### frontNamedView : NamedView [read-only]
Returns the standard named view called "FRONT".

### homeNamedView : NamedView [read-only]
Returns the standard named view called "HOME".

### isValid : boolean [read-only]
Indicates if this object is still valid, i.e. hasn't been deleted or some other action done to invalidate the reference.

### objectType : string [read-only]
This property is supported by all objects in the API and returns a string that contains the full name (namespace::objecttype) describing the type of the object.

It's often useful to use this in combination with the classType method to see if an object is a certain type. For example: if obj.objectType == adsk.core.Point3D.classType():

### rightNamedView : NamedView [read-only]
Returns the standard named view called "RIGHT".

### topNamedView : NamedView [read-only]
Returns the standard named view called "TOP".

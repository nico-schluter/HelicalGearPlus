# NamedView
Namespace: adsk.core
Inherits: Base
Since: September 2023

Represents a named view as seen in the browser.

**Accessed from:** NamedViews.add, NamedViews.frontNamedView, NamedViews.homeNamedView, NamedViews.item, NamedViews.itemByName, NamedViews.rightNamedView, NamedViews.topNamedView

## Methods

### apply() -> boolean
This updates the active viewport to use the camera associated with this named view.
- **Returns** (boolean): Returns true if the operation was successful.

### [static] classType() -> string
Static function that all classes support that returns the type of the class as a string. The returned string matches the string returned by the objectType property. For example if you have a reference to an object and you want to check if it's a SketchLine you can use myObject.objectType == fusion.SketchLine.classType().
- **Returns** (string): Returns a string indicating the type of the object.

### deleteMe()
Deletes this named view. This method will fail for any of the four standard named views. This can be determined by checking to see if the isBuiltIn property is true.

## Properties

### camera : Camera [read-write]
Gets and sets the camera associated with this named view. This property acts as read-only for the four standard named views. This can be determined by checking to see if the isBuiltIn property is true.

### isBuiltIn : boolean [read-only]
Indicates if this named view is one of the four standard named views ("TOP", "FRONT", "RIGHT", and "HOME"). There is limited functionality with the four standard named views.

### isValid : boolean [read-only]
Indicates if this object is still valid, i.e. hasn't been deleted or some other action done to invalidate the reference.

### name : string [read-write]
Gets and sets the name of this named view. This property acts as read-only for the four standard named views. This can be determined by checking to see if the isBuiltIn property is true.

### objectType : string [read-only]
This property is supported by all objects in the API and returns a string that contains the full name (namespace::objecttype) describing the type of the object.

It's often useful to use this in combination with the classType method to see if an object is a certain type. For example: if obj.objectType == adsk.core.Point3D.classType():

### parentProduct : Product [read-only]
Returns the parent product of this named view.

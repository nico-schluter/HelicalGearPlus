# CameraEventArgs
Namespace: adsk.core
Inherits: EventArgs
Since: December 2017

The CameraEventArgs provides information associated with a camera change. Camera changes happen when user changes the view by rotating, zooming in or out, panning, changing from parallel to perspective, or when the extents of the viewport changes.

## Methods

### [static] classType() -> string
Static function that all classes support that returns the type of the class as a string. The returned string matches the string returned by the objectType property. For example if you have a reference to an object and you want to check if it's a SketchLine you can use myObject.objectType == fusion.SketchLine.classType().
- **Returns** (string): Returns a string indicating the type of the object.

## Properties

### firingEvent : Event [read-only]
The event that the firing is in response to.

### isValid : boolean [read-only]
Indicates if this object is still valid, i.e. hasn't been deleted or some other action done to invalidate the reference.

### objectType : string [read-only]
This property is supported by all objects in the API and returns a string that contains the full name (namespace::objecttype) describing the type of the object.

It's often useful to use this in combination with the classType method to see if an object is a certain type. For example: if obj.objectType == adsk.core.Point3D.classType():

### viewport : Viewport [read-only]
Returns the viewport that the modified camera is associated with.

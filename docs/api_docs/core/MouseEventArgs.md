# MouseEventArgs
Namespace: adsk.core
Inherits: EventArgs
Since: August 2014

Provides a set of arguments from a firing MouseEvent to a MouseEventHandler's notify callback method.

## Methods

### [static] classType() -> string
Static function that all classes support that returns the type of the class as a string. The returned string matches the string returned by the objectType property. For example if you have a reference to an object and you want to check if it's a SketchLine you can use myObject.objectType == fusion.SketchLine.classType().
- **Returns** (string): Returns a string indicating the type of the object.

## Properties

### button : MouseButtons [read-only]
Gets which mouse button(s) are pressed. The returned value is bitwise and can indicate that more than one button is pressed.

### clicks : uinteger [read-only]
Gets the number of times the button was pressed and released.

### firingEvent : Event [read-only]
The event that the firing is in response to.

### isValid : boolean [read-only]
Indicates if this object is still valid, i.e. hasn't been deleted or some other action done to invalidate the reference.

### keyboardModifiers : KeyboardModifiers [read-only]
Gets which modifier keys are currently pressed. The returned value is bitwise and can indicate that more than one button is pressed.

### objectType : string [read-only]
This property is supported by all objects in the API and returns a string that contains the full name (namespace::objecttype) describing the type of the object.

It's often useful to use this in combination with the classType method to see if an object is a certain type. For example: if obj.objectType == adsk.core.Point3D.classType():

### position : Point2D [read-only]
Gets the coordinate of the mouse in screen space.

### viewport : Viewport [read-only]
Returns the viewport where the mouse event occurred, if it was within a viewport. If the mouse is not over a viewport this property will return null.

### viewportPosition : Point2D [read-only]
Gets the coordinate of the mouse in viewport space, if the mouse is within a viewport. If the mouse is not over a viewport this property will return null.

### wheelDelta : integer [read-only]
Gets a signed count of the number of detents the mouse wheel has rotated.

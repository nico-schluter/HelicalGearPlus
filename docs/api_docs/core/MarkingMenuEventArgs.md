# MarkingMenuEventArgs
Namespace: adsk.core
Inherits: EventArgs
Since: January 2017

The MarkingMenuEventArgs provides information associated with the marking and context menu being displayed.

## Methods

### [static] classType() -> string
Static function that all classes support that returns the type of the class as a string. The returned string matches the string returned by the objectType property. For example if you have a reference to an object and you want to check if it's a SketchLine you can use myObject.objectType == fusion.SketchLine.classType().
- **Returns** (string): Returns a string indicating the type of the object.

## Properties

### firingEvent : Event [read-only]
The event that the firing is in response to.

### isValid : boolean [read-only]
Indicates if this object is still valid, i.e. hasn't been deleted or some other action done to invalidate the reference.

### linearMarkingMenu : LinearMarkingMenu [read-only]
Provides access to the linear marking menu.

### objectType : string [read-only]
This property is supported by all objects in the API and returns a string that contains the full name (namespace::objecttype) describing the type of the object.

It's often useful to use this in combination with the classType method to see if an object is a certain type. For example: if obj.objectType == adsk.core.Point3D.classType():

### radialMarkingMenu : RadialMarkingMenu [read-only]
Provides access to the radial marking menu.

### selectedEntities : array [read-only]
Returns the currently selected entities that the user left-clicked over. These provide the "context" of what should be displayed in the menu. This can be an empty array in the case where they clicked in a open area within the graphics window.

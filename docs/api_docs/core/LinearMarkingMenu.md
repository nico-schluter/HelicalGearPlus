# LinearMarkingMenu
Namespace: adsk.core
Inherits: Base
Since: January 2017

Represents the linear marking menu which is the vertical menu that's displayed when the user right-clicks within Fusion. This supports customizing the contents of the context menu.

**Accessed from:** MarkingMenuEventArgs.linearMarkingMenu

## Methods

### [static] classType() -> string
Static function that all classes support that returns the type of the class as a string. The returned string matches the string returned by the objectType property. For example if you have a reference to an object and you want to check if it's a SketchLine you can use myObject.objectType == fusion.SketchLine.classType().
- **Returns** (string): Returns a string indicating the type of the object.

### clear() -> boolean
Completely clears the contents of the context menu. If left in this state, the context menu will not be displayed.
- **Returns** (boolean): Returns true if the clear was successful.

## Properties

### controls : ToolbarControls [read-only]
Return the collection of top-level controls in the context menu. It's possible to have drop-down controls (fly-outs) that provide access to additional controls. You can remove and add controls to customize the contents of the context menu.

### isValid : boolean [read-only]
Indicates if this object is still valid, i.e. hasn't been deleted or some other action done to invalidate the reference.

### objectType : string [read-only]
This property is supported by all objects in the API and returns a string that contains the full name (namespace::objecttype) describing the type of the object.

It's often useful to use this in combination with the classType method to see if an object is a certain type. For example: if obj.objectType == adsk.core.Point3D.classType():

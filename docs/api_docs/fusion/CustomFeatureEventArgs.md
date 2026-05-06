# CustomFeatureEventArgs
Namespace: adsk.fusion
Inherits: EventArgs
Since: January 2021

The CustomFeatureEventArgs provides information associated with a custom feature event.

## Methods

### [static] classType() -> string
Static function that all classes support that returns the type of the class as a string. The returned string matches the string returned by the objectType property. For example if you have a reference to an object and you want to check if it's a SketchLine you can use myObject.objectType == fusion.SketchLine.classType().
- **Returns** (string): Returns a string indicating the type of the object.

## Properties

### computeStatus : Status [read-only]
Provides access to the Status object associated with this compute. If the compute is successful you shouldn't do anything with this property. If the compute is not fully successful, you can use this returned Status object to define any errors or warnings that occurred during the compute. These warnings and errors will be shown to the user in the Alerts dialog.

### customFeature : CustomFeature [read-only]
Provides access to the custom feature that is being recomputed.

### firingEvent : Event [read-only]
The event that the firing is in response to.

### isValid : boolean [read-only]
Indicates if this object is still valid, i.e. hasn't been deleted or some other action done to invalidate the reference.

### objectType : string [read-only]
This property is supported by all objects in the API and returns a string that contains the full name (namespace::objecttype) describing the type of the object.

It's often useful to use this in combination with the classType method to see if an object is a certain type. For example: if obj.objectType == adsk.core.Point3D.classType():

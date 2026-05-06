# MFGDMDataEventArgs
Namespace: adsk.core
Inherits: EventArgs
Since: July 2025

The MFGDMDataEventArgs provides information associated with the MFGDM event.

## Methods

### [static] classType() -> string
Static function that all classes support that returns the type of the class as a string. The returned string matches the string returned by the objectType property. For example if you have a reference to an object and you want to check if it's a SketchLine you can use myObject.objectType == fusion.SketchLine.classType().
- **Returns** (string): Returns a string indicating the type of the object.

## Properties

### document : Document [read-only]
Provides access to the document that the event is relative to.

### firingEvent : Event [read-only]
The event that the firing is in response to.

### isValid : boolean [read-only]
Indicates if this object is still valid, i.e. hasn't been deleted or some other action done to invalidate the reference.

### objectType : string [read-only]
This property is supported by all objects in the API and returns a string that contains the full name (namespace::objecttype) describing the type of the object.

It's often useful to use this in combination with the classType method to see if an object is a certain type. For example: if obj.objectType == adsk.core.Point3D.classType():

## Samples
- **Gets all properties using GraphQL**: Fetches bulk component properties of the root component and from occurrences via single GraphQL query.
- **Get part number using GraphQL**: Fetches part number of root component and from occurrences via GQL query.
- **Set part number using GraphQL**: Sets part number of root component and from occurrences via GQL query.

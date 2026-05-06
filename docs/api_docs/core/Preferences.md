# Preferences
Namespace: adsk.core
Inherits: Base
Since: August 2014

The Preferences object provides access to the various preference related objects for getting and setting the various preference values.

**Accessed from:** Application.preferences

## Methods

### [static] classType() -> string
Static function that all classes support that returns the type of the class as a string. The returned string matches the string returned by the objectType property. For example if you have a reference to an object and you want to check if it's a SketchLine you can use myObject.objectType == fusion.SketchLine.classType().
- **Returns** (string): Returns a string indicating the type of the object.

## Properties

### apiPreferences : APIPreferences [read-only]
Gets the APIPreferences object, which provides access to the various preferences associated with the API.

### defaultUnitsPreferences : DefaultUnitsPreferencesCollection [read-only]
Gets the DefaultUnitsPreferences object.

### generalPreferences : GeneralPreferences [read-only]
Gets the GeneralPreferences object.

### graphicsPreferences : GraphicsPreferences [read-only]
Gets the GraphicsPreferences object.

### gridPreferences : GridPreferences [read-only]
Gets the GridPreferences object.

### isValid : boolean [read-only]
Indicates if this object is still valid, i.e. hasn't been deleted or some other action done to invalidate the reference.

### materialPreferences : MaterialPreferences [read-only]
Gets the MaterialPreferences object.

### networkPreferences : NetworkPreferences [read-only]
Gets the NetworkPreferences object.

### objectType : string [read-only]
This property is supported by all objects in the API and returns a string that contains the full name (namespace::objecttype) describing the type of the object.

It's often useful to use this in combination with the classType method to see if an object is a certain type. For example: if obj.objectType == adsk.core.Point3D.classType():

### productPreferences : ProductPreferencesCollection [read-only]
Gets the ProductPreferences object.

### productUsageData : ProductUsageData [read-only]
Gets the ProductUsageData object.

### unitAndValuePreferences : UnitAndValuePreferences [read-only]
Gets the UnitAndValuePreferences object.

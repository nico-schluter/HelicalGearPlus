# FusionDefaultUnitsPreferences
Namespace: adsk.fusion
Inherits: DefaultUnitsPreferences
Since: August 2014

Fusion Default Units for Design Preferences. The following code can be used to access this object. unitPrefs = app.preferences.defaultUnitsPreferences.itemByName('Design')

## Methods

### [static] classType() -> string
Static function that all classes support that returns the type of the class as a string. The returned string matches the string returned by the objectType property. For example if you have a reference to an object and you want to check if it's a SketchLine you can use myObject.objectType == fusion.SketchLine.classType().
- **Returns** (string): Returns a string indicating the type of the object.

## Properties

### defaultUnitSystem : UnitSystems [read-write]
Gets and sets the default unit system when creating a new Fusion file.

### distanceDisplayUnits : DistanceUnits [read-write]
Gets and sets the default design units for length when creating a new Fusion file. Setting this property will have the side effect of changing the defaultUnitSystem property to custom.

### isValid : boolean [read-only]
Indicates if this object is still valid, i.e. hasn't been deleted or some other action done to invalidate the reference.

### massDisplayUnits : MassUnits [read-write]
Gets and sets the default design units for mass when creating a new Fusion file. Setting this property will have the side effect of changing the defaultUnitSystem property to custom.

### name : string [read-only]
Returns the name of this DefaultUnitPreferences object.

### objectType : string [read-only]
This property is supported by all objects in the API and returns a string that contains the full name (namespace::objecttype) describing the type of the object.

It's often useful to use this in combination with the classType method to see if an object is a certain type. For example: if obj.objectType == adsk.core.Point3D.classType():

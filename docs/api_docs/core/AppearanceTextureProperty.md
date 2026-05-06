# AppearanceTextureProperty
Namespace: adsk.core
Inherits: Property
Since: August 2014

A texture value property associated with a material or appearance.

## Methods

### [static] classType() -> string
Static function that all classes support that returns the type of the class as a string. The returned string matches the string returned by the objectType property. For example if you have a reference to an object and you want to check if it's a SketchLine you can use myObject.objectType == fusion.SketchLine.classType().
- **Returns** (string): Returns a string indicating the type of the object.

## Properties

### id : string [read-only]
Returns the unique ID of this property.

### isReadOnly : boolean [read-only]
Indicates if this property is read-only. If True any attempted edits will fail.

### isUsed : boolean [read-only]
Specifies if this AppearanceTexture is being used. This is the equivalent of the check box in the Appearance dialog to enable the use of a text for an appearance or not. if this is False, then the value property should not be used because there isn't an associated. AppearanceTexture.

### isValid : boolean [read-only]
Indicates if this object is still valid, i.e. hasn't been deleted or some other action done to invalidate the reference.

### name : string [read-only]
Returns the name of this property as seen in the user interface. This name is localized and can change based on the current language

### objectType : string [read-only]
This property is supported by all objects in the API and returns a string that contains the full name (namespace::objecttype) describing the type of the object.

It's often useful to use this in combination with the classType method to see if an object is a certain type. For example: if obj.objectType == adsk.core.Point3D.classType():

### parent : Base [read-only]
Returns the parent of this property.For properties associated with an appearance this will return the parent Appearance. For properties associated with a material, this will return the parent Material. For other types of properties, this will return the PropertyGroup it is in.

### value : AppearanceTexture [read-write]
Gets and sets this property value.

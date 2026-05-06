# FloatProperty
Namespace: adsk.core
Inherits: Property
Since: August 2014

A float or real value property.

## Methods

### [static] classType() -> string
Static function that all classes support that returns the type of the class as a string. The returned string matches the string returned by the objectType property. For example if you have a reference to an object and you want to check if it's a SketchLine you can use myObject.objectType == fusion.SketchLine.classType().
- **Returns** (string): Returns a string indicating the type of the object.

### getLimits(hasLowLimit: boolean, lowLimit: double, hasHighLimit: boolean, highLimit: double) -> boolean
Method that returns any limits for the value of this property. The HasLimits property can be used to see if there are any limits or not.

This is most commonly used for properties associated with materials and appearances.
- **hasLowLimit** (boolean): Output Boolean that indicates if there is a low limit or not.
- **lowLimit** (double): If the hasLowLimit argument is true, this argument returns the low limit.
- **hasHighLimit** (boolean): Output Boolean that indicates if there is a high limit or not.
- **highLimit** (double): If the hasHighLimit argument is true, this argument returns the high limit.
- **Returns** (boolean): Returns true if the method call was successful.

## Properties

### connectedTexture : AppearanceTexture [read-only]
When the property is associated with an appearance, this gets the associated texture, if one exists. The HasConnectedTexture property controls if there is an associated texture or not. If it's parent writable you can edit the texture. If no texture exists, this property will return null.

### hasConnectedTexture : boolean [read-write]
When the property is associated with an appearance this indicates if the float value has been overridden using a texture. Setting this property to False will remove the texture so that a float value is used. Setting this property to True will connect a texture to this float value. For properties not associated with an appearance, this acts as read-only and always returns false.

### hasLimits : boolean [read-only]
Gets the boolean flag that indicates if the value of this property has any limits it must be within to be valid. If True, use the GetLimits method to get the limit values.

This is most commonly used for properties associated with materials and appearances and in most cases will return false.

### hasMultipleValues : boolean [read-only]
Gets the boolean flag that indicates if this property has multiple values or not.

This is most commonly used for properties associated with materials and appearances.

### id : string [read-only]
Returns the unique ID of this property.

### isPercentage : boolean [read-only]
Gets the boolean flag that indicates that this property represents a percentage value so the valid values must be in the range of 0.0 to 1.0 unless they’re further limited by additional limits which can be determined with the HasLimits property.

This is most commonly used for properties associated with materials and appearances.

### isReadOnly : boolean [read-only]
Indicates if this property is read-only. If True any attempted edits will fail.

### isValid : boolean [read-only]
Indicates if this object is still valid, i.e. hasn't been deleted or some other action done to invalidate the reference.

### name : string [read-only]
Returns the name of this property as seen in the user interface. This name is localized and can change based on the current language

### objectType : string [read-only]
This property is supported by all objects in the API and returns a string that contains the full name (namespace::objecttype) describing the type of the object.

It's often useful to use this in combination with the classType method to see if an object is a certain type. For example: if obj.objectType == adsk.core.Point3D.classType():

### parent : Base [read-only]
Returns the parent of this property.For properties associated with an appearance this will return the parent Appearance. For properties associated with a material, this will return the parent Material. For other types of properties, this will return the PropertyGroup it is in.

### units : string [read-only]
Gets the units that the value of this property is returned in. The String returned is a valid Fusion unit string. An empty string indicates a unitless value.

### value : double [read-write]
Gets and sets this property value. The value of this property should be ignored if the HasConnectedTexture property is true. Setting this will remove any associated texture, if there is one.

### values : array [read-write]
Gets and sets the values associated with this property. HasMultipleValues property indicates if this property will be returning more than one value.

This is most commonly used for properties associated with materials and appearances.

# ClearanceHoleDataQuery
Namespace: adsk.fusion
Inherits: Base
Since: September 2025

This object provides methods to query the clearance hole to find valid definitions for creating a clearance hole.

**Accessed from:** ClearanceHoleDataQuery.create

## Methods

### allFastenerTypes(standard: string) -> string[]
This method returns an array of all the available fastener types for the given standard. To get the available standards, use the allStandards property.
- **standard** (string): The standard to search within.
- **Returns** (string[]): Returns the specified fastener types or an empty array if an invalid standard is specified.

### allSizes(standard: string, fastenerType: string) -> string[]
This method returns an array of all the sizes for the given standard and fastener type. Valid standards and fastener types can be obtained using the allStandards and allFastenerTypes functions.
- **standard** (string): The standard to search within.
- **fastenerType** (string): The fastener type in the specified standard to search within.
- **Returns** (string[]): Returns the specified sizes or empty array if an invalid standard or fastener type is specified.

### [static] classType() -> string
Static function that all classes support that returns the type of the class as a string. The returned string matches the string returned by the objectType property. For example if you have a reference to an object and you want to check if it's a SketchLine you can use myObject.objectType == fusion.SketchLine.classType().
- **Returns** (string): Returns a string indicating the type of the object.

### create() -> ClearanceHoleDataQuery
Static method to create a new ClearanceHoleDataQuery object. The ClearanceHoleDataQuery object is a utility object that provides methods to query for the valid clearance hole definitions defined in Fusion. This object provides similar functionality as the hole command dialog to find valid clearance standards, fastener types, and sizes, which can be used to create clearance hole features.
- **Returns** (ClearanceHoleDataQuery): Returns a ClearanceHoleDataQuery object.

### standardCustomName(standard: string) -> string
Method that returns the custom name for a given standard. The custom name is the localized name of the standard using the current language specified for Fusion.
- **standard** (string): The standard you want to get the custom name for.
- **Returns** (string): Returns the specified custom name or an empty string if an invalid standard is specified.

## Properties

### allStandards : array [read-only]
This method returns an array of all the available standards. The standards' names are always English. This English name should be used in the other methods that take the standard as an input argument. If you need to display the standard name to the user, you can use the standardCustomName method To get the localized name.

### isValid : boolean [read-only]
Indicates if this object is still valid, i.e. hasn't been deleted or some other action done to invalidate the reference.

### objectType : string [read-only]
This property is supported by all objects in the API and returns a string that contains the full name (namespace::objecttype) describing the type of the object.

It's often useful to use this in combination with the classType method to see if an object is a certain type. For example: if obj.objectType == adsk.core.Point3D.classType():

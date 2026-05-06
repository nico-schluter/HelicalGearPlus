# ClearanceHoleInfo
Namespace: adsk.fusion
Inherits: Base
Since: September 2025

This object defines the methods and properties that define the size of a clearance hole. This object is used to create new hole features whose size is defined as a clearance hole for a specific size fastener. A new ClearanceHoleInfo object is created by using the ClearanceHoleInfo.create method. To determine valid values when creating a ClearanceHoleInfo object, you can use the ClearanceHoleDataQuery object, which is statically created using the ClearanceHoleDataQuery.create method.

If the ClearanceHoleInfo object is obtained from an existing HoleFeature object, modifying properties on the returned ClearanceHoleInfo object will modify the feature.

**Accessed from:** ClearanceHoleInfo.create, HoleFeature.clearanceHoleInfo

## Methods

### [static] classType() -> string
Static function that all classes support that returns the type of the class as a string. The returned string matches the string returned by the objectType property. For example if you have a reference to an object and you want to check if it's a SketchLine you can use myObject.objectType == fusion.SketchLine.classType().
- **Returns** (string): Returns a string indicating the type of the object.

### create(standard: string, fastenerType: string, size: string, fit: ClearanceHoleFits) -> ClearanceHoleInfo
Method that creates a new ClearanceHoleInfo object to use in creating clearance holes. The ClearanceHoleInfo object defines the type, size, and fit of the clearance hole to create. Fusion uses this information to look up the full details of the clearance hole in tables delivered with Fusion. The ClearanceHoleDataQuery object can be used to determine valid input for this information. It's statically created using the ClearanceHoleDataQuery.create method.
- **standard** (string): Input string that specifies the standard.
- **fastenerType** (string): Input string that specifies the fastener type.
- **size** (string): Input string that specifies the fastener size.
- **fit** (ClearanceHoleFits): Input enum value that specifies the fit of the fastener within the hole.
- **Returns** (ClearanceHoleInfo): Returns the newly created ClearanceHoleInfo object or null if the creation failed.

### redefine(standard: string, fastenerType: string, size: string, fit: ClearanceHoleFits) -> boolean
Method that redefines the values associated with an existing ClearanceHoleInfo object. This is done to modify an existing clearance hole. The ClearanceHoleInfo object defines the type, size, and fit of the clearance hole to create. Fusion uses this information to look up the full details of the clearance hole in tables delivered with Fusion. The ClearanceHoleDataQuery object can be used to determine valid input for this information.
- **standard** (string): Input string that specifies the standard.
- **fastenerType** (string): Input string that specifies the fastener type.
- **size** (string): Input string that specifies the fastener size.
- **fit** (ClearanceHoleFits): Input enum value that specifies the amount of clearance between the hole and the fastener.
- **Returns** (boolean): Returns true if the redefinition was successful.

## Properties

### fastenerType : string [read-only]
Returns the string that defines the fastener type.

### fit : ClearanceHoleFits [read-only]
Returns the enum value that defines the amount of clearance between the hole and the fastener.

### isValid : boolean [read-only]
Indicates if this object is still valid, i.e. hasn't been deleted or some other action done to invalidate the reference.

### objectType : string [read-only]
This property is supported by all objects in the API and returns a string that contains the full name (namespace::objecttype) describing the type of the object.

It's often useful to use this in combination with the classType method to see if an object is a certain type. For example: if obj.objectType == adsk.core.Point3D.classType():

### size : string [read-only]
Returns the string that defines the fastener size the clearance hole is sized for.

### standard : string [read-only]
Returns the string that defines the standard. This is typically obtained by using the ClearanceHoleDataQuery object.

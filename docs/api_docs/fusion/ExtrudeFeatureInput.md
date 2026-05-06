# ExtrudeFeatureInput
Namespace: adsk.fusion
Inherits: Base
Since: August 2014

This class defines the methods and properties that pertain to the definition of an extrude feature. This class also provides properties for setting/getting the Profile and Operation of the extrude. The Profile and Operation are defined when the ExtrudeFeatures.createInput method is called so they do not exist as properties on this class.

**Accessed from:** ExtrudeFeatures.createInput

## Methods

### [static] classType() -> string
Static function that all classes support that returns the type of the class as a string. The returned string matches the string returned by the objectType property. For example if you have a reference to an object and you want to check if it's a SketchLine you can use myObject.objectType == fusion.SketchLine.classType().
- **Returns** (string): Returns a string indicating the type of the object.

### setAllExtent(direction: ExtentDirections) -> boolean
This function is retired. See more information in the 'Remarks' section below.

Sets the extrusion extents option to 'All' (i.e. the extrusion is through-all, in both directions.) This method will fail in the case of a non-parametric extrusion.
- **direction** (ExtentDirections): The direction can be either positive, negative, or symmetric.
- **Returns** (boolean): Returns true if successful

### setDistanceExtent(isSymmetric: boolean, distance: ValueInput) -> boolean
This function is retired. See more information in the 'Remarks' section below.

Sets the extrusion extents option to 'Distance'.
- **isSymmetric** (boolean): Set to 'true' for an extrusion symmetrical about the profile plane
- **distance** (ValueInput): ValueInput object that defines the extrude distance. If the isSymmetric argument is 'false', a positive or negative distance can be used to control the direction.
- **Returns** (boolean): Returns true if successful

### setOneSideExtent(extent: ExtentDefinition, direction: ExtentDirections, taperAngle: ValueInput) -> boolean
Defines the extrusion to go in one direction from the profile. The extent of the extrusion is defined by the extent argument.
- **extent** (ExtentDefinition): An ExtentDefinition object that defines how the extent of the extrusion is defined. This can be a specified distance (DistanceExtentDefinition), to an entity (ToEntityExtent), or through-all (AllExtentDefinition). These objects can be obtained by using the static create method on the appropriate class.
- **direction** (ExtentDirections): Specifies the direction of the extrusion. PositiveExtentDirection and NegativeExtentDirection are valid values. PositiveExtentDirection is in the same direction as the normal of the profile's parent sketch plane.
- **taperAngle** (ValueInput): Optional argument that specifies the taper angle. If omitted a taper angle of 0 is used.

This is an optional argument whose default value is null.
- **Returns** (boolean): Returns true is setting the input to a one sided extent was successful.

### setOneSideToExtent(toEntity: Base, matchShape: boolean, directionHint: Vector3D) -> boolean
This function is retired. See more information in the 'Remarks' section below.

Sets the extrusion Direction option to 'One Side' and the Extents option to 'To' (a specified face)
- **toEntity** (Base): The entity that defines the "to" extent. The valid types of entities can vary depending on the type of feature this is being used with. For an extrude it can be a BRepBody, BRepFace, BRepVertex, ConstructionPlane, or ConstructionPoint.
- **matchShape** (boolean): If the matchShape argument is 'true', the toEntity is extended to fully intersect the extrusion.
- **directionHint** (Vector3D): Specifies the direction of the extrusion. This is only used in the case where there are two possible solutions and the extrusion can hit the toEntity in either direction. An example is if the profile of the extrusion is within a hole. The extrusion will intersect the cylinder of the hole in either direction.

Typically there is only a single solution and the direction is determined automatically.

This is an optional argument whose default value is null.
- **Returns** (boolean): Returns true if successful.

### setSymmetricExtent(distance: ValueInput, isFullLength: boolean, taperAngle: ValueInput) -> boolean
Defines the extrusion to go symmetrically in both directions from the profile.
- **distance** (ValueInput): The distance of the extrusions. This is either the full length of half of the length of the final extrusion depending on the value of the isFullLength property.
- **isFullLength** (boolean): Defines if the value defines the full length of the extrusion or half of the length. A value of true indicates it defines the full length.
- **taperAngle** (ValueInput): Optional argument that specifies the taper angle. The same taper angle is used for both sides for a symmetric extrusion. If omitted a taper angle of 0 is used.

This is an optional argument whose default value is null.
- **Returns** (boolean): Returns true is setting the extent was successful.

### setThinExtrude(thinExtrudeWallLocationOne: ThinExtrudeWallLocation, thinExtrudeWallThicknessOne: ValueInput, thinExtrudeWallLocationTwo: ThinExtrudeWallLocation, thinExtrudeWallThicknessTwo: ValueInput) -> boolean
Changes the extrude feature to be a thin extrude. This is only valid if the isThinExtrude property is False. If the extrusion is already a thin extrude, you can use the properties on the ExtrudeFeature to modify the thin extrude specific values.
- **thinExtrudeWallLocationOne** (ThinExtrudeWallLocation): Specifies the position of the thin wall extrude with respect to the profile being extruded. This defines the direction for a single sided thin extrude or side one of a two-sided extrusion.
- **thinExtrudeWallThicknessOne** (ValueInput): A ValueInput object that defines the thickness for a single sided thin extrude or side one of a two-sided extrusion .
- **thinExtrudeWallLocationTwo** (ThinExtrudeWallLocation): Optional argument that specifies the position of side two of a two-sided extrusion. This argument is ignored for a single sided thin extrude.

This is an optional argument whose default value is ThinExtrudeWallLocation.Side1.
- **thinExtrudeWallThicknessTwo** (ValueInput): Optional argument that is a ValueInput object that defines the thickness for side two of a two-sided extrusion. This argument is ignored for a single sided thin extrude.

This is an optional argument whose default value is null.
- **Returns** (boolean): Returns true if successful.

### setTwoSidesDistanceExtent(distanceOne: ValueInput, distanceTwo: ValueInput) -> boolean
This function is retired. See more information in the 'Remarks' section below.

Sets the extrusion extents option to 'Two Side'. This method will fail in the case of a non-parametric extrusion.
- **distanceOne** (ValueInput): ValueInput object that defines the extrude distance for the first side.
- **distanceTwo** (ValueInput): ValueInput object that defines the extrude distance for the second side.
- **Returns** (boolean): Returns true if successful

### setTwoSidesExtent(sideOneExtent: ExtentDefinition, sideTwoExtent: ExtentDefinition, sideOneTaperAngle: ValueInput, sideTwoTaperAngle: ValueInput) -> boolean
Defines the extrusion to go in both directions from the profile. The extent is defined independently for each direction using the input arguments.
- **sideOneExtent** (ExtentDefinition): An ExtentDefinition object that defines how the extent of the extrusion towards side one is defined. This can be a specified distance (DistanceExtentDefinition), to an entity (ToEntityExtent), or through-all (AllExtentDefinition). These objects can be obtained by using the static create method on the appropriate class.
- **sideTwoExtent** (ExtentDefinition): An ExtentDefinition object that defines how the extent of the extrusion towards side two is defined. This can be a specified distance (DistanceExtentDefinition), to an entity (ToEntityExtent), or through-all (AllExtentDefinition). These objects can be obtained by using the static create method on the appropriate class.
- **sideOneTaperAngle** (ValueInput): Optional argument that specifies the taper angle for side one. If omitted a taper angle of 0 is used.

This is an optional argument whose default value is null.
- **sideTwoTaperAngle** (ValueInput): Optional argument that specifies the taper angle for side two. If omitted a taper angle of 0 is used.

This is an optional argument whose default value is null.
- **Returns** (boolean): Returns true is setting the extent was successful.

### setTwoSidesToExtent(toEntityOne: Base, toEntityTwo: Base, matchShape: boolean) -> boolean
This function is retired. See more information in the 'Remarks' section below.

Set the extrusion Direction option to 'Two Side'. This method will fail in the case of a non-parametric extrusion.
- **toEntityOne** (Base): The first entity that defines the "to" extent. The valid types of entities can vary depending on the type of feature this is being used with. For an extrude it can be a BRepBody, BRepFace, BRepVertex, ConstructionPlane, or ConstructionPoint.
- **toEntityTwo** (Base): The second entity that defines the "to" extent. The valid types of entities can vary depending on the type of feature this is being used with. For an extrude it can be a BRepBody, BRepFace, BRepVertex, ConstructionPlane, or ConstructionPoint.
- **matchShape** (boolean): If the matchShape argument is 'true', the toEntity is extended to fully intersect the extrusion.
- **Returns** (boolean): Returns true if successful.

## Properties

### creationOccurrence : Occurrence [read-write]
In order for geometry to be transformed correctly, an Occurrence for creation needs to be specified when the Extrusion is created based on geometry (e.g. a profile and/or face(s)) in another component AND (the Extrusion) is not in the root component. The CreationOccurrence is analogous to the active occurrence in the UI

### extentOne : ExtentDefinition [read-only]
Gets the extent assigned for a single sided extrude or side one of a two-sided extrusion. To set the extent, use one of the set methods on the ExtrudeFeatureInput object.

### extentTwo : ExtentDefinition [read-only]
Gets the extent assigned for side two of the extrusion. If the extrude is single sided extrude this property will return null. The hasTwoExtents property can be used to determine if there are two sides or not. To set the extent, use one of the set methods on the ExtrudeFeatureInput object.

### hasTwoExtents : boolean [read-only]
Property that indicates if the extrusion is a single or two-sided extrusion. If false, the extentTwo and taperAngleTwo properties should not be used.

### isSolid : boolean [read-write]
Specifies if the extrusion should be created as a solid or surface. If it's a surface then there aren't any end caps and it's open. When an ExtrudeFeature input is created, this is initialized to true so a solid will be created if it's not changed.

### isThinExtrude : boolean [read-write]
Sets or returns whether the extrude is a thin extrude. Setting it as false will make it a regular extrude.

### isValid : boolean [read-only]
Indicates if this object is still valid, i.e. hasn't been deleted or some other action done to invalidate the reference.

### objectType : string [read-only]
This property is supported by all objects in the API and returns a string that contains the full name (namespace::objecttype) describing the type of the object.

It's often useful to use this in combination with the classType method to see if an object is a certain type. For example: if obj.objectType == adsk.core.Point3D.classType():

### operation : FeatureOperations [read-write]
Gets and sets the type of operation performed by the extrusion.

### participantBodies : array [read-write]
Gets and sets the list of bodies that will participate in the feature when the operation is a cut or intersection.

If this property has not been set, the default behavior is that all bodies that are intersected by the feature will participate.

This property can return null in the case where the feature has not been fully defined so that possible intersecting bodies can be computed.

### profile : Base [read-write]
Gets and sets the profiles or planar faces used to define the shape of the extrude. This property can return or be set with a single profile, a single planar face, or an ObjectCollection consisting of multiple profiles and planar faces. When an ObjectCollection is used all of the profiles and faces must be co-planar.

To create a surface (non-solid) extrusion, you can use the createOpenProfile and createBRepEdgeProfile methods of the Component object to create an open profile. The isSolid property of the ExtrudeFeatureInput property must also be False.

### startExtent : ExtentDefinition [read-write]
Gets and sets the extent used to define the start of the extrusion. When a new ExtrudeFeatureInput object is created the start extent is initialized to be the profile plane but you can change it to a profile plane with offset or from an object by setting this property with either a OffsetStartDefinition or an EntityStartDefinition object. You can get either one of those objects by using the static create method on the class.

### taperAngle : ValueInput [read-write]
This function is retired. See more information in the 'Remarks' section below.

Gets and sets the taper angle of the extrusion. This is used to define the taper angle for a single sided and symmetric and defines the angle for side one of a two sided extrusion. This property is initialized with a taper angle of zero. A negative angle will taper the extrusion inward while a positive value will taper the extrusion outward. This property is valid for both parametric and non-parametric extrusions.

### taperAngleOne : ValueInput [read-only]
Gets the value that will be used as the taper angle for a single sided extrusion or side one of a two-sided extrusion. To set the taper angle, use one of the set methods on the ExtrudeFeatureInput object.

### taperAngleTwo : ValueInput [read-only]
Gets the value that will be used as the taper angle for side two of a two-sided extrusion. If the extrusion is single-sided, this property will return null. The hasTwoExtents property can be used to determine if there are two sides or not. To set the taper angle, use one of the set methods on the ExtrudeFeatureInput object.

### targetBaseFeature : BaseFeature [read-write]
When creating a feature that is owned by a base feature, set this property to the base feature you want to associate the new feature with. By default, this is null, meaning it will not be associated with a base feature.

Because of a current limitation, if you want to create a feature associated with a base feature, you must set this property AND call the startEdit method of the base feature, create the feature, and then call the finishEdit method of the base feature. The base feature must be in an "edit" state to be able to add any additional items to it.

### thinExtrudeWallLocationOne : ThinExtrudeWallLocation [read-write]
Gets and sets the wall location for a one sided thin extrude or side one of a two sided thin extrude

### thinExtrudeWallLocationTwo : ThinExtrudeWallLocation [read-write]
Gets and sets the wall location for side two of a two sided thin extrude

### thinExtrudeWallThicknessOne : ValueInput [read-write]
Gets and sets the wall thickness for a one sided thin extrude or side one of a two sided thin extrude

### thinExtrudeWallThicknessTwo : ValueInput [read-write]
Gets and sets the wall thickness for side two of a two sided thin extrude

## Samples
- **Extrude Feature API Sample**: Demonstrates creating a new extrude feature.
- **Manage Participant Bodies API Sample**: Demonstrates how to manage participant During Cut operation. Same API can be used to manage participants During intersection also.

# BossFeatureSideInput
Namespace: adsk.fusion
Inherits: Base
Since: October 2022

This class defines the methods and properties that pertain to the definition of a single side of boss feature

**Accessed from:** BossFeatureInput.createSideInput, BossFeatureInput.side1, BossFeatureInput.side2

## Methods

### [static] classType() -> string
Static function that all classes support that returns the type of the class as a string. The returned string matches the string returned by the objectType property. For example if you have a reference to an object and you want to check if it's a SketchLine you can use myObject.objectType == fusion.SketchLine.classType().
- **Returns** (string): Returns a string indicating the type of the object.

### clearRibExtent()
Clears rib extent types for all position points.

### setBlank(diameter: ValueInput)
Set boss shape into blank constant diameter shank with no hole.
- **diameter** (ValueInput): The outside diameter for the boss feature shank.

### setCounterbore(diameter: ValueInput, holeDiameter: ValueInput, holeMajorDiameter: ValueInput, depth: ValueInput)
Set boss shape into constant diameter shank with counterbore hole.
- **diameter** (ValueInput): The outside diameter for the boss feature shank.
- **holeDiameter** (ValueInput): The hole diameter.
- **holeMajorDiameter** (ValueInput): The hole major (or counterbore) diameter.
- **depth** (ValueInput): With respect to hole orientation in the boss feature the parameter is either the counterbore depth or thickness of the material under the screw head.

### setCountersink(diameter: ValueInput, holeDiameter: ValueInput, holeMajorDiameter: ValueInput, depth: ValueInput, countersinkAngle: ValueInput)
Set boss shape into constant diameter shank with countersink hole.
- **diameter** (ValueInput): The outside diameter for the boss feature shank.
- **holeDiameter** (ValueInput): The hole diameter.
- **holeMajorDiameter** (ValueInput): The hole major (or countersink) diameter.
- **depth** (ValueInput): With respect to hole orientation in the boss feature the parameter is either the counterbore depth or thickness of the material under the screw head.
- **countersinkAngle** (ValueInput): Optional parameter for hole countersink angle. If not specified it is set to 90 deg.

This is an optional argument whose default value is null.

### setRibExtent(position: Base, ribExtentTypes: integer[])
Set rib extent type for particular rib for position point provided.
- **position** (Base): Position point object for the rib extent types provided
- **ribExtentTypes** (integer[]): Vector of BossRibExtentTypes for individual rib based on rib count input.

### setSimple(diameter: ValueInput, holeDiameter: ValueInput)
Set boss shape into constant diameter shank with simple hole.
- **diameter** (ValueInput): The outside diameter for the boss feature shank.
- **holeDiameter** (ValueInput): The hole diameter.

## Properties

### alignmentDepth : ValueInput [read-write]
Get or set alignment depth.

### alignmentDiameter : ValueInput [read-write]
Get or set alignment diameter.

### alignmentDraftAngle : ValueInput [read-write]
Get or set alignment draft angle.

### alignmentRootRadius : ValueInput [read-write]
Get or set blend radius of the boss alignment root.

### alignmentTipRadius : ValueInput [read-write]
Get or set blend radius of the boss alignment tip.

### alignmentType : BossAlignmentTypes [read-write]
Get or set boss alignment shape. This usually corresponds to the alignment shape of the boss counterpart.

### diameter : ValueInput [read-write]
Get or set boss shank diameter.

### draftAngle : ValueInput [read-write]
Get or set shank draft angle.

### holeCountersinkAngle : ValueInput [read-write]
Get or set countersink angle for countersink hole. This input is used only for countersink hole.

### holeDepth : ValueInput [read-write]
Get or set hole depth with respect to hole extent type. If hole extent type is set to BossHoleThrough parameter is ignored. If hole extent type is BossBlindFull the parameter is a distance from farthest face. If hole extent type is set to BossBlindDepth the parameter is a distance from start face of the hole.

### holeDiameter : ValueInput [read-write]
Get or set hole diameter.

### holeDraftAngle : ValueInput [read-write]
Get or set hole draft angle.

### holeEndRadius : ValueInput [read-write]
Get or set blend radius of the hole end.

### holeExtentType : BossHoleExtentTypes [read-write]
Get or set hole extent this feature represents. For top side only through hole extent is accepted.

### holeMajorDepth : ValueInput [read-write]
Get or set major hole depth for counterbore and countersink hole or material thickness under screw head based on hole orientation in a boss feature. This input is ignored for blank boss or boss with simple hole.

### holeMajorDiameter : ValueInput [read-write]
Get or set major hole diameter for counterbore or countersink hole. This input is ignored for blank boss or boss with simple hole.

### holeMajorDraftAngle : ValueInput [read-write]
Get or set major hole draft angle for counterbore and countersink hole. This input is ignored for blank boss or boss with simple hole.

### holeMajorRootRadius : ValueInput [read-write]
Get or set blend radius of major hole counterbore root.

### holeMajorTipRadius : ValueInput [read-write]
Get or set blend radius of major hole counterbore.

### holeStartRadius : ValueInput [read-write]
Get or set blend radius of the hole start.

### isValid : boolean [read-only]
Indicates if this object is still valid, i.e. hasn't been deleted or some other action done to invalidate the reference.

### objectType : string [read-only]
This property is supported by all objects in the API and returns a string that contains the full name (namespace::objecttype) describing the type of the object.

It's often useful to use this in combination with the classType method to see if an object is a certain type. For example: if obj.objectType == adsk.core.Point3D.classType():

### offsetClearance : ValueInput [read-write]
Get or set offset clearance as additional small offset from the selected parting plane and position point.

### ribChamferAngle : ValueInput [read-write]
Get or set rib chamfer angle. This input is used only for rib with chamfer.

### ribCount : ValueInput [read-write]
Get or set number of ribs.

### ribCutSize : ValueInput [read-write]
Get or set size of rib chamfer or fillet.

### ribDraftAngle : ValueInput [read-write]
Get or set ribs draft angle.

### ribLength : ValueInput [read-write]
Get or set ribs length measured from the shank axis.

### ribOffset : ValueInput [read-write]
Get or set ribs offset from the top face or alignment face.

### ribOuterDraftAngle : ValueInput [read-write]
Get or set rib outer draft angle.

### ribRootRadius : ValueInput [read-write]
Get or set rib base root blend radius.

### ribRotation : ValueInput [read-write]
Get or set rotation angle of the first rib from the reference vector. Reference vector is X-axis of the parent sketch from selected sketch point(s).

### ribThickness : ValueInput [read-write]
Get or set ribs thickness.

### ribTipRadius : ValueInput [read-write]
Get or set rib outer tip blend radius.

### ribTotalAngle : ValueInput [read-write]
Get or set total angle for ribs distribution. Default is 360 deg.

### ribType : BossRibShapeTypes [read-write]
Type of boss ribs this feature represents.

### rootRadius : ValueInput [read-write]
Get or set blend radius of the boss shank and participant body.

### tipRadius : ValueInput [read-write]
Get or set blend radius of the boss shank top parting face.

## Samples
- **Boss Feature Sample**: Demonstrates creating a new boss feature

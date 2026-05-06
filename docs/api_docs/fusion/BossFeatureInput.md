# BossFeatureInput
Namespace: adsk.fusion
Inherits: Base
Since: October 2022

This class defines the methods and properties that pertain to the definition of a boss feature or a boss connection

**Accessed from:** BossFeature.createInput, BossFeatures.createInput

## Methods

### [static] classType() -> string
Static function that all classes support that returns the type of the class as a string. The returned string matches the string returned by the objectType property. For example if you have a reference to an object and you want to check if it's a SketchLine you can use myObject.objectType == fusion.SketchLine.classType().
- **Returns** (string): Returns a string indicating the type of the object.

### createSideInput() -> BossFeatureSideInput
Creates a new BossFeatureSideInput object that is used to specify the input for boss feature side. This object can be set to side1 or side2. Side1 is meant to be side where screw head engages with the boss and Side2 is meant to be a side where screw thread engages with the part or metal inserts.
- **Returns** (BossFeatureSideInput): Returns BossFeatureSideInput if successful.

### setPositionBySketchPoints(pointOrPoints: Base) -> boolean
Defines the position and orientation of the boss feature using a sketch point(s).
- **pointOrPoints** (Base): The sketch point or ObjectCollection of sketch points that defines the position(s) for boss mating location. The orientation of the boss feature is inferred from the normal (Z-axis) of the point's parent sketch. The natural direction (or direction of the screw) will be opposite the normal of the sketch. If multiple sketch points are provided all must belong to the same sketch. Participant bodies will be inferred from closest visible bodies unless specified explicitly.
- **Returns** (boolean): Returns true if successful.

## Properties

### creationOccurrence : Occurrence [read-write]
In order for geometry to be transformed correctly, an Occurrence for creation needs to be specified when the boss feature is created based on geometry (e.g. point) in another component AND (the boss) is not in the root component. The CreationOccurrence is analogous to the active occurrence in the UI A value of null indicates that everything is in the context of a single component. The occurrence provided sets scope for detection of target participant bodies.

### isDefaultDirection : boolean [read-write]
Get or set if the boss feature (or boss connection) goes in the default direction or is reversed.

### isValid : boolean [read-only]
Indicates if this object is still valid, i.e. hasn't been deleted or some other action done to invalidate the reference.

### objectType : string [read-only]
This property is supported by all objects in the API and returns a string that contains the full name (namespace::objecttype) describing the type of the object.

It's often useful to use this in combination with the classType method to see if an object is a certain type. For example: if obj.objectType == adsk.core.Point3D.classType():

### offset : ValueInput [read-write]
Get or set offset of the parting face from the selected position point.

### participantBodies : array [read-write]
Gets and sets the list of bodies that will participate in the boss feature. If body provided does not intersect with direction vector at proposed position points it will be ignored. If more bodies intersect at given position point only the closest body will be accepted. Boss feature works with solid bodies only. If this property has not been set (or is empty) closest visible bodies will be detected automatically based on proposed positions and orientation.

### side1 : BossFeatureSideInput [read-write]
Gets or sets inputs for top side of the boss feature connection. It is the side where screw head engages with the boss. Default Side1 direction is considered direction of Z-axis of the parent sketch for selected position point.

### side2 : BossFeatureSideInput [read-write]
Gets or sets inputs for bottom side of the boss feature connection. It is the side where screw thread engages with the part or metal insert. Default Side2 direction is considered opposite to the direction Z-axis of the parent sketch for selected position point.

### targetBaseFeature : BaseFeature [read-write]
When creating a feature that is owned by a base feature, set this property to the base feature you want to associate the new feature with. By default, this is null, meaning it will not be associated with a base feature.

Because of a current limitation, if you want to create a feature associated with a base feature, you must set this property AND call the startEdit method of the base feature, create the feature, and then call the finishEdit method of the base feature. The base feature must be in an "edit" state to be able to add any additional items to it.

## Samples
- **Boss Feature Sample**: Demonstrates creating a new boss feature

# SweepFeatureInput
Namespace: adsk.fusion
Inherits: Base
Since: November 2014

This class defines the methods and properties that pertain to the definition of a sweep feature.

**Accessed from:** SweepFeatures.createInput, SweepFeatures.createInputForSolid

## Methods

### [static] classType() -> string
Static function that all classes support that returns the type of the class as a string. The returned string matches the string returned by the objectType property. For example if you have a reference to an object and you want to check if it's a SketchLine you can use myObject.objectType == fusion.SketchLine.classType().
- **Returns** (string): Returns a string indicating the type of the object.

## Properties

### creationOccurrence : Occurrence [read-write]
In order for geometry to be transformed correctly, an Occurrence for creation needs to be specified when the sweep is created based on geometry (e.g. a profile and/or face(s)) in another component AND (the sweep) is not in the root component. The CreationOccurrence is analogous to the active occurrence in the UI

### distanceOne : ValueInput [read-write]
Gets and sets the distance for the first side. The distance is a value from 0 to 1 indicating the position along the path where 0 is at the start and 1 is at the end. The value is default to 1.0.

### distanceTwo : ValueInput [read-write]
Gets and sets the distance for the second side. The distance is a value from 0 to 1 indicating the position along the path where 0 is at the start and 1 is at the end. The value defaults to 0 in the case where the path is closed, otherwise it defaults to 1.0. It is ignored if the path is only on one side of the profile or if the sweep definition includes a guide rail. It's always the distance against the normal of the profile if available.

### extent : SweepExtentTypes [read-write]
Gets and sets the sweep extent type. It defaults to PerpendicularToPathExtentType. This property is ignored when a guide rail has not been specified.

### guideRail : Path [read-write]
Gets and sets the guide rail to create the sweep. This can be set to null to remove the guide rail definition and have a single path sweep feature.

### guideSurfaces : array [read-write]
Gets and sets the guide surfaces to create the sweep. This can be set to an empty array to remove the guide surfaces and have a single path sweep feature. By default connected faces that are tangent to any of the guide faces are set as guide faces. Use the isChainSelection property to disable the use of tangent faces.

### isChainSelection : boolean [read-write]
Get and sets whether faces that are tangentially connected to the guide surfaces are also made guide surfaces.

### isDirectionFlipped : boolean [read-write]
Gets and sets if the direction of the sweep is flipped. This property only applies to sweep features that include a guide rail and whose path runs on both sides of the profile.

### isSolid : boolean [read-write]
Specifies if the sweep should be created as a solid or surface. If it's a surface then there aren't any end caps and it's open. This is initialized to true so a solid will be created if it's not changed.

### isValid : boolean [read-only]
Indicates if this object is still valid, i.e. hasn't been deleted or some other action done to invalidate the reference.

### objectType : string [read-only]
This property is supported by all objects in the API and returns a string that contains the full name (namespace::objecttype) describing the type of the object.

It's often useful to use this in combination with the classType method to see if an object is a certain type. For example: if obj.objectType == adsk.core.Point3D.classType():

### operation : FeatureOperations [read-write]
Gets and sets the type of operation performed by the sweep.

### orientation : SweepOrientationTypes [read-write]
Gets and sets the sweep orientation. It defaults to PerpendicularOrientationType. This property is ignored when sweeping a solid or a guide rail or surface has been specified.

### participantBodies : array [read-write]
Gets and sets the list of bodies that will participate in the feature when the operation is a cut or intersection.

If this property has not been set, the default behavior is that all bodies that are intersected by the feature will participate.

This property can return null in the case where the feature has not been fully defined so that possible intersecting bodies can be computed.

### path : Path [read-write]
Gets and sets the path to create the sweep.

### profile : Base [read-write]
Gets and sets the profiles or planar faces used to define the shape of the sweep. This property can return or be set with a single Profile, a single planar face, or an ObjectCollection consisting of multiple profiles and planar faces. When an ObjectCollection is used all of the profiles and faces must be co-planar.

### profileScaling : SweepProfileScalingOptions [read-write]
Gets and sets the sweep profile scaling option. It defaults to SweepProfileScaleOption. This property is only used when a guide rail has been specified.

### solidAlignedAxis : Base [read-write]
Gets and sets the axis to align the solid being swept with. The axis is used when sweeping a solid, and the solid orientation is set to AlignedSolidOrientationType. It can be a sketch line, linear edge, or construction axis.

### solidBody : BRepBody [read-write]
Gets and sets the BRepBody object to sweep. It must be a solid body. Setting this property results in the type being a single path sweep, and if the profile, guide path, or surface are set, they are set to null.

### solidOrientation : SweepSolidOrientationTypes [read-write]
Gets and sets the solid sweep orientation. It defaults to PerpendicularSolidOrientationType. Setting the solid orientation to AlignedSolidOrientationType requires the solid aligned axis to be set. This property is ignored if sweeping a profile.

### solidTwistAxis : Base [read-write]
Gets and sets the twist axis of the solid being swept. The axis is used when sweeping a solid, and the twist angle is set. It can be a sketch line, linear edge, construction axis, or a face that defines an axis (cylinder, cone, torus, etc.).

### taperAngle : ValueInput [read-write]
Gets and sets the taper angle of the sweep. This property is initialized with a taper angle of zero. A negative angle will taper the sweep inward while a positive value will taper the sweep outward.

This property is ignored if sweeping a solid or a guide rail or surface has been specified. This property is valid for both parametric and non-parametric extrusions.

### targetBaseFeature : BaseFeature [read-write]
When creating a feature that is owned by a base feature, set this property to the base feature you want to associate the new feature with. By default, this is null, meaning it will not be associated with a base feature.

Because of a current limitation, if you want to create a feature associated with a base feature, you must set this property AND call the startEdit method of the base feature, create the feature, and then call the finishEdit method of the base feature. The base feature must be in an "edit" state to be able to add any additional items to it.

### twistAngle : ValueInput [read-write]
Gets and sets the twist angle of the sweep. This property is initialized with a twist angle of zero. When sweeping a solid setting the twist angle requires the solid twist axis to be set.

This property is ignored if a guide rail or surface has been specified. This property is valid for both parametric and non-parametric extrusions.

## Samples
- **Sweep Feature API Sample**: Demonstrates creating a new sweep feature.
- **Sweep with guide rail Feature API Sample**: Demonstrates creating a new Sweep feature that uses a guide rail along with a profile.
- **Two Rail Sweep Feature API Sample**: Demonstrates creating new two rail sweep feature.

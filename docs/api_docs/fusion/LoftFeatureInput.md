# LoftFeatureInput
Namespace: adsk.fusion
Inherits: Base
Since: August 2016

This object defines the all of the input necessary to create a loft feature. It is the programming equivalent to the Loft command dialog. Through this object you provide the input needed to fully define a loft. To create the loft feature you pass this object the LoftFeatures.add method.

**Accessed from:** LoftFeatures.createInput

## Methods

### [static] classType() -> string
Static function that all classes support that returns the type of the class as a string. The returned string matches the string returned by the objectType property. For example if you have a reference to an object and you want to check if it's a SketchLine you can use myObject.objectType == fusion.SketchLine.classType().
- **Returns** (string): Returns a string indicating the type of the object.

## Properties

### centerLineOrRails : LoftCenterLineOrRails [read-only]
The single centerline or set of rails that define the shape of the loft. Use methods on the returned LoftCenterLineOrRails object to define the centerline or rails.

### creationOccurrence : Occurrence [read-write]
In order for geometry to be transformed correctly, an Occurrence for creation needs to be specified when the loft is created based on geometry (e.g. a profile and/or face(s)) when the loft is being created in another component AND the loft is not in the root component. The CreationOccurrence is analogous to the active occurrence in the UI

### endLoftEdgeAlignment : LoftEdgeAlignments [read-write]
Specifies the end edge alignment option for the loft feature. The default is Free Edges.

### isClosed : boolean [read-write]
Specifies if the loft closes back on itself. In other words, the first section is also used as the last section and the connection is smooth. This property defaults to false.

### isSolid : boolean [read-write]
Specifies if the loft should be created as a solid or surface. This is initialized to true so a solid will attempt to be created if it's not changed.

### isTangentEdgesMerged : boolean [read-write]
Specifies if the loft will keep or merge tangent edges. These are edges between tangent faces in the resulting loft surface. If true, the faces will be merged so the connecting edge no longer exists

### isValid : boolean [read-only]
Indicates if this object is still valid, i.e. hasn't been deleted or some other action done to invalidate the reference.

### loftSections : LoftSections [read-only]
The set of sections, (or profiles as they're referred to in the user-interface), that the loft will pass through. Use the add method on the LoftSections object to specify new sections.

### objectType : string [read-only]
This property is supported by all objects in the API and returns a string that contains the full name (namespace::objecttype) describing the type of the object.

It's often useful to use this in combination with the classType method to see if an object is a certain type. For example: if obj.objectType == adsk.core.Point3D.classType():

### operation : FeatureOperations [read-write]
Gets and sets the type of operation performed by the loft.

### participantBodies : array [read-write]
Gets and sets the list of bodies that will participate in the feature when the operation is a cut or intersection.

If this property has not been set, the default behavior is that all bodies that are intersected by the feature will participate.

This property can return null in the case where the feature has not been fully defined so that possible intersecting bodies can be computed.

### startLoftEdgeAlignment : LoftEdgeAlignments [read-write]
Specifies the start edge alignment option for the loft feature. The default is Free Edges.

### targetBaseFeature : BaseFeature [read-write]
When creating a feature that is owned by a base feature, set this property to the base feature you want to associate the new feature with. By default, this is null, meaning it will not be associated with a base feature.

Because of a current limitation, if you want to create a feature associated with a base feature, you must set this property AND call the startEdit method of the base feature, create the feature, and then call the finishEdit method of the base feature. The base feature must be in an "edit" state to be able to add any additional items to it.

## Samples
- **Loft Feature API Sample**: Demonstrates creating a new loft feature.

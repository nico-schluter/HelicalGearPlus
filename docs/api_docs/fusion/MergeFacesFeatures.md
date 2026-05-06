# MergeFacesFeatures
Namespace: adsk.fusion
Inherits: Base
Since: September 2024

A collection object that supports the ability to merge faces. Merging faces is currently limited to a Direct Modeling design or a body in a base feature. The result of merging faces is a direct B-Rep modification, and the change is not represented as a feature in the browser. As a result, a MergeFacesFeature object does not exist, and this collection only supports the merging faces and not accessing any existing features.

**Accessed from:** Features.mergeFacesFeatures

## Methods

### add(input: MergeFacesFeatureInput) -> boolean
Creates a new merge face feature.
- **input** (MergeFacesFeatureInput): A MergeFacesFeatureInput object that defines the desired merge. Use the createInput method to create a new MergeFacesFeatureInput object and then use methods on it (the MergeFacesFeatureInput object) to define the merge.
- **Returns** (boolean): Returns true if successful. Because this is limited to direct modelling only that directly modifies the B-Rep body and does not create a MergeFacesFeature object there is nothing to return besides if the merge was successful or no.

### [static] classType() -> string
Static function that all classes support that returns the type of the class as a string. The returned string matches the string returned by the objectType property. For example if you have a reference to an object and you want to check if it's a SketchLine you can use myObject.objectType == fusion.SketchLine.classType().
- **Returns** (string): Returns a string indicating the type of the object.

### createInput(inputFaces: BRepFace[], isChainSelection: boolean) -> MergeFacesFeatureInput
Creates a MergeFacesFeatureInput object for defining a simple merge face feature. Use properties and methods on this object to define the merge you want to create and then use the Add method, passing in the MergeFacesFeatureInput object.
- **inputFaces** (BRepFace[]): An array of BRepFace objects that define the faces the merge will be performed on. The faces need to be connected and from the same body (solid or surface).
- **isChainSelection** (boolean): A boolean value for setting whether or not faces that are connected and from the same body (solid or surface) will be included in the faces to merge. The default value is false.

This is an optional argument whose default value is False.
- **Returns** (MergeFacesFeatureInput): Returns the newly created MergeFacesFeatureInput object or null if the creation failed.

## Properties

### isValid : boolean [read-only]
Indicates if this object is still valid, i.e. hasn't been deleted or some other action done to invalidate the reference.

### objectType : string [read-only]
This property is supported by all objects in the API and returns a string that contains the full name (namespace::objecttype) describing the type of the object.

It's often useful to use this in combination with the classType method to see if an object is a certain type. For example: if obj.objectType == adsk.core.Point3D.classType():

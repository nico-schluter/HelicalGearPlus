# VolumetricModel
Namespace: adsk.volume
Inherits: Base
Since: May 2025

The main volumetric graph object. It has a parent component and is defined in this parent component's space. It also contains the primary and cell graphs.

## Methods

### [static] classType() -> string
Static function that all classes support that returns the type of the class as a string. The returned string matches the string returned by the objectType property. For example if you have a reference to an object and you want to check if it's a SketchLine you can use myObject.objectType == fusion.SketchLine.classType().
- **Returns** (string): Returns a string indicating the type of the object.

### createSampler() -> VolumetricSampler
Creates a VolumetricSampler object that can be used to sample the volumetric model.
- **Returns** (VolumetricSampler): Returns a VolumetricSampler object that will sample this VolumetricModel.

### getGraph(graphType: GraphTypes)
Returns a graph from the volumetric model.
- **graphType** (GraphTypes): Which kind of graph to return.

### registerCustomSDFCallback(id: string, callback: CustomSDFCallbackEventHandler) -> boolean
Handling for custom Signed Distance Field callback events. These can be registered by the API client, they will provide a string ID and a handler object that implements the abstract methods. To use the callback, a GeometryGraphNodeProperty's customSDFCallbackID should be set to the same string ID.

Register a custom Signed Distance Field callback handler with a given ID.
- **id** (string): The ID to be used in a GeometryGraphNodeProperty's customSDFCallbackID.
- **callback** (CustomSDFCallbackEventHandler): The callback object implemented by the client.
- **Returns** (boolean): True if registered successfully. False otherwise.

### removeCustomSDFCallback(id: string) -> boolean
De-register the Signed Distance Field callback handler with the given ID.
- **id** (string): The ID used in registerCustomSDFCallback()
- **Returns** (boolean): True if removed successfully. False otherwise.

## Properties

### boundaryBody : Base [read-only]
Get or set the main boundary body for this volumetric model. The volumetric model is bound by the axis aligned bounding box and will only be rendered within this body.

### isLightBulbOn : boolean [read-write]
Is the light bulb / eye (as displayed in the browser) controlling the model's visibility on.

### isValid : boolean [read-only]
Indicates if this object is still valid, i.e. hasn't been deleted or some other action done to invalidate the reference.

### objectType : string [read-only]
This property is supported by all objects in the API and returns a string that contains the full name (namespace::objecttype) describing the type of the object.

It's often useful to use this in combination with the classType method to see if an object is a certain type. For example: if obj.objectType == adsk.core.Point3D.classType():

### parentComponent : Component [read-only]
Returns the parent Component.

## Samples
- **Volumetric Custom Feature API Sample**: Demonstrates how to create a Volumetric Custom Feature using the API for graph creation.


To run the sample script, have a document open in Fusion’s DESIGN workspace. This script will create a component with a box by sketching then extruding that sketch. It will then use that box as a boundary body and create a Volumetric Custom Feature.


The script will the create a gyroid lattice using the Volumetric Model API with the appropriate Graphs, Nodes and Connections for a minimal example. Finally, the script will convert that Volumetric Model to Mesh using the API and the VolumetricModelToMeshFeature.

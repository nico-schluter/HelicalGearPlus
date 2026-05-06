# ConstructionAxisInput
Namespace: adsk.fusion
Inherits: Base
Since: August 2014

A ConstructionAxisInput is a throwaway object used to create a ConstructionAxis The usage pattern is: a. create a ConstructionAxisInput (ConstructionAxes.CreateInput) b. call one of the member functions to specify how the ConstructionAxis is created c. create the ConstructionAxis (call ConstructionAxes.Add) d. stop referencing the ConstructionAxisInput (so it gets deleted).

**Accessed from:** ConstructionAxes.createInput

## Methods

### [static] classType() -> string
Static function that all classes support that returns the type of the class as a string. The returned string matches the string returned by the objectType property. For example if you have a reference to an object and you want to check if it's a SketchLine you can use myObject.objectType == fusion.SketchLine.classType().
- **Returns** (string): Returns a string indicating the type of the object.

### setByCircularFace(circularFace: BRepFace) -> boolean
This input method is for creating an axis coincident with the axis of a cylindrical, conical or torus face.

This can result in a parametric or non-parametric construction axis depending on whether the parent component is parametric or is a direct edit component.
- **circularFace** (BRepFace): The face from a cylinder, cone, or torus.
- **Returns** (boolean): Returns true if the creation of the ConstructionAxisInput is successful.

### setByEdge(edgeEntity: Base) -> boolean
This input method is for creating a construction axis from a specified linear/circular edge or sketch curve. This can result in a parametric or non-parametric construction axis depending on whether the parent component is parametric or is a direct edit component.
- **edgeEntity** (Base): A linear/circular edge, construction line, or sketch line
- **Returns** (boolean): Returns true if the creation of the ConstructionAxisInput is successful.

### setByLine(line: InfiniteLine3D) -> boolean
This input method is for creating a non-parametric construction axis whose position in space is defined by an InfiniteLine3D object.

This method of defining a construction axis is only valid when working in the direct modeling mode. This is not valid when working in the parametric modeling mode and will fail.
- **line** (InfiniteLine3D): An InFiniteLine3D object
- **Returns** (boolean): Returns true if the creation of the ConstructionAxisInput is successful.

### setByNormalToFaceAtPoint(face: BRepFace, pointEntity: Base) -> boolean
This input method if for creating a construction axis normal to a specified face or sketch profile and that passes through a specified point. This can result in a parametric or non-parametric construction axis depending on whether the parent component is parametric or is a direct edit component.
- **face** (BRepFace): The face (BRepFace object) to create the axis normal to.
- **pointEntity** (Base): A construction point, sketch point or vertex the axis passes through. This point does not have to lie on the face.
- **Returns** (boolean): Returns true if the creation of the ConstructionAxisInput is successful.

### setByPerpendicularAtPoint(face: BRepFace, pointEntity: Base) -> boolean
This input method is for creating an axis that is normal to a face at a specified point.
- **face** (BRepFace): A face (BRepFace object) to create the axis normal to.
- **pointEntity** (Base): A construction point, sketch point or vertex the axis is to pass through.
- **Returns** (boolean): Returns true if the creation of the ConstructionAxisInput is successful.

### setByTwoPlanes(planarEntityOne: Base, planarEntityTwo: Base) -> boolean
This input method is for creating a construction axis coincident with the intersection of two planes or planar faces. This will fail if the two planes are parallel. This can result in a parametric or non-parametric construction axis depending on whether the parent component is parametric or is a direct edit component.
- **planarEntityOne** (Base): The first planar face or construction plane to intersect
- **planarEntityTwo** (Base): The second planar face or construction plane to intersect
- **Returns** (boolean): Returns true if the creation of the ConstructionAxisInput is successful.

### setByTwoPoints(pointEntityOne: Base, pointEntityTwo: Base) -> boolean
This input method is for creating a construction axis that passes through the two points (work points, sketch points or vertices). This will fail if the two points are coincident. This can result in a parametric or non-parametric construction axis depending on whether the parent component is parametric or is a direct edit component.
- **pointEntityOne** (Base): The first construction point, sketch point or vertex the axis passes through
- **pointEntityTwo** (Base): The second construction point, sketch point or vertex the axis passes through
- **Returns** (boolean): Returns true if the creation of the ConstructionAxisInput is successful.

## Properties

### creationOccurrence : Occurrence [read-write]
In order for geometry to be transformed correctly, an Occurrence for creation needs to be specified when the ConstructionAxis is created based on geometry (e.g. a straight edge) in another component AND (the ConstructionAxis) is not in the root component. The CreationOccurrence is analogous to the active occurrence in the UI

### isValid : boolean [read-only]
Indicates if this object is still valid, i.e. hasn't been deleted or some other action done to invalidate the reference.

### objectType : string [read-only]
This property is supported by all objects in the API and returns a string that contains the full name (namespace::objecttype) describing the type of the object.

It's often useful to use this in combination with the classType method to see if an object is a certain type. For example: if obj.objectType == adsk.core.Point3D.classType():

### targetBaseOrFormFeature : Base [read-write]
When creating a construction axis that is owned by a base or form feature, set this property to the base or form feature you want to associate the new construction plane with. By default, this is null, meaning it will not be associated with a base or form feature.

Because of a current limitation, if you want to create a construction axis associated with a base or form feature, you must set this property AND call the startEdit method of the base or form feature, create the feature, and then call the finishEdit method of the base or form feature. The base or form feature must be in an "edit" state to be able to add any additional items to it.

## Samples
- **Construction Axis API Sample**: Demonstrates creating construction axis in various ways.

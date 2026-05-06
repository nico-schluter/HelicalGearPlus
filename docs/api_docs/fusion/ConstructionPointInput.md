# ConstructionPointInput
Namespace: adsk.fusion
Inherits: Base
Since: August 2014

A ConstructionPointInput is a throwaway object used to create a ConstructionPoint The usage pattern is a. create a ConstructionPointInput (ConstructionPoints.CreateInput) b. call one of the member functions to specify how the ConstructionPoint is created c. create the ConstructionPoint (call ConstructionPoints.Add) d. stop referencing the ConstructionPointInput (so it gets deleted).

**Accessed from:** ConstructionPoints.createInput

## Methods

### [static] classType() -> string
Static function that all classes support that returns the type of the class as a string. The returned string matches the string returned by the objectType property. For example if you have a reference to an object and you want to check if it's a SketchLine you can use myObject.objectType == fusion.SketchLine.classType().
- **Returns** (string): Returns a string indicating the type of the object.

### setByCenter(circularEntity: Base) -> boolean
This input method is for creating a construction point at the center of a spherical face (sphere or torus), circular edge or sketch arc/circle This can result in a parametric or non-parametric construction point depending on whether the parent component is parametric or is a direct edit component.
- **circularEntity** (Base): A spherical face (sphere or torus), circular edge or sketch arc/circle
- **Returns** (boolean): Returns true if the creation of the ConstructionPointInput is successful.

### setByEdgePlane(edge: Base, plane: Base) -> boolean
This input method is for creating a construction point at the intersection of a construction plane, planar face or sketch profile and a linear edge, construction axis or sketch line. This can result in a parametric or non-parametric construction point depending on whether the parent component is parametric or is a direct edit component.
- **edge** (Base): A linear B-Rep edge, construction axis or sketch line.
- **plane** (Base): A plane, planar B-Rep face or construction plane.
- **Returns** (boolean): Returns true if the creation of the ConstructionPointInput is successful.

### setByPoint(point: Base) -> boolean
This input method is for creating a construction point on the specified point or vertex. The point can be either a B-Rep vertex, SketchPoint, or a Point3D object.

Providing a Point3D object is only valid when working in the direct edit modeling mode. This is not valid when working in the parametric modeling mode and will fail.

Even when providing a B-Rep vertex, or SketchPoint the result will be non-parametric if the parent component is a direct edit component.
- **point** (Base): A B-Rep vertex, SketchPoint, or Point object
- **Returns** (boolean): Returns true if the creation of the ConstructionPointInput is successful.

### setByThreePlanes(planeOne: Base, planeTwo: Base, planeThree: Base) -> boolean
This input method is for creating a construction point at the intersection of the three planes or planar faces. This can result in a parametric or non-parametric construction point depending on whether the parent component is parametric or is a direct edit component.
- **planeOne** (Base): The first plane or planar face to intersect
- **planeTwo** (Base): The second plane or planar face to intersect
- **planeThree** (Base): The third plane or planar face to intersect
- **Returns** (boolean): Returns true if the creation of the ConstructionPointInput is successful.

### setByTwoEdges(edgeOne: Base, edgeTwo: Base) -> boolean
This input method is for creating a construction point at the intersection of the two linear edges or sketch lines. The edges can be B-Rep edges or sketch lines. This can result in a parametric or non-parametric construction point depending on whether the parent component is parametric or is a direct edit component.
- **edgeOne** (Base): The first B-Rep edge or sketch line
- **edgeTwo** (Base): The second B-Rep edge or sketch line
- **Returns** (boolean): Returns true if the creation of the ConstructionPointInput is successful.

## Properties

### creationOccurrence : Occurrence [read-write]
In order for geometry to be transformed correctly, an occurrence for creation needs to be specified when the ConstructionPoint is created based on geometry (e.g. a sketch point) in another component AND (the ConstructionPoint) is not in the root component. The CreationOccurrence is analogous to the active occurrence in the UI

### isValid : boolean [read-only]
Indicates if this object is still valid, i.e. hasn't been deleted or some other action done to invalidate the reference.

### objectType : string [read-only]
This property is supported by all objects in the API and returns a string that contains the full name (namespace::objecttype) describing the type of the object.

It's often useful to use this in combination with the classType method to see if an object is a certain type. For example: if obj.objectType == adsk.core.Point3D.classType():

### targetBaseOrFormFeature : Base [read-write]
When creating a construction point that is owned by a base or form feature, set this property to the base or form feature you want to associate the new construction point with. By default, this is null, meaning it will not be associated with a base or form feature.

Because of a current limitation, if you want to create a construction point associated with a base or form feature, you must set this property AND call the startEdit method of the base or form feature, create the feature, and then call the finishEdit method of the base or form feature. The base or form feature must be in an "edit" state to be able to add any additional items to it.

## Samples
- **Construction Point API Sample**: Demonstrates creating construction point by different ways

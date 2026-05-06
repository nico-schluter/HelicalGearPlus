# ConstructionPlaneInput
Namespace: adsk.fusion
Inherits: Base
Since: August 2014

A ConstructionPlaneInput is a throwaway object used to create a ConstructionPlane The usage pattern is: a. create a ConstructionPlaneInput (ConstructionPlanes.CreateInput) b. call one of the member functions to specify how the ConstructionPlane is created c. create the ConstructionPlane (call ConstructionPlanes.Add) d. stop referencing the ConstructionPlaneInput (so it gets deleted).

**Accessed from:** ConstructionPlanes.createInput

## Methods

### [static] classType() -> string
Static function that all classes support that returns the type of the class as a string. The returned string matches the string returned by the objectType property. For example if you have a reference to an object and you want to check if it's a SketchLine you can use myObject.objectType == fusion.SketchLine.classType().
- **Returns** (string): Returns a string indicating the type of the object.

### setByAngle(linearEntity: Base, angle: ValueInput, planarEntity: Base) -> boolean
This input method is for creating a construction plane through an edge, axis or line at a specified angle. This can result in a parametric or non-parametric construction plane depending on whether the parent component is parametric or is a direct edit component.
- **linearEntity** (Base): The axis about which to rotate the plane
- **angle** (ValueInput): The angle at which to create the plane
- **planarEntity** (Base): The planar face or construction plane the angle is measured from.
- **Returns** (boolean): Returns true if the creation of the ConstructionPlaneInput is successful

### setByDistanceOnPath(pathEntity: Base, distance: ValueInput) -> boolean
This input method is for creating a construction plane normal to, and at specified distance along, a path defined by an edge or sketch profile. This can result in a parametric or non-parametric construction plane depending on whether the parent component is parametric or is a direct edit component.
- **pathEntity** (Base): The path can be an edge, sketch curve, or a path of multiple entities.
- **distance** (ValueInput): The distance is a value from 0 to 1 indicating the position along the path where 0 is at the start and 1 is at the end.
- **Returns** (boolean): Returns true if the creation of the ConstructionPlaneInput is successful.

### setByOffset(planarEntity: Base, offset: ValueInput) -> boolean
This input method is for creating a construction plane that is offset from a planar face or construction plane at a specified distance. This can result in a parametric or non-parametric construction plane depending on whether the parent component is parametric or is a direct edit component.
- **planarEntity** (Base): A plane, planar face or construction plane from which to create the offset plane
- **offset** (ValueInput): ValueInput object that specifies the offset distance for the plane
- **Returns** (boolean): Returns true if the creation of the ConstructionPlaneInput is successful.

### setByOffsetThroughPoint(planarEntity: Base, point: Base) -> boolean
Defines a construction plane that is offset from a planar face or construction plane and whose offset distance is defined by a vertex, sketch point, or construction point where the plane passes through the point.
- **planarEntity** (Base): A planar BRepFace, ConstructionPlane, or Plane object that the new construction plane will be offset from. A Plane object is only valid in a direct-edit design or a base feature. In that case a non-parametric result is created.
- **point** (Base): A BRepVertex, SketchPoint, ConstructionPoint, or Point3D that defines the offset distance. A Point3D is only valid in a direct-edit design. In that case a non-parametric result is created.
- **Returns** (boolean): Returns true if construction plane definition is successful.

### setByPlane(plane: Plane) -> boolean
This input method is for creating a non-parametric construction plane positioned in space as defined by the input Plane object.

This method of defining a construction plane is only valid when working in the direct modeling mode. This is not valid when working in the parametric modeling mode and will fail.
- **plane** (Plane): A transient plane object
- **Returns** (boolean): Returns true if the construction plane definition is successful.

### setByTangent(tangentFace: BRepFace, angle: ValueInput, planarEntity: Base) -> boolean
This input method is for creating a construction plane tangent to a cylindrical or conical face at a specified point. This can result in a parametric or non-parametric construction plane depending on whether the parent component is parametric or is a direct edit component.
- **tangentFace** (BRepFace): A cylindrical or conical face to create the plane tangent to
- **angle** (ValueInput): The angle relative to the planarEntity input at which to create the tangent plane
- **planarEntity** (Base): The planar face or construction plane the tangent is measured from.
- **Returns** (boolean): Returns true if the creation of the ConstructionPlaneInput is successful

### setByTangentAtPoint(tangentFace: BRepFace, pointEntity: Base) -> boolean
This input method is for creating a construction plane tangent to a face and aligned to a point. This can result in a parametric or non-parametric construction plane depending on whether the parent component is parametric or is a direct edit component.
- **tangentFace** (BRepFace): A face to create the plane tangent to
- **pointEntity** (Base): A construction point, sketch point or vertex the tangent plane aligns to. This point need not lie on the tangent face.
- **Returns** (boolean): Returns true if the creation of the ConstructionPlaneInput is successful.

### setByThreePoints(pointEntityOne: Base, pointEntityTwo: Base, pointEntityThree: Base) -> boolean
This input method is for creating a construction plane through three points that define a triangle. This can result in a parametric or non-parametric construction plane depending on whether the parent component is parametric or is a direct edit component.
- **pointEntityOne** (Base): The first construction point, sketch point or vertex in the triangle
- **pointEntityTwo** (Base): The second construction point, sketch point or vertex in the triangle
- **pointEntityThree** (Base): The third construction point, sketch point or vertex in the triangle
- **Returns** (boolean): Returns true if the creation of the ConstructionPlaneInput is successful. This will fail if the points do not form a triangle (no two points can be coincident and all three cannot be colinear).

### setByTwoEdges(linearEntityOne: Base, linearEntityTwo: Base) -> boolean
This input method is for creating a construction plane that passes through two coplanar linear entities or axes. Defines a plane by specifying two coplanar linear entities. This can result in a parametric or non-parametric construction plane depending on whether the parent component is parametric or is a direct edit component.
- **linearEntityOne** (Base): The first of two coplanar linear entities to define the plane
- **linearEntityTwo** (Base): The second of two coplanar linear entities to define the plane
- **Returns** (boolean): Returns true if the creation of the ConstructionPlaneInput is successful. This will fail if the two linear entities are not coplanar.

### setByTwoPlanes(planarEntityOne: Base, planarEntityTwo: Base) -> boolean
This input method is for creating a construction plane at the midpoint between two planar faces or construction planes. This can result in a parametric or non-parametric construction plane depending on whether the parent component is parametric or is a direct edit component.
- **planarEntityOne** (Base): The first planar face or construction plane to create a bisecting plane between
- **planarEntityTwo** (Base): The second planar face or construction plane to create a bisecting plane between
- **Returns** (boolean): Returns true if the creation of the ConstructionPlaneInput is successful. This will fail if the two planes are co-planar.

## Properties

### creationOccurrence : Occurrence [read-write]
In order for geometry to be transformed correctly, an Occurrence for creation needs to be specified when the ConstructionPlane is created based on geometry (e.g. a planarEntity) in another component AND (the ConstructionPlane) is not in the root component. The CreationOccurrence is analogous to the active occurrence in the UI

### isValid : boolean [read-only]
Indicates if this object is still valid, i.e. hasn't been deleted or some other action done to invalidate the reference.

### objectType : string [read-only]
This property is supported by all objects in the API and returns a string that contains the full name (namespace::objecttype) describing the type of the object.

It's often useful to use this in combination with the classType method to see if an object is a certain type. For example: if obj.objectType == adsk.core.Point3D.classType():

### targetBaseOrFormFeature : Base [read-write]
When creating a construction plane that is owned by a base or form feature, set this property to the base or form feature you want to associate the new construction plane with. By default, this is null, meaning it will not be associated with a base or form feature.

Because of a current limitation, if you want to create a construction plane associated with a base or form feature, you must set this property AND call the startEdit method of the base or form feature, create the feature, and then call the finishEdit method of the base or form feature. The base or form feature must be in an "edit" state to be able to add any additional items to it.

## Samples
- **Construction Plane API Sample**: Demonstrates creating construction plane by different ways.
- **Loft Feature API Sample**: Demonstrates creating a new loft feature.

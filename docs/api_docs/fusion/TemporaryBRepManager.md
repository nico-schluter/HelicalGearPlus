# TemporaryBRepManager
Namespace: adsk.fusion
Inherits: Base
Since: December 2017

A utility object that provides functionality to create and manipulate B-Rep data outside the context of a document. The provides direct access to the modeling core without the overhead of parametrics, persistence, transactions, or graphics. It also provides a way of directly defining and creating B-Rep data.

**Accessed from:** TemporaryBRepManager.get

## Methods

### booleanOperation(targetBody: BRepBody, toolBody: BRepBody, booleanType: BooleanTypes) -> boolean
Performs the specified Boolean operation between the two input bodies. The input bodies need not be solid but can be faces that are combined or trimmed.
- **targetBody** (BRepBody): The target body that will be modified as a result of the Boolean operation.
- **toolBody** (BRepBody): The tool body that will be used to operate on the target body.
- **booleanType** (BooleanTypes): The type of Boolean operation to perform.
- **Returns** (boolean): Returns true if the operation was successful. If successful, the target body is modified as a result of the Boolean operation. Because of this the targetBody must always be a temporary BRepBody. The toolbody is not modified. This is analogous to a machining operation where you have the target that is being machined and the tool that removes material.

### [static] classType() -> string
Static function that all classes support that returns the type of the class as a string. The returned string matches the string returned by the objectType property. For example if you have a reference to an object and you want to check if it's a SketchLine you can use myObject.objectType == fusion.SketchLine.classType().
- **Returns** (string): Returns a string indicating the type of the object.

### copy(bRepEntity: Base) -> BRepBody
Creates a temporary copy of the input BRepBody, BRepFace, or BRepEdge object.
- **bRepEntity** (Base): The BRepBody, BRepFace, BRepLoop, or BRepEdge to create a copy of. This can be a parametric B-Rep entity or a temporary B-Rep entity.
- **Returns** (BRepBody): Returns a BRepBody that contains the result. If a BRepBody is input the copy is of the entire body. If a BRepFace is input, then the result is a BRepBody that contains a single face. If a BRepLoop is input then the result is a BRepBody that contains a wire where each edge in the loop will have a corresponding edge in the wire. If a BRepEdge is input then the result is a BRepBody that contains a wire that contains the single edge.

### createBox(box: OrientedBoundingBox3D) -> BRepBody
Creates a new temporary solid box BRepBody object.
- **box** (OrientedBoundingBox3D): The OrientedBoundingBox3D object that defines the position, orientation, and size of the box to crate.
- **Returns** (BRepBody): Returns the newly created temporary BRepBody object or null in the case of failure.

### createCylinderOrCone(pointOne: Point3D, pointOneRadius: double, pointTwo: Point3D, pointTwoRadius: double) -> BRepBody
Creates a temporary solid cylinder or cone BRepBody object.
- **pointOne** (Point3D): A point at one end of the cylinder or cone.
- **pointOneRadius** (double): The radius of the cylinder or cone at the point one end, in centimeters.
- **pointTwo** (Point3D): A point at the opposite end of the cylinder or cone.
- **pointTwoRadius** (double): The radius of the cylinder or cone at the point two end, in centimeters. For a cylinder the pointTwoRadius should be equal to the pointOneRadius.
- **Returns** (BRepBody): Returns the newly created temporary BRepBody object or null in the case of failure.

### createEllipticalCylinderOrCone(pointOne: Point3D, pointOneMajorRadius: double, pointOneMinorRadius: double, pointTwo: Point3D, pointTwoMajorRadius: double, majorAxisDirection: Vector3D) -> BRepBody
Creates a temporary elliptical solid cylinder or cone BrepBody object.
- **pointOne** (Point3D): A point at one end of the cylinder or cone.
- **pointOneMajorRadius** (double): The major radius of the cylinder or cone at the point one end, in centimeters.
- **pointOneMinorRadius** (double): The minor radius of the cylinder or cone at the point one end, in centimeters.
- **pointTwo** (Point3D): A point at the opposite end of the cone.
- **pointTwoMajorRadius** (double): The major radius of the cylinder or cone at the point two end, in centimeters. The minor radius is automatically determined using the point one ratio of the minor and major radii.
- **majorAxisDirection** (Vector3D): A Vector3D object that defines the direction of the major axis.
- **Returns** (BRepBody): Returns the newly created temporary BRepBody object or null in the case of failure.

### createFaceFromPlanarWires(wireBodies: BRepBody[]) -> BRepBody
Creates a body from multiple wires that all lie within the same plane. Multiple wires are used when creating a plane with interior holes. One wire defines the outer shape and the other wires define the interior loops of the created face.
- **wireBodies** (BRepBody[]): An array of bodies that contain planar wires. Each wire must be closed, they should not overlap, and they should all lie on the same plane.
- **Returns** (BRepBody): Returns a BRepBody containing the created BRepFace object or null in the case of failure.

### createFromFile(filename: string) -> BRepBodies
Creates new BRepBody objects based on the contents of the specified file.
- **filename** (string): The full path and name of the file to read in. This can be a SMT, SMB, SAT, or SAB file.
- **Returns** (BRepBodies): A BRepBodies collection object is returned which can contain multiple BRepBody objects. null is returned in the case where it was unable to read the file.

### createHelixWire(axisPoint: Point3D, axisVector: Vector3D, startPoint: Point3D, pitch: double, turns: double, taperAngle: double) -> BRepBody
Creates a B-Rep body that contains a wire with a single edge that represents a helical curve.
- **axisPoint** (Point3D): A Point3D object that defines a point along the axis of the helix.
- **axisVector** (Vector3D): A Vector3D object that defines the direction of the axis of the helix.
- **startPoint** (Point3D): A Point3D that defines the start point of the helix. This is a point on the helix and defines the starting point of the helix. The distance of this point to the axis defines the starting radius of the helix.
- **pitch** (double): The pitch of the helix, or the distance between each of the turns, in centimeters.
- **turns** (double): The number of turns of the helix.
- **taperAngle** (double): The taper angle of the helix in radians.
- **Returns** (BRepBody): Returns a temporary BRepBody object that contains a wire body that is the shape of the specified helix. Return null if the creation failed.

### createProjectedBodyOutline(body: BRepBody, projectionPlane: Plane, tolerance: double, containsApproximation: boolean) -> BRepBody
Computes the approximate outline of a body. The outline is the loops formed from projecting the non-occluded silhouette curves of the body onto a plane. The outline is returned as a temporary BRepBody consisting of planar BRepFace objects whose boundaries form the outline.

The computed outline can be an approximation i.e. not precise. This is to make it useful in cases where robustness is more important than precision. For most cases, a precise analytical result is computed, but in some cases, the silhouette of a curved surface may be approximated by a series of straight lines. Even though it's an approximation you can control the tolerance of the approximation. A tighter tolerance will result in a longer compute time.
- **body** (BRepBody): Input BRepBody object to calculate the projected outline for.
- **projectionPlane** (Plane): Input Plane object that defines the position and orientation of the plane to project the body onto. The resulting body will lie on this plane.
- **tolerance** (double): Input value that specifies the tolerance in centimeters to use when approximating smooth surfaces with line segments. A negative tolerance uses the default value which is 0.001 times the length of the diagonal of the bounding box of the input body. A positive tolerance must be greater than the point tolerance (0.000001).
- **containsApproximation** (boolean): Output value that indicates if the result contains any silhouette curves that are an approximation of the true silhouette.
- **Returns** (BRepBody): Returns a BRepBody object consisting of planar BRepFace objects whose boundaries define the body's outline.

### createRuledSurface(sectionOne: BRepWire, sectionTwo: BRepWire) -> BRepBody
Creates a new body by creating a ruled surface between the two input wire bodies.
- **sectionOne** (BRepWire): BRepWire that defines the shape of the first section.
- **sectionTwo** (BRepWire): BRepWire that defines the shape of the second section.
- **Returns** (BRepBody): Returns the created ruled surface as a BRepBody object.

### createSilhouetteCurves(face: BRepFace, viewDirection: Vector3D, returnCoincidentSilhouettes: boolean) -> BRepBody
Calculates the silhouette curve geometry for a given face as viewed from a given direction.
- **face** (BRepFace): Input BRepFace object to calculate the silhouette curve for.
- **viewDirection** (Vector3D): Input Vector3D object that defines the view direction to calculate the silhouette curve relative to. The silhouette curve(s) will lie along the path where the face normal is perpendicular to the view direction.
- **returnCoincidentSilhouettes** (boolean): Input Boolean that specifies if silhouette curves that are coincident to the edges of the face should be returned or not. If true, these curves will be returned.
- **Returns** (BRepBody): Returns a SurfaceBody object that will contain one or more BRepWire objects that represent the silhouette curve(s). This method can return null in the case where there is not a silhouette curve for the specified face.

### createSphere(center: Point3D, radius: double) -> BRepBody
Creates a temporary spherical BRepBody object.
- **center** (Point3D): The center point of the sphere.
- **radius** (double): The radius of the sphere in centimeters.
- **Returns** (BRepBody): Returns the newly created temporary BRepBody object or null in the case of failure.

### createTorus(center: Point3D, axis: Vector3D, majorRadius: double, minorRadius: double) -> BRepBody
Creates a temporary toroidal BRepBody object.
- **center** (Point3D): The center point of the torus.
- **axis** (Vector3D): The axis of the torus.
- **majorRadius** (double): The radius, in centimeters, of the major radius of the torus. If the torus was created by sweeping a circle around another circle this would be the radius of the path circle.
- **minorRadius** (double): The radius, in centimeters, of the minor radius of the torus. If the torus was created by sweeping a circle around another circle this would be the radius of the profile circle.
- **Returns** (BRepBody): Returns the newly created temporary BRepBody object or null in the case of failure.

### createWireFromCurves(curves: Curve3D[], edgeMap: BRepEdge[], allowSelfIntersections: boolean) -> BRepBody
Give an array of curve geometry objects, this method creates a new wire body.
- **curves** (Curve3D[]): An array containing the input Curve3D objects. These can be Arc3D, Circle3D, Ellipse3D, EllipticalArc3D or Line3D objects.
- **edgeMap** (BRepEdge[]): An array of edges in the returned body. The order that the edges are in this collection is the same order as the original corresponding Curve3D object is in the input curves array. This allows you to map between the original input curve and created edge.
- **allowSelfIntersections** (boolean): Specifies if you want to allow self-intersection in the input curves or not.

This is an optional argument whose default value is False.
- **Returns** (BRepBody): Returns the B-Rep body containing the created wire or null in the case of failure.

### deleteFaces(faces: BRepFace[], deleteSpecifiedFaces: boolean) -> boolean
Deletes one or more faces from a temporary BRepBody. The body that will be modified is determined by getting the parent body of the input faces.
- **faces** (BRepFace[]): An array of BRepFace objects to delete. If more than one face is provided, all of the faces must exist within the same body.
- **deleteSpecifiedFaces** (boolean): This allows you to either delete the faces that were input or to keep those faces and delete all the other faces in the body.
- **Returns** (boolean): Returns true if the operation was successful.

### exportToFile(bodies: BRepBody[], filename: string) -> boolean
Exports the input bodies to the specified file.
- **bodies** (BRepBody[]): An array of BRepBody objects that you want to export.
- **filename** (string): The filename to write the BRepBody objects to. The type of file to create is inferred from the extension of the file. The valid extensions are ".sat" and ".smt".
- **Returns** (boolean): Returns true if the export was successful.

### get() -> TemporaryBRepManager
Gets the TempoaryBRepManager object. This object provides access to functionality to create an manipulate temporary B-Rep data outside the context of a document.
- **Returns** (TemporaryBRepManager): Returns the TemporaryBRepManager object.

### imprintOverlapBodies(bodyOne: BRepBody, bodyTwo: BRepBody, imprintCoincidentEdges: boolean, resultBodyOne: BRepBody, resultBodyTwo: BRepBody, bodyOneOverlappingFaces: BRepFace[], bodyTwoOverlappingFaces: BRepFace[], bodyOneOverlappingEdges: BRepEdge[], bodyTwoOverlappingEdges: BRepEdge[], tolerance: double) -> boolean
Method that finds regions of faces on two bodies which overlap and creates new bodies where the faces are split at the edges of the overlaps. This does not modify the original bodies but creates new temporary bodies that contain the imprints.
- **bodyOne** (BRepBody): Input BRepBody that will participate in the imprint operation. This body can be either a parametric or temporary body.
- **bodyTwo** (BRepBody): Input BRepBody that will participate in the imprint operation. This body can be either a parametric or temporary body.
- **imprintCoincidentEdges** (boolean): Input Boolean that indicates if overlapping edges should be included in the result. The picture below shows an example of when this argument will make a difference. The two bodies have overlapping faces and there is also an overlapping edge. If this argument is true, then the edge shown in red below will be included in the output as an overlapping edge. If False it will not be included and only the edges of the overlapping faces will be in the overlapping faces collections.
- **resultBodyOne** (BRepBody): Output temporary BRepBody that contains the imprinted body that corresponds to the body provided through the bodyOne argument.
- **resultBodyTwo** (BRepBody): Output temporary BRepBody that contains the imprinted body that corresponds to the body provided through the bodyTwo argument.
- **bodyOneOverlappingFaces** (BRepFace[]): Output array of BRepFace objects that represent the overlapping faces that are part of resultBodyOne. Faces at the same index within the collection returned here and that returned by the bodyTwoOverlappingFaces are overlapping.
- **bodyTwoOverlappingFaces** (BRepFace[]): Output array of BRepFace objects that represent the overlapping faces that are part of resultBodyTwo. Faces at the same index within the collection returned here and that returned by the bodyOneOverlappingFaces are overlapping.
- **bodyOneOverlappingEdges** (BRepEdge[]): Output array of BRepEdge objects that represent the overlapping edges that are part of resultBodyOne. Edges at the same index within the collection returned here and that returned by the bodyTwoOverlappingEdges are overlapping.
- **bodyTwoOverlappingEdges** (BRepEdge[]): Output array of BRepEdge objects that represent the overlapping edges that are part of resultBodyTwo. Edges at the same index within the collection returned here and that returned by the bodyOneOverlappingEdges are overlapping.
- **tolerance** (double): Optional Input double that specifies the tolerance, in centimeters, to use when comparing the bodies. If not specified, or a value of zero is specified, the internal modeling tolerance will be used.

This is an optional argument whose default value is 0.0.
- **Returns** (boolean): Returns true if the imprint calculation was successful.

### planeIntersection(body: BRepBody, plane: Plane) -> BRepBody
Calculates the intersection between the input body and plane and creates a wire body that represents the intersection curves.
- **body** (BRepBody): The BRepBody to intersection.
- **plane** (Plane): The geometry Plane to intersect with the body.
- **Returns** (BRepBody): Returns a BRepBody that contains a wire body that represents the intersection.

### transform(body: BRepBody, transform: Matrix3D) -> boolean
Transforms the input body using the specified transformation matrix.
- **body** (BRepBody): The BRepBody object to transform.
- **transform** (Matrix3D): The transformation matrix that defines the transform to apply to the body.
- **Returns** (boolean): Returns true if the specified transform was successfully applied to the body.

## Properties

### isValid : boolean [read-only]
Indicates if this object is still valid, i.e. hasn't been deleted or some other action done to invalidate the reference.

### objectType : string [read-only]
This property is supported by all objects in the API and returns a string that contains the full name (namespace::objecttype) describing the type of the object.

It's often useful to use this in combination with the classType method to see if an object is a certain type. For example: if obj.objectType == adsk.core.Point3D.classType():

## Samples
- **TemporaryBRepManager API Sample**: TemporaryBRepManager related functions

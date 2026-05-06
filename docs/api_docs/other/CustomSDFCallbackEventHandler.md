# CustomSDFCallbackEventHandler
Namespace: adsk.volume
Inherits: EventHandler
Since: May 2025

API clients can implement subclasses of this handler to enable custom Signed Distance Field geometries.

## Methods

### boundingBox(bboxOut: BoundingBox3D) -> boolean
This method should be implemented in the subclass of the handler to return the bounding box of the Signed Distance Field that it can provide. This method will be called infrequently by the system.
- **bboxOut** (BoundingBox3D): This is a return parameter. The values of this should be set by the client implementation.
- **Returns** (boolean): True if there is a valid bounding box.

### signedDistanceAt(x: double, y: double, z: double) -> double
This method should be implemented in the subclass of the handler to return the Signed Distance value at the given coordinates within the bounding box. This method will be called very frequently and potentially from several differrent threads, it should be made as fast as possible
- **x** (double): X coordinate of the sampled point.
- **y** (double): Y coordinate of the sampled point.
- **z** (double): Z coordinate of the sampled point.
- **Returns** (double): The signed distance value at the sampled point (X,Y,Z).

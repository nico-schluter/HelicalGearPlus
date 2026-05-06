# CustomGraphicsGroup
Namespace: adsk.fusion
Inherits: CustomGraphicsEntity
Since: September 2017

Represents of group of custom graphics entities. A group can also own other graphics groups.

**Accessed from:** CustomGraphicsGroup.addGroup, CustomGraphicsGroups.add, CustomGraphicsGroups.item

## Methods

### addBRepBody(body: BRepBody) -> CustomGraphicsBRepBody
Adds a new CustomGraphicsBRepBody object to this group. This displays a real or transient BRepBody object as custom graphics. No relationship exists back to the original input body so if it is changed, the custom graphics will not change.

The body associated with the CustomGraphicsBRep body is a copy of the original input body. Equivalent Faces, Edges, and vertices can be found by using the indexes in the collection. For example if you have a face of the original body and find that it is at index 24 in the BRepFaces collection of that body, the equivalent face in the custom graphics body will also be at index 24. This works as long as the original body is not modified in any way.
- **body** (BRepBody): The real or transient BRepBody object to draw using custom graphics.
- **Returns** (CustomGraphicsBRepBody): Returns the newly created CustomGraphicsBRepBody object or null in the case of failure.

### addCurve(curve: Curve3D) -> CustomGraphicsCurve
Adds a new CustomGraphicsCurve entity to this group. A CustomGraphicsCurve is a wireframe graphic that is based on any object derived from Curve3D (except InfiniteLine3D). This is useful when drawing curved geometry where the alternative is to stroke the smooth curve and draw it as a series of lines. Using this you can directly use the curve and Fusion will automatically take care of creating the correct display for the current level of detail.
- **curve** (Curve3D): The curve that defines the shape of the graphics entity. Any of the curve types derived from Curve3D are valid except for InfiniteLine3D.
- **Returns** (CustomGraphicsCurve): Returns the newly created CustomGraphicsCurve object or null in the case of failure.

### addGroup() -> CustomGraphicsGroup
Creates a new, empty CustomGraphicsGroup that is owned by this CustomGraphicsGroup.
- **Returns** (CustomGraphicsGroup): Returns the new CustomGraphicsGroup object or null in the case of a failure.

### addLines(coordinates: CustomGraphicsCoordinates, indexList: integer[], isLineStrip: boolean, lineStripLengths: integer[]) -> CustomGraphicsLines
Adds a new CustomGraphicsLines entity to this group.
- **coordinates** (CustomGraphicsCoordinates): The CustomGraphicsCoordinates object that defines the coordinates of the vertices of the lines. A CustomGraphicsCoordinates object can be created using the static create method of the CustomGraphicsCoordinates class.
- **indexList** (integer[]): An array of integers that represent indices into the coordinates to define the order the coordinates are used to draw the lines. If an empty array is provided, the coordinates are used in the order they're provided in the provided CustomGraphicsCoordinates object.
- **isLineStrip** (boolean): A boolean indicating if a series of individual lines or a connected set of lines (a line strip) is to be drawn. If individual lines are drawn, (this argument is false), each pair of coordinates defines a single line. If a line strip is drawn, (this argument is true), the first pair of coordinates define the first line and the third coordinate defines a line that connects to the second coordinate. The fourth coordinate creates a line connecting to the third coordinate, and so on.
- **lineStripLengths** (integer[]): If isLineStrip is true, this argument is used to define the number of coordinates to use in each line strip. It is an array of integers that defines the number of coordinates for each line strip. For example, if the array [4,10] is input, 4 coordinates are connected for the first line strip and 10 are used to create a second line strip. If an empty array is provided, a single line strip is created. If isLineStrip is False, this argument is ignored.

This is an optional argument whose default value is null.
- **Returns** (CustomGraphicsLines): Returns the new CustomGraphicsLines object or null in the case of a failure.

### addMesh(coordinates: CustomGraphicsCoordinates, coordinateIndexList: integer[], normalVectors: double[], normalIndexList: integer[]) -> CustomGraphicsMesh
Adds a new CustomGraphicsMesh entity to this group.
- **coordinates** (CustomGraphicsCoordinates): The CustomGraphicsCoordinates object that defines the coordinates of the vertices of the mesh. A CustomGrahpicsCoordinates object can be created using the static create method of the CustomGraphicsCoordinates class.
- **coordinateIndexList** (integer[]): An array of integers that represent indices into the coordinates to define the vertices of the triangles. If an empty array is provided, then it's assumed that the first three coordinates defines the first triangle, the next three define the second triangle, and so on.
- **normalVectors** (double[]): An array of doubles that represent the x, y, z components of the normals at each coordinate. There should be a normal defined for each coordinate. If an empty array is provided for the normal vectors, Fusion will automatically calculate normal vectors that are 90 degrees to the face of the triangle, making it appear flat.
- **normalIndexList** (integer[]): An array of integers that represent indices into the normal vectors to define the which vector corresponds to which vertex. This should be the same size as the vertex index list. If an empty array is input and normal vectors are provided, it is assumed that the normals match up one-to-one to each coordinate.
- **Returns** (CustomGraphicsMesh): Returns the new CustomGraphicsMesh object or null in the case of a failure.

### addPointSet(coordinates: CustomGraphicsCoordinates, indexList: integer[], pointType: CustomGraphicsPointTypes, pointImage: string) -> CustomGraphicsPointSet
Adds a new CustomGraphicsPointSet entity to this group. This will be displayed as one or more points where all of the points will display using the same image.
- **coordinates** (CustomGraphicsCoordinates): The CustomGraphicsCoordinates object that defines the coordinates where the points will be displayed. A CustomGraphicsCoordinates object can be created using the static create method of the CustomGraphicsCoordinates class.
- **indexList** (integer[]): An array of integers that represent indices into the coordinates to define which coordinates to use when drawing points. If an empty array is provided, a point is drawn for every coordinate.
- **pointType** (CustomGraphicsPointTypes): Specifies the type of point to display. Currently there are two choices; UserDefinedCustomGraphicsPointType and PointCloudCustomGraphicsPointType. When set to PointCloudCustomGraphicsPointType, each point displays as a single pixel and is the most efficient point display type for displaying sets that contain very large quantities of points. When set to UserDefinedCustomGraphicsPointType, you specify the image to display as the point. This can be any PNG image and is centered on the point.
- **pointImage** (string): If the pointType is PointCloudCustomGraphicsPointType this argument is ignored and can be an empty string. This argument must be specified if the pointType is UserDefinedCustomGraphicsPointType. This is the path to the PNG image file that will be displayed as the point. It can be either a full path to the file or a relative path that is respect to the .py, dll, or dylib file being run. There is no restriction on the size of the image, but generally very small images would be used for points.
- **Returns** (CustomGraphicsPointSet): Returns the newly created CustomGraphicsPointSet object or null in the case of failure.

### addText(formattedText: string, font: string, size: double, transform: Matrix3D) -> CustomGraphicsText
Adds a new CustomGraphicsText entity to this group. This will be displayed as a single line of text. It is placed so that the upper-left corner is at the point defined and the text will be parallel to the X-Y plane of the world coordinate system and in the X direction. To change it's position relative to the input point you can change the horizontal and vertical justification on the returned CustomGrahicsText object. You can also reorient the text by changing the transform of the returned CustomGraphicsText object.
- **formattedText** (string): The text string to be displayed. Overall formatting can be defined using properties on the returned CustomGraphicsText object. Formatting overrides can be defined within the string using formatting codes.
- **font** (string): The name of the font to use when displaying the text.
- **size** (double): The size of the text in centimeters.
- **transform** (Matrix3D): Transformation matrix that specifies the position and orientation of the text in model space. The origin of the text is the upper-left corner.
- **Returns** (CustomGraphicsText): Returns the newly created CustomGraphicsText object or null in the case of failure.

### [static] classType() -> string
Static function that all classes support that returns the type of the class as a string. The returned string matches the string returned by the objectType property. For example if you have a reference to an object and you want to check if it's a SketchLine you can use myObject.objectType == fusion.SketchLine.classType().
- **Returns** (string): Returns a string indicating the type of the object.

### deleteMe() -> boolean
Deletes the entity from the custom graphics group.
- **Returns** (boolean): Returns true if the deletion was successful.

### getOpacity(opacity: double, isOverride: boolean) -> boolean
Gets the opacity of the graphics entity.
- **opacity** (double): The opacity value where 1.0 is completely opaque and 0.0 is completely transparent.
- **isOverride** (boolean): Indicates if this entities opacity will override the opacity defined by the material. If true, it will override the material opacity and if false the opacity values will accumulate.
- **Returns** (boolean): Returns true if getting the opacity information was successful.

### item(index: uinteger) -> CustomGraphicsEntity
Function that returns the specified custom graphics entity within this group. This also includes any child graphics groups.
- **index** (uinteger): The index of the item within the collection to return. The first item in the collection has an index of 0.
- **Returns** (CustomGraphicsEntity): Returns the specified item or null if an invalid index was specified.

### setOpacity(opacity: double, isOverride: boolean) -> boolean
Sets the opacity of the graphics entity. By default, when a new entity is it is completely opaque and does not override the opacity defined by the material.
- **opacity** (double): The opacity value where 1.0 is completely opaque and 0.0 is completely transparent.
- **isOverride** (boolean): Indicates if this entities opacity will override the opacity defined by the material. If true, it will override the material opacity and if false the opacity values will accumulate.
- **Returns** (boolean): Returns true if setting the opacity information was successful.

## Properties

### billBoarding : CustomGraphicsBillBoard [read-write]
Gets and sets the billboarding behavior of this custom graphics entity. To define billboarding you can set this property using a CustomGraphicsBillBoard objects that you statically create using the create method of the CustomGraphicsBillBoard class. To remove billboarding from this entity you can set this property to null.

Billboarding is used to specify that the orientation of custom graphics is defined relative to the screen instead of model space. This is commonly used for legends and symbols that you want to always face the user, even as the camera is rotated.

### boundingBox : BoundingBox3D [read-only]
Returns a box oriented parallel to the world x-y-x axes that contains the graphics entity. Depending on whether the graphics are drawn in model space or screen space this will return the bounding box in either centimeters (model) or pixels (screen). In the case where it returns the bounding box in pixel space, the Z coordinates of the box will be 0 and can be ignored.

### color : CustomGraphicsColorEffect [read-write]
Gets and sets the current color definition for this entity. The color of custom graphics can be defined in many ways; solid color, simple material, and appearance.

### count : uinteger [read-only]
Returns the number of graphics entities within the group.

### cullMode : CustomGraphicsCullModes [read-write]
Gets and sets the culling model to use when rendering the entity. Culling is used when the entity contains a mesh or B-Rep faces and defines which sides of the mesh or face are rendered. This is primarily used for a watertight mesh or solid B-Rep so that the "inside" of the faces is not rendered since it's never visible to the user.

When a new graphics entity is created its default cull mode is CustomGraphicsCullBack which will optimize the rendering of "solid" meshes so the inside is not rendered.

### depthPriority : integer [read-write]
Gets and sets the depth priority associated with the graphics entity. The depth priority defines how one graphics entity will be drawn with respect to another entity. This is useful when there are entities that lie in the same space so it's ambiguous which should be drawn on the other. For example, if you draw a curve on a planar mesh and want the curve to be completely visible. You can set the depth priority of the curve to be greater than the mesh so it will be drawn after the mesh and will remain visible.

When a new graphics entity is created it's default depth priority is 0.

### id : string [read-write]
An id you can specify for the entity. By default, all new graphics entities do not have an id and this property will return an empty string. But in cases where entities will be selected, assigning an id can make understanding what was selected much easier.

### isChildrenSelectable : boolean [read-write]
Defines if the child custom graphic entities are selectable or if the entire group is selected in the UI. By default this is true. If false, the isSelectable property defines if this group is selectable. If true, the isSelectable property of each child entity defines if it is selectable.

### isSelectable : boolean [read-write]
Gets and sets if the graphics entity is selectable within the graphics window. By default, when a new entity is created it is selectable.

### isValid : boolean [read-only]
Indicates if this object is still valid, i.e. hasn't been deleted or some other action done to invalidate the reference.

### isVisible : boolean [read-write]
Gets and sets if the graphics entity is visible in the graphics window. By default, when a new entity is created it is visible.

### name : string [read-write]
Gets and sets the name displayed when this entity is selected. If no name has been set, "Custom Graphics" will be displayed.

### objectType : string [read-only]
This property is supported by all objects in the API and returns a string that contains the full name (namespace::objecttype) describing the type of the object.

It's often useful to use this in combination with the classType method to see if an object is a certain type. For example: if obj.objectType == adsk.core.Point3D.classType():

### parent : Base [read-only]
Returns the parent Component for a top-level group or the CustomGraphicsGroup object for graphics entities and child groups.

### transform : Matrix3D [read-write]
Gets and sets the transform associated with the graphics entity. When a new graphics entity is created its default transform is an identity matrix which results in the graphics entity being displayed in model space using the original coordinate data used to define the entity.

### viewPlacement : CustomGraphicsViewPlacement [read-write]
Gets and sets the graphics view placement being applied to this graphics entity. A CustomGraphicsViewPlacement object can be created using the static create method of the class. When assigned to a graphics entity the position of the graphics is defined relative to the view in 2D view space (pixels) rather than in 3D model space (centimeters).

### viewScale : CustomGraphicsViewScale [read-write]
Gets and sets the graphics view scale being applied to this graphics entity. A CustomGraphicsViewScale object can be created using the static create method of the class. When assigned to a graphics entity the size of the graphics entity is defined in view space (pixels) instead of model space (centimeters).

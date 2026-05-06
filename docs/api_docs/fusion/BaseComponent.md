# BaseComponent
Namespace: adsk.fusion
Inherits: Base
Since: August 2014

The BaseComponent object that defines all of the common design data and is the base class for the product specific components.

## Methods

### allOccurrencesByComponent(component: Component) -> OccurrenceList
Returns all occurrences, at any level of the assembly, that reference the specified component. The returned list is read-only.
- **component** (Component): The component that is being referenced by the occurrences that will be returned.
- **Returns** (OccurrenceList): The occurrences referenced by the specified component.

### [static] classType() -> string
Static function that all classes support that returns the type of the class as a string. The returned string matches the string returned by the objectType property. For example if you have a reference to an object and you want to check if it's a SketchLine you can use myObject.objectType == fusion.SketchLine.classType().
- **Returns** (string): Returns a string indicating the type of the object.

### findBRepUsingPoint(point: Point3D, entityType: BRepEntityTypes, proximityTolerance: double, visibleEntitiesOnly: boolean) -> ObjectCollection
Finds all the entities of the specified type at the specified location.
- **point** (Point3D): Input coordinate that specifies the component space point at which to find the entities.
- **entityType** (BRepEntityTypes): The type of B-Rep entity wanted. You can also take advantage of B-Rep topology to infer other that other entities were found. For example, If you get a BRepEdge it implies that the faces the edge connects were also found. If a BRepVertex is returned it implies the edges that the vertex connects were found and the faces that the edges connect were found.
- **proximityTolerance** (double): Specifies the tolerance for the search. All entities within this distance from the search point that match the filter will be returned. If not specified a default tolerance is used.

This is an optional argument whose default value is -1.0.
- **visibleEntitiesOnly** (boolean): indicates whether or not invisible objects should be included in the search. Defaults to True indicating that invisible objects will be ignored.

This is an optional argument whose default value is True.
- **Returns** (ObjectCollection): Returns an ObjectCollection containing the entities found. The returned collection can be empty indicating nothing was found.

### findBRepUsingRay(originPoint: Point3D, rayDirection: Vector3D, entityType: BRepEntityTypes, proximityTolerance: double, visibleEntitiesOnly: boolean, hitPoints: ObjectCollection) -> ObjectCollection
Finds all the B-Rep entities that are intersected by the specified ray. This can return BRepFace, BrepEdge, and BRepVertex objects.
- **originPoint** (Point3D): Input point that defines the origin of the ray. The search for entities begins at this point.
- **rayDirection** (Vector3D): Input vector that defines the direction of the ray. The ray is infinite so the length of the vector is ignored.
- **entityType** (BRepEntityTypes): The type of B-Rep entity wanted. You can also take advantage of B-Rep topology to infer other intersections. For example, If you get a BRepEdge it implies that the faces the edge connects were also intersected. If a BRepVertex is returned it implies the edges that the vertex connects were intersected and the faces that the edges connect were intersected.
- **proximityTolerance** (double): Optional argument that specifies the tolerance for the search. All entities within this distance from the ray and of the specified type will be returned. If not specified a default small tolerance is used.

This is an optional argument whose default value is -1.0.
- **visibleEntitiesOnly** (boolean): Optional argument that indicates whether or not invisible entities should be included in the search. Defaults to True indicating that invisible entities will be ignored.

This is an optional argument whose default value is True.
- **hitPoints** (ObjectCollection): An ObjectCollection of Point3D objects that represent the coordinates where the ray hit the found entity. There will be the same number of hit points as returned entities and they will be in the collections in the same order. In other words, hit point 1 corresponds with found entity 1, hit point 2 corresponds with found entity 2, and so on. Because of the proximity tolerance the hitPoint may not actually lie on the entity but will be within the proximity tolerance to it. It's an optional out argument, returns the hit points if an existing ObjectCollection is input. You can create a new ObjectCollection by using the static create method on the ObjectCollection class.

This is an optional argument whose default value is null.
- **Returns** (ObjectCollection): Returns an ObjectCollection containing the entities found. The returned collection can be empty indicating nothing was found. The points are returned in an order where they are arranged based on their distance from the origin point where the closest point is first. If an entity is hit more than once, the entity is returned once for the first intersection.

### occurrencesByComponent(component: Component) -> OccurrenceList
Returns all occurrences at the top-level of this component that reference the specified component. The returned list is read-only.
- **component** (Component): The component that is being referenced by the occurrences that will be returned.
- **Returns** (OccurrenceList): The occurrences referenced by the specified component.

## Properties

### allOccurrences : OccurrenceList [read-only]
Returns all of the occurrences in the assembly regardless of their level within the assembly structure. The returned list is read-only.

### bRepBodies : BRepBodies [read-only]
Returns the B-Rep bodies collection associated with this component.

### canvases : Canvases [read-only]
Returns the canvases collection associated with this component. This provides access to the existing canvases and supports the creation of new canvases.

### constructionAxes : ConstructionAxes [read-only]
Returns the construction axes collection associated with this component. This provides access to the existing construction axes and supports the creation of new construction axes.

### constructionPlanes : ConstructionPlanes [read-only]
Returns the construction planes collection associated with this component. This provides access to the existing construction planes and supports the creation of new construction planes.

### constructionPoints : ConstructionPoints [read-only]
Returns the construction points collection associated with this component. This provides access to the existing construction points and supports the creation of new construction points.

### dataComponent : DataComponent [read-only]
Returns the DataComponent associated with this component. The DataComponent provides ID information that can be used to access this component using the MFG DM API. These ID's don't exist until a component has been saved. The ID's are generated by MFG DM API on the cloud, so there will be a slight delay after saving before the ID's are available. This property returns null in the case the MFG DM API information doesn't exist yet.

When opening a design, the MFG DM API information is obtained from the cloud and as a result may not be available immediately after opening a document. Again, this property will return null in this case too. Essentially, null is returned in all cases where good ID information is not yet available.

### decals : Decals [read-only]
Returns the decals collection associated with this component. This provides access to the existing decals and supports the creation of new decals.

### isValid : boolean [read-only]
Indicates if this object is still valid, i.e. hasn't been deleted or some other action done to invalidate the reference.

### name : string [read-write]
Property that gets and sets the name of this component. This is the name shown in the browser for each occurrence referencing this component.

### objectType : string [read-only]
This property is supported by all objects in the API and returns a string that contains the full name (namespace::objecttype) describing the type of the object.

It's often useful to use this in combination with the classType method to see if an object is a certain type. For example: if obj.objectType == adsk.core.Point3D.classType():

### occurrences : Occurrences [read-only]
Property that returns the Occurrences collection associated with this component. This provides access to the occurrences at the top-level of this component and provides the functionality to add new occurrences.

### parentDesign : Design [read-only]
Returns the parent product this component is owned by.

### propertyGroups : PropertyGroups [read-only]
Returns the PropertyGroups object associated with this component.

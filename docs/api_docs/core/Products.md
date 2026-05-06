# Products
Namespace: adsk.core
Inherits: Base
Since: August 2014

The Products object provides access to all of the products that exist in the document.

**Accessed from:** Document.products, DrawingDocument.products, FusionDocument.products

## Methods

### [static] classType() -> string
Static function that all classes support that returns the type of the class as a string. The returned string matches the string returned by the objectType property. For example if you have a reference to an object and you want to check if it's a SketchLine you can use myObject.objectType == fusion.SketchLine.classType().
- **Returns** (string): Returns a string indicating the type of the object.

### item(index: uinteger) -> Product
Function that returns the specified product using an index into the collection.
- **index** (uinteger): The index of the item within the collection to return. The first item in the collection has an index of 0.
- **Returns** (Product): Returns the specified item or null if an invalid index was specified.

### itemByProductType(productType: string) -> Product
Returns the specified product, if it exists within this document.
- **productType** (string): The product type string. For example, to get the product that represents the design data you use "DesignProductType" or to get the product that represent the CAM data you use "CAMProductType".

A complete list of available products can be obtained by using the Application.supportedProductTypes property.
- **Returns** (Product): Returns the specified item or null if the specified productType does not exist within this document.

## Properties

### count : uinteger [read-only]
Returns the number of products within the collection.

### isValid : boolean [read-only]
Indicates if this object is still valid, i.e. hasn't been deleted or some other action done to invalidate the reference.

### objectType : string [read-only]
This property is supported by all objects in the API and returns a string that contains the full name (namespace::objecttype) describing the type of the object.

It's often useful to use this in combination with the classType method to see if an object is a certain type. For example: if obj.objectType == adsk.core.Point3D.classType():

## Samples
- **Gets all properties using GraphQL**: Fetches bulk component properties of the root component and from occurrences via single GraphQL query.
- **Generate Toolpaths API Sample**: Demonstrates generating the toolpaths in the active document.
- **Post Toolpaths API Sample**: Demonstrates posting toolpaths in the active document.
- **Save and Insert File API Sample**: Demonstrates creating save a new file and then inserting it into a design. To use this sample, have a design open that has been saved and run the script. It will create a new design that contains a cylinder, save it to the same folder the active design was saved to, and then insert it into the active design.
- **Set part number using GraphQL**: Sets part number of root component and from occurrences via GQL query.

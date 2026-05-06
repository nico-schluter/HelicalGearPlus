# Documents
Namespace: adsk.core
Inherits: Base
Since: August 2014

The Documents object provides access to all of the currently open documents and provides methods to create and open documents.

**Accessed from:** Application.documents

## Methods

### add(documentType: DocumentTypes, visible: boolean, options: NamedValues) -> Document
Creates and opens a new document of the specified type.
- **documentType** (DocumentTypes): A value from the DocumentTypes enum that specifies the type of document to create.
- **visible** (boolean): Optional argument specifying is the document should be visible or not. Currently, documents can only be created visibly so this argument must always be true.

This is an optional argument whose default value is True.
- **options** (NamedValues): Various options that are supported that are specific to the document type. See the documentation for the DocumentTypes enum for information about the options supported for the various types.

This is an optional argument whose default value is null.
- **Returns** (Document): Returns the created document

### [static] classType() -> string
Static function that all classes support that returns the type of the class as a string. The returned string matches the string returned by the objectType property. For example if you have a reference to an object and you want to check if it's a SketchLine you can use myObject.objectType == fusion.SketchLine.classType().
- **Returns** (string): Returns a string indicating the type of the object.

### item(index: uinteger) -> Document
Function that returns the specified document using an index into the collection.
- **index** (uinteger): The index of the item within the collection to return. The first item in the collection has an index of 0.
- **Returns** (Document): Returns the specified item or null if an invalid index was specified.

### open(dataFile: DataFile, visible: boolean) -> Document
Opens an item that has previously been saved.
- **dataFile** (DataFile): The item to open.
- **visible** (boolean): Specifies if the document should be opened visibly or not.

This is an optional argument whose default value is True.
- **Returns** (Document): Returns the open document or null if the open failed.

## Properties

### count : uinteger [read-only]
Returns the number of currently open documents. This includes documents that are visible and invisible.

### isValid : boolean [read-only]
Indicates if this object is still valid, i.e. hasn't been deleted or some other action done to invalidate the reference.

### objectType : string [read-only]
This property is supported by all objects in the API and returns a string that contains the full name (namespace::objecttype) describing the type of the object.

It's often useful to use this in combination with the classType method to see if an object is a certain type. For example: if obj.objectType == adsk.core.Point3D.classType():

## Samples
- **Loft Feature API Sample**: Demonstrates creating a new loft feature.

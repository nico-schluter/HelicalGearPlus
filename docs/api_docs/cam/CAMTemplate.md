# CAMTemplate
Namespace: adsk.cam
Inherits: Base
Since: April 2023

Object that represents a template for a set of operations. These can be created from operations, optionally stored to files or in a library. The template can be used to re-create those operations in another document.

**Accessed from:** CAMTemplate.createEmpty, CAMTemplate.createFromFile, CAMTemplate.createFromOperations, CAMTemplate.createFromXML, CAMTemplate.createHoleTemplateFromOperations, CAMTemplateLibrary.childTemplates, CAMTemplateLibrary.templateAtURL, CreateFromCAMTemplateInput.camTemplate

## Methods

### [static] classType() -> string
Static function that all classes support that returns the type of the class as a string. The returned string matches the string returned by the objectType property. For example if you have a reference to an object and you want to check if it's a SketchLine you can use myObject.objectType == fusion.SketchLine.classType().
- **Returns** (string): Returns a string indicating the type of the object.

### createEmpty() -> CAMTemplate
Create an empty CAMTemplate
- **Returns** (CAMTemplate): Returns the newly created template.

### createFromFile(filePath: string) -> CAMTemplate
Create a CAMTemplate from a file on disk, i.e. Import the template file. Invalid files will produce errors
- **filePath** (string): The path to a template file.
- **Returns** (CAMTemplate): Returns the newly created template.

### createFromOperations(operations: Operation[]) -> CAMTemplate
Create a CAMTemplate from a list of Operations
- **operations** (Operation[]): An array of operations to bundle into a template.
- **Returns** (CAMTemplate): Returns the newly created template.

### createFromXML(xml: string) -> CAMTemplate
Creates a CAMTemplate from an XML string. Invalid template XML will produce errors
- **xml** (string): The XML representation to act as a base for creating a template.
- **Returns** (CAMTemplate): Returns the newly created template.

### createHoleTemplateFromOperations(operations: Operation[]) -> CAMTemplate
Create a hole CAMTemplate from a list of hole operations. Hole templates may be used in Hole Recognition
- **operations** (Operation[]): A list of operations to bundle into a template. Only 2D Adaptive, 2D Chamfer, 2D Contour, 2D Pocket, Bore, Circular, Drill and Thread operations are allowed in hole templates. Passing in other operation types will throw an error.
- **Returns** (CAMTemplate): Returns the newly created template.

### getHoleSignatureXML()
Convert hole signature to XML. This will be empty if this is not a hole template, or if there is no signature.

### save(filePath: string) -> boolean
Save the CAMTemplate to a file
- **filePath** (string): The path to the file you wish to save
- **Returns** (boolean): Returns true if the template was saved successfully, false otherwise.

### setHoleSignatureXML(xmlSnippet: string) -> boolean
Provide an XML snippet to specify a hole signature. This will have no effect if this is not a hole template. This will fail if the provided snippet is not valid.
- **Returns** (boolean): This will return true on success, false on failure.

## Properties

### attributes : Attributes [read-only]
Returns the collection of attributes associated with this template.

### description : string [read-write]
Gets and sets the description of the template.

### isHoleTemplate : boolean [read-only]
Whether or not this is a hole template

### isValid : boolean [read-only]
Indicates if this object is still valid, i.e. hasn't been deleted or some other action done to invalidate the reference.

### name : string [read-write]
Gets and sets the name of the template.

### objectType : string [read-only]
This property is supported by all objects in the API and returns a string that contains the full name (namespace::objecttype) describing the type of the object.

It's often useful to use this in combination with the classType method to see if an object is a certain type. For example: if obj.objectType == adsk.core.Point3D.classType():

### operations : CAMTemplateOperations [read-write]
Expose operations.

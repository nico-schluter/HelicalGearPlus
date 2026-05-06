# DrawingDocument
Namespace: adsk.drawing
Inherits: Document
Since: December 2020

Object that represents a Fusion 360 drawing document.

## Methods

### activate() -> boolean
Causes this document to become the active document in the user interface.
- **Returns** (boolean): Returns true if the activation was successful.

### [static] classType() -> string
Static function that all classes support that returns the type of the class as a string. The returned string matches the string returned by the objectType property. For example if you have a reference to an object and you want to check if it's a SketchLine you can use myObject.objectType == fusion.SketchLine.classType().
- **Returns** (string): Returns a string indicating the type of the object.

### close(saveChanges: boolean) -> boolean
Closes this document.
- **saveChanges** (boolean): This argument defines what the behavior of the close is when the document has been modified. If the document hasn't been modified then this argument is ignored and the document is closed. If the document has been modified and this argument is false then Fusion will close the document and lose any changes. If the document has been modified and this argument is true then it will prompt the user if they want to save the changes or not, just the same as if the user was to interactively close the document.
- **Returns** (boolean): Returns true if closing the document was successful.

### save(description: string) -> boolean
Saves a version of the current document. You must use the SaveAs method the first time a document is saved. You can determine if a document has been saved by checking the value of the isSaved property.
- **description** (string): The version description for this document
- **Returns** (boolean): Returns true if saving the document was successful.

### saveAs(name: string, dataFolder: DataFolder, description: string, tag: string) -> boolean
Performs a Save As on this document. This saves the currently open document to the specified location and this document becomes the saved document. If this is a new document that has never been saved you must use the SaveAs method in order to specify the location and name. You can determine if the document has been saved by checking the value of the isSaved property.
- **name** (string): The name to use for this document. If this is an empty string, Fusion will use the default name assigned when the document was created.
- **dataFolder** (DataFolder): The data folder to save this document to.
- **description** (string): The description string of the document. This can be an empty string.
- **tag** (string): The tag string of the document. This can be an empty string.
- **Returns** (boolean): Returns true if the save as was successful.

### saveDataVersion(versionDescription: string) -> boolean
Creates a version on a dirty document by implictly saving it first. This method is not applicable when saving a document for the first time. In that case, you must use the Document.saveAs method. You can determine if a document has been saved by checking the value of the isSaved property.
- **versionDescription** (string): The description associated with the data version.
- **Returns** (boolean): Returns true if saving the document with data version was successful.

### saveMilestone(milestoneName: string, versionDescription: string) -> boolean
Saves the document as a new milestone. This method is not applicable when saving a document for the first time. In that case, you must use the SaveAs method. You can determine if a document has been saved by checking the value of the isSaved property.
- **milestoneName** (string): The name of the milestone as seen in the data panel and Fusion web client. If an empty string is provided a default name will be used.
- **versionDescription** (string): The description associated with the version. If an empty string is provided, a default description will be used.
- **Returns** (boolean): Returns true if saving the document as a milestone was successful.

### updateAllReferences()
Updates all out of date external references. This is equivalent to clicking the "Out of Date" button in the Quick Access Toolbar to update all out of date external references.

## Properties

### allDocumentReferences : DocumentReferences [read-only]
Returns a collection containing all of the documents referenced directly by this document and those referenced by all sub-assemblies.

### attributes : Attributes [read-only]
Returns the collection of attributes associated with this document.

### creationId : string [read-only]
Returns the creation ID of this document. When a new document is created, Fusion assigns it a creation ID that will remain constant for the life of the document. The ID that is assigned is unique. However, it's possible that more than one document can have the same ID. This happens in the case where a document is copied. In this case a new document is created but an existing document is copied. It's only when a new document is created that a creation ID is generated and assigned.

Using this ID can be useful in cases where the save of a new document is started and you can use this ID to match the completion of the save operation on the cloud to the original document.

### dataFile : DataFile [read-only]
Gets the DataFile that represents this document in A360.

### documentReferences : DocumentReferences [read-only]
Returns a collection containing the documents directly referenced by this document.

### drawing : Drawing [read-only]
Returns the Drawing product object associated with this drawing document.

### isActive : boolean [read-only]
Gets if this document is the active document in the user interface.

### isModified : boolean [read-only]
Property that indicates if the document has been modified since it was last saved.

### isSaved : boolean [read-only]
Property that indicates if this document has been saved or not. The initial save of a document requires that the name and location be specified and requires the saveAs method to be used. If the document has been saved then the save method can be used to save changes made.

### isUpToDate : boolean [read-only]
Indicates if any external references in the assembly are out of date. This is the API equivalent to the "Out of Date" notification displayed in the Quick Access Toolbar.

### isValid : boolean [read-only]
Indicates if this object is still valid, i.e. hasn't been deleted or some other action done to invalidate the reference.

### isVisible : boolean [read-only]
Gets if a currently open document is open as visible.

### name : string [read-write]
This property gets and sets the name of the document. You can only set the name of a document before the document is saved for the first time. You can use the isSaved property to determine this. If the document has not been saved and the name is changed, the specified name will be the default name shown in the Save dialog, which the user can modify before saving the document.

If the file has been saved, this property behaves as read-only. Setting the name will fail because the name is controlled by the DataFile associated with this document. However, you can edit the name of the DataFile, which you can obtain by using the dataFile property of the document.

### objectType : string [read-only]
This property is supported by all objects in the API and returns a string that contains the full name (namespace::objecttype) describing the type of the object.

It's often useful to use this in combination with the classType method to see if an object is a certain type. For example: if obj.objectType == adsk.core.Point3D.classType():

### parent : Application [read-only]
Returns the parent Application object.

### products : Products [read-only]
Returns the products associated with this document.

### version : string [read-only]
Returns the Fusion version this document was last saved with.

# SharedLink
Namespace: adsk.core
Inherits: Base
Since: May 2024

Provides access to the URL that can be used to share this DataFile with others. This object also provides access to the various settings that control the link's behavior.

**Accessed from:** DataFile.sharedLink

## Methods

### [static] classType() -> string
Static function that all classes support that returns the type of the class as a string. The returned string matches the string returned by the objectType property. For example if you have a reference to an object and you want to check if it's a SketchLine you can use myObject.objectType == fusion.SketchLine.classType().
- **Returns** (string): Returns a string indicating the type of the object.

### setPassword(password: string) -> boolean
Sets the password to access the web page to view the file. Setting a password makes using the password required to access the page. The password takes effect immediately for anyone using the URL. To turn off the password requirement, set the isPasswordRequired property to false.
- **password** (string): The password to use.
- **Returns** (boolean): Returns true if setting the password was successful.

## Properties

### isDownloadAllowed : boolean [read-write]
Specifies if the user with the shared link can download the file or only view it. Changing this setting changes the behavior of the existing link. When a DataFile is shared, and a link is created, this defaults to true, allowing anyone with the link to download the file.

### isPasswordRequired : boolean [read-write]
Gets if a password is required to access the file's web page using the link URL. This property can be set to false to turn off the password requirement. It cannot be set to true. To enable a password, use the setPassword method, which sets the password and has the side effect of setting this property to true.

### isShared : boolean [read-write]
Gets and sets if a shared link should be made available for this DataFile. This property defaults to false for a new DataFile. Setting it to true will allow the URL for the file to be obtained. Setting it to false will restrict access to the URL and block access for anyone currently using it. In other words, this is a dynamic setting and doesn't just control getting the link URL.

### isValid : boolean [read-only]
Indicates if this object is still valid, i.e. hasn't been deleted or some other action done to invalidate the reference.

### linkURL : string [read-only]
Returns the URL of the shared link. Returns an empty string in the case where isShared is False.

### objectType : string [read-only]
This property is supported by all objects in the API and returns a string that contains the full name (namespace::objecttype) describing the type of the object.

It's often useful to use this in combination with the classType method to see if an object is a certain type. For example: if obj.objectType == adsk.core.Point3D.classType():

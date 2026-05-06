# ApplicationEventArgs
Namespace: adsk.core
Inherits: EventArgs
Since: January 2016

The ApplicationEventArgs provides information associated with an application event. Note that some properties are not available on every event

## Methods

### [static] classType() -> string
Static function that all classes support that returns the type of the class as a string. The returned string matches the string returned by the objectType property. For example if you have a reference to an object and you want to check if it's a SketchLine you can use myObject.objectType == fusion.SketchLine.classType().
- **Returns** (string): Returns a string indicating the type of the object.

## Properties

### firingEvent : Event [read-only]
The event that the firing is in response to.

### hasInternetAccess : boolean [read-only]
Gets if the client computer has access to the Internet.

### isOffLine : boolean [read-write]
Gets and sets if Fusion is offline or not.

### isValid : boolean [read-only]
Indicates if this object is still valid, i.e. hasn't been deleted or some other action done to invalidate the reference.

### objectType : string [read-only]
This property is supported by all objects in the API and returns a string that contains the full name (namespace::objecttype) describing the type of the object.

It's often useful to use this in combination with the classType method to see if an object is a certain type. For example: if obj.objectType == adsk.core.Point3D.classType():

## Samples
- **Application Event API Sample**: Add-In that demonstrates application events. To use this sample, create a new folder using the name you want to use for the new add-in. Inside the folder, create a new file that is the same name as the folder but has a .py extension. Copy the code below into the .py file. Create another file that is the same name as the folder but has a .manifest extension and copy the JSON data below into that file.

{
"autodeskProduct": "Fusion360",
"type": "addin",
"author": "",
"description": {
"": ""
},
"supportedOS": "windows|mac",
"editEnabled": true
}

Run the "Scripts and Add-Ins" command and click the green plus button near the top of the dialog. Browse to the location where you created the folder and select the folder. The add-in should now be displayed in the list of add-ins on the "Add-Ins" tab of the dialog. Select the add-in and click the "Run" button. This will load the add-in and when any of the application events occurr that it is watching for it will report them in the TEXT COMMAND window.

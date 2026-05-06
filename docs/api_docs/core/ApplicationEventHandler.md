# ApplicationEventHandler
Namespace: adsk.core
Inherits: EventHandler
Since: January 2016

The ApplicationEventHandler is a client implemented class that can be added as a handler to an ApplicationEvent.

## Methods

### notify(eventArgs: ApplicationEventArgs)
The function called by Fusion when the associated event is fired.
- **eventArgs** (ApplicationEventArgs): Returns an object that provides access to additional information associated with the event.

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

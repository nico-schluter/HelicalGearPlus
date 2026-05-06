# ProgressBar
Namespace: adsk.core
Inherits: Base
Since: May 2024

Provides access to the progress bar.

**Accessed from:** UserInterface.progressBar

## Methods

### [static] classType() -> string
Static function that all classes support that returns the type of the class as a string. The returned string matches the string returned by the objectType property. For example if you have a reference to an object and you want to check if it's a SketchLine you can use myObject.objectType == fusion.SketchLine.classType().
- **Returns** (string): Returns a string indicating the type of the object.

### hide() -> boolean
Hides the progress or busy bar. This should be used when the process has completed.
- **Returns** (boolean): Returns true if successful.

### show(message: string, minimumValue: integer, maximumValue: integer, isModal: boolean) -> boolean
This method displays a message in the progress bar in the lower-right corner of the Fusion window. The progress bar can be used to display a continually updated message indicating the progress of a process. The progress is determined by comparing the current progress value with the minimum and maximum values.
- **message** (string): Specifies the message that will be displayed in the progress bar. The following symbols can be used to display values. "%p" is replaced by the percentage completed. "%v" is replaced by the current value. "%m" is replaced by the total number of steps. For example, the message "Processing section %v of %m." will result in the message "Processing section 1 of 10." to be displayed if the maximum value is 10 and the current value is 1.

An empty string can be specified if you don't want a message and use only the progress meter.
- **minimumValue** (integer): Specifies the minimum value of the progress. This value and the maximum and progress values to compute the current percentage complete. This is the initial progress value when the progress bar is first displayed.
- **maximumValue** (integer): Specifies the maximum value of the progress. This value and the minimum and progress values are used to compute the current percentage completion.
- **isModal** (boolean): Specifies if the progress bar should be modal or not. If modal, the progress bar takes over the UI of Fusion, and the user cannot interact with any of the Fusion user interface. You need to be careful when using a modal dialog to make sure you hide the progress bar when you're finished or have an error condition that causes you to abort because otherwise, the user will need to kill the Fusion process.

This is an optional argument whose default value is False.
- **Returns** (boolean): Returns true if successful.

### showBusy(message: string, isModal: boolean) -> boolean
This method displays a message in the busy bar in the lower-right corner of the Fusion window. The busy bar can be used to display a continually updated message indicating the progress of a process. The busy bar is different from the progress bar, because it does not show a meter indicating the current progress. Instead is shows a continually moving bar to indicate processing without showing the current progress. This is useful in cases where the length of the process is unknown.
- **message** (string): Specifies the message that will be displayed in the busy bar. An empty string can be specified if you don't want a message and use only the busy meter.
- **isModal** (boolean): Specifies if the busy bar should be modal or not. If modal, the busy bar takes over the UI of Fusion, and the user cannot interact with any of the Fusion user interface. You need to be careful when using a modal dialog to make sure you hide the busy bar when you're finished or have an error condition that causes you to abort because otherwise, the user will need to kill the Fusion process.

This is an optional argument whose default value is False.
- **Returns** (boolean): Returns true if successful.

## Properties

### isValid : boolean [read-only]
Indicates if this object is still valid, i.e. hasn't been deleted or some other action done to invalidate the reference.

### message : string [read-write]
Gets and sets the message to display in the progress bar. The following symbols can be used to display values. "%p" is replaced by the percentage completed. "%v" is replaced by the current value. %m is replaced by the total number of steps. For example, the message "Processing section %v of %m." will result in the message "Processing section 1 of 10." to be displayed if the maximum value is 10 and the current value is 1.

When a busy bar is displayed, only a simple message is supported and symbols are not supported.

If your process is running in the main thread of Fusion, you will need to call adsk.doEvents to give control back to Fusion, so it can update the UI.

### objectType : string [read-only]
This property is supported by all objects in the API and returns a string that contains the full name (namespace::objecttype) describing the type of the object.

It's often useful to use this in combination with the classType method to see if an object is a certain type. For example: if obj.objectType == adsk.core.Point3D.classType():

### progressValue : integer [read-write]
Gets and sets the current progress value. This value determines the progress based on this value relative to the minimum and maximum values specified when the progress bar was created. This will also update the values displayed in the message string.

If your process is running in the main thread of Fusion, you will need to call adsk.doEvents to give control back to Fusion, so it can update the UI.

This value is ignored when a busy bar is displayed.

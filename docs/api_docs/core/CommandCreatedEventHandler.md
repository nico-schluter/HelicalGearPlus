# CommandCreatedEventHandler
Namespace: adsk.core
Inherits: EventHandler
Since: August 2014

Class that contains the call back function that is called when the CommandCreated event is fired.

## Methods

### notify(eventArgs: CommandCreatedEventArgs)
This notify member is called when an event is triggered from any event that this handler has been added to.
- **eventArgs** (CommandCreatedEventArgs): The arguments object with details about this event and the firing CommandEvent.

## Samples
- **Command Inputs API Sample**: Creates a command dialog that demonstrates all of the available command inputs.


To use the sample, create a new Python or C++ script and copy and paste this code, replacing the default code. You also need to unpack this zip file which contains a resource folder into the same folder where the source code file (.py or .cpp) is.

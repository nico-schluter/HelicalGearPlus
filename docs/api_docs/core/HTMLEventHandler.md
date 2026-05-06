# HTMLEventHandler
Namespace: adsk.core
Inherits: EventHandler
Since: March 2017

The HTMLEventHandler is a client implemented class that can be added as a handler to a HTML event which is triggered by JavaScript that associated with HTML displayed within a palette calling the adsk.fusionSendData function to send data from the HTML back to your add-in.

## Methods

### notify(eventArgs: HTMLEventArgs)
The function called by Fusion when the associated event is fired.
- **eventArgs** (HTMLEventArgs): Returns an object that provides access to additional information associated with the event.

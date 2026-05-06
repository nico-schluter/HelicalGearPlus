# MFGDMDataEventHandler
Namespace: adsk.core
Inherits: EventHandler
Since: July 2025

The MFGDMDataEventHandler is a client implemented class that can be added as a handler to a MFGDMDataEvent.

## Methods

### notify(eventArgs: MFGDMDataEventArgs)
The function called by Fusion when the associated event is fired.
- **eventArgs** (MFGDMDataEventArgs): Returns an object that provides access to additional information associated with the event.

## Samples
- **Gets all properties using GraphQL**: Fetches bulk component properties of the root component and from occurrences via single GraphQL query.
- **Get part number using GraphQL**: Fetches part number of root component and from occurrences via GQL query.
- **Set part number using GraphQL**: Sets part number of root component and from occurrences via GQL query.

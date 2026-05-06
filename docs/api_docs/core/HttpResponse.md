# HttpResponse
Namespace: adsk.core
Inherits: Base
Since: January 2024

An object that provides the data associated with an HTTP response.

**Accessed from:** HttpEventArgs.response, HttpRequest.executeSync

## Methods

### [static] classType() -> string
Static function that all classes support that returns the type of the class as a string. The returned string matches the string returned by the objectType property. For example if you have a reference to an object and you want to check if it's a SketchLine you can use myObject.objectType == fusion.SketchLine.classType().
- **Returns** (string): Returns a string indicating the type of the object.

### getHeader(name: string) -> string
Gets the value of a header.
- **name** (string): The case insensitive name of the header.
- **Returns** (string): Returns the value of the header, or empty if the header was not found. You can use the hasHeader method to determine if the header exists before getting it. This is especially useful in the case where the header exists but has an empty string value.

### hasHeader(name: string) -> boolean
Gets if the response has a header with the given name. This is useful to distinguish between the case where a header is not set and the case where a header is set to an empty string.
- **name** (string): The case insensitive name of the header.
- **Returns** (boolean): True if a header with this name was set in the response.

### headers(names: string[], values: string[]) -> boolean
Get the response headers.
- **names** (string[]): An array of all the header key names.
- **values** (string[]): An array of all the header values.
- **Returns** (boolean): Returns true on success or false on error.

## Properties

### data : string [read-only]
Gets the response body data.

### isValid : boolean [read-only]
Indicates if this object is still valid, i.e. hasn't been deleted or some other action done to invalidate the reference.

### objectType : string [read-only]
This property is supported by all objects in the API and returns a string that contains the full name (namespace::objecttype) describing the type of the object.

It's often useful to use this in combination with the classType method to see if an object is a certain type. For example: if obj.objectType == adsk.core.Point3D.classType():

### request : HttpRequest [read-only]
Gets the request that generated this response.

### statusCode : integer [read-only]
Gets the status code of the response.

## Samples
- **Gets all properties using GraphQL**: Fetches bulk component properties of the root component and from occurrences via single GraphQL query.
- **Get part number using GraphQL**: Fetches part number of root component and from occurrences via GQL query.
- **Set part number using GraphQL**: Sets part number of root component and from occurrences via GQL query.

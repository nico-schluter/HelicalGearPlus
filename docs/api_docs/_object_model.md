# Fusion 360 API — Object Model Navigation

This guide shows how to navigate from the Application root to key objects.
Use this to understand how to reach the object you need.

## Entry Points

```python
import adsk.core, adsk.fusion, adsk.cam

app = adsk.core.Application.get()         # The Application singleton
ui = app.userInterface                     # UI for dialogs, commands, palettes
doc = app.activeDocument                   # Current open document
product = app.activeProduct                # Current product (Design, CAM, etc)
design = adsk.fusion.Design.cast(product)  # Cast to Design for modeling
rootComp = design.rootComponent            # Root component of the design
```

## Key Navigation Paths

**Get all bodies in root component**
`rootComp.bRepBodies → BRepBodies collection`

**Get bodies from any component**
`component.bRepBodies → BRepBodies`

**Get all occurrences (component instances)**
`rootComp.occurrences → Occurrences → each has .component`

**Traverse full assembly recursively**
`rootComp.allOccurrences → flat list of all nested occurrences`

**Access sketches**
`rootComp.sketches → Sketches collection → .add(plane) to create`

**Create features (extrude, revolve, etc)**
`rootComp.features → Features → .extrudeFeatures, .revolveFeatures, etc`

**Access construction geometry**
`rootComp.constructionPlanes / .constructionAxes / .constructionPoints`

**Work with parameters**
`design.allParameters / design.userParameters → ParameterList`

**Access the timeline**
`design.timeline → Timeline`

**Get/set materials and appearances**
`design.appearances / app.materialLibraries`

**Export/import files**
`design.exportManager / app.importManager`

**CAM operations**
`adsk.cam.CAM.cast(product) → .setups → Setup → .operations`

**Create temporary B-Rep bodies (no document overhead)**
`adsk.fusion.TemporaryBRepManager.get() — boolean ops, primitives, transforms`

**Custom UI commands**
`ui.commandDefinitions.addButtonDefinition() → CommandCreatedEvent`

**Custom graphics (overlays)**
`rootComp.customGraphicsGroups → add lines, meshes, text`

**Access attributes (custom metadata)**
`any entity .attributes collection → Attributes.add(groupName, name, value)`

**Joints and motion**
`rootComp.joints / .asBuiltJoints / .jointOrigins`

**Sheet metal**
`component.flatPattern → FlatPattern`

## Important Utility Classes

- **TemporaryBRepManager**: Create/modify B-Rep bodies outside document context. Boolean ops, primitive creation, transforms. Backbone of many add-ins.
- **ValueInput**: Wraps numeric values for feature creation. Use ValueInput.createByReal(val) or ValueInput.createByString('10 mm').
- **Matrix3D**: 3D transformation matrix. Use for positioning, rotating, transforming objects.
- **Point3D / Vector3D**: Core geometry types. All coordinates are in cm.
- **ObjectCollection**: Generic collection for passing multiple objects to methods.
- **CustomGraphicsGroup**: Add visual overlays without modifying the model.
- **Attributes**: Attach custom key-value metadata to any design entity.
- **BaseFeature**: Container for externally-created B-Rep bodies added to the timeline.

## Units

All internal values are in **centimeters** (lengths), **radians** (angles).
Use `design.unitsManager` to convert to/from user display units.

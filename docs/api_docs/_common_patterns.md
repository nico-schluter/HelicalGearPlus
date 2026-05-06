# Fusion 360 API — Common Patterns

## Add-in Skeleton

```python
import adsk.core, adsk.fusion, traceback

def run(context):
    app = adsk.core.Application.get()
    ui = app.userInterface
    try:
        # Your code here
        design = adsk.fusion.Design.cast(app.activeProduct)
        rootComp = design.rootComponent
        pass
    except:
        if ui:
            ui.messageBox(traceback.format_exc())
```

## Create a Simple Extrusion

```python
# Create sketch on XY plane
sketches = rootComp.sketches
xyPlane = rootComp.xYConstructionPlane
sketch = sketches.add(xyPlane)

# Draw a rectangle
lines = sketch.sketchCurves.sketchLines
rect = lines.addTwoPointRectangle(
    adsk.core.Point3D.create(0, 0, 0),
    adsk.core.Point3D.create(5, 5, 0)  # 5cm x 5cm
)

# Get profile and extrude
profile = sketch.profiles.item(0)
extrudes = rootComp.features.extrudeFeatures
dist = adsk.core.ValueInput.createByReal(2.0)  # 2cm
ext = extrudes.addSimple(profile, dist, adsk.fusion.FeatureOperations.NewBodyFeatureOperation)
```

## TemporaryBRepManager — Create and Combine Shapes

```python
# Get the temp B-Rep manager
tempMgr = adsk.fusion.TemporaryBRepManager.get()

# Create a box
box = tempMgr.createBox(adsk.core.OrientedBoundingBox3D.create(
    adsk.core.Point3D.create(0, 0, 0),
    adsk.core.Vector3D.create(1, 0, 0),
    adsk.core.Vector3D.create(0, 1, 0),
    10, 10, 10  # 10cm cube
))

# Create a cylinder to subtract
cyl = tempMgr.createCylinderOrCone(
    adsk.core.Point3D.create(5, 5, 0),  # bottom center
    3,  # radius in cm
    adsk.core.Point3D.create(5, 5, 10), # top center
    3   # top radius (same = cylinder)
)

# Boolean subtract: box - cylinder
tempMgr.booleanOperation(box, cyl, adsk.fusion.BooleanTypes.DifferenceBooleanType)

# Add result to the design via BaseFeature
baseFeature = rootComp.features.baseFeatures.add()
baseFeature.startEdit()
rootComp.bRepBodies.add(box, baseFeature)
baseFeature.finishEdit()
```

## Register a Custom Command

```python
import adsk.core, adsk.fusion

handlers = []  # Must keep references alive

class MyCommandCreatedHandler(adsk.core.CommandCreatedEventHandler):
    def notify(self, args):
        cmd = args.command
        inputs = cmd.commandInputs
        inputs.addValueInput('length', 'Length', 'mm',
                             adsk.core.ValueInput.createByString('10 mm'))
        # Add execute handler...

def run(context):
    app = adsk.core.Application.get()
    ui = app.userInterface
    cmdDef = ui.commandDefinitions.addButtonDefinition(
        'myCommand', 'My Command', 'Does something useful')
    handler = MyCommandCreatedHandler()
    cmdDef.commandCreated.add(handler)
    handlers.append(handler)
    cmdDef.execute()
```

## Traverse All Bodies in Assembly

```python
def getAllBodies(component):
    bodies = []
    for body in component.bRepBodies:
        bodies.append(body)
    for occ in component.occurrences:
        bodies.extend(getAllBodies(occ.component))
    return bodies
```

## Key Tips

- All lengths in **cm**, all angles in **radians**
- Use `adsk.fusion.Design.cast(app.activeProduct)` to get the design
- Use `TemporaryBRepManager` for complex geometry — much faster than parametric features
- Keep event handler references alive in a global list or they get garbage collected
- Use `BaseFeature` to add externally-created bodies to the design timeline
- Use `design.findEntityByToken()` to persist references across sessions
- Check `isValid` before using any object reference that might be stale
- Use deferred compute to do multiple sketch changes without a full recompute each time


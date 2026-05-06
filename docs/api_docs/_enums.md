# Fusion 360 API — Enums Reference

All enumeration types in the Fusion 360 API, grouped by namespace.

# adsk.cam

## AdditiveTechnologies
Namespace: adsk.cam
List of technologies a additive machine could have
Defined in namespace "adsk::cam" and the header file is <Cam\CamTypeDefs.h>

| Name | Value | Description |
|------|-------|-------------|
| BinderJettingTechnology | 4 | Multi fusion jet additive manufacturing process |
| DEDTechnology | 1 | Directed energy deposition additive manufacturing process. |
| EbeamTechnology | 9 | Electron Beam Technology |
| FFFTechnology | 0 | Fused filament fabrication additive manufacturing process. |
| MFJTechnology | 3 | Multi fusion jet additive manufacturing process |
| MPBFTechnology | 2 | Machine powder bed fusion additive manufacturing process. |
| NATechnology | 7 | Non Additive Technology, meaning this is not a additive machine |
| OtherTechnology | 8 | Every other additive manufacturing process not covered by the types above |
| SLATechnology | 5 | Stereo lithographic apparatus additive manufacturing process |
| SLSTechnology | 6 | Selective laser sintering additive manufacturing process |

## ArrangePriorityTypes
Namespace: adsk.cam
Enum for the types of priority for an arrange selection.
Defined in namespace "adsk::cam" and the header file is <Cam\CamTypeDefs.h>

| Name | Value | Description |
|------|-------|-------------|
| HighArrangePriorityType | 1 | High arrange priority |
| LowArrangePriorityType | 3 | Low arrange priority |
| MediumArrangePriorityType | 2 | Medium arrange priority |
| VeryHighArrangePriorityType | 0 | Very high arrange priority |
| VeryLowArrangePriorityType | 4 | Very low arrange priority |

## AutomaticGenerationModes
Namespace: adsk.cam
Defines the automatic generation during the creation of an operation using OperationInput or createFromCAMTemplate2.
Defined in namespace "adsk::cam" and the header file is <Cam\CamTypeDefs.h>

| Name | Value | Description |
|------|-------|-------------|
| ForceGeneration | 0 | Generate newly created operations. |
| SkipGeneration | 1 | Do not generate newly created operations. |
| UserPreference | 2 | Generate operations based on the preference set in the options UI. |

## CAM3MFSupportInclusionType
Namespace: adsk.cam
Sets how the support should be included into the 3mf Options are not to be included, as 3mf support object or as 3mf model object
Defined in namespace "adsk::cam" and the header file is <Cam\CamTypeDefs.h>

| Name | Value | Description |
|------|-------|-------------|
| IncludeAsModelType | 2 | Include the support as 3mf model object |
| IncludeAsSupportType | 1 | Include the support as 3mf support object |
| NotIncluded | 0 | Don't include the support. |

## CAMAdditiveContainerTypes
Namespace: adsk.cam
Enum specifying the types of additive containers available in Fusion. Some additive containers not listed here are available via other API classes, i.e. PrintSetting
Defined in namespace "adsk::cam" and the header file is <Cam\CamTypeDefs.h>

| Name | Value | Description |
|------|-------|-------------|
| AdditiveProcessSimulationCAMAdditiveContainerType | 3 | Contains all additive process simulation studies. Containers of this type cannot be deleted. |
| BodyPresetCAMAdditiveContainerType | 2 | Contains all body presets used in the setup. Containers of this type cannot be deleted. |
| OptimizedOrientationCAMAdditiveContainerType | 1 | Contains all optimized orientation operations. |
| SupportCAMAdditiveContainerType | 0 | Contains all support operations. |

## DefaultGroupType
Namespace: adsk.cam
Types of default groups. Used to specify which default group to be retrieved by defaultGroup method.
Defined in namespace "adsk::cam" and the header file is <Cam\CamTypeDefs.h>

| Name | Value | Description |
|------|-------|-------------|
| Adjacent_GroupType | 5 | Group containing Adjacent surfaces. |
| Drive_GroupType | 2 | Group containing Drive surfaces. |
| Fixture_GroupType | 0 | Group containing surfaces belonging to the fixture. Some of these may have been defined in the setup. |
| Floor_GroupType | 3 | Group containing Floor surfaces. |
| Model_GroupType | 1 | Group containing surfaces belonging to the model. These have been defined in the setup or using the model override selector. |
| Wall_GroupType | 4 | Group containing Wall surfaces. |

## ExtensionMethods
Namespace: adsk.cam
Enum for the types of extension methods for a chain selection. It defines how open curves are extended on their open end.
Defined in namespace "adsk::cam" and the header file is <Cam\CamTypeDefs.h>

| Name | Value | Description |
|------|-------|-------------|
| ClosestBoundaryExtensionMethod | 1 | Closest boundary type of extension. |
| ParallelExtensionMethod | 2 | Parallel type of extension. |
| TangentExtensionMethod | 0 | Tangent type of extension. |

## ExtensionTypes
Namespace: adsk.cam
Enum for types of extension capping.
Defined in namespace "adsk::cam" and the header file is <Cam\CamTypeDefs.h>

| Name | Value | Description |
|------|-------|-------------|
| BoundaryExtensionType | 0 | Caps the extended curves at the stock. |
| DistanceExtensionType | 1 | Caps the extended curves depending on the startExtensionLength and endExtensionLength properties. |

## FloatParameterValueTypes
Namespace: adsk.cam
Defines the type of a FloatParameterValue.
Defined in namespace "adsk::cam" and the header file is <Cam\CamTypeDefs.h>

| Name | Value | Description |
|------|-------|-------------|
| AngleValueType | 2 | Angle in radians (rad) |
| AreaValueType | 9 | Area in square centimeters (cm²) |
| FlowRateValueType | 8 | Flow rate in liters/minute (l/min) |
| LengthValueType | 1 | Length in centimeters (cm) |
| LinearVelocityValueType | 3 | Linear velocity in millimeters/minute (mm/min) |
| PowerValueType | 7 | Power in Watts (W) |
| RotationalVelocityValueType | 4 | Rotational velocity in revolutions per minute (rpm) |
| TemperatureValueType | 11 | Temperature in degrees Celsius (C) |
| TimeValueType | 5 | Time in seconds (s) |
| UnspecifiedValueType | 0 | Unspecified type can reprecent any type |
| VolumeValueType | 10 | Volume in cubic centimeters (cm³) |
| WeightValueType | 6 | Weight in kilograms (kg) |

## FusionHubExecutionBehaviors
Namespace: adsk.cam
Enum to define the behavior when posting to Fusion hub.
Defined in namespace "adsk::cam" and the header file is <Cam\CamTypeDefs.h>

| Name | Value | Description |
|------|-------|-------------|
| FusionHubExecutionBehavior_ExportWithRelationship | 2 | Post to Fusion Hub while setting the parent document as a relationship. In the UI this will raise a "save document" dialog if the parent document's save state is not up to date. Cancelling the dialog, or if none is shown, will result in the document not being saved and the post result being exported without setting the relationship in Fusion Hub. This is the default value. |
| FusionHubExecutionBehavior_ForceExportWithRelationship | 0 | Post to Fusion Hub while setting the parent document as a relationship. In the UI this will raise a "save document" dialog if the parent document's save state is not up to date. Cancelling the dialog, or if none is shown, will result in the document not being saved and the post result not being exported. |
| FusionHubExecutionBehavior_SilentForceExportWithRelationship | 1 | Post to Fusion Hub while setting the parent document as a relationship. The document and post result are both saved in the Fusion Hub folder specified. If the document has not been saved before, then a new document named "NCProgramPostProcess_YYYYMMDD_HH:MM:SS" will be created with YYYYMMDD_HH:MM:SS being substituted with the current date time. |
| FusionHubExecutionBehavior_SkipRelationship | 3 | Post to Fusion Hub without setting the parent document as a relationship. The parent document does not need to be saved to post to Fusion Hub. |

## GeneratedDataType
Namespace: adsk.cam
Enum for the identifiers of generated results an OperationBase object can have
Defined in namespace "adsk::cam" and the header file is <Cam\CamTypeDefs.h>

| Name | Value | Description |
|------|-------|-------------|
| AdditiveFEAGeneratedDataType | 1 | Additive FEA identifier. |
| OptimizedOrientationGeneratedDataType | 0 | Optimized orientation identifier |

## HoleSegmentType
Namespace: adsk.cam
Represents the recognized geometric shape of a hole segment.
Defined in namespace "adsk::cam" and the header file is <Cam\CamTypeDefs.h>

| Name | Value | Description |
|------|-------|-------------|
| HoleSegmentTypeCone | 1 | Hole segment is conical in shape. |
| HoleSegmentTypeCylinder | 0 | Hole segment is cylindrical in shape. |
| HoleSegmentTypeFlat | 2 | Hole segment is flat in shape, i.e. planar and perpendicular to the hole axis. |
| HoleSegmentTypeTorus | 3 | Hole segment is toroidal in shape. |

## LibraryLocations
Namespace: adsk.cam
List of locations representing folders in the library dialogs.
Defined in namespace "adsk::cam" and the header file is <Cam\CamTypeDefs.h>

| Name | Value | Description |
|------|-------|-------------|
| CloudLibraryLocation | 1 | Represents the cloud folder in the library. |
| ExternalLibraryLocation | 4 | Represents an external folder that is not in the library. |
| Fusion360LibraryLocation | 5 | Represents the fusion 360 folder in the library. |
| HubLibraryLocation | 6 | Represents the hub libraries folder in the library. |
| LocalLibraryLocation | 0 | Represents the local folder in the library. |
| NetworkLibraryLocation | 2 | Represents the network folder in the library. For internal use only. |
| OnlineSamplesLibraryLocation | 3 | Represents the online samples folder in the library. For internal use only. |

## LoopTypes
Namespace: adsk.cam
Enum to define the type of loop for a face contour selection.
Defined in namespace "adsk::cam" and the header file is <Cam\CamTypeDefs.h>

| Name | Value | Description |
|------|-------|-------------|
| AllLoops | 0 | Specifies inside and outside loops of the selected geometry. |
| OnlyInsideLoops | 2 | Specifies only the inner contours. There can be none or any number of inner contours per entity. |
| OnlyOutsideLoops | 1 | Specifies only the outer contours of the loop. There is only one outer contour per entity. |

## MachineAnglePreferences
Namespace: adsk.cam
Preference for rotary axis starting angles.
Defined in namespace "adsk::cam" and the header file is <Cam\CamTypeDefs.h>

| Name | Value | Description |
|------|-------|-------------|
| MachineAngleNoPreference | 0 | No preference, use any solution. |
| MachineAnglePreferNegative | 1 | Prefer starting rotary axis with a negative tilt. |
| MachineAnglePreferPositive | 2 | Prefer starting rotary axis with a positive tilt. |

## MachineAxisCoordinates
Namespace: adsk.cam
Options to control which coordinate is used for post processing, independent of the axis direction. Instructs the post processor to treat the axis as X, Y, or Z for linear and A, B, or C for rotary.
Defined in namespace "adsk::cam" and the header file is <Cam\CamTypeDefs.h>

| Name | Value | Description |
|------|-------|-------------|
| MachineCoordinate_None | 0 | Axis has no coordinate set. |
| MachineCoordinate_X_A | 1 | Axis coordinate Linear X, Rotary A |
| MachineCoordinate_Y_B | 2 | Axis coordinate Linear Y, Rotary B |
| MachineCoordinate_Z_C | 3 | Axis coordinate Linear X, Rotary C |

## MachineAxisTypes
Namespace: adsk.cam
List of machine axis types for MachineAxis
Defined in namespace "adsk::cam" and the header file is <Cam\CamTypeDefs.h>

| Name | Value | Description |
|------|-------|-------------|
| LinearMachineAxisType | 0 | An axis that moves in a straight line |
| RotaryMachineAxisType | 1 | An axis that rotates about a point |

## MachineCoolant
Namespace: adsk.cam
Enumeration of possible coolants that a machine can use.
Defined in namespace "adsk::cam" and the header file is <Cam\CamTypeDefs.h>

| Name | Value | Description |
|------|-------|-------------|
| MachineCoolant_AIR | 3 |  |
| MachineCoolant_AIR_THROUGH_TOOL | 4 |  |
| MachineCoolant_FLOOD | 0 |  |
| MachineCoolant_FLOOD_MIST | 6 |  |
| MachineCoolant_FLOOD_THROUGH_TOOL | 7 |  |
| MachineCoolant_MIST | 1 |  |
| MachineCoolant_SUCTION | 5 |  |
| MachineCoolant_THROUGH_TOOL | 2 |  |

## MachineElementInputType
Namespace: adsk.cam
Enumeration of the types of machine element inputs that can be created.
Defined in namespace "adsk::cam" and the header file is <Cam\CamTypeDefs.h>

| Name | Value | Description |
|------|-------|-------------|
| ExtruderElement | 2 |  |
| LaserElement | 3 |  |
| MultiAxisElement | 0 |  |
| ToolingCapabilityElement | 1 |  |

## MachineItemType
Namespace: adsk.cam
Enumeration of possible MachineItem types.
Defined in namespace "adsk::cam" and the header file is <Cam\CamTypeDefs.h>

| Name | Value | Description |
|------|-------|-------------|
| MachineItemType_FIXTURE | 4 |  |
| MachineItemType_INVALID | 9 |  |
| MachineItemType_MACHINE_PART | 6 |  |
| MachineItemType_MODEL | 5 |  |
| MachineItemType_STOCK | 3 |  |
| MachineItemType_TOOL | 0 |  |
| MachineItemType_TOOL_CUTTER | 1 |  |
| MachineItemType_TOOL_NONCUTTER | 2 |  |
| MachineItemType_TURRET_ACTIVE_TOOL | 7 |  |
| MachineItemType_TURRET_INACTIVE_TOOL | 8 |  |

## MachineNonTCPInterpolationMode
Namespace: adsk.cam
Interpolation modes available for non-TCP motions.
Defined in namespace "adsk::cam" and the header file is <Cam\CamTypeDefs.h>

| Name | Value | Description |
|------|-------|-------------|
| MachineNonTCPInterpolationMode_IndependentAxes | 1 | Moves the axes together, completing the motion simultaneously, although the tool's tip may deviate from the direct line between the start and finish points. |
| MachineNonTCPInterpolationMode_SynchronizedAxes | 0 | Moves the axes independently at maximum speed, potentially resulting in different completion times for each axis |

## MachinePartTypes
Namespace: adsk.cam
List of part types for MachinePart
Defined in namespace "adsk::cam" and the header file is <Cam\CamTypeDefs.h>

| Name | Value | Description |
|------|-------|-------------|
| AxisMachinePartType | 1 | Part type for a part that represents a machine axis. |
| BasicMachinePartType | 0 | Basic type for machine parts. Can be used to represent non-moving elements of the machine such as the machine's base or an enclosure. |
| FixtureAttachmentMachinePartType | 3 | Part type for a part that represents the attachment point and orientation for work holding. |
| ToolAttachmentMachinePartType | 2 | Part type for a part that represents the attachment point and orientation for a tool or tool holder. |

## MachineResetOptions
Namespace: adsk.cam
Axis reset preference options for MachineAxisConfiguration.whenToReset.
Defined in namespace "adsk::cam" and the header file is <Cam\CamTypeDefs.h>

| Name | Value | Description |
|------|-------|-------------|
| MachineResetBeforeEveryOperation | 1 | Reset axis to zero before each operation begins. |
| MachineResetBeforeOpAndOnRewind | 3 | Reset axis to zero before each operation begins and during automated rewinds. |
| MachineResetNever | 0 | Remember axis position from previous operation |
| MachineResetOnRewind | 2 | Reset axis to zero during automated rewinds. |

## MachineTCPInterpolationMode
Namespace: adsk.cam
Interpolation modes available for TCP motions.
Defined in namespace "adsk::cam" and the header file is <Cam\CamTypeDefs.h>

| Name | Value | Description |
|------|-------|-------------|
| MachineTCPInterpolationMode_IndependentAxes | 1 | Moves the axes together, completing the motion simultaneously, although the tool's tip may deviate from the direct line between the start and finish points. |
| MachineTCPInterpolationMode_SynchronizedAxes | 0 | Moves the axes independently at maximum speed, potentially resulting in different completion times for each axis |
| MachineTCPInterpolationMode_ToolTip | 2 | Adjusts the linear axes to keep the tool's tip positioned along the direct line between the start and finish points. |

## MachineTemplate
Namespace: adsk.cam
List of the machine templates to create a machine from.
Defined in namespace "adsk::cam" and the header file is <Cam\CamTypeDefs.h>

| Name | Value | Description |
|------|-------|-------------|
| Generic3Axis | 1 | Represents a generic 3 axis machine with 3 linear axes. |
| Generic4Axis | 2 | Represents a generic 4 axis machine with 3 linear axes and 1 rotary. Default rotary axis is A. |
| Generic5AxisHeadHead | 3 | Represents a generic 5 axis machine with 3 linear axes and 2 rotary. Default rotary axes are A and C in a Head-Head configuration. |
| Generic5AxisHeadTable | 4 | Represents a generic 5 axis machine with 3 linear axes and 2 rotary. Default rotary axes are A and C in a Head-Table configuration. |
| Generic5AxisTableTable | 5 | Represents a generic 5 axis machine with 3 linear axes and 2 rotary. Default rotary axes are A and C in a Table-Table configuration. |
| GenericFFF | 6 | Represents a generic FFF machine with two extruders. The default build room dimension is 300mm by 300mm by 300mm. |
| GenericLathe | 0 | Represents a generic 2 axis turning machine. |

## MachiningMode
Namespace: adsk.cam
Specifies how to treat a surface group
Defined in namespace "adsk::cam" and the header file is <Cam\CamTypeDefs.h>

| Name | Value | Description |
|------|-------|-------------|
| Avoid_MachiningMode | 0 | The tool avoids these surfaces while it machines nearby surfaces. The tool stays clear from the avoid surfaces by the specified clearances. |
| Fixture_MachiningMode | 3 | The tool avoids these surfaces by the specified clearances. |
| Gouge_MachiningMode | 2 | The tool does not actively avoid or machine these surfaces. However, if these surfaces are on the path of the tool then it may gouge and cut through them. |
| Machine_MachiningMode | 1 | The tool machines the selected surfaces leaving stock on them according to the stock to leave value. |

## ModifyUtilityTypes
Namespace: adsk.cam
Types of provided ModifyUtility.
Defined in namespace "adsk::cam" and the header file is <Cam\CamTypeDefs.h>

| Name | Value | Description |
|------|-------|-------------|
| AdditiveSetupModifyUtility | 0 | Utility for modifications of additive setups. Corresponds to AdditiveSetupUtility. |

## MultiAxisDegreesPerMinuteType
Namespace: adsk.cam
Enumeration of the multi-axis degrees per minute types that can be used in MultiAxisDPMFeedrateSettings and its specializations.
Defined in namespace "adsk::cam" and the header file is <Cam\CamTypeDefs.h>

| Name | Value | Description |
|------|-------|-------------|
| MultiAxisDegreesPerMinuteType_Combination | 1 | Sets the feedrate as a combination of degrees per minute and linear feed per minute. Used typically for machines that require a form of degrees per minute feedrates. |
| MultiAxisDegreesPerMinuteType_Standard | 0 | Sets the feedrate based on the diameter of the cutting operation and calculates the degrees of the move. Used for most rotary axes. |

## MultiAxisFeedMode
Namespace: adsk.cam
Enumeration of the multi-axis feed modes that can be used in MultiAxisFeedrateSettings and its specializations.
Defined in namespace "adsk::cam" and the header file is <Cam\CamTypeDefs.h>

| Name | Value | Description |
|------|-------|-------------|
| MultiAxisFeedMode_DegreesPerMinute | 1 | Sets the feedrate based on the diameter of the cutting operation and calculates the degrees of the move. Used for most rotary axes. |
| MultiAxisFeedMode_InverseTime | 0 | Sets the time for completing a move as an inverse of the feedrate. The smaller the value, the faster the move. |
| MultiAxisFeedMode_ProgrammerdFeedrate | 2 | Applies the programmed feedrates without adjustments. |

## MultiAxisInverseTimeUnit
Namespace: adsk.cam
The time unit used to calculate the feedrate for the MultiAxisInverseTimeFeedrateSettings
Defined in namespace "adsk::cam" and the header file is <Cam\CamTypeDefs.h>

| Name | Value | Description |
|------|-------|-------------|
| MultiAxisInverseTimeUnit_Minutes | 1 |  |
| MultiAxisInverseTimeUnit_Seconds | 0 |  |

## MultiAxisRetractPreference
Namespace: adsk.cam
Enumeration of the multi-axis retract preferences that can be used in MultiAxisRetractAndReconfigureSettings.
Defined in namespace "adsk::cam" and the header file is <Cam\CamTypeDefs.h>

| Name | Value | Description |
|------|-------|-------------|
| MultiAxisRetractPreference_RetractAtApex | 0 | Always retract when repositioning rotary axes. |
| MultiAxisRetractPreference_StayAtApex | 1 | Allows the tool to stay down without retracting when the rotary axes are repositioned. The tool must be perpendicular to the rotary axis rotational vector (so that only one rotary axis will move) and TCP must be enabled for this axis. |

## MultiAxisRewindPreference
Namespace: adsk.cam
Enumeration of the multi-axis rewind preferences that can be used in MultiAxisRetractAndReconfigureSettings.
Defined in namespace "adsk::cam" and the header file is <Cam\CamTypeDefs.h>

| Name | Value | Description |
|------|-------|-------------|
| MultiAxisRewindPreference_RewindAtLinear | 0 | It can retract at any point, including cutting moves. |
| MultiAxisRewindPreference_RewindAtRapid | 1 | Allows the retract and rewind to occur at a rapid (non-cutting) move instead of at the limits of the rotary axis when possible. It may not be possible in all cases to retract and rewind at a rapid move, in this case the rewind occurs at a cutting move. |

## MultiAxisSingularityLinearizeMethod
Namespace: adsk.cam
The linearization method the MultiAxisSingularitySettings should use. Different values will be used in different MultiAxisSingularitySettings specializations.
Defined in namespace "adsk::cam" and the header file is <Cam\CamTypeDefs.h>

| Name | Value | Description |
|------|-------|-------------|
| MultiAxisSingularityLinearize_Linear | 0 | Moves the tool end point along the straight line by adding points to the toolpath. It keeps the tool within the specified Linearization Tolerance. |
| MultiAxisSingularityLinearize_Rotary | 1 | Applies a linear shape to the moves around the singularity by adding points to the toolpath. It keeps the tool within the specified Linearization Tolerance. The rotary linearization optimizes the tool for revolved movement as if the tool were moving around a cylinder or other object created by revolution. |

## OperationStates
Namespace: adsk.cam
The possible states of an operation. Some operations do not generate toolpaths, their state ignores the potential toolpath states.
Defined in namespace "adsk::cam" and the header file is <Cam\CamTypeDefs.h>

| Name | Value | Description |
|------|-------|-------------|
| IsInvalidOperationState | 1 | Indicates the state where the operation or its toolpath is invalid. |
| IsValidOperationState | 0 | Indicates the state where the operation is valid and is up to date and the toolpath exists if applicable. |
| NoToolpathOperationState | 3 | Indicates the state where the toolpath does not exist for an operation. Not applicable for operations that do not generate toolpaths. |
| SuppressedOperationState | 2 | Indicates the state where the operation is suppressed. Toolpaths do not exist for suppressed operations. |

## OperationStrategyTypes
Namespace: adsk.cam
The valid options for the Strategy Type of an operation.
Defined in namespace "adsk::cam" and the header file is <Cam\CamTypeDefs.h>

| Name | Value | Description |
|------|-------|-------------|
| AdaptiveClearing | 10 | A 3D roughing strategy for clearing large quantities of material effectively. |
| AdaptiveClearing2D | 0 | A 2D strategy that creates a roughing operation that uses a more optimized toolpath that avoids abrupt direction changes. |
| Bore | 7 | A 2D strategy for milling cylindrical pockets and islands by selecting the cylindrical geometry directly. |
| Chamfer2D | 36 | A 2D machining strategy that machines along contours creating a chamfered surface. |
| Circular | 8 | A 2D strategy for milling cylindrical pockets and islands. |
| Contour | 13 | A 3D strategy for finishing steep walls, but can be used for semi-finish and finish machining on the more vertical areas of a part. |
| Contour2D | 3 | A 2D strategy that creates toolpaths based on a 2D contour. Contours can be open or closed and can be on different Z-levels, but each contour is flat (2D). |
| Drilling | 22 | A strategy that supports a wide range of drilling, tapping and hole making operations such as counterbores and countersinks. |
| Engrave | 9 | A 2D strategy that machines along contours with V-shaped chamfered walls. |
| Face | 2 | A 2D strategy that produces quick part facing to prepare raw stock for machining. |
| Flow | 33 | A 3D finishing strategy which follows the isocurves of a surface to machine parts with curved surfaces. Flow is a 3-Axis toolpath by default but can be used in multi-axis modes. |
| Flow2 | 34 | A 3D finishing strategy which follows the isocurves of a surface to machine parts with curved surfaces. Flow is a 3-Axis toolpath by default but can be used in multi-axis modes. |
| Horizontal | 15 | A 3D strategy that automatically detects all the flat areas of the part and clears them with an offsetting path. |
| Jet2D | 23 | A strategy that creates a 2D toolpath for waterjet, laser, and plasma cutting processes. |
| ManualInspection | 43 | Manual inspection. |
| ManualMeasure | 48 | Recorded results of a manual inspection. |
| Morph | 37 | A 3D finishing strategy for machining shallow areas between selected contours with a consistent cutting direction. |
| MorphedSpiral | 20 | A 3D strategy similar to Spiral except that this operation generates the spiral from the selected boundary as opposed to Spiral which trims the generated passes to the machining boundary. |
| MultiAxisContour | 38 | A multi-axis strategy for machining with the tip of the tool along a given contact curve. |
| MultiAxisMorph | 39 | A multi-axis strategy for machining shallow areas between selected contours with a consistent cutting direction. |
| Parallel | 12 | A 3D finishing strategy. The passes are parallel in the XY-plane and follow the surface in the Z-direction. |
| PartAlignment | 46 | Part alignment. |
| PathMeasure | 47 | A surface inspection measurement with a results folder. |
| Pencil | 16 | A 3D strategy that creates toolpaths along internal corners and fillets with small radii, removing material that no other tool can reach. |
| Pocket2D | 1 | A 2D strategy that creates a roughing operation that uses toolpaths parallel to selected geometry. |
| PocketClearing | 11 | A 3D conventional roughing strategy for clearing large quantities of material effectively. |
| ProbeGeometry | 45 | Probe Geometry operation |
| ProbeWCS | 44 | Probe WCS operation |
| Projection | 21 | A finishing strategy that allows you to machine along contours with the center of the tool. The provided contours are automatically projected onto the surface, so they do not have to actually lie on the surface. |
| Radial | 19 | A 3D strategy similar to Spiral machining. This operation also starts from a center point, providing the ability to machine radial parts. It also provides the option to stop short of the center of the radial passes, where they become very dense. |
| Ramp | 14 | A 3D finishing strategy intended for steep areas similar to the contour strategy. However, this strategy ramps down walls rather than machining them with a constant Z, as contour does. |
| RestFinishing | 40 | A finishing operation to machine any remaining stock left from previous operations. |
| RotaryFinishing | 35 | A multi-axis machining strategy that lets you machine along and around a rotating axis. Rotary Finishing can be used for parts that are machined most efficiently when utilizing the 4th Machine Axis. |
| Scallop | 17 | A 3D strategy that creates passes at a constant distance from one another by offsetting them inwards along the surface. The passes follow sloping and vertical walls to maintain the stepover. |
| Slot | 4 | A 2D strategy that mills a slot by following the center line of the slot. |
| Spiral | 18 | A 3D strategy that creates a spiral toolpath from a given center point, generating a constant contact as it machines within a given boundary. |
| SteepAndShallow | 32 | A 3D finishing strategy that uses Contour passes for steep areas and Parallel or Scallop passes for shallow areas. |
| SurfaceInspection | 42 | A strategy for the inspection of geometry using probe. |
| Swarf | 41 | A multi-axis strategy for machining with the side of the tool. |
| Thread | 6 | A 2D strategy for thread milling cylindrical pockets and islands. |
| Trace | 5 | A 2D strategy that machines along contours with varying Z values and with, or without, left and right side compensation. |
| TurningChamfer | 24 | The turning chamfer strategy is used for chamfering sharp corners that have not been chamfered in the design. |
| TurningFace | 25 | The face strategy is used for machining the front side of the part. |
| TurningGroove | 26 | The turning groove strategy is used for grooving at selected positions only. This can for instance be used to make a groove on the backside before threading. |
| TurningPart | 27 | This strategy is used for cutting off the part once the part has been fully machined or for machining it on another spindle. |
| TurningProfile | 28 | The turning profile strategy is used for both roughing and finishing of the part using general turning tools. |
| TurningProfileGroove | 29 | The turning groove strategy is used for both roughing and finishing of the part using groove tools. |
| TurningStockTransfer | 30 | The turning stock transfer strategy is intended for automatic stock transfer between the two spindles. No toolpath is associated with this strategy. The post is responsible for outputting the desired NC code. |
| TurningThread | 31 | This strategy is used for turning threads. Both cylindrical and conical threads are supported. The CNC control must have built-in support for synchronizing the spindle and feed. |

## OperationTypes
Namespace: adsk.cam
The valid options for the Operation Type of a Setup.
Defined in namespace "adsk::cam" and the header file is <Cam\CamTypeDefs.h>

| Name | Value | Description |
|------|-------|-------------|
| AdditiveOperation | 3 | Specifies an additive type operation |
| JetOperation | 2 | Specifies a Jet type operation |
| MillingOperation | 0 | Specifies a milling type operation |
| TurningOperation | 1 | Specifies a turning type operation |

## PostCapabilities
Namespace: adsk.cam
List of capabilities a post configuration can support. These capabilities represent either a class of operations (milling, turning, etc.) or some additional functionality (e.g. machine simulation).
Defined in namespace "adsk::cam" and the header file is <Cam\CamTypeDefs.h>

| Name | Value | Description |
|------|-------|-------------|
| Additive | 64 | Post supports additive operations. |
| Cascading | 32 | Post configuration is intended to run as a complement to another post that produces NC code to pass additional data to an external application. |
| Inspection | 128 | Post supports surface inspection operations. |
| Intermediate | 8 | Post outputs data in an intermediate format intended for processing by another application rather than NC code for a machine. |
| Jet | 16 | Post supports jet cutting operations (e.g. water jet, plasma, or laser). |
| MachineSimulation | 256 | Post configuration provides additional data to support machine simulation. |
| Milling | 1 | Post supports milling operations. |
| SetupSheet | 4 | Post creates a setup sheet rather than NC code. |
| Turning | 2 | Post supports turning operations. |
| Undefined | 0 | Undefined, default when query is created. |

## PostOutputUnitOptions
Namespace: adsk.cam
List of the valid options for the outputUnit property on a PostProcessInput object .
Defined in namespace "adsk::cam" and the header file is <Cam\CamTypeDefs.h>

| Name | Value | Description |
|------|-------|-------------|
| DocumentUnitsOutput | 0 | Post the toolpath in the document units |
| InchesOutput | 1 | Post the toolpath in inches |
| MillimetersOutput | 2 | Post the toolpath in millimeters |

## PostProcessExecutionBehaviors
Namespace: adsk.cam
Defined in namespace "adsk::cam" and the header file is <Cam\CamTypeDefs.h>

| Name | Value | Description |
|------|-------|-------------|
| PostProcessExecutionBehavior_Fail | 1 | If any issue with an operation arises, the post processing should throw an exception. |
| PostProcessExecutionBehavior_OmitInvalidAndEmptyOperations | 0 | Default value, post process only valid operations containing toolpath data. |
| PostProcessExecutionBehavior_PostAll | 2 | Post process all operations disregarding their state. |

## PrintSettingItemTypes
Namespace: adsk.cam
Enum that represents the types of CAMParameters. Represents the General and Exporter parameters type in PrintSetting.
Defined in namespace "adsk::cam" and the header file is <Cam\CamTypeDefs.h>

| Name | Value | Description |
|------|-------|-------------|
| EXPORTER | 1 |  |
| GENERAL | 0 |  |

## RecognizedPocketBottomType
Namespace: adsk.cam
Types of pocket bottoms that can exist. Flat represents a standard flat bottom with sharp edges at the walls. (Flat may also have some portions that are through, but may not have any portions that are chamfered or filleted.) Through represents a pocket with no bottom anywhere along the boundary and sharp edges at the walls. Chamfer and fillet represent pockets where that type of feature goes around all edges of the boundary and islands, between the bottom and the walls. Other represents any other cases, such as a mix of different bottom types for different edges.
Defined in namespace "adsk::cam" and the header file is <Cam\CamTypeDefs.h>

| Name | Value | Description |
|------|-------|-------------|
| RecognizedPocketBottomTypeChamfer | 2 |  |
| RecognizedPocketBottomTypeFillet | 3 |  |
| RecognizedPocketBottomTypeFlat | 0 |  |
| RecognizedPocketBottomTypeOther | 4 |  |
| RecognizedPocketBottomTypeThrough | 1 |  |

## SetupChangeEventType
Namespace: adsk.cam
List of setup change event types.
Defined in namespace "adsk::cam" and the header file is <Cam\CamTypeDefs.h>

| Name | Value | Description |
|------|-------|-------------|
| Arbitrary | 0 | Arbitrary change |
| PrintSettingSelection | 1 | Selection of print setting |

## SetupSheetFormats
Namespace: adsk.cam
List of the formats to choose from when generating setup sheets
Defined in namespace "adsk::cam" and the header file is <Cam\CamTypeDefs.h>

| Name | Value | Description |
|------|-------|-------------|
| ExcelFormat | 1 | Generates an Excel document |
| HTMLFormat | 0 | Generates an HTML document |

## SetupStockModes
Namespace: adsk.cam
List of setup stock modes.
Defined in namespace "adsk::cam" and the header file is <Cam\CamTypeDefs.h>

| Name | Value | Description |
|------|-------|-------------|
| FixedBoxStock | 0 | Fixed Size Box |
| FixedCylinderStock | 2 | Fixed Size Cylinder |
| FixedTubeStock | 4 | Fixed Size Tube |
| PreviousSetupStock | 7 | From Preceding Setup |
| RelativeBoxStock | 1 | Relative Size Box |
| RelativeCylinderStock | 3 | Relative Size Cylinder |
| RelativeTubeStock | 5 | Relative Size Tube |
| SolidStock | 6 | From Solid |

## SideTypes
Namespace: adsk.cam
Enum for the order of loops.
Defined in namespace "adsk::cam" and the header file is <Cam\CamTypeDefs.h>

| Name | Value | Description |
|------|-------|-------------|
| AlwaysInsideSideType | 1 | AlwaysInside |
| AlwaysOutsideSideType | 0 | AlwaysOutside |
| StartInsideSideType | 3 | StartInside has the order inside - outside - inside ... |
| StartOutsideSideType | 2 | StartOutside has the order outside - inside - outside ... |

## SplitSupportTypes
Namespace: adsk.cam
Split support behavior depending on the type of support.
Defined in namespace "adsk::cam" and the header file is <Cam\CamTypeDefs.h>

| Name | Value | Description |
|------|-------|-------------|
| SolidOpenMergedSplitSupportType | 0 | Solid and open support into one single mesh body. |
| SolidOpenSeparateSplitSupportType | 1 | Solid and open support into two separate mesh bodies. |

# adsk.core

## AppearanceSourceTypes
Namespace: adsk.core
The different types of sources for an appearance.
Defined in namespace "adsk::core" and the header file is <Core\CoreTypeDefs.h>

| Name | Value | Description |
|------|-------|-------------|
| BodyAppearanceSource | 1 | The entity is its current appearance because of an appearance assigned to the body. |
| FaceAppearanceSource | 3 | The entity is its current appearance because of an appearance assigned to the face. |
| MaterialAppearanceSource | 0 | Then entity is its current appearance because of the appearance associated with the material assigned to a component or body. |
| OccurrenceAppearanceSource | 2 | The entity is its current appearance because of an appearance assigned to the occurrence. |
| OverrideAppearanceSource | 4 | The entity is its current appearance because of an override that's been applied. |

## BooleanOptions
Namespace: adsk.core
The different values that can be used when specifying whether an item should use a default, or be true or false.
Defined in namespace "adsk::core" and the header file is <Core\CoreTypeDefs.h>

| Name | Value | Description |
|------|-------|-------------|
| DefaultBooleanOption | 0 | Specifies that the default value should be used. |
| FalseBooleanOption | 2 | Specifies the value is False. |
| TrueBooleanOption | 1 | Specifies the value is True. |

## CameraTypes
Namespace: adsk.core
The different types of cameras.
Defined in namespace "adsk::core" and the header file is <Core\CoreTypeDefs.h>

| Name | Value | Description |
|------|-------|-------------|
| OrthographicCameraType | 0 | An orthographic camera. Things are the same size in the view regardless of there distance from the eye. |
| PerspectiveCameraType | 1 | An perspective camera. Things are smaller the further they are away from the eye. |
| PerspectiveWithOrthoFacesCameraType | 2 | An perspective camera. Things are smaller the further they are away from the eye. |

## CloseError
Namespace: adsk.core
List of possible errors when closing a document.
Defined in namespace "adsk::core" and the header file is <Core\CoreTypeDefs.h>

| Name | Value | Description |
|------|-------|-------------|
| CloseCancelledError | 200 | The close operation was canceled by the user |

## CommandTerminationReason
Namespace: adsk.core
Defines the termination reason for a command. Commands can be terminated for a number of different reasons, and based on the reason commands have to do different things during termination so this enum defines various reasons for termination
Defined in namespace "adsk::core" and the header file is <Core\CoreTypeDefs.h>

| Name | Value | Description |
|------|-------|-------------|
| AbortedTerminationReason | 3 | The command is terminated by clicking OK button, and executed failed. |
| CancelledTerminationReason | 2 | The command is terminated by clicking Cancel button. |
| CompletedTerminationReason | 1 | The command is terminated by clicking OK button, and executed successfully. |
| PreEmptedTerminationReason | 4 | The command is terminated by activating another command. |
| SessionEndingTerminationReason | 5 | The command is terminated by closing the document. |
| UnknownTerminationReason | 0 | The command is terminated out of the reasons list below. |

## Curve2DTypes
Namespace: adsk.core
The different types of 2D curves.
Defined in namespace "adsk::core" and the header file is <Core\CoreTypeDefs.h>

| Name | Value | Description |
|------|-------|-------------|
| Arc2DCurveType | 1 | Transient 2D arc. |
| Circle2DCurveType | 2 | Transient 2D circle. |
| Ellipse2DCurveType | 3 | Transient 2D ellipse. |
| EllipticalArc2DCurveType | 4 | Transient 2D elliptical arc. |
| InfiniteLine2DCurveType | 5 | Transient 2D infinite line. |
| Line2DCurveType | 0 | Transient 2D line segment. |
| NurbsCurve2DCurveType | 6 | Transient 2D NURBS curve. |
| Polyline2DCurveType | 7 | Transient 2D polyline. |

## Curve3DTypes
Namespace: adsk.core
The different types of 3D curves.
Defined in namespace "adsk::core" and the header file is <Core\CoreTypeDefs.h>

| Name | Value | Description |
|------|-------|-------------|
| Arc3DCurveType | 1 | Transient 3D arc. |
| Circle3DCurveType | 2 | Transient 3D circle. |
| Ellipse3DCurveType | 3 | Transient 3D ellipse. |
| EllipticalArc3DCurveType | 4 | Transient 3D elliptical arc. |
| InfiniteLine3DCurveType | 5 | Transient 3D infinite line. |
| Line3DCurveType | 0 | Transient 3D line segment. |
| NurbsCurve3DCurveType | 6 | Transient 3D NURBS curve. |
| Polyline3DCurveType | 7 | Transient 3D polyline. |

## DefaultModelingOrientations
Namespace: adsk.core
A list of the valid modeling orientations.
Defined in namespace "adsk::core" and the header file is <Core\CoreTypeDefs.h>

| Name | Value | Description |
|------|-------|-------------|
| YUpModelingOrientation | 0 | The model Y is the up direction. |
| ZUpModelingOrientation | 1 | The model Z is the up direction. |

## DefaultOrbits
Namespace: adsk.core
A list of the valid orbit modes.
Defined in namespace "adsk::core" and the header file is <Core\CoreTypeDefs.h>

| Name | Value | Description |
|------|-------|-------------|
| ConstrainedOrbit | 0 | Constrained orbit mode. |
| FreeOrbit | 1 | Free orbit mode. |

## DegradedSelectionDisplayStyles
Namespace: adsk.core
A list of the valid degraded display styles.
Defined in namespace "adsk::core" and the header file is <Core\CoreTypeDefs.h>

| Name | Value | Description |
|------|-------|-------------|
| NormalWithGlowDegradedSelectionStyle | 0 | Normal with glow degraded selection style. |
| SimpleWithoutGlowDegradedSelectionStyle | 1 | Simple without glow degraded selection style. |

## DegreeDisplayFormats
Namespace: adsk.core
List of the valid degree display formats.
Defined in namespace "adsk::core" and the header file is <Core\CoreTypeDefs.h>

| Name | Value | Description |
|------|-------|-------------|
| DecimalDegreeDisplay | 0 | Decimal degree display. |
| MinutesAndSecondsDegreeDisplay | 1 | Minutes and seconds degree display. |

## DialogResults
Namespace: adsk.core
Defines the valid return types from a dialog.
Defined in namespace "adsk::core" and the header file is <Core\CoreTypeDefs.h>

| Name | Value | Description |
|------|-------|-------------|
| DialogCancel | 1 | The dialog box return value is Cancel (usually sent from a button labeled Cancel). |
| DialogError | -1 | An unexpected error occurred. |
| DialogNo | 3 | The dialog box return value is No (usually sent from a button labeled No). |
| DialogOK | 0 | The dialog box return value is OK (usually sent from a button labeled OK). |
| DialogYes | 2 | The dialog box return value is Yes (usually sent from a buttons labeled Yes and Retry). |

## DocumentTypes
Namespace: adsk.core
The types of documents that can be created.
Defined in namespace "adsk::core" and the header file is <Core\CoreTypeDefs.h>

| Name | Value | Description |
|------|-------|-------------|
| FusionDesignDocumentType | 0 | Fusion design document type. |

## DropDownStyles
Namespace: adsk.core
Defines the different styles that a drop-down input can be.
Defined in namespace "adsk::core" and the header file is <Core\CoreTypeDefs.h>

| Name | Value | Description |
|------|-------|-------------|
| CheckBoxDropDownStyle | 2 | Defines a drop-down that contains a list of check boxes where multiple items can be checked. |
| LabeledIconDropDownStyle | 0 | Defines a drop-down where it contains a list items where each item has text and an icon. If the icon of the list item is set to null, a radio button will be displayed instead of the icon. A single item can be selected at a time. |
| TextListDropDownStyle | 1 | Defines a drop-down that contains a scrollable list of text only items and one item can be selected from the list. |

## FootAndInchDisplayFormats
Namespace: adsk.core
List of the valid foot and inch formats.
Defined in namespace "adsk::core" and the header file is <Core\CoreTypeDefs.h>

| Name | Value | Description |
|------|-------|-------------|
| ArchitecturalFootAndInchDisplay | 2 | Architectural foot and inch display format. |
| DecimalFootAndInchDisplay | 0 | Decimal foot and inch display format. |
| FractionalFootAndInchDisplay | 1 | Fractional foot and inch display format. |

## FutureStates
Namespace: adsk.core
The different states of a future.
Defined in namespace "adsk::core" and the header file is <Core\CoreTypeDefs.h>

| Name | Value | Description |
|------|-------|-------------|
| FailedFutureState | 2 | The process associated with the future has failed. |
| FinishedFutureState | 1 | The process associated with the future has successfully finished. |
| ProcessingFutureState | 0 | The process associated with the future is still processing. |

## GenericErrors
Namespace: adsk.core
Errors that every API call can return via Application::GetLastError. These can be augmented with class and function specific errors.
Defined in namespace "adsk::core" and the header file is <Core\CoreTypeDefs.h>

| Name | Value | Description |
|------|-------|-------------|
| BadApiCallError | 3 | The client made some sort of mistake calling the API object |
| ClassSpecificError | 100 | Errors reserved for several functions in a class. |
| ExpressionError | 6 | e.g. Errors related to bad value expressions or units - e.g. "1 in + 1 Kg" is an invalid expression |
| FunctionSpecificError | 200 | Errors reserved for a specific function in a class. |
| InternalValidationError | 2 | Internal API validation failed |
| InvalidGeometryError | 7 | When creating or changing an object via reference geometry, the geometry wasn't specified correctly (e.g. an Occurrence needs to be specified). |
| Ok | 0 | No error occurred. |
| OperationFailed | 5 | The API operation failed with the supplied error message. |
| UnderlyingObjectDeletedError | 4 | The API object is referencing a Neutron object that has been deleted. |
| UnexpectedError | 1 | An internal error occurred - e.g. a library function throw an exception. |

## GraphicsDrivers
Namespace: adsk.core
A list of the valid graphics drivers.
Defined in namespace "adsk::core" and the header file is <Core\CoreTypeDefs.h>

| Name | Value | Description |
|------|-------|-------------|
| AutoSelectGraphicsDriver | 2 | Let Fusion automatically select the Graphics Driver. This option applies to both Windows and Mac. |
| DirectX11GraphicsDriver | 1 | DirectX 11 Graphics Driver. This option only applies to Windows. |
| DirectX9GraphicsDriver | 0 | DirectX 9 Graphics Driver. This option is no longer supported for Windows because Fusion no longer supports DirectX9. |
| OpenGLCoreProfileGraphicsDriver | 3 | OpenGL Core Profile Graphics Driver. This option only applies to Mac. |
| OpenGLGraphicsDriver | 4 | OpenGL Graphics Driver. This option only applies to Mac. |

## GraphicsPresets
Namespace: adsk.core
Defines the different options for preset graphic setting definitions.
Defined in namespace "adsk::core" and the header file is <Core\CoreTypeDefs.h>

| Name | Value | Description |
|------|-------|-------------|
| CustomGraphicsPreset | 2 | Allows setting the graphics settings with any values. |
| PerformanceGraphicsPreset | 0 | Sets the graphics settings to get the best performance. |
| QualityGraphicsPreset | 1 | Sets the graphics settings to get the best quality. |

## HorizontalAlignments
Namespace: adsk.core
Defines the different horizontal alignments that can be applied to text.
Defined in namespace "adsk::core" and the header file is <Core\CoreTypeDefs.h>

| Name | Value | Description |
|------|-------|-------------|
| CenterHorizontalAlignment | 1 | Aligned along the center. |
| LeftHorizontalAlignment | 0 | Aligned to the left. |
| RightHorizontalAlignment | 2 | Aligned to the right. |

## HttpMethods
Namespace: adsk.core
The HTTP methods supported by the HttpRequest object.
Defined in namespace "adsk::core" and the header file is <Core\CoreTypeDefs.h>

| Name | Value | Description |
|------|-------|-------------|
| DeleteMethod | 3 | DELETE HTTP method. |
| GetMethod | 0 | GET HTTP method. |
| PatchMethod | 4 | PATCH HTTP method. |
| PostMethod | 1 | POST HTTP method. |
| PutMethod | 2 | PUT HTTP method. |

## HubTypes
Namespace: adsk.core
The different types of hubs.
Defined in namespace "adsk::core" and the header file is <Core\CoreTypeDefs.h>

| Name | Value | Description |
|------|-------|-------------|
| PersonalHubType | 0 | A personal hub. |
| TeamHubType | 1 | An A360 team hub. |

## KeyCodes
Namespace: adsk.core
Key values on the keyboard.
Defined in namespace "adsk::core" and the header file is <Core\CoreTypeDefs.h>

| Name | Value | Description |
|------|-------|-------------|
| AKeyCode | 65 | A |
| AltKeyCode | 16777251 | Alt |
| AsciiCircumKeyCode | 94 | ASCII circum |
| AsciiTildeKeyCode | 126 | ASCII tilde |
| AsteriskKeyCode | 42 | Asterisk |
| BackslashKeyCode | 92 | Backslash |
| BackspaceKeyCode | 16777219 | Backspace |
| BacktabKeyCode | 16777218 | Backtab |
| BarKeyCode | 124 | Bar |
| BKeyCode | 66 | B |
| BraceLeftKeyCode | 123 | Brace left |
| BraceRightKeyCode | 125 | Brace right |
| BracketLeftKeyCode | 91 | Bracket left |
| BracketRightKeyCode | 93 | Bracket right |
| CKeyCode | 67 | C |
| ClearKeyCode | 16777227 | Clear |
| ColonKeyCode | 58 | Colon |
| CommaKeyCode | 44 | Comma |
| ControlKeyCode | 16777249 | Control |
| D0KeyCode | 48 | D0 |
| D1KeyCode | 49 | D1 |
| D2KeyCode | 50 | D2 |
| D3KeyCode | 51 | D3 |
| D4KeyCode | 52 | D4 |
| D5KeyCode | 53 | D5 |
| D6KeyCode | 54 | D6 |
| D7KeyCode | 55 | D7 |
| D8KeyCode | 56 | D8 |
| D9KeyCode | 57 | D9 |
| DeleteKeyCode | 16777223 | Delete |
| DKeyCode | 68 | D |
| DownKeyCode | 16777237 | Down |
| EKeyCode | 69 | E |
| EndKeyCode | 16777233 | End |
| EnterKeyCode | 16777221 | Enter |
| EqualKeyCode | 61 | Equal |
| EscapeKeyCode | 16777216 | Escape |
| F10KeyCode | 16777273 | F10 |
| F11KeyCode | 16777274 | F11 |
| F12KeyCode | 16777275 | F12 |
| F1KeyCode | 16777264 | F1 |
| F2KeyCode | 16777265 | F2 |
| F3KeyCode | 16777266 | F3 |
| F4KeyCode | 16777267 | F4 |
| F5KeyCode | 16777268 | F5 |
| F6KeyCode | 16777269 | F6 |
| F7KeyCode | 16777270 | F7 |
| F8KeyCode | 16777271 | F8 |
| F9KeyCode | 16777272 | F9 |
| FKeyCode | 70 | F |
| GKeyCode | 71 | G |
| GraveAccentKeyCode | 96 | Grave accent |
| GreaterKeyCode | 62 | Greater |
| HKeyCode | 72 | H |
| HomeKeyCode | 16777232 | Home |
| IKeyCode | 73 | I |
| InsertKeyCode | 16777222 | Insert |
| JKeyCode | 74 | J |
| KKeyCode | 75 | K |
| LeftKeyCode | 16777234 | Left |
| LessKeyCode | 60 | Less |
| LKeyCode | 76 | L |
| MenuKeyCode | 16777301 | Menu |
| MetaKeyCode | 16777250 | Meta |
| MinusKeyCode | 45 | Minus |
| MKeyCode | 77 | M |
| NKeyCode | 78 | N |
| NoKeyCode | 0 | No key |
| OKeyCode | 79 | O |
| PageDownKeyCode | 16777239 | Page down |
| PageUpKeyCode | 16777238 | Page up |
| PauseKeyCode | 16777224 | Pause |
| PeriodKeyCode | 46 | Period |
| PKeyCode | 80 | P |
| PlusKeyCode | 43 | Plus |
| PrintKeyCode | 16777225 | Print |
| QKeyCode | 81 | Q |
| QuestionKeyCode | 63 | Question |
| QuoteLeftKeyCode | 96 | Quote left |
| ReturnKeyCode | 16777220 | Return |
| RightKeyCode | 16777236 | Right |
| RKeyCode | 82 | R |
| SemicolonKeyCode | 59 | Semicolon |
| ShiftKeyCode | 16777248 | Shift |
| SKeyCode | 83 | S |
| SlashKeyCode | 47 | Slash |
| SpaceKeyCode | 32 | Space |
| SysReqKeyCode | 16777226 | SysReq |
| TabKeyCode | 16777217 | Tab |
| TKeyCode | 84 | T |
| UKeyCode | 85 | U |
| UnderscoreKeyCode | 95 | Underscore |
| UpKeyCode | 16777235 | Up |
| VKeyCode | 86 | V |
| WKeyCode | 87 | W |
| XKeyCode | 88 | X |
| YKeyCode | 89 | Y |
| ZKeyCode | 90 | Z |

## KeyboardModifiers
Namespace: adsk.core
Keyboard modifier values.
Defined in namespace "adsk::core" and the header file is <Core\CoreTypeDefs.h>

| Name | Value | Description |
|------|-------|-------------|
| AltKeyboardModifier | 134217728 | Alt |
| CtrlKeyboardModifier | 67108864 | Control |
| MetaKeyboardModifier | 268435456 | Meta |
| NoKeyboardModifier | 0 | None |
| ShiftKeyboardModifier | 33554432 | Shift |

## LightingEnvironments
Namespace: adsk.core
Defines the list of available lighting environments.
Defined in namespace "adsk::core" and the header file is <Core\CoreTypeDefs.h>

| Name | Value | Description |
|------|-------|-------------|
| DarkSkyLightingEnvironment | 0 | Defines the Dark Sky lighting environment. |
| GreyRoomLightingEnvironment | 1 | Defines the Grey Room lighting environment. |
| InfinityPoolLightingEnvironment | 4 | Defines the Infinity Pool lighting environment. |
| PhotoBoothLightingEnvironment | 2 | Defines the Photo Booth lighting environment. |
| RiverRubiconLightingEnvironment | 5 | Defines the River Rubicon lighting environment. |
| TranquilityBlueLightingEnvironment | 3 | Defines the Tranquility Blue lighting environment. |

## ListControlDisplayTypes
Namespace: adsk.core
The different types of items that can be displayed in a list control.
Defined in namespace "adsk::core" and the header file is <Core\CoreTypeDefs.h>

| Name | Value | Description |
|------|-------|-------------|
| CheckBoxListType | 0 | The list control contains check boxes. |
| RadioButtonlistType | 1 | The list controls contains radio buttons. |
| StandardListType | 2 | The list control is a list of text items with optional icons. |

## LogLevels
Namespace: adsk.core
Log message level
Defined in namespace "adsk::core" and the header file is <Core\CoreTypeDefs.h>

| Name | Value | Description |
|------|-------|-------------|
| ErrorLogLevel | 0 | Use this type to log error message. |
| InfoLogLevel | 2 | Use this type to log info message. |
| WarningLogLevel | 1 | Use this type to log warning message. |

## LogTypes
Namespace: adsk.core
Location where messages should be logged.
Defined in namespace "adsk::core" and the header file is <Core\CoreTypeDefs.h>

| Name | Value | Description |
|------|-------|-------------|
| ConsoleLogType | 1 | Log information to Fusion text command window. This logs only the provided message string. |
| FileLogType | 0 | Log information to the Fusion app log file. |

## MaterialDisplayUnits
Namespace: adsk.core
List of the different types of material related units supported for displaying values.
Defined in namespace "adsk::core" and the header file is <Core\CoreTypeDefs.h>

| Name | Value | Description |
|------|-------|-------------|
| EnglishFootDisplayUnits | 7 | English ft |
| EnglishInchDisplayUnits | 6 | English in |
| EnglishStandardDisplayUnits | 5 | English standard |
| MetricCGSDisplayUnits | 3 | Metric cgs |
| MetricMKSDisplayUnits | 1 | Metric mks |
| MetricMMNSDisplayUnits | 2 | Metric mmNs |
| MetricStandardDisplayUnits | 0 | Metric standard |
| MetricUMNSDisplayUnits | 4 | Metric umNsd |

## MessageBoxButtonTypes
Namespace: adsk.core
Defines the valid return types from a message box.
Defined in namespace "adsk::core" and the header file is <Core\CoreTypeDefs.h>

| Name | Value | Description |
|------|-------|-------------|
| OKButtonType | 0 | The message box contains an OK button. |
| OKCancelButtonType | 1 | The message box contains OK and Cancel buttons. |
| RetryCancelButtonType | 2 | The message box contains Retry and Cancel buttons. |
| YesNoButtonType | 3 | The message box contains Yes and No buttons. |
| YesNoCancelButtonType | 4 | The message box contains Yes, No, and Cancel buttons. |

## MessageBoxIconTypes
Namespace: adsk.core
Defines the different icons that can be used in a message box.
Defined in namespace "adsk::core" and the header file is <Core\CoreTypeDefs.h>

| Name | Value | Description |
|------|-------|-------------|
| CriticalIconType | 4 | An icon indicating that a critical problem message is being displayed. |
| InformationIconType | 2 | An icon indicating that informational message is being displayed. |
| NoIconIconType | 0 | No icon is to be used. |
| QuestionIconType | 1 | An icon indicating that a question is being asked. |
| WarningIconType | 3 | An icon indicating that a warning message is being displayed. |

## MouseButtons
Namespace: adsk.core
Mouse button values.
Defined in namespace "adsk::core" and the header file is <Core\CoreTypeDefs.h>

| Name | Value | Description |
|------|-------|-------------|
| LeftMouseButton | 1 | Left |
| MiddleMouseButton | 4 | Middle |
| NoMouseButton | 0 | None |
| RightMouseButton | 2 | Right |

## NetworkProxySettings
Namespace: adsk.core
A list of the valid network proxy settings.
Defined in namespace "adsk::core" and the header file is <Core\CoreTypeDefs.h>

| Name | Value | Description |
|------|-------|-------------|
| AutomaticProxySettings | 0 | Automatic proxy setting. |
| NoProxyProxySettings | 1 | No proxy setting. |
| OverrideProxySettings | 3 | Override proxy setting. |
| WindowsDefaultProxySettings | 2 | Windows default proxy setting. |

## NurbsSurfaceProperties
Namespace: adsk.core
The different surface property types.
Defined in namespace "adsk::core" and the header file is <Core\CoreTypeDefs.h>

| Name | Value | Description |
|------|-------|-------------|
| ClosedNurbsSurface | 2 | Closed |
| OpenNurbsSurface | 1 | Open |
| PeriodicNurbsSurface | 4 | Periodic |
| RationalNurbsSurface | 8 | Rational |

## OpenDocumentError
Namespace: adsk.core
The possible errors when a document is opened.
Defined in namespace "adsk::core" and the header file is <Core\CoreTypeDefs.h>

| Name | Value | Description |
|------|-------|-------------|
| DocumentNotFoundError | 200 | Error indicating the specified file does not exist. |

## OperatingSystems
Namespace: adsk.core
Defines the various operating systems that a script or add-in can run on.
Defined in namespace "adsk::core" and the header file is <Core\CoreTypeDefs.h>

| Name | Value | Description |
|------|-------|-------------|
| MacOperatingSystem | 1 | Specifies the script or add-in will only run on Mac. |
| WindowsAndMacOperatingSystem | 2 | Specifies the script or add-in will run on Windows and Mac. |
| WindowsOperatingSystem | 0 | Specifies the script or add-in will only run on Windows. |

## PaletteDockingOptions
Namespace: adsk.core
Defines the different options available when docking a palette to the Fusion main window area.
Defined in namespace "adsk::core" and the header file is <Core\CoreTypeDefs.h>

| Name | Value | Description |
|------|-------|-------------|
| PaletteDockOptionsNone | 0 | Specifies the palette cannot be docked to the Fusion main window area. |
| PaletteDockOptionsToHorizontalOnly | 2 | Specifies that the palette can only be docked to the top and bottom of the Fusion main window area. |
| PaletteDockOptionsToVerticalAndHorizontal | 3 | Specifies that the palette can be docked to the sides, top, or bottom of the Fusion main window area. |
| PaletteDockOptionsToVerticalOnly | 1 | Specifies that the palette can only be docked to the sides of the Fusion main window area. |

## PaletteDockingStates
Namespace: adsk.core
Defines the various docking states that a palette can be in.
Defined in namespace "adsk::core" and the header file is <Core\CoreTypeDefs.h>

| Name | Value | Description |
|------|-------|-------------|
| PaletteDockStateBottom | 2 | The palette is docked to the bottom of the main window area. |
| PaletteDockStateFloating | 0 | The palette is not docked but is floating. |
| PaletteDockStateLeft | 3 | The palette is docked to the left of the main window area. |
| PaletteDockStateRight | 4 | The palette is docked to the right of the main window area. |
| PaletteDockStateTop | 1 | The palette is docked to the top of the main window area. |

## PaletteSnapOptions
Namespace: adsk.core
Defines the various positions that a palette can be snapped to another palette.
Defined in namespace "adsk::core" and the header file is <Core\CoreTypeDefs.h>

| Name | Value | Description |
|------|-------|-------------|
| PaletteSnapOptionsBottom | 3 | Specifies the palette is snapped to the bottom of another palette. |
| PaletteSnapOptionsLeft | 1 | Specifies the palette is snapped to the left of another palette. |
| PaletteSnapOptionsRight | 2 | Specifies the palette is snapped to the right of another palette. |
| PaletteSnapOptionsTop | 0 | Specifies the palette is snapped to the top of another palette. |

## PanZoomOrbitShortcuts
Namespace: adsk.core
A list of the different predefined keyboard shortcuts for pan, zoom, and orbit.
Defined in namespace "adsk::core" and the header file is <Core\CoreTypeDefs.h>

| Name | Value | Description |
|------|-------|-------------|
| AliasPanZoomOrbitShortcut | 1 | Use Alias pan, zoom, and orbit keyboard shortcuts. |
| Fusion360PanZoomOrbitShortcut | 0 | Use Fusion pan, zoom, and orbit keyboard shortcuts. |
| InventorPanZoomOrbitShortcut | 2 | Use Inventor pan, zoom, and orbit keyboard shortcuts. |
| PowerMillPanZoomOrbitShortcut | 5 | Use PowerMill pan, zoom, and orbit keyboard shortcuts. |
| SolidWorksPanZoomOrbitShortcut | 3 | Use SolidWorks pan, zoom, and orbit keyboard shortcuts. |
| TinkercadPanZoomOrbitShortcut | 4 | Use Tinkercad pan, zoom, and orbit keyboard shortcuts. |

## ProgrammingLanguages
Namespace: adsk.core
Defines the various languages supported for Fusion scripts and add-ins.
Defined in namespace "adsk::core" and the header file is <Core\CoreTypeDefs.h>

| Name | Value | Description |
|------|-------|-------------|
| CPPProgramminglanguage | 2 | Specifies a script or add-in written using the C++ programming language. |
| PromptForLanguage | 0 | Used with the APIPreferences object to specify the user should be prompted when creating a new script or add-in. |
| PythonProgrammingLanguage | 1 | Specifies a script or add-in written using the Python programming language. |
| TypeScriptProgrammingLanguage | 3 | Specifies a script or add-in written using the TypeScript programming language. |

## ProjectedTextureMapTypes
Namespace: adsk.core
The different types of projected texture maps.
Defined in namespace "adsk::core" and the header file is <Core\CoreTypeDefs.h>

| Name | Value | Description |
|------|-------|-------------|
| AutomaticTextureMapProjection | 0 | The default projection that is determined automatically. |
| BoxTextureMapProjection | 2 | A texture map that is projected from six orthogonal planes as if the body was in a box and each plane of the box is projected onto the body. |
| CylindricalTextureMapProjection | 4 | A texture map that is projected as a cylinder onto the body. |
| PlanarTextureMapProjection | 1 | A texture map that is projected onto the body along a single direction. |
| SphericalTextureMapProjection | 3 | A texture map that is projected as a sphere onto the body. |

## SaveLocalErrors
Namespace: adsk.core
List of possible errors when saving a document locally.
Defined in namespace "adsk::core" and the header file is <Core\CoreTypeDefs.h>

| Name | Value | Description |
|------|-------|-------------|
| DiskFullSaveLocalError | 201 | The disk is full. |
| FileReadOnlySaveLocalError | 202 | The specified file exists and is read-only. |
| SaveCancelledSaveLocalError | 200 | The save was canceled. |

## ScriptSourceLocations
Namespace: adsk.core
Defines the different locations where Fusion looks for scripts and add-ins.
Defined in namespace "adsk::core" and the header file is <Core\CoreTypeDefs.h>

| Name | Value | Description |
|------|-------|-------------|
| AppStoreScriptSourceLocation | 0 | The location where add-ins are installed from the Autodesk App Store. Windows - %appdata%\Autodesk\ApplicationPlugins Mac - ~/Library/Application Support/Autodesk/ApplicationPlugins |
| InternalScriptSourceLocation | 3 | One of the internal folders where add-ins are installed with Fusion. |
| LinkedScriptSourceLocation | 5 | The script or add-in can be located anywhere and has been manually added to the known list of scripts and add-ins as a link. |
| OtherInstalledScriptSourceLocation | 1 | The folder where non-App Store add-ins are installed. Windows - %appdata%\Autodesk\FusionAddins Mac - ~/Library/Application Support/Autodesk/FusionAddins |
| SamplesScriptSourceLocation | 4 | One of the sample folders where sample scripts and add-ins are installed with Fusion. |
| UserDefinedScriptSourceLocation | 2 | The folder defined in the API tab of the Preferences dialog. |

## SelectionDisplayStyles
Namespace: adsk.core
A list of the valid selection display styles.
Defined in namespace "adsk::core" and the header file is <Core\CoreTypeDefs.h>

| Name | Value | Description |
|------|-------|-------------|
| NormalDisplayStyle | 0 | Normal selection display. |
| SimpleDisplayStyle | 1 | Simple selection display. |

## StatusMessageTypes
Namespace: adsk.core
The different types of status messages that can be used with the StatusCode object.
Defined in namespace "adsk::core" and the header file is <Core\CoreTypeDefs.h>

| Name | Value | Description |
|------|-------|-------------|
| StatusMessageErrorType | 1 | An error that prevents the operation from succeeding. |
| StatusMessageNoneType | 0 | No error or warning is associated with the status code. |
| StatusMessageWarningType | 2 | A warning that the operation has succeeded but without expected results. |

## SurfaceTypes
Namespace: adsk.core
The different types of surfaces.
Defined in namespace "adsk::core" and the header file is <Core\CoreTypeDefs.h>

| Name | Value | Description |
|------|-------|-------------|
| ConeSurfaceType | 2 | A cone surface. |
| CylinderSurfaceType | 1 | A cylindrical surface. |
| EllipticalConeSurfaceType | 6 | An elliptical cone surface. |
| EllipticalCylinderSurfaceType | 5 | An elliptical cylinder surface. |
| NurbsSurfaceType | 7 | A NURBS surface. |
| PlaneSurfaceType | 0 | A planar surface. |
| SphereSurfaceType | 3 | A spherical surface. |
| TorusSurfaceType | 4 | A torus surface. |

## TablePresentationStyles
Namespace: adsk.core
The different styles that a TableCommandInput can use for its display.
Defined in namespace "adsk::core" and the header file is <Core\CoreTypeDefs.h>

| Name | Value | Description |
|------|-------|-------------|
| itemBorderTablePresentationStyle | 1 | ??? |
| nameValueTablePresentationStyle | 0 | ??? |
| transparentBackgroundTablePresentationStyle | 2 | ??? |

## TextureTypes
Namespace: adsk.core
The different types of textures.
Defined in namespace "adsk::core" and the header file is <Core\CoreTypeDefs.h>

| Name | Value | Description |
|------|-------|-------------|
| CheckerTexture | 2 | A procedural checkered texture. |
| GradientTexture | 3 | A procedural gradient texture. |
| ImageTexture | 1 | A texture defined by an image. |
| MarbleTexture | 4 | A procedural marble texture. |
| NoiseTexture | 5 | A procedural noise texture. |
| SpeckleTexture | 6 | A procedural speckle texture. |
| TileTexture | 7 | A procedural tile texture. |
| UnknownTexture | 0 | Unknown texture type. |
| WaveTexture | 8 | A procedural wave texture. |
| WoodTexture | 9 | A procedural wood texture. |

## TransparencyDisplayEffects
Namespace: adsk.core
A list of the valid transparency display effects.
Defined in namespace "adsk::core" and the header file is <Core\CoreTypeDefs.h>

| Name | Value | Description |
|------|-------|-------------|
| BetterDisplayTransparencyEffect | 1 | Better display transparency effect. |
| BetterPerformanceTransparencyEffect | 0 | Better performance transparency effect. |

## TriadChanges
Namespace: adsk.core
Defines the different types of edits that can be applied by the user to a triad command input.
Defined in namespace "adsk::core" and the header file is <Core\CoreTypeDefs.h>

| Name | Value | Description |
|------|-------|-------------|
| TriadChangeHorizontalFlip | 18 | Defines a horizontal (around the around the Y-Z plane) flip of the triad. |
| TriadChangeUnknown | 0 | Defines an unknown change. |
| TriadChangeVerticalFlip | 19 | Defines a vertical (around the around the X-Z plane) flip of the triad. |
| TriadChangeXRotation | 8 | Defines a rotation around the X axis of the triad. |
| TriadChangeXScale | 11 | Defines a change in scale along the X axis of the triad. |
| TriadChangeXTranslation | 1 | Defines a translation in the X direction of the triad. |
| TriadChangeXYScale | 14 | Defines a uniform change in scale along the X and Y axes of the triad. |
| TriadChangeXYTranslation | 4 | Defines a translation on the X-Y plane of the triad. |
| TriadChangeXYZScale | 17 | Defines a uniform change in scale along the X, Y, and Z axes of the triad. |
| TriadChangeXYZTranslation | 7 | Defines a translation in the X, Y, and Z directions of the triad. |
| TriadChangeXZScale | 16 | Defines a uniform change in scale along the X and Z axes of the triad. |
| TriadChangeXZTranslation | 6 | Defines a translation on the X-Z plane of the triad. |
| TriadChangeYRotation | 9 | Defines a rotation around the Y axis of the triad. |
| TriadChangeYScale | 12 | Defines a change in scale along the Y axis of the triad. |
| TriadChangeYTranslation | 2 | Defines a translation in the Y direction of the triad. |
| TriadChangeYZScale | 15 | Defines a uniform change in scale along the Y and Z axes of the triad. |
| TriadChangeYZTranslation | 5 | Defines a translation on the Y-Z plane of the triad. |
| TriadChangeZRotation | 10 | Defines a rotation around the Z axis of the triad. |
| TriadChangeZScale | 13 | Defines a change in scale along the Z axis of the triad. |
| TriadChangeZTranslation | 3 | Defines a translation in the Z direction of the triad. |

## UploadStates
Namespace: adsk.core
The different states of a file upload process.
Defined in namespace "adsk::core" and the header file is <Core\CoreTypeDefs.h>

| Name | Value | Description |
|------|-------|-------------|
| UploadFailed | 2 | The upload has failed. |
| UploadFinished | 1 | The upload has completed. |
| UploadProcessing | 0 | The upload is still processing. |

## UserInterfaceThemes
Namespace: adsk.core
Defines the different color themes used by the user interface.
Defined in namespace "adsk::core" and the header file is <Core\CoreTypeDefs.h>

| Name | Value | Description |
|------|-------|-------------|
| ClassicUserInterfaceTheme | 0 | The Fusion classic user interface theme. |
| DarkBlueUserInterfaceTheme | 2 | The dark blue user interface theme. |
| DarkGrayUserInterfaceTheme | 3 | The dark gray user interface theme. |
| DeviceUserInterfaceTheme | 4 | Match the OS device theme. |
| LightGrayUserInterfaceTheme | 1 | The light gray user interface theme. |

## UserLanguages
Namespace: adsk.core
A list of the valid languages.
Defined in namespace "adsk::core" and the header file is <Core\CoreTypeDefs.h>

| Name | Value | Description |
|------|-------|-------------|
| ChinesePRCLanguage | 0 | Peoples Republic of China Chinese |
| ChineseTaiwanLanguage | 1 | Taiwan Chinese |
| CzechLanguage | 2 | Czech |
| EnglishLanguage | 3 | English |
| FrenchLanguage | 4 | French |
| GermanLanguage | 5 | German |
| HungarianLanguage | 6 | Hungarian |
| ItalianLanguage | 7 | Italian |
| JapaneseLanguage | 8 | Japanese |
| KoreanLanguage | 9 | Korean |
| PolishLanguage | 10 | Polish |
| PortugueseBrazilianLanguage | 11 | Brazilian Portuguese |
| RussianLanguage | 12 | Russian |
| SpanishLanguage | 13 | Spanish |
| TurkishLanguage | 14 | Turkish |

## ValueInputError
Namespace: adsk.core
Errors that can occur when using the ValueInput object.
Defined in namespace "adsk::core" and the header file is <Core\CoreTypeDefs.h>

| Name | Value | Description |
|------|-------|-------------|
| ValueNotOfTypeError | 100 | Returned when the RealValue or StringValue properties of the ValueInput are called and there is no data to return of that type. |

## ValueTypes
Namespace: adsk.core
The different types of values that a ValueInput can be.
Defined in namespace "adsk::core" and the header file is <Core\CoreTypeDefs.h>

| Name | Value | Description |
|------|-------|-------------|
| BooleanValueType | 3 | Indicates the ValueInput is a boolean value. |
| ObjectValueType | 2 | Indicates the ValueInput is a reference to an object. |
| RealValueType | 1 | Indicates the ValueInput is a real value. |
| StringValueType | 0 | Indicates the ValueInput is a string value. |

## VectorError
Namespace: adsk.core
Error values for various vector operations.
Defined in namespace "adsk::core" and the header file is <Core\CoreTypeDefs.h>

| Name | Value | Description |
|------|-------|-------------|
| ZeroLengthVectorError | 100 | Zero length vector is not allowed. Various vector ops - e.g. IsParallel - don't work with zero length vectors |

## VerticalAlignments
Namespace: adsk.core
Defines the different vertical alignments that can be applied to text.
Defined in namespace "adsk::core" and the header file is <Core\CoreTypeDefs.h>

| Name | Value | Description |
|------|-------|-------------|
| BottomVerticalAlignment | 2 | Aligned to the bottom. |
| MiddleVerticalAlignment | 1 | Aligned along the middle. |
| TopVerticalAlignment | 0 | Aligned to the top. |

## ViewOrientations
Namespace: adsk.core
Common view orientations.
Defined in namespace "adsk::core" and the header file is <Core\CoreTypeDefs.h>

| Name | Value | Description |
|------|-------|-------------|
| ArbitraryViewOrientation | 0 | The view is oriented in an orientation other than one of the predefined orientations. |
| BackViewOrientation | 1 | The view is oriented to see the back of the model. |
| BottomViewOrientation | 2 | The view is oriented to see the bottom of the model. |
| FrontViewOrientation | 3 | The view is oriented to see the front of the model. |
| IsoBottomLeftViewOrientation | 4 | The view is oriented to see the bottom left corner of the model. |
| IsoBottomRightViewOrientation | 5 | The view is oriented to see the bottom right corner of the model. |
| IsoTopLeftViewOrientation | 6 | The view is oriented to see the top left corner of the model. |
| IsoTopRightViewOrientation | 7 | The view is oriented to see the top right corner of the model. |
| LeftViewOrientation | 8 | The view is oriented to see the left of the model. |
| RightViewOrientation | 9 | The view is oriented to see the right of the model. |
| TopViewOrientation | 10 | The view is oriented to see the top of the model. |

## VisualStyles
Namespace: adsk.core
A list of the support visual styles that Fusion uses when rendering the model.
Defined in namespace "adsk::core" and the header file is <Core\CoreTypeDefs.h>

| Name | Value | Description |
|------|-------|-------------|
| ShadedVisualStyle | 0 | Shaded display style. |
| ShadedWithHiddenEdgesVisualStyle | 1 | Shaded with hidden edges displayed. |
| ShadedWithVisibleEdgesOnlyVisualStyle | 2 | Shaded with only the visible edges displayed. |
| WireframeVisualStyle | 3 | Wireframe display style. |
| WireframeWithHiddenEdgesVisualStyle | 4 | Wireframe with hidden edges displayed. |
| WireframeWithVisibleEdgesOnlyVisualStyle | 5 | Wireframe with only the visible edges displayed. |

# adsk.drawing

## PDFSheetsExport
Namespace: adsk.drawing
The various options that define which sheets to print.
Defined in namespace "adsk::drawing" and the header file is <Drawing\DrawingTypeDefs.h>

| Name | Value | Description |
|------|-------|-------------|
| AllPDFSheetsExport | 0 | Exports all of the sheets in the drawing as a single PDF file. |
| CurrentPDFSheetExport | 2 | Exports the current active sheet. |
| RangePDFSheetsExport | 3 | Exports a defined range of sheets. |
| SelectedPDFSheetsExport | 1 | Exports all of the current selected sheets in the drawing. The active sheet is always selected but the user can also select additional sheets. |

# adsk.fusion

## ArrangePriorities
Namespace: adsk.fusion
Defines the different types of arrange priorities that are supported.
Defined in namespace "adsk::fusion" and the header file is <Fusion\FusionTypeDefs.h>

| Name | Value | Description |
|------|-------|-------------|
| HighArrangePriority | 3 | High arrange priority. |
| LowArrangePriority | 1 | Low arrange priority. |
| MediumArrangePriority | 2 | Medium arrange priority. |
| VeryHighArrangePriority | 4 | Very high arrange priority. |
| VeryLowArrangePriority | 0 | Very low arrange priority. |

## ArrangeRotationTypes
Namespace: adsk.fusion
Defines the different types of rotations supported.
Defined in namespace "adsk::fusion" and the header file is <Fusion\FusionTypeDefs.h>

| Name | Value | Description |
|------|-------|-------------|
| AllRotationsArrangeRotationType | 1 | Specifies that all rotation types are allowed. |
| GlobalArrangeRotationType | 0 | Specifies that a component is using the global rotation type. |
| NoneArrangeRotationType | 2 | Specifies that no rotation is allowed. |
| Only180ArrangeRotationType | 3 | Specifies that only 180 deg rotation is allowed. |
| Only90And270ArrangeRotationType | 4 | Specifies that only 90 and 270 deg rotation is allowed. |

## ArrangeSolverTypes
Namespace: adsk.fusion
Defines the different types of arrangement solvers that are supported.
Defined in namespace "adsk::fusion" and the header file is <Fusion\FusionTypeDefs.h>

| Name | Value | Description |
|------|-------|-------------|
| Arrange2DRectangularSolverType | 1 | Rectangular 2D arrangement solver. This is an arrangement type where the rectangular bounding box of the component is used to calculate the arrangement, not the actual shape of the part. |
| Arrange2DTrueShapeSolverType | 0 | True Shape 2D arrangement solver. This is an arrangement type where the components are arranged on a plane so they fit tightly together honoring the arrangement definition. |
| Arrange3DSolverType | 2 | 3D arrangement solver. This is an arrangement type where the parts are arranged within a 3D rectangular volume where the bounding box of the parts is used to determine the size of the part. |

## AutoLookAtSketchSettings
Namespace: adsk.fusion
The different options for the AutoLookAtSketch preference setting.
Defined in namespace "adsk::fusion" and the header file is <Fusion\FusionTypeDefs.h>

| Name | Value | Description |
|------|-------|-------------|
| AlwaysOrthographicAutoLookAtSketchSetting | 2 | Turn on the Auto Look at Sketch functionality and use an orthographic camera when looking at the sketch. |
| OffAutoLookAtSketchSetting | 0 | Turn off the Auto Look at Sketch functionality. |
| UserCameraAutoLookAtSketchSetting | 1 | Turn on the Auto Look at Sketch functionality and use the current camera setting when looking at the sketch. |

## BRepConvertOptions
Namespace: adsk.fusion
Defines the various options when converting the geometry of a B-Rep body or face to NURBS. This is used by the convert method of the BRepBody and BRepFace objects.
Defined in namespace "adsk::fusion" and the header file is <Fusion\FusionTypeDefs.h>

| Name | Value | Description |
|------|-------|-------------|
| AnalyticsToNURBSConversion | 1 | Converts all analytic surfaces (cylinder, elliptical cylinder, cone, elliptical cone, sphere, and torus) except planes to NURBS surfaces. |
| PlanesToNURBSConversion | 2 | Converts all planar faces to NURBS surfaces. |
| ProceduralToNURBSConversion | 0 | Converts all procedurally calculated faces and edges into NURBS within the base tolerance. For example, an edge that is the intersection of two faces is represented as the exact analytical intersection of the two faces. This is converted into a NURBS curve as part of the conversion. |
| SplitPeriodicFacesConversion | 4 | Splits any periodic surfaces so they become open surfaces. |

## BRepEntityTypes
Namespace: adsk.fusion
Used by the findBRepUsingRay and findBRepUsingPoint methods to specify the desired return type.
Defined in namespace "adsk::fusion" and the header file is <Fusion\FusionTypeDefs.h>

| Name | Value | Description |
|------|-------|-------------|
| BRepBodyEntityType | 0 | Specifies that BRepBody objects should be returned. |
| BRepEdgeEntityType | 2 | Specifies that BRepEdge objects should be returned. |
| BRepFaceEntityType | 1 | Specifies that BRepFace objects should be returned. |
| BRepVertexEntityType | 3 | Specifies that BRepVertex objects should be returned. |

## BendPositionTypes
Namespace: adsk.fusion
Bend location types used for creating flanges and hems.
Defined in namespace "adsk::fusion" and the header file is <Fusion\FusionTypeDefs.h>

| Name | Value | Description |
|------|-------|-------------|
| InsideBendPositionType | 2 | Reference Plane through other Edge, Material inside |
| LegacyBendPositionType | 0 | Legacy bend location type no longer used. Not tangent to side, same reference plane as eBendInnerVS, but material can flip. |
| OutsideBendPositionType | 1 | Reference Plane through selected Edge, Material outside |
| StartEdgeBendPositionType | 3 | Reference Plane is the Side Face, Bend starts at selected edge |
| TangentToSideBendPositionType | 4 | Reference Plane is the Side Face, Bend Tangent to Ref Plane if angle >= 90 |

## BendReliefShapes
Namespace: adsk.fusion
The bend relief shapes used for a single bend.
Defined in namespace "adsk::fusion" and the header file is <Fusion\FusionTypeDefs.h>

| Name | Value | Description |
|------|-------|-------------|
| RoundBendReliefShape | 2 | Round shape for the bend relief. |
| StraightBendReliefShape | 0 | Straight shape for the bend relief. |
| TearBendReliefShape | 1 | Tear shape for the bend relief. |

## BooleanTypes
Namespace: adsk.fusion
Defines the different type of boolean operations that are supported.
Defined in namespace "adsk::fusion" and the header file is <Fusion\FusionTypeDefs.h>

| Name | Value | Description |
|------|-------|-------------|
| DifferenceBooleanType | 0 | Subtracts the tool body from the target body. |
| IntersectionBooleanType | 1 | Intersection the tool body with the target body. |
| UnionBooleanType | 2 | Unions the tool body with the target body. |

## BossAlignmentTypes
Namespace: adsk.fusion
List of different types of boss alignment shape types.
Defined in namespace "adsk::fusion" and the header file is <Fusion\FusionTypeDefs.h>

| Name | Value | Description |
|------|-------|-------------|
| BossAlignFlat | 0 | Boss flat alignment. |
| BossAlignStepIn | 2 | Boss with step in. |
| BossAlignStepOut | 1 | Boss with step out. |

## BossHoleExtentTypes
Namespace: adsk.fusion
List of the different types of boss hole extent types.
Defined in namespace "adsk::fusion" and the header file is <Fusion\FusionTypeDefs.h>

| Name | Value | Description |
|------|-------|-------------|
| BossBlindDepth | 2 | Blind hole set by hole depth. |
| BossBlindFull | 1 | Blind hole of max depth with offset from bottom. |
| BossHoleThrough | 0 | Hole through all body. |

## BossRibExtentTypes
Namespace: adsk.fusion
List of different types of boss rib extent type.
Defined in namespace "adsk::fusion" and the header file is <Fusion\FusionTypeDefs.h>

| Name | Value | Description |
|------|-------|-------------|
| RibSizeByLength | 0 | Boss rib has given shape and length as specified. |
| RibSizeToNext | 1 | Boss rib has shape of web and extents to next face. |
| RibSuppressed | 2 | Boss rib is suppressed. |

## BossRibShapeTypes
Namespace: adsk.fusion
List of different types of boss rib shape.
Defined in namespace "adsk::fusion" and the header file is <Fusion\FusionTypeDefs.h>

| Name | Value | Description |
|------|-------|-------------|
| BossRibShapeChamfer | 1 | Boss with chamfered ribs. |
| BossRibShapeFillet | 2 | Boss with filleted ribs |
| BossRibShapeNone | 0 | Boss with no ribs. |

## BossShapeTypes
Namespace: adsk.fusion
List of different boss shank shape types.
Defined in namespace "adsk::fusion" and the header file is <Fusion\FusionTypeDefs.h>

| Name | Value | Description |
|------|-------|-------------|
| BossBlank | 0 | Blank boss with no hole and constant diameter. |
| BossConstDiameter | 1 | Boss with constant outer shank diameter. |
| BossConstThickness | 2 | Boss with constant shank thickness. Not supported yet. |

## BoundingBoxEntityTypes
Namespace: adsk.fusion
Specifies the various types of entities that can be included in bounding box calculations. This is a bitwise friendly enum so types can be combined to specify more than one type.
Defined in namespace "adsk::fusion" and the header file is <Fusion\FusionTypeDefs.h>

| Name | Value | Description |
|------|-------|-------------|
| AllEntitiesBoundingBoxEntityType | 0 | Will include all types of geometry in the calculation. |
| ConstructionBoundingBoxEntityType | 16 | Includes the visible portion of construction geometry in the bounding box calculation. |
| MeshBodyBoundingBoxEntityType | 4 | Includes mesh bodies in the bounding box calculation. |
| SketchBoundingBoxEntityType | 8 | Includes sketch geometry in the bounding box calculation. |
| SolidBRepBodyBoundingBoxEntityType | 1 | Includes Solid B-Rep bodies in the bounding box calculation. |
| SurfaceBodyBoundingBoxEntityType | 2 | Includes B-Rep bodies that are not watertight (surfaces) in the bounding box calculation. |

## CalculationAccuracy
Namespace: adsk.fusion
The different accuracy settings for calculating area and physical property related values. The higher the accuracy setting, the longer it will take to perform the calculations.
Defined in namespace "adsk::fusion" and the header file is <Fusion\FusionTypeDefs.h>

| Name | Value | Description |
|------|-------|-------------|
| HighCalculationAccuracy | 2 | Sets the calculation accuracy to high, which returns results within a +/- 0.1% error margin. |
| LowCalculationAccuracy | 0 | Sets the calculation accuracy to low, which returns results within a +/- 1% error margin. |
| MediumCalculationAccuracy | 1 | Sets the calculation accuracy to medium, which returns results within a +/- 0.5% error margin. |
| VeryHighCalculationAccuracy | 3 | Sets the calculation accuracy to very high, which returns results within a +/- 0.01% error margin. |

## ChainedCurveOptions
Namespace: adsk.fusion
Controls options used when creating a Path and determining the rules for how curves are considered to be chained or connected.
Defined in namespace "adsk::fusion" and the header file is <Fusion\FusionTypeDefs.h>

| Name | Value | Description |
|------|-------|-------------|
| connectedChainedCurves | 1 | Will find curves that are geometrically connected without regards to the geometry condition at the connection. This is limited to sketch curves. |
| noChainedCurves | 0 | No chaining is done. This is useful when inputting a single entity and you don't want any chaining to be done. |
| openEdgesChainedCurves | 3 | Will find edges that are geometrically end connected and are open edges of an open BRepBody. |
| tangentAndOpenEdgesChainedCurves | 4 | Will find edges that are geometrically end connected, are tangent at the connection, and are open edges of an open BRepBody. |
| tangentChainedCurves | 2 | Will find curves that are geometrically connected and tangent at the connection. This will work for both sketch curves and edges. |

## ChamferCornerTypes
Namespace: adsk.fusion
Specifies the type of corner to model when multiple edges come together at a vertex.
Defined in namespace "adsk::fusion" and the header file is <Fusion\FusionTypeDefs.h>

| Name | Value | Description |
|------|-------|-------------|
| BlendCornertype | 2 | A blend surface is created to define the corner. |
| ChamferCornerType | 0 | The default corner type, where a small patch is created at the corner. |
| MiterCornerType | 1 | The chamfer surfaces extend and intersect one another to create the corner. |

## ChamferTypes
Namespace: adsk.fusion
List of the different ways a chamfer can be defined.
Defined in namespace "adsk::fusion" and the header file is <Fusion\FusionTypeDefs.h>

| Name | Value | Description |
|------|-------|-------------|
| DistanceAndAngleChamferType | 2 | chamfer feature created using a distance and an angle |
| EqualDistanceChamferType | 0 | chamfer feature created using one equal distance |
| TwoDistancesChamferType | 1 | chamfer feature created using two distances |

## ClearanceHoleFits
Namespace: adsk.fusion
List of the different types of fit that a clearance hole can be.
Defined in namespace "adsk::fusion" and the header file is <Fusion\FusionTypeDefs.h>

| Name | Value | Description |
|------|-------|-------------|
| CloseClearanceHoleFit | 0 | The clearance hole is a tight or close fit around the fastener. |
| LooseClearanceHoleFit | 2 | The clearance hole is a loose fit around the fastener. |
| NormalClearanceHoleFit | 1 | The clearance hole is a normal fit around the fastener. |

## CoilFeatureSectionPositions
Namespace: adsk.fusion
List of the section positions of coil feature.
Defined in namespace "adsk::fusion" and the header file is <Fusion\FusionTypeDefs.h>

| Name | Value | Description |
|------|-------|-------------|
| InsideCoilFeatureSectionPosition | 0 | The coil section is inside of the profile. |
| OnCenterCoilFeatureSectionPosition | 1 | The coil section center is on the profile. |
| OutsideCoilFeatureSectionPosition | 2 | The coil section is outside of the profile. |

## CoilFeatureSectionTypes
Namespace: adsk.fusion
List of the section types of coil primitive feature.
Defined in namespace "adsk::fusion" and the header file is <Fusion\FusionTypeDefs.h>

| Name | Value | Description |
|------|-------|-------------|
| CircularCoilFeatureSectionType | 0 | The coil section is circular. |
| SquareCoilFeatureSectionType | 1 | The coil section is square. |
| TriangularExternalCoilFeatureSectionType | 2 | The coil section is triangular (external). |
| TriangularInternalCoilFeatureSectionType | 3 | The coil section is triangular (internal). |

## CoilFeatureTypes
Namespace: adsk.fusion
List of the coil types.
Defined in namespace "adsk::fusion" and the header file is <Fusion\FusionTypeDefs.h>

| Name | Value | Description |
|------|-------|-------------|
| HeightAndPitchCoilFeatureType | 2 | Coil is defined by specifying height, pitch and angle. |
| RevolutionsAndHeightCoilFeatureType | 0 | Coil is defined by specifying revolutions, height and angle. |
| RevolutionsAndPitchCoilFeatureType | 1 | Coil is defined by specifying revolutions, pitch and angle. |
| SpiralCoilFeatureType | 3 | Coil is defined by specifying revolutions and pitch. |

## ConfigurationClearanceHoleColumns
Namespace: adsk.fusion
Enum that defines the valid combinations of clearance hole columns that can be configured.
Defined in namespace "adsk::fusion" and the header file is <Fusion\FusionTypeDefs.h>

| Name | Value | Description |
|------|-------|-------------|
| Size_ClearanceHoleColumns | 2 | Defines that the clearance hole size and fit will be used to partially define the clearance hole. The Hole feature controls the standard and fastener type, and the fit is defined separately. |
| Standard_Type_Size_ClearanceHoleColumns | 0 | Defines that the clearance hole standard, fastener type, and and size will be used to define the clearance hole. The fit is defined separately. |
| Type_Size_ClearanceHoleColumns | 1 | Defines that the clearance hole fastener type, and size will be used to partially define the clearance hole. The Hole feature controls the standard, and the fit is defined separately. |

## ConfigurationFeatureAspectTypes
Namespace: adsk.fusion
Defines a list of all of the different aspects of a feature that can be configured.
Defined in namespace "adsk::fusion" and the header file is <Fusion\FusionTypeDefs.h>

| Name | Value | Description |
|------|-------|-------------|
| ClearanceHoleFitFeatureAspectType | 13 | A feature aspect that defines the fit of a clearance hole. |
| ClearanceHoleSizeFeatureAspectType | 12 | A feature aspect that defines the size of a clearance hole. |
| ClearanceHoleStandardFeatureAspectType | 10 | A feature aspect that defines the standard for a clearance hole. |
| ClearanceHoleTypeFeatureAspectType | 11 | A feature aspect that defines the fastener type of a clearance hole. |
| JointFlipFeatureAspectType | 7 | A feature aspect that controls if a joint is flipped. |
| JointSnapOneFeatureAspectType | 8 | A feature aspect that defines the snap to the first occurrence of a joint. |
| JointSnapTwoFeatureAspectType | 9 | A feature aspect that defines the snap to the second occurrence of a joint. |
| ThreadClassFeatureAspectType | 3 | A feature aspect that defines the thread class of a thread or tapped hole. |
| ThreadDesignationFeatureAspectType | 2 | A feature aspect that defines the thread designation of a thread or tapped hole. |
| ThreadFullLengthFeatureAspectType | 5 | A feature aspect that defines if the thread goes the full length of the cylinder. |
| ThreadIsRightHandedFeatureAspectType | 6 | A feature aspect that defines if the thread is right or left handed. |
| ThreadModeledFeatureAspectType | 4 | A feature aspect that defines if the thread is cosmetic or modeled. |
| ThreadSizeFeatureAspectType | 1 | A feature aspect that defines the thread size of a thread or tapped hole. |
| ThreadTypeFeatureAspectType | 0 | A feature aspect that defines the thread type of a thread or tapped hole. |

## ConfigurationThreadColumns
Namespace: adsk.fusion
Enum that defines the valid combinations of thread columns that can be configured.
Defined in namespace "adsk::fusion" and the header file is <Fusion\FusionTypeDefs.h>

| Name | Value | Description |
|------|-------|-------------|
| TaperedDesignationColumns | 6 | Defines that the designation will be used to partially define a tapered tapped hole. The tapped hole controls thread type and size. |
| TaperedSize_DesignationColumns | 5 | Defines that the size and designation will be used to partially define a tapered tapped hole. The tapped hole controls the thread type. |
| TaperedThreadType_Size_DesignationColumns | 4 | Defines that the thread type, size, and designation will fully define a tapered tapped hole. |
| ThreadClassColumns | 3 | Defines that the thread class will be used to partially define the thread. The Thread feature or tapped hole controls the thread type, size, and designation. |
| ThreadDesignation_ClassColumns | 2 | Defines that the thread designation and class will be used to partially define the thread. The Thread feature or tapped hole controls the thread type and size. |
| ThreadSize_Designation_ClassColumns | 1 | Defines that the thread size, designation, and class will be used to partially define the thread. The Thread feature or tapped hole controls the thread type. |
| ThreadType_Size_Designation_ClassColumns | 0 | Defines that the thread type, size, designation, and class will fully define the thread on the thread feature or tapped hole. |

## CornerBendTransitionTypes
Namespace: adsk.fusion
The different bend transition types for corner closures.
Defined in namespace "adsk::fusion" and the header file is <Fusion\FusionTypeDefs.h>

| Name | Value | Description |
|------|-------|-------------|
| SmoothCornerBendTransitionType | 0 | Smooth bend transition. |
| StraightLineCornerBendTransitionType | 1 | Straight line bend transition. |
| TrimToBendCornerBendTransitionType | 2 | Trim to bend transition. |

## CornerClosureFeatureDefinitionTypes
Namespace: adsk.fusion
The different types of corner closures that can be created.
Defined in namespace "adsk::fusion" and the header file is <Fusion\FusionTypeDefs.h>

| Name | Value | Description |
|------|-------|-------------|
| ThreeBendCornerClosureFeatureDefinitionType | 2 | A three-bend corner closure that handles three-bend intersections with advanced relief options. |
| TwoBendCornerClosureFeatureDefinitionType | 1 | A two-bend corner closure that includes relief features for two-bend intersections. |
| UndefinedCornerClosureFeatureDefinitionType | 0 | The corner closure type is undefined. This occurs when a new CornerClosureFeatureInput is created and before a specific type has been defined. |

## CornerThreeBendReliefShapeTypes
Namespace: adsk.fusion
The different relief shapes for three-bend corner closures.
Defined in namespace "adsk::fusion" and the header file is <Fusion\FusionTypeDefs.h>

| Name | Value | Description |
|------|-------|-------------|
| FullRoundCornerThreeBendReliefShapeType | 2 | Full round relief shape. |
| IntersectionCornerThreeBendReliefShapeType | 1 | Intersection relief shape. |
| NoReplacementCornerThreeBendReliefShapeType | 0 | No replacement relief shape. |
| RoundWithRadiusCornerThreeBendReliefShapeType | 3 | Round with radius relief shape. |

## CornerTwoBendReliefPlacementTypes
Namespace: adsk.fusion
The different placement types for two-bend corner relief.
Defined in namespace "adsk::fusion" and the header file is <Fusion\FusionTypeDefs.h>

| Name | Value | Description |
|------|-------|-------------|
| IntersectionCornerTwoBendReliefPlacementType | 1 | Intersection placement for the relief. |
| TangentCornerTwoBendReliefPlacementType | 0 | Tangent placement for the relief. |

## CornerTwoBendReliefShapeTypes
Namespace: adsk.fusion
The different relief shapes for two-bend corner closures.
Defined in namespace "adsk::fusion" and the header file is <Fusion\FusionTypeDefs.h>

| Name | Value | Description |
|------|-------|-------------|
| ArcWeldCornerTwoBendReliefShapeType | 5 | Arc weld relief shape. |
| LaserWeldCornerTwoBendReliefShapeType | 6 | Laser weld relief shape. |
| LinearWeldCornerTwoBendReliefShapeType | 4 | Linear weld relief shape. |
| RoundCornerTwoBendReliefShapeType | 0 | Round relief shape. |
| SquareCornerTwoBendReliefShapeType | 1 | Square relief shape. |
| TearCornerTwoBendReliefShapeType | 2 | Tear relief shape. |
| TrimToBendCornerTwoBendReliefShapeType | 3 | Trim to bend relief shape. |

## CustomGraphicsBillBoardStyles
Namespace: adsk.fusion
Specifies the different styles that can be used to control billboarding.
Defined in namespace "adsk::fusion" and the header file is <Fusion\FusionTypeDefs.h>

| Name | Value | Description |
|------|-------|-------------|
| AxialBillBoardStyle | 2 | Sets the billboarding so that the graphics X axis will align with a defined axis. |
| RightReadingBillBoardStyle | 3 | Sets the billboarding so that graphics can never be viewed from the back. As the view is rotated, the graphics will be automatically flipped so they are always viewed from the front. |
| ScreenBillBoardStyle | 1 | Billboards relative to the screen, so the x-y plane of the graphics will always remain parallel to the view plane. and the graphics X axis will align with the view's x axis. |

## CustomGraphicsCullModes
Namespace: adsk.fusion
The various culling modes supported by custom graphics.
Defined in namespace "adsk::fusion" and the header file is <Fusion\FusionTypeDefs.h>

| Name | Value | Description |
|------|-------|-------------|
| CustomGraphicsCullBack | 1 | Cull the graphics that are back facing. |
| CustomGraphicsCullFront | 0 | Cull the graphics that are front facing. |
| CustomGraphicsCullNone | 2 | Do not perform any culling. |

## CustomGraphicsPointTypes
Namespace: adsk.fusion
A list of predefined point images that you can use for a CustomGraphicsPointSet.
Defined in namespace "adsk::fusion" and the header file is <Fusion\FusionTypeDefs.h>

| Name | Value | Description |
|------|-------|-------------|
| PointCloudCustomGraphicsPointType | 1 | Displays the point using a single pixel. This is the most efficient point display type and can be used to display very large quantities of points. |
| UserDefinedCustomGraphicsPointType | 0 | Specifies that the type of point is user defined, which means you supply the image. |

## DefaultDesignTypeOptions
Namespace: adsk.fusion
The valid options for the default modeling type setting.
Defined in namespace "adsk::fusion" and the header file is <Fusion\FusionTypeDefs.h>

| Name | Value | Description |
|------|-------|-------------|
| DirectDesignTypeOption | 1 | Create a direct edit (non-parametric) design. |
| ParametricDesignTypeOption | 2 | Create a parametric design. |
| PromptForDesignTypeOption | 0 | Prompt the user for the design type. |

## DefaultWorkspaces
Namespace: adsk.fusion
The valid options for the Default workspaces setting.
Defined in namespace "adsk::fusion" and the header file is <Fusion\FusionTypeDefs.h>

| Name | Value | Description |
|------|-------|-------------|
| ModelWorkspace | 0 | The model workspace. |
| PatchWorkspace | 2 | The patch workspace. |
| SculptWorkspace | 1 | The sculpt workspace. |

## DeleteMeError
Namespace: adsk.fusion
Specific error types for DeleteMe methods.
Defined in namespace "adsk::fusion" and the header file is <Fusion\FusionTypeDefs.h>

| Name | Value | Description |
|------|-------|-------------|
| ParameterReferencedByOtherParameterError | 200 | The parameter is referenced by another parameter. |

## DesignIntentTypes
Namespace: adsk.fusion
The different types of design intent.
Defined in namespace "adsk::fusion" and the header file is <Fusion\FusionTypeDefs.h>

| Name | Value | Description |
|------|-------|-------------|
| AssemblyDesignIntentType | 1 | Defines the intent to create an assembly design. |
| HybridDesignIntentType | 2 | Defines the intent to create a hybrid design. |
| PartDesignIntentType | 0 | Defines the intent to create a part design. |

## DesignTypes
Namespace: adsk.fusion
Fusion design types
Defined in namespace "adsk::fusion" and the header file is <Fusion\FusionTypeDefs.h>

| Name | Value | Description |
|------|-------|-------------|
| DirectDesignType | 0 | Direct modeling design. |
| ParametricDesignType | 1 | Parametric modeling design. |

## DimensionOrientations
Namespace: adsk.fusion
The different dimension orientations.
Defined in namespace "adsk::fusion" and the header file is <Fusion\FusionTypeDefs.h>

| Name | Value | Description |
|------|-------|-------------|
| AlignedDimensionOrientation | 0 | The dimension is aligned to the entity being dimensioned. |
| HorizontalDimensionOrientation | 1 | The dimension is horizontal. |
| VerticalDimensionOrientation | 2 | The dimension is vertical. |

## DistanceUnits
Namespace: adsk.fusion
Valid unit types for distance.
Defined in namespace "adsk::fusion" and the header file is <Fusion\FusionTypeDefs.h>

| Name | Value | Description |
|------|-------|-------------|
| CentimeterDistanceUnits | 1 | Centimeter |
| FootDistanceUnits | 4 | Foot |
| HectometerDistanceUnits | 7 | Hectometer |
| InchDistanceUnits | 3 | Inch |
| MeterDistanceUnits | 2 | Meter |
| MicronDistanceUnits | 6 | Micron |
| MilDistanceUnits | 9 | Mil (One thousandth of an inch) |
| MileDistanceUnits | 8 | Mile |
| MillimeterDistanceUnits | 0 | Millimeter |
| NauticalMileDistanceUnits | 10 | Nautical Mile |
| YardDistanceUnits | 5 | Yard |

## ExpressionError
Namespace: adsk.fusion
The expression of the parameter. Setting this can fail because of an invalid expression or because a cyclic reference is created between parameters.
Defined in namespace "adsk::fusion" and the header file is <Fusion\FusionTypeDefs.h>

| Name | Value | Description |
|------|-------|-------------|
| CyclicParameterReferenceError | 200 | A cyclical parametric reference occurred. |

## ExtentDirections
Namespace: adsk.fusion
List of the valid extent directions.
Defined in namespace "adsk::fusion" and the header file is <Fusion\FusionTypeDefs.h>

| Name | Value | Description |
|------|-------|-------------|
| NegativeExtentDirection | 1 | Feature extent in the negative direction. For sketch based features this is typically in the direction opposite the sketch normal. |
| PositiveExtentDirection | 0 | Feature extent in the positive direction. For sketch based features this is typically in the same direction as the sketch normal. |
| SymmetricExtentDirection | 2 | Feature extent in both directions. |

## FeatureExtentTypes
Namespace: adsk.fusion
Used to indicate which type of extent is used for a feature.
Defined in namespace "adsk::fusion" and the header file is <Fusion\FusionTypeDefs.h>

| Name | Value | Description |
|------|-------|-------------|
| OneSideFeatureExtentType | 0 | Specifies a feature extent that is defined in a single direction. |
| SymmetricFeatureExtentType | 2 | Specifies a feature extent that is defined symmetrically in two directions. |
| TwoSidesFeatureExtentType | 1 | Specifies a feature extent that is defined in two directions. |

## FeatureHealthStates
Namespace: adsk.fusion
The various states that a feature can be in. This is used for the states of modeling features, construction geometry, and sketches.
Defined in namespace "adsk::fusion" and the header file is <Fusion\FusionTypeDefs.h>

| Name | Value | Description |
|------|-------|-------------|
| ErrorFeatureHealthState | 2 | The feature, construction geometry, or sketch has an error. Use the errorOrWarningMessage property to get the message. |
| HealthyFeatureHealthState | 0 | The feature, construction geometry, or sketch is successfully computed. |
| RolledBackFeatureHealthState | 4 | The feature, construction geometry, or sketch is rolled back so it has not computed. |
| SuppressedFeatureHealthState | 3 | The feature, construction geometry, or sketch is suppressed so it has not computed. |
| UnknownFeatureHealthState | 5 | The state of the object is unknown. This can occur in the case where the object being queried is a TimelineObject whose associated entity does not have a health state. For example, if it is a TimelineGroup or an position snapshot. |
| WarningFeatureHealthState | 1 | The feature, construction geometry, or sketch has a warning. Use the errorOrWarningMessage property to get the message. |

## FeatureOperations
Namespace: adsk.fusion
List of the different operations a feature can perform.
Defined in namespace "adsk::fusion" and the header file is <Fusion\FusionTypeDefs.h>

| Name | Value | Description |
|------|-------|-------------|
| CutFeatureOperation | 1 | The feature cuts or removes materials. |
| IntersectFeatureOperation | 2 | The feature intersects with an existing body and the result is the intersecting volume. |
| JoinFeatureOperation | 0 | The feature joins or adds material. |
| NewBodyFeatureOperation | 3 | Results in the creation of a new body. |
| NewComponentFeatureOperation | 4 | Results in the creation of a new component that contains the new body. |

## FilletFeatureTypes
Namespace: adsk.fusion
List of the fillet feature types.
Defined in namespace "adsk::fusion" and the header file is <Fusion\FusionTypeDefs.h>

| Name | Value | Description |
|------|-------|-------------|
| FilletFeatureType | 0 | The fillet feature type. |
| FullRoundFilletFeatureType | 2 | The full round fillet feature type. |
| RuleFilletFeatureType | 1 | The rule fillet feature type. |

## HemFeatureDefinitionTypes
Namespace: adsk.fusion
The different types of hems that can be created.
Defined in namespace "adsk::fusion" and the header file is <Fusion\FusionTypeDefs.h>

| Name | Value | Description |
|------|-------|-------------|
| DoubleHemFeatureDefinitionType | 6 | A double hem is where the edge is bent over twice to form a hem that doubles back on itself. |
| FlatHemFeatureDefinitionType | 1 | A flat hem is like an open hem but the gap is closed and the edge is flattened against the main sheet. |
| OpenHemFeatureDefinitionType | 2 | An open hem is simple bend along an edge that leaves a gap between the hem and the main sheet. |
| RolledHemFeatureDefinitionType | 3 | A rolled hem is where the edge is rolled over to form a tube-like profile. |
| RopeHemFeatureDefinitionType | 5 | A rope hem is where the edge is rolled over (like a rolled hem) with an added length after the roll parallel to the main sheet. |
| TeardropHemFeatureDefinitionType | 4 | A teardrop hem is where the edge is bent around a diameter to form a teardrop like profile. |
| UndefinedHemFeatureDefinitionType | 0 | The hem type is undefined. This occurs when a new HemFeatureInput is created and before a specific type has been defined. |

## HoleEdgePositions
Namespace: adsk.fusion
List of the valid edge positions for holes.
Defined in namespace "adsk::fusion" and the header file is <Fusion\FusionTypeDefs.h>

| Name | Value | Description |
|------|-------|-------------|
| EdgeEndPointPosition | 2 | The end point of an Edge. |
| EdgeMidPointPosition | 1 | The midpoint of an Edge. |
| EdgeStartPointPosition | 0 | The start point of an Edge. |

## HoleTapTypes
Namespace: adsk.fusion
List of the valid tap types for holes.
Defined in namespace "adsk::fusion" and the header file is <Fusion\FusionTypeDefs.h>

| Name | Value | Description |
|------|-------|-------------|
| ClearanceHoleTapType | 1 | A clearance hole tap type. |
| SimpleHoleTapType | 0 | A simple (no threads) hole tap type. |
| TaperTappedHoleTapType | 3 | A taper tapped hole tap type. |
| TappedHoleTapType | 2 | A tapped hole tap type. |

## HoleTypes
Namespace: adsk.fusion
List of the different types of holes.
Defined in namespace "adsk::fusion" and the header file is <Fusion\FusionTypeDefs.h>

| Name | Value | Description |
|------|-------|-------------|
| CounterboreHoleType | 1 | A counterbore hole. |
| CountersinkHoleType | 2 | a countersink hole. |
| SimpleHoleType | 0 | A simple drilled hole. |

## JointDirections
Namespace: adsk.fusion
Specifies the different types of directions that can be used to define directions of a joint.
Defined in namespace "adsk::fusion" and the header file is <Fusion\FusionTypeDefs.h>

| Name | Value | Description |
|------|-------|-------------|
| CustomJointDirection | 3 | Defines that the joint direction is custom and is defined by an entity. |
| XAxisJointDirection | 0 | Defines a direction in the X-axis of the joints coordinate system. |
| YAxisJointDirection | 1 | Defines a direction in the Y-axis of the joints coordinate system. |
| ZAxisJointDirection | 2 | Defines a direction in the Z-axis of the joints coordinate system. |

## JointGeometryTypes
Namespace: adsk.fusion
List of the different types of ways that geometry for a joint can be defined.
Defined in namespace "adsk::fusion" and the header file is <Fusion\FusionTypeDefs.h>

| Name | Value | Description |
|------|-------|-------------|
| JointBetweenTwoPlanesGeometry | 8 | Joint geometry defined between two planes. |
| JointBRepEdgeGeometry | 3 | Joint geometry defined by a B-Rep edge. |
| JointBRepVertexGeometry | 2 | Joint geometry defined by a B-Rep Vertex. |
| JointByTwoEdgeIntersectionGeometry | 9 | Joint geometry defined by two edge intersection. |
| JointConstructionPointGeometry | 0 | Joint geometry defined by a construction point. |
| JointNonPlanarBRepFaceGeometry | 7 | Joint geometry defined by a non-planar B-Rep face. |
| JointPlanarBRepFaceGeometry | 6 | Joint geometry defined by a planar B-Rep face. |
| JointProfileGeometry | 5 | Joint geometry defined by a profile. |
| JointSketchCurveGeometry | 4 | Joint geometry defined by a sketch curve. |
| JointSketchPointGeometry | 1 | Joint geometry defined by a sketch point. |
| JointTangentBRepFaceEdgeGeometry | 11 | Joint geometry defined by tangent face and edge. |
| JointTangentBRepFaceGeometry | 10 | Joint geometry defined by tangent faces: cylinder or cone, sphere, torus and spline |

## JointKeyPointTypes
Namespace: adsk.fusion
List of the various keypoints of geometry that can be used when defining joint geometry.
Defined in namespace "adsk::fusion" and the header file is <Fusion\FusionTypeDefs.h>

| Name | Value | Description |
|------|-------|-------------|
| CenterKeyPoint | 3 | Specifies the position of the keypoint at the center of the entity. This applies to entities like circles, ellipses, planar faces, and profiles. |
| EndKeyPoint | 2 | Specifies the position of the keypoint at the end of the entity. |
| MiddleKeyPoint | 1 | Specifies the position of the keypoint at the middle of the entity. |
| StartKeyPoint | 0 | Specifies the position of the keypoint at the start of the entity. |

## JointMotionTypes
Namespace: adsk.fusion
List of the various types of motions of joints.
Defined in namespace "adsk::fusion" and the header file is <Fusion\FusionTypeDefs.h>

| Name | Value | Description |
|------|-------|-------------|
| BallJointPitchMotionType | 0 | Ball joint pitch motion. |
| BallJointRollMotionType | 1 | Ball joint roll motion. |
| BallJointYawMotionType | 2 | Ball joint yaw motion. |
| CylindricalJointRotateMotionType | 3 | Cylindrical joint rotate motion. |
| CylindricalJointSlideMotionType | 4 | Cylindrical joint slide motion. |
| PinSlotJointRotateMotionType | 5 | PinSlot joint rotate motion. |
| PinSlotJointSlideMotionType | 6 | PinSlot joint slide motion. |
| PlanarJointRotateMotionType | 7 | Planar joint rotate motion. |
| PlanarJointSlideOneMotionType | 8 | Planar joint slide 1 motion. |
| PlanarJointSlideTwoMotionType | 9 | Planar joint slide 2 motion. |
| RevoluteJointRotateMotionType | 10 | Revolute joint rotate motion. |
| SliderJointSlideMotionType | 11 | Slider joint slide motion. |

## JointQuadrantAngleTypes
Namespace: adsk.fusion
List of the various angle types of geometry that can be used when defining joint geometry on cylinder or cone, sphere and torus
Defined in namespace "adsk::fusion" and the header file is <Fusion\FusionTypeDefs.h>

| Name | Value | Description |
|------|-------|-------------|
| MiddleJointQuadrantAngleType | 2 | Specifies the angle at the half point of a circle |
| QuarterJointQuadrantAngleType | 1 | Specifies the angle at the quarter point of a circle |
| StartJointQuadrantAngleType | 0 | Specifies the angle at the start point of a circle |
| ThirdQuarterJointQuadrantAngleType | 3 | Specifies the angle at the third quarter point of a circle |

## JointTangentFaceEdgePointTypes
Namespace: adsk.fusion
List of the tangent face types, including cylinder or cone, sphere, torus and spline.
Defined in namespace "adsk::fusion" and the header file is <Fusion\FusionTypeDefs.h>

| Name | Value | Description |
|------|-------|-------------|
| EndJointTangentFaceEdgePointType | 4 | Specifies the end point of the edge. |
| MiddleJointTangentFaceEdgePointType | 2 | Specifies the middle point of the edge. |
| QuarterJointTangentFaceEdgePointType | 1 | Specifies the point at the quarter of whole length of the edge. |
| StartJointTangentFaceEdgePointType | 0 | Specifies the start point of the edge. |
| ThirdQuarterJointTangentFaceEdgePointType | 3 | Specifies the point at third quarter of whole length of the edge. |

## JointTangentFaceTypes
Namespace: adsk.fusion
List of the tangent face types, including cylinder or cone, sphere, torus and spline.
Defined in namespace "adsk::fusion" and the header file is <Fusion\FusionTypeDefs.h>

| Name | Value | Description |
|------|-------|-------------|
| CylinderOrConeJointTangentFaceType | 1 | Specifies the tangent face type for cyliner or cone |
| NoneJointTangentFaceType | 0 | Specifies the tangent face type for cyliner or cone |
| SphereJointTangentFaceType | 2 | Specifies the tangent face type for sphere |
| SplineJointTangentFaceType | 4 | Specifies the tangent face type for spline |
| TorusJointTangentFaceType | 3 | Specifies the tangent face type for torus |

## JointTypes
Namespace: adsk.fusion
List of the various types of joints.
Defined in namespace "adsk::fusion" and the header file is <Fusion\FusionTypeDefs.h>

| Name | Value | Description |
|------|-------|-------------|
| BallJointType | 6 | Specifies a ball type of joint. |
| CylindricalJointType | 3 | Specifies a cylindrical type of joint. |
| InferredJointType | 7 | Specifies a joint that is inferred from the input geometry. |
| PinSlotJointType | 4 | Specifies a pin-slot type of joint. |
| PlanarJointType | 5 | Specifies a planar type of joint. |
| RevoluteJointType | 1 | Specifies a revolute type of joint. |
| RigidJointType | 0 | Specifies a rigid type of joint. |
| SliderJointType | 2 | Specifies a slider type of joint. |

## LineStylePatterns
Namespace: adsk.fusion
Specifies the line styles that can be applied to custom graphics lines and curves.
Defined in namespace "adsk::fusion" and the header file is <Fusion\FusionTypeDefs.h>

| Name | Value | Description |
|------|-------|-------------|
| centerLineStylePattern | 1 | A center line type of pattern which is a series of long and short lines. |
| continuousLineStylePattern | 0 | A solid line with no breaks. |
| dashedLineStylePattern | 2 | A center line type of pattern made of a series of short lines. |
| dotLineStylePattern | 3 | A center line type of pattern made of a series of dots. |
| hiddenLineStylePattern | 4 | A center line type of pattern made of a series of short lines. |
| phantomLineStylePattern | 5 | A center line type of pattern made of a series of a long line and two short lines. |
| tracksLineStylePattern | 6 | A center line type of pattern made of a single continuous line and many short perpendicular lines. |
| zigzagLineStylePattern | 7 | A center line type of pattern made of a series of 45 degree lines to create a zig-zag pattern. |

## LocalRenderStates
Namespace: adsk.fusion
The different states of a local rendering.
Defined in namespace "adsk::fusion" and the header file is <Fusion\FusionTypeDefs.h>

| Name | Value | Description |
|------|-------|-------------|
| FailedLocalRenderState | 3 | Indicates the rendering has failed and is no longer processing. |
| FinishedLocalRenderState | 2 | Indicates the rendering has finished. |
| ProcessingLocalRenderState | 1 | Indicates the rendering is processing. |
| QueuedLocalRenderState | 0 | Indicates the rendering is queued, waiting to start. |

## LoftEdgeAlignments
Namespace: adsk.fusion
List of Loft Edge Alignment Options
Defined in namespace "adsk::fusion" and the header file is <Fusion\FusionTypeDefs.h>

| Name | Value | Description |
|------|-------|-------------|
| AlignEdgesLoftEdgeAlignment | 1 | Specifies the edges of the loft are aligned with the edges of the face the loft starts or ends at. |
| AlignToSurfaceLoftEdgeAlignment | 2 | Specifies the edges of the loft are aligned with the face the loft starts or ends at. |
| FreeEdgesLoftEdgeAlignment | 0 | Specifies the loft edges are not influenced by edges or faces the loft starts or ends at. |

## LoftRailEdgeConditions
Namespace: adsk.fusion
Defines the different conditions that can be applied to a loft rail when the rail entity is defined by BRepEdge objects.
Defined in namespace "adsk::fusion" and the header file is <Fusion\FusionTypeDefs.h>

| Name | Value | Description |
|------|-------|-------------|
| G0LoftRailEdgeCondition | 0 | Defines a G0 or connected edge condition. |
| G1LoftRailEdgeCondition | 1 | Defines a G1 or tangent edge condition. |
| G2LoftRailEdgeCondition | 2 | Defines a G2 or curvature continuous edge condition. |

## MassUnits
Namespace: adsk.fusion
Valid unit types for mass.
Defined in namespace "adsk::fusion" and the header file is <Fusion\FusionTypeDefs.h>

| Name | Value | Description |
|------|-------|-------------|
| GramMassUnits | 0 | Grams |
| KilogramMassUnits | 1 | Kilograms |
| OunceMassUnits | 3 | Ounces |
| PoundMassUnits | 2 | Pounds |
| SlugMassUnits | 5 | Slugs |
| TonMassUnits | 4 | Tons |

## MeshCombineOperationTypes
Namespace: adsk.fusion
Specify the combine method for the mesh.
Defined in namespace "adsk::fusion" and the header file is <Fusion\FusionTypeDefs.h>

| Name | Value | Description |
|------|-------|-------------|
| CutMeshCombineType | 1 | Removes overlapping areas from target body. |
| IntersectMeshCombineType | 2 | Combines overlapping areas into a mesh body. |
| JoinMeshCombineType | 0 | Combines multiple mesh bodies into a single mesh body by enclosing their volumes. |
| MergeMeshCombineType | 3 | Combines multiple mesh bodies into a single mesh body without altering the faces of the original mesh. |

## MeshConvertAccuracyTypes
Namespace: adsk.fusion
Specify the resolution for the organic mesh conversion if ByAccuracyMeshConvertResolutionType is selected
Defined in namespace "adsk::fusion" and the header file is <Fusion\FusionTypeDefs.h>

| Name | Value | Description |
|------|-------|-------------|
| HighMeshConvertAccuracyType | 2 | Converts the body with high accuracy compared to the original mesh body. (Average) |
| LowMeshConvertAccuracyType | 0 | Converts the body with low accuracy compared to the original mesh body. (Fastest) |
| MediumMeshConvertAccuracyType | 1 | Converts the body with medium accuracy compared to the original mesh body. (Fast) |
| PreciseMeshConvertAccuracyType | 3 | Converts the body with the highest possible accuracy compared to the original mesh body. (Slowest) |

## MeshConvertMethodTypes
Namespace: adsk.fusion
Specify the convert method for the mesh.
Defined in namespace "adsk::fusion" and the header file is <Fusion\FusionTypeDefs.h>

| Name | Value | Description |
|------|-------|-------------|
| FacetedMeshConvertMethodType | 0 | Converts individual faces on the mesh body to individual faces on the new solid or surface body. |
| OrganicMeshConvertMethodType | 2 | This converts the mesh body to an organically shaped solid or surface body. Only accessible if the product design extension is active. |
| PrismaticMeshConvertMethodType | 1 | Merges groups of faces in prismatic features into singular faces on the new solid or surface body. Face groups are used to infer prismatic features. |

## MeshConvertOperationTypes
Namespace: adsk.fusion
Specify the operation method for the mesh conversion.
Defined in namespace "adsk::fusion" and the header file is <Fusion\FusionTypeDefs.h>

| Name | Value | Description |
|------|-------|-------------|
| BaseFeatureMeshConvertOperationType | 1 | A base feature is created after the operation. |
| ParametricFeatureMeshConvertOperationType | 0 | A parametric MeshConvert feature is created after the operation. |

## MeshConvertResolutionTypes
Namespace: adsk.fusion
Specify the resolution method for the organic mesh conversion.
Defined in namespace "adsk::fusion" and the header file is <Fusion\FusionTypeDefs.h>

| Name | Value | Description |
|------|-------|-------------|
| ByAccuracyMeshConvertResolutionType | 0 | Creates a solid or surface body that matches the shape of the original mesh body more or less accurately, based on the resolution you select. |
| ByFacetNumberMeshConvertResolutionType | 1 | Creates solid or surface body with a specific number of faces. |

## MeshGenerateFaceGroupsMethodTypes
Namespace: adsk.fusion
Specify the generate face group method for the mesh.
Defined in namespace "adsk::fusion" and the header file is <Fusion\FusionTypeDefs.h>

| Name | Value | Description |
|------|-------|-------------|
| AccurateGenerateFaceGroupsType | 1 | Generates face groups by matching mesh faces to simple geometric primitives. Prioritizes accuracy over speed. |
| FastGenerateFaceGroupsType | 0 | Generates face groups based on an angle threshold between faces. Prioritizes speed over accuracy. |

## MeshReduceMethodTypes
Namespace: adsk.fusion
Specify the reduce method for the mesh.
Defined in namespace "adsk::fusion" and the header file is <Fusion\FusionTypeDefs.h>

| Name | Value | Description |
|------|-------|-------------|
| AdaptiveReduceType | 0 | Creates smaller(larger) faces in areas of high (low) detail. |
| UniformReduceType | 1 | Creates faces of similar size in all areas. |

## MeshReduceTargetTypes
Namespace: adsk.fusion
Specify what the target criteria for the reduction should be.
Defined in namespace "adsk::fusion" and the header file is <Fusion\FusionTypeDefs.h>

| Name | Value | Description |
|------|-------|-------------|
| FaceCountMeshReduceTargetType | 2 | Reduces mesh to a given specific number of faces. |
| MaximumDeviationMeshReduceTargetType | 0 | Reduces mesh by merging faces within a maximum deviation from the original mesh shape. If this criteria type is used, the reduce method type is ignored and the adaptive method is always applied. |
| ProportionMeshReduceTargetType | 1 | Reduces mesh to a given proportion of the number of faces on the original mesh. |

## MeshRefinementSettings
Namespace: adsk.fusion
The different refinement settings supported when exporting the design as an STL or 3MF file.
Defined in namespace "adsk::fusion" and the header file is <Fusion\FusionTypeDefs.h>

| Name | Value | Description |
|------|-------|-------------|
| MeshRefinementCustom | 3 | Indicates that the settings are not predefined values associated with high, medium, or low quality export. |
| MeshRefinementHigh | 0 | Sets the various settings to the values associated with a high quality export. |
| MeshRefinementLow | 2 | Sets the various settings to the values associated with a low quality export. |
| MeshRefinementMedium | 1 | Sets the various settings to the values associated with a medium quality export. |

## MeshRemeshMethodTypes
Namespace: adsk.fusion
Specify the re-mesh method for the mesh.
Defined in namespace "adsk::fusion" and the header file is <Fusion\FusionTypeDefs.h>

| Name | Value | Description |
|------|-------|-------------|
| AdaptiveRemeshType | 0 | Creates smaller(larger) faces in areas of high (low) detail. |
| UniformRemeshType | 1 | Creates faces of similar size in all areas. |

## MeshRepairRebuildTypes
Namespace: adsk.fusion
Specify the method for the rebuild type of mesh repair. If AccurateMeshRepairRebuildType is chosen, an offset can be set.
Defined in namespace "adsk::fusion" and the header file is <Fusion\FusionTypeDefs.h>

| Name | Value | Description |
|------|-------|-------------|
| AccurateMeshRepairRebuildType | 2 | Rebuilds mesh body as accurately as possible. |
| AdaptiveMeshRepairRebuildType | 4 | The mesh will be rebuilt in an adaptive style. |
| AdaptivePreserveSharpEdgesMeshRepairRebuildType | 5 | The mesh will be rebuilt in an adaptive style, while preserving sharp edges. |
| BlockyMeshRepairRebuildType | 3 | The mesh will be rebuilt in a blocky style. |
| FastMeshRepairRebuildType | 0 | Rebuilds mesh body quickly, but not accurately. |
| PreserveSharpEdgesMeshRepairRebuildType | 1 | Rebuilds mesh body quickly, while preserving sharp edges. |

## MeshRepairTypes
Namespace: adsk.fusion
Specify the main repair type for the mesh. If RebuildMeshRepairType is chosen, other parameters can be set.
Defined in namespace "adsk::fusion" and the header file is <Fusion\FusionTypeDefs.h>

| Name | Value | Description |
|------|-------|-------------|
| CloseHolesMeshRepairType | 0 | Simplest and fastest type of repair, only close holes and fix flipped triangles are used to fix the part. |
| RebuildMeshRepairType | 3 | Reconstructs the mesh body using one of 4 MeshRepairRebuildTypes. All inner structures are destroyed. |
| StitchAndRemoveMeshRepairType | 1 | Makes the same changes as CloseHolesMeshRepairType, and also stitches triangles, removes double triangles, removes degenerated faces, and removes tiny shells. |
| WrapMeshRepairType | 2 | Uses in addition to the methods in StitchAndRemoveMeshRepairType also the wrapped method. This methods takes time and removes internal structure. |

## MeshSeparateTypes
Namespace: adsk.fusion
Specifies the output options for separating a mesh body. Only valid if the input is a mesh body.
Defined in namespace "adsk::fusion" and the header file is <Fusion\FusionTypeDefs.h>

| Name | Value | Description |
|------|-------|-------------|
| FaceGroupMeshSeparateType | 1 | Separates all face groups into independent mesh bodies. |
| ShellMeshSeparateType | 0 | Separates all mesh shells into independent mesh bodies. |

## MeshUnits
Namespace: adsk.fusion
The unit types that can be specified when importing a .stl or .obj file as a mesh.
Defined in namespace "adsk::fusion" and the header file is <Fusion\FusionTypeDefs.h>

| Name | Value | Description |
|------|-------|-------------|
| CentimeterMeshUnit | 0 | Interpret the coordinate data using centimeters. |
| FootMeshUnit | 4 | Interpret the coordinate data using feet. |
| InchMeshUnit | 3 | Interpret the coordinate data using inches. |
| MeterMeshUnit | 2 | Interpret the coordinate data using meters. |
| MillimeterMeshUnit | 1 | Interpret the coordinate data using millimeters. |

## OffsetCornerTypes
Namespace: adsk.fusion
Specifies the different types of corners that can be created when offsetting a wire body. These settings are used when the curves are offset outwards, which creates a gap at the corner. These represent the three ways the gap is filled.
Defined in namespace "adsk::fusion" and the header file is <Fusion\FusionTypeDefs.h>

| Name | Value | Description |
|------|-------|-------------|
| CircularOffsetCornerType | 0 | Creates an arc at the corner to fill the gap. This is similar to filleting the corner with a fillet that is the same radius as the offset. |
| ExtendedOffsetCornerType | 2 | Extends the offset curves so the connect at the corner. |
| LinearOffsetCornerType | 1 | Creates lines that are tangent to the offset curves and connect at the corner. |

## ParameterValueTypes
Namespace: adsk.fusion
Specifies the different types of values that a parameter can be.
Defined in namespace "adsk::fusion" and the header file is <Fusion\FusionTypeDefs.h>

| Name | Value | Description |
|------|-------|-------------|
| NumericParameterValueType | 0 | Indicates the parameter has a numeric value. |
| TextParameterValueType | 1 | Indicates the parameter has a string value. |

## PatternComputeOptions
Namespace: adsk.fusion
List of the compute options for mirroring and patterning features in the parametric modeling environment.
Defined in namespace "adsk::fusion" and the header file is <Fusion\FusionTypeDefs.h>

| Name | Value | Description |
|------|-------|-------------|
| AdjustPatternCompute | 2 | Adjust pattern compute. This is the slowest of all compute options. It can almost never produce a wrong result (e.g. works well even on Split features) |
| IdenticalPatternCompute | 1 | Identical pattern compute. Used when you want force the resulting mirror or pattern to create identical results regardless of the dependencies that define the feature being copied. |
| OptimizedPatternCompute | 0 | Optimized pattern compute. This is the fastest of all compute options. This option may fail or give wrong results in some very rare cases (e.g. when patterning a Split feature) |

## PatternDistanceType
Namespace: adsk.fusion
Defines the different ways to specify the spacing between elements in a pattern.
Defined in namespace "adsk::fusion" and the header file is <Fusion\FusionTypeDefs.h>

| Name | Value | Description |
|------|-------|-------------|
| ExtentPatternDistanceType | 0 | The total distance of the pattern is specified with the quantity evenly spaced within that distance. |
| SpacingPatternDistanceType | 1 | The distance between each pattern element is specified. |

## PatternEntityTypes
Namespace: adsk.fusion
Specifies the different types of entities that can be patterned.
Defined in namespace "adsk::fusion" and the header file is <Fusion\FusionTypeDefs.h>

| Name | Value | Description |
|------|-------|-------------|
| BodiesPatternType | 2 | Pattern of bodies |
| FacesPatternType | 0 | Pattern of faces |
| FeaturesPatternType | 1 | Pattern of features |
| OccurrencesPatternType | 3 | Pattern of occurrences |

## PipeSectionTypes
Namespace: adsk.fusion
List of the different section types of a Pipe.
Defined in namespace "adsk::fusion" and the header file is <Fusion\FusionTypeDefs.h>

| Name | Value | Description |
|------|-------|-------------|
| CircularPipeSectionType | 0 | Pipe section has a circular shape. |
| SquarePipeSectionType | 1 | Pipe section has a square shape. |
| TriangularPipeSectionType | 2 | Pipe section has a triangular shape. |

## PointContainment
Namespace: adsk.fusion
Types that define the nature of the relationship between a point and a containing entity.
Defined in namespace "adsk::fusion" and the header file is <Fusion\FusionTypeDefs.h>

| Name | Value | Description |
|------|-------|-------------|
| PointInsidePointContainment | 0 | The point lies inside. |
| PointOnPointContainment | 1 | The point lies on the boundary. |
| PointOutsidePointContainment | 2 | The point lies outside. |
| UnknownPointContainment | 3 | The containment relationship is unknown. |

## RenderAspectRatios
Namespace: adsk.fusion
Types that indicate the output aspect ratio when rendering a scene. This is used with in-canvas rendering, to allow you to define a different aspect ratio than the current active viewport.
Defined in namespace "adsk::fusion" and the header file is <Fusion\FusionTypeDefs.h>

| Name | Value | Description |
|------|-------|-------------|
| CurrentViewportRenderAspectRatio | 0 | Specifies that the Current Viewport aspect ratio is used. |
| CustomRenderAspectRatio | 6 | Specifies that a custom aspect ratio is used. |
| Landscape5to4RenderAspectRatio | 4 | Specifies a 5:4 landscape aspect ratio. |
| Portrait4to5RenderAspectRatio | 5 | Specifies a 4:5 portrait aspect ratio. |
| Presentation4to3RenderAspectRatio | 2 | Specifies a 4:3 presentation aspect ratio. |
| Square1to1RenderAspectRatio | 1 | Specifies a 1:1 square aspect ratio. |
| Widescreen16to9RenderAspectRatio | 3 | Specifies a 16:9 wide screen aspect ratio. |

## RenderResolutions
Namespace: adsk.fusion
The different standard resolutions supported when rendering.
Defined in namespace "adsk::fusion" and the header file is <Fusion\FusionTypeDefs.h>

| Name | Value | Description |
|------|-------|-------------|
| CustomRenderResolution | 17 | Custom resolution. |
| Mobile1136x640RenderResolution | 6 | 1136x640 resolution. Commonly used for images shown on a mobile device. |
| Mobile1334x750RenderResolution | 7 | 1334x750 resolution. Commonly used for images shown on a mobile device. |
| Mobile1920x1080RenderResolution | 8 | 1920x1080 resolution. Commonly used for images shown on a mobile device. |
| Mobile2048x1536RenderResolution | 9 | 2048x1536 resolution. Commonly used for images shown on a mobile device. |
| Mobile960x640RenderResolution | 5 | 960x640 resolution. Commonly used for images shown on a mobile device. |
| Print1800x1200RenderResolution | 10 | 1800x1200 resolution. Commonly used for images that will be printed. |
| Print2100x1500RenderResolution | 11 | 2100x1500 resolution. Commonly used for images that will be printed. |
| Print3000x2400RenderResolution | 12 | 3000x2400 resolution. Commonly used for images that will be printed. |
| Print3300x2550RenderResolution | 13 | 3300x2550 resolution. Commonly used for images that will be printed. |
| Video1280x720RenderResolution | 15 | 1280x720 resolution. Commonly used for images that will be used for video. |
| Video1920x1080RenderResolution | 16 | 1920x1080 resolution. Commonly used for images that will be used for video. |
| Video854x480RenderResolution | 14 | 854x480 resolution. Commonly used for images that will be used for video. |
| Web1024x768RenderResolution | 1 | 1024x768 resolution. Commonly used for images shown in a browser. |
| Web1152x864RenderResolution | 2 | 1152x864 resolution. Commonly used for images shown in a browser. |
| Web1280x1024RenderResolution | 3 | 1280x1024 resolution. Commonly used for images shown in a browser. |
| Web1600x1200RenderResolution | 4 | 1600x1200 resolution. Commonly used for images shown in a browser. |
| Web800x600RenderResolution | 0 | 800x600 resolution. Commonly used for low-res images shown in a browser. |

## RenderSceneBackgroundTypes
Namespace: adsk.fusion
Types that indicate the type of background being used to render the scene.
Defined in namespace "adsk::fusion" and the header file is <Fusion\FusionTypeDefs.h>

| Name | Value | Description |
|------|-------|-------------|
| EnvironmentRenderSceneBackgroundType | 0 | Specifies that an environment is being used as the background of the scene. |
| SolidColorRenderSceneBackgroundType | 1 | Specifies that a solid color is being used as the background of the scene. |

## RipFeatureDefinitionTypes
Namespace: adsk.fusion
Specifies the different ways a Rip feature can be defined.
Defined in namespace "adsk::fusion" and the header file is <Fusion\FusionTypeDefs.h>

| Name | Value | Description |
|------|-------|-------------|
| AlongEdgeRipFeatureDefinitionType | 2 | Rips along an edge. |
| BetweenPointsRipFeatureDefinitionType | 3 | Rips between two points on a face. The points may be defined either by vertices, or by an edge and an offset along that edge. |
| FaceRipFeatureDefinitionType | 1 | Rips an entire face. |
| UndefinedRipFeatureDefinitionType | 0 | The rip type is undefined. This occurs when a new RipFeatureInput is created and before a specific type has been defined. |

## RuleFilletRuleTypes
Namespace: adsk.fusion
List of the rule types of rule fillet.
Defined in namespace "adsk::fusion" and the header file is <Fusion\FusionTypeDefs.h>

| Name | Value | Description |
|------|-------|-------------|
| AllEdgesRuleFilletRuleType | 0 | The all edges rule type. |
| BetweenFacesOrFeaturesRuleFilletRuleType | 1 | The between faces or features rule type. |

## RuleFilletTopologyTypes
Namespace: adsk.fusion
List of the topology types of rule fillet.
Defined in namespace "adsk::fusion" and the header file is <Fusion\FusionTypeDefs.h>

| Name | Value | Description |
|------|-------|-------------|
| FilletsOnlyRuleFilletTopologyType | 2 | The fillets only topology type. |
| RoundsAndFilletsRuleFilletTopologyType | 0 | The rounds and fillets topology type. |
| RoundsOnlyRuleFilletTopologyType | 1 | The rounds only topology type. |

## RuledSurfaceCornerTypes
Namespace: adsk.fusion
List of Ruled Surface corner types.
Defined in namespace "adsk::fusion" and the header file is <Fusion\FusionTypeDefs.h>

| Name | Value | Description |
|------|-------|-------------|
| MiteredRuledSurfaceCornerType | 1 | The corners will be mitered. |
| RoundedRuledSurfaceCornerType | 0 | The corners will be rounded. |

## RuledSurfaceTypes
Namespace: adsk.fusion
List of Ruled Surface Types.
Defined in namespace "adsk::fusion" and the header file is <Fusion\FusionTypeDefs.h>

| Name | Value | Description |
|------|-------|-------------|
| DirectionRuledSurfaceType | 2 | Creates new faces perpendicular to the current faces. |
| NormalRuledSurfaceType | 1 | Creates new faces tangent to the current faces. |
| TangentRuledSurfaceType | 0 | Create Ruled Surface from edges or sketch curves |

## ShellTypes
Namespace: adsk.fusion
List of Shell Types
Defined in namespace "adsk::fusion" and the header file is <Fusion\FusionTypeDefs.h>

| Name | Value | Description |
|------|-------|-------------|
| RoundedOffsetShellType | 1 | Use rounded corners when creating the shell. |
| SharpOffsetShellType | 0 | Use sharp corners when creating the shell. (Legacy) |

## SilhouetteSplitOperations
Namespace: adsk.fusion
List of Silhouette Split feature operations.
Defined in namespace "adsk::fusion" and the header file is <Fusion\FusionTypeDefs.h>

| Name | Value | Description |
|------|-------|-------------|
| SilhouetteSplitFacesOnlyOperation | 0 | Split only the faces of a solid |
| SilhouetteSplitShelledBodyOperation | 1 | Split a shelled body |
| SilhouetteSplitSolidBodyOperation | 2 | Split a solid body |

## SketchCurveConstructionStates
Namespace: adsk.fusion
Used by the Sketch.setConstructionState method setting the construction state on sketch curves.
Defined in namespace "adsk::fusion" and the header file is <Fusion\FusionTypeDefs.h>

| Name | Value | Description |
|------|-------|-------------|
| ConstructionSketchCurveConstructionState | 1 | Specifies that the construction state should be set to construction. |
| NormalSketchCurveConstructionState | 2 | Specifies that the construction state should be set to normal. |
| ToggleSketchCurveConstructionState | 0 | Specifies that the construction state should be toggled from its current state. |

## SketchLineCenterlineStates
Namespace: adsk.fusion
Used by the Sketch.setCenterlineState method setting the centerline state on sketch lines.
Defined in namespace "adsk::fusion" and the header file is <Fusion\FusionTypeDefs.h>

| Name | Value | Description |
|------|-------|-------------|
| CenterlineSketchLineCenterlineState | 1 | Specifies that the centerline state should be set to centerline. |
| NormalSketchLineCenterlineState | 2 | Specifies that the centerline state should be set to normal. |
| ToggleSketchLineCenterlineState | 0 | Specifies that the centerline state should be toggled from its current state. |

## SplineDegrees
Namespace: adsk.fusion
Defines the options used when specifying the degree of a spline.
Defined in namespace "adsk::fusion" and the header file is <Fusion\FusionTypeDefs.h>

| Name | Value | Description |
|------|-------|-------------|
| SplineDegreeEight | 8 | Defines a degree 8 spline. |
| SplineDegreeFive | 5 | Defines a degree 5 spline. |
| SplineDegreeFour | 4 | Defines a degree 4 spline. |
| SplineDegreeNine | 9 | Defines a degree 9 spline. |
| SplineDegreeOne | 1 | Defines a degree 1 spline. |
| SplineDegreeSeven | 7 | Defines a degree 7 spline. |
| SplineDegreeSix | 6 | Defines a degree 6 spline. |
| SplineDegreeThree | 3 | Defines a degree 3 spline. |
| SplineDegreeTwo | 2 | Defines a degree 2 spline. |

## SplitFaceSplitTypes
Namespace: adsk.fusion
List of the ways to split a face using the split face feature.
Defined in namespace "adsk::fusion" and the header file is <Fusion\FusionTypeDefs.h>

| Name | Value | Description |
|------|-------|-------------|
| alongVectorSplitType | 1 | Split a face using a projection of the split tool along a specified direction. |
| closestPointSplitType | 2 | Split a face by projecting the split tool to the closest point on the faces being split. |
| surfaceIntersectionSplitType | 0 | Split face using a surface-to-surface intersection as the split curve. |

## SurfaceContinuityTypes
Namespace: adsk.fusion
List of Surface Continuity Types.
Defined in namespace "adsk::fusion" and the header file is <Fusion\FusionTypeDefs.h>

| Name | Value | Description |
|------|-------|-------------|
| ConnectedSurfaceContinuityType | 0 | Creates a surface with G0 edges (connected at an angle). |
| CurvatureSurfaceContinuityType | 2 | Creates a surface with G2 edges (blended with continuous curvature). |
| TangentSurfaceContinuityType | 1 | Creates a surface with G1 edges (tangential). |

## SurfaceExtendAlignment
Namespace: adsk.fusion
List of Surface Extend Alignments
Defined in namespace "adsk::fusion" and the header file is <Fusion\FusionTypeDefs.h>

| Name | Value | Description |
|------|-------|-------------|
| AlignEdges | 1 | The extended edges are aligned with the natural direction of the existing surface edges. |
| FreeEdges | 0 | The extended edges are not aligned with the existing surface edges. |

## SurfaceExtendTypes
Namespace: adsk.fusion
List of Surface Extend Types.
Defined in namespace "adsk::fusion" and the header file is <Fusion\FusionTypeDefs.h>

| Name | Value | Description |
|------|-------|-------------|
| NaturalSurfaceExtendType | 0 | Extends the current faces. |
| PerpendicularSurfaceExtendType | 2 | Creates new faces perpendicular to the current faces. |
| TangentSurfaceExtendType | 1 | Creates new faces tangent to the current faces. |

## SurfaceProjectTypes
Namespace: adsk.fusion
Used by the Sketch.projectToSurface method when defined how to project a curve onto a surface.
Defined in namespace "adsk::fusion" and the header file is <Fusion\FusionTypeDefs.h>

| Name | Value | Description |
|------|-------|-------------|
| AlongVectorSurfaceProjectType | 1 | Projects the curve along a defined vector. |
| ClosestPointSurfaceProjectType | 0 | Projects the curve using the closest point on the surface to the curve. |

## SweepExtentTypes
Namespace: adsk.fusion
List of the types of sweep extent.
Defined in namespace "adsk::fusion" and the header file is <Fusion\FusionTypeDefs.h>

| Name | Value | Description |
|------|-------|-------------|
| FullExtentsExtentType | 1 | Full extents extent type. |
| PerpendicularToPathExtentType | 0 | Perpendicular to Path extent type. |

## SweepOrientationTypes
Namespace: adsk.fusion
List of the types of sweep orientation.
Defined in namespace "adsk::fusion" and the header file is <Fusion\FusionTypeDefs.h>

| Name | Value | Description |
|------|-------|-------------|
| ParallelOrientationType | 0 | Parallel orientation type. |
| PerpendicularOrientationType | 1 | Perpendicular orientation type. |

## SweepProfileScalingOptions
Namespace: adsk.fusion
List of the sweep profile scaling options.
Defined in namespace "adsk::fusion" and the header file is <Fusion\FusionTypeDefs.h>

| Name | Value | Description |
|------|-------|-------------|
| SweepProfileNoScalingOption | 2 | Stretch profile option. |
| SweepProfileScaleOption | 0 | Scale profile option. |
| SweepProfileStretchOption | 1 | Stretch profile option. |

## SweepSolidOrientationTypes
Namespace: adsk.fusion
The various orientation types when doing a solid sweep.
Defined in namespace "adsk::fusion" and the header file is <Fusion\FusionTypeDefs.h>

| Name | Value | Description |
|------|-------|-------------|
| AlignedSolidOrientationType | 2 | Keep the orientation of the tool body aligned to a direction vector. The tool may rotate around this vector as it is swept along the path. |
| PerpendicularSolidOrientationType | 0 | Maintain the orientation of the tool body relative to the sweep path. As the tool body sweeps along the path, it will rotate to maintain the same relative angle to the path. |
| RigidSolidOrientationType | 1 | The orientation of the tool body does not change as it is swept along the path. The tool will be translated but not rotated. |

## TessellateRefinementTypes
Namespace: adsk.fusion
Specify the refinement setting type for the tessellation process.
Defined in namespace "adsk::fusion" and the header file is <Fusion\FusionTypeDefs.h>

| Name | Value | Description |
|------|-------|-------------|
| CustomTessellateRefinementType | 3 | Applies custom refinement settings to tessellate the body. |
| HighTessellateRefinementType | 0 | Applies a preset with high refinement settings to tessellate the body. |
| LowTessellateRefinementType | 2 | Applies a preset with low refinement settings to tessellate the body. |
| MediumTessellateRefinementType | 1 | Applies a preset with medium refinement settings to tessellate the body. |

## TextBoxKeyPoints
Namespace: adsk.fusion
Defines the nine key points that exist for a sketch text box and can be used as the origin when rotating the text. The named positions are with respect to the text box. For example when the text box has not been rotated the top-left key point will be the point in the upper-left corner of the text box. If the text box has been rotated 180 degrees, the top-left key point will be the point in the lower-right corner of the text box.
Defined in namespace "adsk::fusion" and the header file is <Fusion\FusionTypeDefs.h>

| Name | Value | Description |
|------|-------|-------------|
| BottomLeftTextBoxKeyPoint | 6 | The key point at the bottom-left corner of the text box. |
| BottomMiddleTextBoxKeyPoint | 7 | The key point at the midpoint of the bottom line of the text box. |
| BottomRightTextBoxKeyPoint | 8 | The key point at the bottom-right corner of the text box. |
| MiddleLeftTextBoxKeyPoint | 3 | The key point at the midpoint of the left line of the text box. |
| MiddleRightTextBoxKeyPoint | 5 | The key point at the midpoint of the right line of the text box. |
| MiddleTextBoxKeyPoint | 4 | The key point in the center of the text box. |
| TopLeftTextBoxKeyPoint | 0 | The key point in the upper-left corner of the text box. |
| TopMiddleTextBoxKeyPoint | 1 | The key point at the midpoint of the upper line of the text box. |
| TopRightTextBoxKeyPoint | 2 | The key point in the upper-right corner of the text box. |

## TextStyles
Namespace: adsk.fusion
Defines the various text style formatting options that can be applied to text. These are bitwise values to they can be combined.
Defined in namespace "adsk::fusion" and the header file is <Fusion\FusionTypeDefs.h>

| Name | Value | Description |
|------|-------|-------------|
| TextStyleBold | 1 | Specifies that the text has bold text style. |
| TextStyleItalic | 2 | Specifies that the text has italic text style. |
| TextStyleUnderline | 4 | Specifies that the text has underline text style. Not currently supported. |

## ThickenTypes
Namespace: adsk.fusion
List of Thicken Types
Defined in namespace "adsk::fusion" and the header file is <Fusion\FusionTypeDefs.h>

| Name | Value | Description |
|------|-------|-------------|
| RoundedThickenType | 1 | Use rounded corners when creating the thicken. |
| SharpThickenType | 0 | Use sharp corners when creating the thicken. |

## ThinExtrudeWallLocation
Namespace: adsk.fusion
List of Thin Extrude Wall Locations
Defined in namespace "adsk::fusion" and the header file is <Fusion\FusionTypeDefs.h>

| Name | Value | Description |
|------|-------|-------------|
| Center | 1 | The wall location type where the thin extrude is centered on the profile |
| Side1 | 0 | The wall location type where the thin extrude is offset towards one side of the profile |
| Side2 | 2 | The wall location type where the thin extrude is offset towards one side of the profile |

## ThreadLocations
Namespace: adsk.fusion
List of the positions of a thread feature when it is not full length.
Defined in namespace "adsk::fusion" and the header file is <Fusion\FusionTypeDefs.h>

| Name | Value | Description |
|------|-------|-------------|
| HighEndThreadLocation | 0 | Position thread at the high end of the cylinder. You can determine the high end in the model by using the geometry property of the cylindrical BRepFace object, which will return a Cylinder object. The axis property of the Cylinder is a vector and the high end of the cylinder is at the far end of the cylinder with respect to the axis vector. |
| LowEndThreadLocation | 1 | Position thread at the low end of the cylinder. You can determine the low end in the model by using the geometry property of the cylindrical BRepFace object, which will return a Cylinder object. The axis property of the Cylinder is a vector and the low end of the cylinder is at the near end of the cylinder with respect to the axis vector. |

## ThreeBendReliefShapes
Namespace: adsk.fusion
The bend relief shapes used when three bends intersect.
Defined in namespace "adsk::fusion" and the header file is <Fusion\FusionTypeDefs.h>

| Name | Value | Description |
|------|-------|-------------|
| FullRoundThreeBendReliefShape | 2 | Full round bend relief. |
| IntersectionThreeBendReliefShape | 1 | Intersection bend relief. |
| NoReplacementThreeBendReliefShape | 0 | No replacement for the bend relief. |
| RoundWithRadiusThreeBendReliefShape | 3 | Round radius bend relief. |

## TriangleMeshQualityOptions
Namespace: adsk.fusion
Types that indicate the level of quality of a triangle mesh.
Defined in namespace "adsk::fusion" and the header file is <Fusion\FusionTypeDefs.h>

| Name | Value | Description |
|------|-------|-------------|
| HighQualityTriangleMesh | 13 | High quality |
| LowQualityTriangleMesh | 8 | Low quality |
| NormalQualityTriangleMesh | 11 | Normal quality |
| VeryHighQualityTriangleMesh | 15 | Very high quality |

## TwoBendReliefPlacements
Namespace: adsk.fusion
The placement options for a two-bend relief.
Defined in namespace "adsk::fusion" and the header file is <Fusion\FusionTypeDefs.h>

| Name | Value | Description |
|------|-------|-------------|
| IntersectionTwoBendReliefPlacement | 1 | Specifies that the center point of the two-bend relief shape is located at the intersection of the bend center lines. This is the only valid placement option for square two-bend relief shapes. For round shapes, this and tangent placement is valid. |
| NoTwoBendReliefPlacement | 0 | Specifies that no two-bend relief placement is defined. This is returned for all two-bend relief shapes except for round and square shapes. |
| TangentTwoBendReliefPlacement | 2 | Specifies that the shape of the two-bend relief is tangential to the flange sides. This is only used for round to bend relief shapes where this or intersection placement is valid. |

## TwoBendReliefShapes
Namespace: adsk.fusion
The bend relief shapes used when two bends intersect.
Defined in namespace "adsk::fusion" and the header file is <Fusion\FusionTypeDefs.h>

| Name | Value | Description |
|------|-------|-------------|
| ArcWeldTwoBendReliefShape | 5 | Arc weld for the bend relief. |
| LaserWeldTwoBendReliefShape | 6 | Laser weld for the bend relief. |
| LinearWeldTwoBendReliefShape | 4 | Linear weld for the bend relief. |
| RoundTwoBendReliefShape | 0 | Round shape for the bend relief. |
| SquareTwoBendReliefShape | 1 | Square shape for the bend relief. |
| TearTwoBendReliefShape | 2 | Tear shape for the bend relief. |
| TrimToBendTwoBendReliefShape | 3 | Trim to the bends for the bend relief. |

## UnitSystems
Namespace: adsk.fusion
Predefined combinations of length and mass units used for units in the design.
Defined in namespace "adsk::fusion" and the header file is <Fusion\FusionTypeDefs.h>

| Name | Value | Description |
|------|-------|-------------|
| CentimeterGramUnitSystem | 2 | Specifies centimeters as the default distance units and grams as the default mass units of the design. |
| CustomUnitSystem | 0 | A custom unit system that supports any combination of distance and mass units as the default units of the design. |
| FootPoundUnitSystem | 5 | Specifies feet as the default distance units and pounds as the default mass units of the design. |
| InchOunceUnitSystem | 4 | Specifies inches as the default distance units and ounces as the default mass units of the design. |
| MeterKilogramUnitSystem | 3 | Specifies meters as the default distance units and kilograms as the default mass units of the design. |
| MillimeterGramUnitSystem | 1 | Specifies millimeters as the default distance units and grams as the default mass units of the design. |

## UntrimLoopTypes
Namespace: adsk.fusion
List of Untrim Loop Types.
Defined in namespace "adsk::fusion" and the header file is <Fusion\FusionTypeDefs.h>

| Name | Value | Description |
|------|-------|-------------|
| AllLoopsUntrimType | 0 | Untrim all loops of faces |
| ExternalLoopsUntrimType | 1 | Untrim external loops of faces |
| InternalLoopsUntrimType | 2 | Untrim internal loops of faces |
| ManualLoopsUntrimType | 3 | Untrim manually selected loops |

## ViewCorners
Namespace: adsk.fusion
Specifies which of the four view corners custom graphics will be drawn in relation to. The notUsedViewCorner setting indicates the graphics are not positioned with respect to the view.
Defined in namespace "adsk::fusion" and the header file is <Fusion\FusionTypeDefs.h>

| Name | Value | Description |
|------|-------|-------------|
| lowerLeftViewCorner | 2 | Indicates that custom graphics are positioned with respect to the lower-left corner of the view. |
| lowerRightViewCorner | 3 | Indicates that custom graphics are positioned with respect to the lower-right corner of the view. |
| upperLeftViewCorner | 0 | Indicates that custom graphics are positioned with respect to the upper-left corner of the view. |
| upperRightViewCorner | 1 | Indicates that custom graphics are positioned with respect to the upper-right corner of the view. |

## VolumetricMeshRefinementTypes
Namespace: adsk.fusion
List of Volumetric Model to Mesh Refinement Types.
Defined in namespace "adsk::fusion" and the header file is <Fusion\FusionTypeDefs.h>

| Name | Value | Description |
|------|-------|-------------|
| VolumetricMeshRefinementCustomType | 3 | Creates a custom resolution mesh from the volumetric model. |
| VolumetricMeshRefinementHighType | 0 | Creates a high resolution mesh from the volumetric model. |
| VolumetricMeshRefinementLowType | 2 | Creates a low resolution mesh from the volumetric model. |
| VolumetricMeshRefinementMediumType | 1 | Creates a medium resolution mesh from the volumetric model. |

## VolumetricMeshingApproachTypes
Namespace: adsk.fusion
List of Meshing Approaches for converting a volumetric model to a mesh.
Defined in namespace "adsk::fusion" and the header file is <Fusion\FusionTypeDefs.h>

| Name | Value | Description |
|------|-------|-------------|
| VolumetricMeshingAdvancedType | 0 | Mesh the volumetric model using advanced techniques that preserve sharp features on the boundary of the model. |
| VolumetricMeshingOriginalType | 1 | Mesh the volumetric model using the original meshing techniques. |

# adsk.volume

## ControlPointInterpolators
Namespace: adsk.volume
Types of interpolation functions for the control point maps.
Defined in namespace "adsk::volume" and the header file is <Volume\VolumeTypeDefs.h>

| Name | Value | Description |
|------|-------|-------------|
| CubicInterpolator | 2 | Point are interpolated using a cubic function. |
| LinearInterpolator | 0 | The point values are interpolated linearly. |
| NearestInterpolator | 1 | The value is set to the value of whichever point is nearest. |
| SmoothInterpolator | 3 | Points are interpolated with smooth tangent transitions. |

## GraphOutputNodeTypes
Namespace: adsk.volume
Types of graph output nodes for the main graph.
Defined in namespace "adsk::volume" and the header file is <Volume\VolumeTypeDefs.h>

| Name | Value | Description |
|------|-------|-------------|
| BoundarySDFOutputNodeType | 0 | Scalar. Distance field of the boundary object of the model. Only used in the primary graph. |
| CellLatticeShapeOutputNodeType | 6 | Scalar. Defines the shape of the volumetric lattice cell. Only used in the cell graph. |
| CellTextureShapeOutputNodeType | 7 | Scalar. Defines the shape of the volumetric texture cell. Only used in the cell graph. |
| ColorOutputNodeType | 2 | RGBA. The color of the model at all points within it. Only used in the primary graph. |
| LatticeCoordinatesOutputNodeType | 3 | Vector3. The coordinate system for the lattice cells. Mapping from the global xyz coordinates to lattice cell coordinates. Only used in the primary graph. |
| LatticeDensityOutputNodeType | 1 | Scalar. Density/solidity of the volumetric model lattice at all points within it. Only used in the primary graph. |
| TextureCoordinatesOutputNodeType | 5 | Vector3. The coordinate system for the volumetric texture cells. Mapping from the global xyz coordinates to texture cell coordinates. Only used in the primary graph. |
| TextureDensityOutputNodeType | 4 | Scalar. Strength of the volumetric model texture at all points within it. Only used in the primary graph. |

## GraphTypes
Namespace: adsk.volume
Graph types for a volumetric model.
Defined in namespace "adsk::volume" and the header file is <Volume\VolumeTypeDefs.h>

| Name | Value | Description |
|------|-------|-------------|
| CellGraphType | 1 | The graph for the cell that is repeated across the volume. |
| PrimaryGraphType | 0 | The main graph containing the boundary, density, colour and UVW mapping subgraphs. |

## NodePinTypes
Namespace: adsk.volume
Different types that graph nodes input and output types can be.
Defined in namespace "adsk::volume" and the header file is <Volume\VolumeTypeDefs.h>

| Name | Value | Description |
|------|-------|-------------|
| ColorNodePinType | 3 |  |
| NoNodePinType | 0 |  |
| ScalarNodePinType | 1 |  |
| VectorNodePinType | 2 |  |

#### import the simple module from the paraview
from paraview.simple import *
#### disable automatic camera reset on 'Show'
paraview.simple._DisableFirstRenderCameraReset()

# create a new 'OpenFOAMReader'
vizfoam = OpenFOAMReader(FileName='/mnt/bighome/nluminar/macromodel/zampogna_cavity_1000/viz.foam')
vizfoam.MeshRegions = ['internalMesh']
vizfoam.CellArrays = ['K', 'U', 'angle1', 'angle2', 'gradient_p', 'p', 'reynolds']

# get animation scene
animationScene1 = GetAnimationScene()

# update animation scene based on data timesteps
animationScene1.UpdateAnimationUsingDataTimeSteps()

# get active view
renderView1 = GetActiveViewOrCreate('RenderView')
# uncomment following to set a specific view size
# renderView1.ViewSize = [1054, 904]

# get color transfer function/color map for 'p'
pLUT = GetColorTransferFunction('p')

# get opacity transfer function/opacity map for 'p'
pPWF = GetOpacityTransferFunction('p')

# show data in view
vizfoamDisplay = Show(vizfoam, renderView1)
# trace defaults for the display properties.
vizfoamDisplay.Representation = 'Surface'
vizfoamDisplay.ColorArrayName = ['POINTS', 'p']
vizfoamDisplay.LookupTable = pLUT
vizfoamDisplay.OSPRayScaleArray = 'p'
vizfoamDisplay.OSPRayScaleFunction = 'PiecewiseFunction'
vizfoamDisplay.SelectOrientationVectors = 'U'
vizfoamDisplay.ScaleFactor = 0.1
vizfoamDisplay.SelectScaleArray = 'p'
vizfoamDisplay.GlyphType = 'Arrow'
vizfoamDisplay.GlyphTableIndexArray = 'p'
vizfoamDisplay.DataAxesGrid = 'GridAxesRepresentation'
vizfoamDisplay.PolarAxes = 'PolarAxesRepresentation'
vizfoamDisplay.ScalarOpacityFunction = pPWF
vizfoamDisplay.ScalarOpacityUnitDistance = 0.05508826811560769
vizfoamDisplay.GaussianRadius = 0.05
vizfoamDisplay.SetScaleArray = ['POINTS', 'p']
vizfoamDisplay.ScaleTransferFunction = 'PiecewiseFunction'
vizfoamDisplay.OpacityArray = ['POINTS', 'p']
vizfoamDisplay.OpacityTransferFunction = 'PiecewiseFunction'

# init the 'PiecewiseFunction' selected for 'OSPRayScaleFunction'
vizfoamDisplay.OSPRayScaleFunction.Points = [0.002180787269026041, 0.0, 0.5, 0.0, 0.01113197486847639, 1.0, 0.5, 0.0]

# init the 'GridAxesRepresentation' selected for 'DataAxesGrid'
vizfoamDisplay.DataAxesGrid.XTitleColor = [0.0, 0.0, 0.0]
vizfoamDisplay.DataAxesGrid.YTitleColor = [0.0, 0.0, 0.0]
vizfoamDisplay.DataAxesGrid.ZTitleColor = [0.0, 0.0, 0.0]
vizfoamDisplay.DataAxesGrid.XLabelColor = [0.0, 0.0, 0.0]
vizfoamDisplay.DataAxesGrid.YLabelColor = [0.0, 0.0, 0.0]
vizfoamDisplay.DataAxesGrid.ZLabelColor = [0.0, 0.0, 0.0]

# init the 'PolarAxesRepresentation' selected for 'PolarAxes'
vizfoamDisplay.PolarAxes.PolarAxisTitleColor = [0.0, 0.0, 0.0]
vizfoamDisplay.PolarAxes.PolarAxisLabelColor = [0.0, 0.0, 0.0]
vizfoamDisplay.PolarAxes.LastRadialAxisTextColor = [0.0, 0.0, 0.0]
vizfoamDisplay.PolarAxes.SecondaryRadialAxesTextColor = [0.0, 0.0, 0.0]

# init the 'PiecewiseFunction' selected for 'ScaleTransferFunction'
vizfoamDisplay.ScaleTransferFunction.Points = [0.002180787269026041, 0.0, 0.5, 0.0, 0.01113197486847639, 1.0, 0.5, 0.0]

# init the 'PiecewiseFunction' selected for 'OpacityTransferFunction'
vizfoamDisplay.OpacityTransferFunction.Points = [0.002180787269026041, 0.0, 0.5, 0.0, 0.01113197486847639, 1.0, 0.5, 0.0]

# reset view to fit data
renderView1.ResetCamera()

# show color bar/color legend
vizfoamDisplay.SetScalarBarVisibility(renderView1, True)

# update the view to ensure updated data information
renderView1.Update()

# create a new 'Threshold'
threshold1 = Threshold(Input=vizfoam)
threshold1.Scalars = ['POINTS', 'p']
threshold1.ThresholdRange = [-1.4334799516291241e-06, 2.2285400973487413e-06]

# set active source
SetActiveSource(vizfoam)

# destroy threshold1
Delete(threshold1)
del threshold1

# create a new 'Clip'
clip1 = Clip(Input=vizfoam)
clip1.ClipType = 'Plane'
clip1.Scalars = ['POINTS', 'p']
clip1.Value = 3.9753007285980857e-07

# init the 'Plane' selected for 'ClipType'
clip1.ClipType.Origin = [0.5, 0.03999999910593033, 0.5]

# toggle 3D widget visibility (only when running from the GUI)
Hide3DWidgets(proxy=clip1.ClipType)

# reset view to fit data
renderView1.ResetCamera()

# Properties modified on clip1.ClipType
clip1.ClipType.Origin = [0.5, 0.03999999910593033, 0.28]
clip1.ClipType.Normal = [0.0, 0.0, -1.0]

# Properties modified on clip1.ClipType
clip1.ClipType.Origin = [0.5, 0.03999999910593033, 0.28]
clip1.ClipType.Normal = [0.0, 0.0, -1.0]

# show data in view
clip1Display = Show(clip1, renderView1)
# trace defaults for the display properties.
clip1Display.Representation = 'Surface'
clip1Display.ColorArrayName = ['POINTS', 'p']
clip1Display.LookupTable = pLUT
clip1Display.OSPRayScaleArray = 'p'
clip1Display.OSPRayScaleFunction = 'PiecewiseFunction'
clip1Display.SelectOrientationVectors = 'U'
clip1Display.ScaleFactor = 0.1
clip1Display.SelectScaleArray = 'p'
clip1Display.GlyphType = 'Arrow'
clip1Display.GlyphTableIndexArray = 'p'
clip1Display.DataAxesGrid = 'GridAxesRepresentation'
clip1Display.PolarAxes = 'PolarAxesRepresentation'
clip1Display.ScalarOpacityFunction = pPWF
clip1Display.ScalarOpacityUnitDistance = 0.07389620939066364
clip1Display.GaussianRadius = 0.05
clip1Display.SetScaleArray = ['POINTS', 'p']
clip1Display.ScaleTransferFunction = 'PiecewiseFunction'
clip1Display.OpacityArray = ['POINTS', 'p']
clip1Display.OpacityTransferFunction = 'PiecewiseFunction'

# init the 'PiecewiseFunction' selected for 'OSPRayScaleFunction'
clip1Display.OSPRayScaleFunction.Points = [0.002180787269026041, 0.0, 0.5, 0.0, 0.01113197486847639, 1.0, 0.5, 0.0]

# init the 'GridAxesRepresentation' selected for 'DataAxesGrid'
clip1Display.DataAxesGrid.XTitleColor = [0.0, 0.0, 0.0]
clip1Display.DataAxesGrid.YTitleColor = [0.0, 0.0, 0.0]
clip1Display.DataAxesGrid.ZTitleColor = [0.0, 0.0, 0.0]
clip1Display.DataAxesGrid.XLabelColor = [0.0, 0.0, 0.0]
clip1Display.DataAxesGrid.YLabelColor = [0.0, 0.0, 0.0]
clip1Display.DataAxesGrid.ZLabelColor = [0.0, 0.0, 0.0]

# init the 'PolarAxesRepresentation' selected for 'PolarAxes'
clip1Display.PolarAxes.PolarAxisTitleColor = [0.0, 0.0, 0.0]
clip1Display.PolarAxes.PolarAxisLabelColor = [0.0, 0.0, 0.0]
clip1Display.PolarAxes.LastRadialAxisTextColor = [0.0, 0.0, 0.0]
clip1Display.PolarAxes.SecondaryRadialAxesTextColor = [0.0, 0.0, 0.0]

# init the 'PiecewiseFunction' selected for 'ScaleTransferFunction'
clip1Display.ScaleTransferFunction.Points = [0.002180787269026041, 0.0, 0.5, 0.0, 0.01113197486847639, 1.0, 0.5, 0.0]

# init the 'PiecewiseFunction' selected for 'OpacityTransferFunction'
clip1Display.OpacityTransferFunction.Points = [0.002180787269026041, 0.0, 0.5, 0.0, 0.01113197486847639, 1.0, 0.5, 0.0]

# hide data in view
Hide(vizfoam, renderView1)

# show color bar/color legend
clip1Display.SetScalarBarVisibility(renderView1, True)

# update the view to ensure updated data information
renderView1.Update()

# create a new 'Clip'
clip2 = Clip(Input=clip1)
clip2.ClipType = 'Plane'
clip2.Scalars = ['POINTS', 'p']
clip2.Value = 2.9423879444046008e-08

# init the 'Plane' selected for 'ClipType'
clip2.ClipType.Origin = [0.5, 0.03999999910593033, 0.14000000059604645]

# Properties modified on clip2.ClipType
clip2.ClipType.Origin = [0.5, 0.03999999910593033, 0.04]
clip2.ClipType.Normal = [0.0, 0.0, 1.0]

# Properties modified on clip2.ClipType
clip2.ClipType.Origin = [0.5, 0.03999999910593033, 0.04]
clip2.ClipType.Normal = [0.0, 0.0, 1.0]

# show data in view
clip2Display = Show(clip2, renderView1)
# trace defaults for the display properties.
clip2Display.Representation = 'Surface'
clip2Display.ColorArrayName = ['POINTS', 'p']
clip2Display.LookupTable = pLUT
clip2Display.OSPRayScaleArray = 'p'
clip2Display.OSPRayScaleFunction = 'PiecewiseFunction'
clip2Display.SelectOrientationVectors = 'U'
clip2Display.ScaleFactor = 0.1
clip2Display.SelectScaleArray = 'p'
clip2Display.GlyphType = 'Arrow'
clip2Display.GlyphTableIndexArray = 'p'
clip2Display.DataAxesGrid = 'GridAxesRepresentation'
clip2Display.PolarAxes = 'PolarAxesRepresentation'
clip2Display.ScalarOpacityFunction = pPWF
clip2Display.ScalarOpacityUnitDistance = 0.07704309721222295
clip2Display.GaussianRadius = 0.05
clip2Display.SetScaleArray = ['POINTS', 'p']
clip2Display.ScaleTransferFunction = 'PiecewiseFunction'
clip2Display.OpacityArray = ['POINTS', 'p']
clip2Display.OpacityTransferFunction = 'PiecewiseFunction'

# init the 'PiecewiseFunction' selected for 'OSPRayScaleFunction'
clip2Display.OSPRayScaleFunction.Points = [0.002180787269026041, 0.0, 0.5, 0.0, 0.01113197486847639, 1.0, 0.5, 0.0]

# init the 'GridAxesRepresentation' selected for 'DataAxesGrid'
clip2Display.DataAxesGrid.XTitleColor = [0.0, 0.0, 0.0]
clip2Display.DataAxesGrid.YTitleColor = [0.0, 0.0, 0.0]
clip2Display.DataAxesGrid.ZTitleColor = [0.0, 0.0, 0.0]
clip2Display.DataAxesGrid.XLabelColor = [0.0, 0.0, 0.0]
clip2Display.DataAxesGrid.YLabelColor = [0.0, 0.0, 0.0]
clip2Display.DataAxesGrid.ZLabelColor = [0.0, 0.0, 0.0]

# init the 'PolarAxesRepresentation' selected for 'PolarAxes'
clip2Display.PolarAxes.PolarAxisTitleColor = [0.0, 0.0, 0.0]
clip2Display.PolarAxes.PolarAxisLabelColor = [0.0, 0.0, 0.0]
clip2Display.PolarAxes.LastRadialAxisTextColor = [0.0, 0.0, 0.0]
clip2Display.PolarAxes.SecondaryRadialAxesTextColor = [0.0, 0.0, 0.0]

# init the 'PiecewiseFunction' selected for 'ScaleTransferFunction'
clip2Display.ScaleTransferFunction.Points = [0.002180787269026041, 0.0, 0.5, 0.0, 0.01113197486847639, 1.0, 0.5, 0.0]

# init the 'PiecewiseFunction' selected for 'OpacityTransferFunction'
clip2Display.OpacityTransferFunction.Points = [0.002180787269026041, 0.0, 0.5, 0.0, 0.01113197486847639, 1.0, 0.5, 0.0]

# hide data in view
Hide(clip1, renderView1)

# show color bar/color legend
clip2Display.SetScalarBarVisibility(renderView1, True)

# update the view to ensure updated data information
renderView1.Update()

# toggle 3D widget visibility (only when running from the GUI)
Hide3DWidgets(proxy=clip2.ClipType)

# create a new 'Clip'
clip3 = Clip(Input=clip2)
clip3.ClipType = 'Plane'
clip3.Scalars = ['POINTS', 'p']
clip3.Value = 2.9423879444046008e-08

# init the 'Plane' selected for 'ClipType'
clip3.ClipType.Origin = [0.5, 0.03999999910593033, 0.1600000001490116]

# toggle 3D widget visibility (only when running from the GUI)
Hide3DWidgets(proxy=clip3.ClipType)

# show data in view
clip3Display = Show(clip3, renderView1)
# trace defaults for the display properties.
clip3Display.Representation = 'Surface'
clip3Display.ColorArrayName = ['POINTS', 'p']
clip3Display.LookupTable = pLUT
clip3Display.OSPRayScaleArray = 'p'
clip3Display.OSPRayScaleFunction = 'PiecewiseFunction'
clip3Display.SelectOrientationVectors = 'U'
clip3Display.ScaleFactor = 0.05
clip3Display.SelectScaleArray = 'p'
clip3Display.GlyphType = 'Arrow'
clip3Display.GlyphTableIndexArray = 'p'
clip3Display.DataAxesGrid = 'GridAxesRepresentation'
clip3Display.PolarAxes = 'PolarAxesRepresentation'
clip3Display.ScalarOpacityFunction = pPWF
clip3Display.ScalarOpacityUnitDistance = 0.05204671170008069
clip3Display.GaussianRadius = 0.025
clip3Display.SetScaleArray = ['POINTS', 'p']
clip3Display.ScaleTransferFunction = 'PiecewiseFunction'
clip3Display.OpacityArray = ['POINTS', 'p']
clip3Display.OpacityTransferFunction = 'PiecewiseFunction'

# init the 'PiecewiseFunction' selected for 'OSPRayScaleFunction'
clip3Display.OSPRayScaleFunction.Points = [0.002180787269026041, 0.0, 0.5, 0.0, 0.01113197486847639, 1.0, 0.5, 0.0]

# init the 'GridAxesRepresentation' selected for 'DataAxesGrid'
clip3Display.DataAxesGrid.XTitleColor = [0.0, 0.0, 0.0]
clip3Display.DataAxesGrid.YTitleColor = [0.0, 0.0, 0.0]
clip3Display.DataAxesGrid.ZTitleColor = [0.0, 0.0, 0.0]
clip3Display.DataAxesGrid.XLabelColor = [0.0, 0.0, 0.0]
clip3Display.DataAxesGrid.YLabelColor = [0.0, 0.0, 0.0]
clip3Display.DataAxesGrid.ZLabelColor = [0.0, 0.0, 0.0]

# init the 'PolarAxesRepresentation' selected for 'PolarAxes'
clip3Display.PolarAxes.PolarAxisTitleColor = [0.0, 0.0, 0.0]
clip3Display.PolarAxes.PolarAxisLabelColor = [0.0, 0.0, 0.0]
clip3Display.PolarAxes.LastRadialAxisTextColor = [0.0, 0.0, 0.0]
clip3Display.PolarAxes.SecondaryRadialAxesTextColor = [0.0, 0.0, 0.0]

# init the 'PiecewiseFunction' selected for 'ScaleTransferFunction'
clip3Display.ScaleTransferFunction.Points = [0.002180787269026041, 0.0, 0.5, 0.0, 0.01113197486847639, 1.0, 0.5, 0.0]

# init the 'PiecewiseFunction' selected for 'OpacityTransferFunction'
clip3Display.OpacityTransferFunction.Points = [0.002180787269026041, 0.0, 0.5, 0.0, 0.01113197486847639, 1.0, 0.5, 0.0]

# hide data in view
Hide(clip2, renderView1)

# show color bar/color legend
clip3Display.SetScalarBarVisibility(renderView1, True)

# update the view to ensure updated data information
renderView1.Update()

# Properties modified on clip3.ClipType
clip3.ClipType.Origin = [0.04, 0.03999999910593033, 0.1600000001490116]

# Properties modified on clip3.ClipType
clip3.ClipType.Origin = [0.04, 0.03999999910593033, 0.1600000001490116]

# update the view to ensure updated data information
renderView1.Update()

# create a new 'Clip'
clip4 = Clip(Input=clip3)
clip4.ClipType = 'Plane'
clip4.Scalars = ['POINTS', 'p']
clip4.Value = 2.9423879444046008e-08

# init the 'Plane' selected for 'ClipType'
clip4.ClipType.Origin = [0.5199999995529652, 0.03999999910593033, 0.1600000001490116]

# toggle 3D widget visibility (only when running from the GUI)
Hide3DWidgets(proxy=clip4.ClipType)

# Properties modified on clip4.ClipType
clip4.ClipType.Origin = [0.96, 0.03999999910593033, 0.1600000001490116]
clip4.ClipType.Normal = [-1.0, 0.0, 0.0]

# Properties modified on clip4.ClipType
clip4.ClipType.Origin = [0.96, 0.03999999910593033, 0.1600000001490116]
clip4.ClipType.Normal = [-1.0, 0.0, 0.0]

# show data in view
clip4Display = Show(clip4, renderView1)
# trace defaults for the display properties.
clip4Display.Representation = 'Surface'
clip4Display.ColorArrayName = ['POINTS', 'p']
clip4Display.LookupTable = pLUT
clip4Display.OSPRayScaleArray = 'p'
clip4Display.OSPRayScaleFunction = 'PiecewiseFunction'
clip4Display.SelectOrientationVectors = 'U'
clip4Display.ScaleFactor = 0.09199999794363976
clip4Display.SelectScaleArray = 'p'
clip4Display.GlyphType = 'Arrow'
clip4Display.GlyphTableIndexArray = 'p'
clip4Display.DataAxesGrid = 'GridAxesRepresentation'
clip4Display.PolarAxes = 'PolarAxesRepresentation'
clip4Display.ScalarOpacityFunction = pPWF
clip4Display.ScalarOpacityUnitDistance = 0.07275057282595088
clip4Display.GaussianRadius = 0.04599999897181988
clip4Display.SetScaleArray = ['POINTS', 'p']
clip4Display.ScaleTransferFunction = 'PiecewiseFunction'
clip4Display.OpacityArray = ['POINTS', 'p']
clip4Display.OpacityTransferFunction = 'PiecewiseFunction'

# init the 'PiecewiseFunction' selected for 'OSPRayScaleFunction'
clip4Display.OSPRayScaleFunction.Points = [0.002180787269026041, 0.0, 0.5, 0.0, 0.01113197486847639, 1.0, 0.5, 0.0]

# init the 'GridAxesRepresentation' selected for 'DataAxesGrid'
clip4Display.DataAxesGrid.XTitleColor = [0.0, 0.0, 0.0]
clip4Display.DataAxesGrid.YTitleColor = [0.0, 0.0, 0.0]
clip4Display.DataAxesGrid.ZTitleColor = [0.0, 0.0, 0.0]
clip4Display.DataAxesGrid.XLabelColor = [0.0, 0.0, 0.0]
clip4Display.DataAxesGrid.YLabelColor = [0.0, 0.0, 0.0]
clip4Display.DataAxesGrid.ZLabelColor = [0.0, 0.0, 0.0]

# init the 'PolarAxesRepresentation' selected for 'PolarAxes'
clip4Display.PolarAxes.PolarAxisTitleColor = [0.0, 0.0, 0.0]
clip4Display.PolarAxes.PolarAxisLabelColor = [0.0, 0.0, 0.0]
clip4Display.PolarAxes.LastRadialAxisTextColor = [0.0, 0.0, 0.0]
clip4Display.PolarAxes.SecondaryRadialAxesTextColor = [0.0, 0.0, 0.0]

# init the 'PiecewiseFunction' selected for 'ScaleTransferFunction'
clip4Display.ScaleTransferFunction.Points = [0.002180787269026041, 0.0, 0.5, 0.0, 0.01113197486847639, 1.0, 0.5, 0.0]

# init the 'PiecewiseFunction' selected for 'OpacityTransferFunction'
clip4Display.OpacityTransferFunction.Points = [0.002180787269026041, 0.0, 0.5, 0.0, 0.01113197486847639, 1.0, 0.5, 0.0]

# hide data in view
Hide(clip3, renderView1)

# show color bar/color legend
clip4Display.SetScalarBarVisibility(renderView1, True)

# update the view to ensure updated data information
renderView1.Update()

# create a new 'Calculator'
calculator1 = Calculator(Input=clip4)
calculator1.Function = ''

# Properties modified on calculator1
calculator1.ResultArrayName = 'U*'
calculator1.Function = 'U*100'

# show data in view
calculator1Display = Show(calculator1, renderView1)
# trace defaults for the display properties.
calculator1Display.Representation = 'Surface'
calculator1Display.ColorArrayName = ['POINTS', 'p']
calculator1Display.LookupTable = pLUT
calculator1Display.OSPRayScaleArray = 'p'
calculator1Display.OSPRayScaleFunction = 'PiecewiseFunction'
calculator1Display.SelectOrientationVectors = 'U*'
calculator1Display.ScaleFactor = 0.09199999794363976
calculator1Display.SelectScaleArray = 'p'
calculator1Display.GlyphType = 'Arrow'
calculator1Display.GlyphTableIndexArray = 'p'
calculator1Display.DataAxesGrid = 'GridAxesRepresentation'
calculator1Display.PolarAxes = 'PolarAxesRepresentation'
calculator1Display.ScalarOpacityFunction = pPWF
calculator1Display.ScalarOpacityUnitDistance = 0.07275057282595088
calculator1Display.GaussianRadius = 0.04599999897181988
calculator1Display.SetScaleArray = ['POINTS', 'p']
calculator1Display.ScaleTransferFunction = 'PiecewiseFunction'
calculator1Display.OpacityArray = ['POINTS', 'p']
calculator1Display.OpacityTransferFunction = 'PiecewiseFunction'

# init the 'PiecewiseFunction' selected for 'OSPRayScaleFunction'
calculator1Display.OSPRayScaleFunction.Points = [0.002180787269026041, 0.0, 0.5, 0.0, 0.01113197486847639, 1.0, 0.5, 0.0]

# init the 'GridAxesRepresentation' selected for 'DataAxesGrid'
calculator1Display.DataAxesGrid.XTitleColor = [0.0, 0.0, 0.0]
calculator1Display.DataAxesGrid.YTitleColor = [0.0, 0.0, 0.0]
calculator1Display.DataAxesGrid.ZTitleColor = [0.0, 0.0, 0.0]
calculator1Display.DataAxesGrid.XLabelColor = [0.0, 0.0, 0.0]
calculator1Display.DataAxesGrid.YLabelColor = [0.0, 0.0, 0.0]
calculator1Display.DataAxesGrid.ZLabelColor = [0.0, 0.0, 0.0]

# init the 'PolarAxesRepresentation' selected for 'PolarAxes'
calculator1Display.PolarAxes.PolarAxisTitleColor = [0.0, 0.0, 0.0]
calculator1Display.PolarAxes.PolarAxisLabelColor = [0.0, 0.0, 0.0]
calculator1Display.PolarAxes.LastRadialAxisTextColor = [0.0, 0.0, 0.0]
calculator1Display.PolarAxes.SecondaryRadialAxesTextColor = [0.0, 0.0, 0.0]

# init the 'PiecewiseFunction' selected for 'ScaleTransferFunction'
calculator1Display.ScaleTransferFunction.Points = [0.002180787269026041, 0.0, 0.5, 0.0, 0.01113197486847639, 1.0, 0.5, 0.0]

# init the 'PiecewiseFunction' selected for 'OpacityTransferFunction'
calculator1Display.OpacityTransferFunction.Points = [0.002180787269026041, 0.0, 0.5, 0.0, 0.01113197486847639, 1.0, 0.5, 0.0]

# hide data in view
Hide(clip4, renderView1)

# show color bar/color legend
calculator1Display.SetScalarBarVisibility(renderView1, True)

# update the view to ensure updated data information
renderView1.Update()

# create a new 'Calculator'
calculator2 = Calculator(Input=calculator1)
calculator2.Function = ''

# Properties modified on calculator2
calculator2.ResultArrayName = 'grad_p*'
calculator2.Function = 'gradient_p*1e4'

# show data in view
calculator2Display = Show(calculator2, renderView1)
# trace defaults for the display properties.
calculator2Display.Representation = 'Surface'
calculator2Display.ColorArrayName = ['POINTS', 'p']
calculator2Display.LookupTable = pLUT
calculator2Display.OSPRayScaleArray = 'p'
calculator2Display.OSPRayScaleFunction = 'PiecewiseFunction'
calculator2Display.SelectOrientationVectors = 'grad_p*'
calculator2Display.ScaleFactor = 0.09199999794363976
calculator2Display.SelectScaleArray = 'p'
calculator2Display.GlyphType = 'Arrow'
calculator2Display.GlyphTableIndexArray = 'p'
calculator2Display.DataAxesGrid = 'GridAxesRepresentation'
calculator2Display.PolarAxes = 'PolarAxesRepresentation'
calculator2Display.ScalarOpacityFunction = pPWF
calculator2Display.ScalarOpacityUnitDistance = 0.07275057282595088
calculator2Display.GaussianRadius = 0.04599999897181988
calculator2Display.SetScaleArray = ['POINTS', 'p']
calculator2Display.ScaleTransferFunction = 'PiecewiseFunction'
calculator2Display.OpacityArray = ['POINTS', 'p']
calculator2Display.OpacityTransferFunction = 'PiecewiseFunction'

# init the 'PiecewiseFunction' selected for 'OSPRayScaleFunction'
calculator2Display.OSPRayScaleFunction.Points = [0.002180787269026041, 0.0, 0.5, 0.0, 0.01113197486847639, 1.0, 0.5, 0.0]

# init the 'GridAxesRepresentation' selected for 'DataAxesGrid'
calculator2Display.DataAxesGrid.XTitleColor = [0.0, 0.0, 0.0]
calculator2Display.DataAxesGrid.YTitleColor = [0.0, 0.0, 0.0]
calculator2Display.DataAxesGrid.ZTitleColor = [0.0, 0.0, 0.0]
calculator2Display.DataAxesGrid.XLabelColor = [0.0, 0.0, 0.0]
calculator2Display.DataAxesGrid.YLabelColor = [0.0, 0.0, 0.0]
calculator2Display.DataAxesGrid.ZLabelColor = [0.0, 0.0, 0.0]

# init the 'PolarAxesRepresentation' selected for 'PolarAxes'
calculator2Display.PolarAxes.PolarAxisTitleColor = [0.0, 0.0, 0.0]
calculator2Display.PolarAxes.PolarAxisLabelColor = [0.0, 0.0, 0.0]
calculator2Display.PolarAxes.LastRadialAxisTextColor = [0.0, 0.0, 0.0]
calculator2Display.PolarAxes.SecondaryRadialAxesTextColor = [0.0, 0.0, 0.0]

# init the 'PiecewiseFunction' selected for 'ScaleTransferFunction'
calculator2Display.ScaleTransferFunction.Points = [0.002180787269026041, 0.0, 0.5, 0.0, 0.01113197486847639, 1.0, 0.5, 0.0]

# init the 'PiecewiseFunction' selected for 'OpacityTransferFunction'
calculator2Display.OpacityTransferFunction.Points = [0.002180787269026041, 0.0, 0.5, 0.0, 0.01113197486847639, 1.0, 0.5, 0.0]

# hide data in view
Hide(calculator1, renderView1)

# show color bar/color legend
calculator2Display.SetScalarBarVisibility(renderView1, True)

# update the view to ensure updated data information
renderView1.Update()

# Hide orientation axes
renderView1.OrientationAxesVisibility = 0

# get color legend/bar for pLUT in view renderView1
pLUTColorBar = GetScalarBar(pLUT, renderView1)

# change scalar bar placement
pLUTColorBar.Orientation = 'Vertical'
pLUTColorBar.Position = [0.7239658444022768, 0.6217699115044248]
pLUTColorBar.ScalarBarLength = 0.29999999999999993

# get layout
layout1 = GetLayout()

# split cell
layout1.SplitVertical(0, 0.5)

# set active view
SetActiveView(None)

# Create a new 'Render View'
renderView2 = CreateView('RenderView')
renderView2.ViewSize = [1054, 437]
renderView2.AnnotationColor = [0.0, 0.0, 0.0]
renderView2.AxesGrid = 'GridAxes3DActor'
renderView2.OrientationAxesLabelColor = [0.0, 0.0, 0.0]
renderView2.StereoType = 0
renderView2.Background = [1.0, 1.0, 1.0]

# init the 'GridAxes3DActor' selected for 'AxesGrid'
renderView2.AxesGrid.XTitleColor = [0.0, 0.0, 0.0]
renderView2.AxesGrid.YTitleColor = [0.0, 0.0, 0.0]
renderView2.AxesGrid.ZTitleColor = [0.0, 0.0, 0.0]
renderView2.AxesGrid.XLabelColor = [0.0, 0.0, 0.0]
renderView2.AxesGrid.YLabelColor = [0.0, 0.0, 0.0]
renderView2.AxesGrid.ZLabelColor = [0.0, 0.0, 0.0]

# place view in the layout
layout1.AssignView(2, renderView2)

# create a new 'Tecplot Reader'
permeability_re100dat = TecplotReader(FileNames=['/mnt/bighome/nluminar/macromodel/zampogna_cavity_1000/permeability_re1000.dat'])
permeability_re100dat.DataArrayStatus = ['U', 'V', 'P', 'dPx', 'dPy', 'K11', 'K33']

# show data in view
permeability_re100datDisplay = Show(permeability_re100dat, renderView2)
# trace defaults for the display properties.
permeability_re100datDisplay.Representation = 'Surface'
permeability_re100datDisplay.ColorArrayName = [None, '']
permeability_re100datDisplay.OSPRayScaleArray = 'K11'
permeability_re100datDisplay.OSPRayScaleFunction = 'PiecewiseFunction'
permeability_re100datDisplay.SelectOrientationVectors = 'K11'
permeability_re100datDisplay.ScaleFactor = 0.09199999794363976
permeability_re100datDisplay.SelectScaleArray = 'K11'
permeability_re100datDisplay.GlyphType = 'Arrow'
permeability_re100datDisplay.GlyphTableIndexArray = 'K11'
permeability_re100datDisplay.DataAxesGrid = 'GridAxesRepresentation'
permeability_re100datDisplay.PolarAxes = 'PolarAxesRepresentation'
permeability_re100datDisplay.ScalarOpacityUnitDistance = 0.11590562517402621

# init the 'PiecewiseFunction' selected for 'OSPRayScaleFunction'
permeability_re100datDisplay.OSPRayScaleFunction.Points = [0.002180787269026041, 0.0, 0.5, 0.0, 0.01113197486847639, 1.0, 0.5, 0.0]

# init the 'GridAxesRepresentation' selected for 'DataAxesGrid'
permeability_re100datDisplay.DataAxesGrid.XTitleColor = [0.0, 0.0, 0.0]
permeability_re100datDisplay.DataAxesGrid.YTitleColor = [0.0, 0.0, 0.0]
permeability_re100datDisplay.DataAxesGrid.ZTitleColor = [0.0, 0.0, 0.0]
permeability_re100datDisplay.DataAxesGrid.XLabelColor = [0.0, 0.0, 0.0]
permeability_re100datDisplay.DataAxesGrid.YLabelColor = [0.0, 0.0, 0.0]
permeability_re100datDisplay.DataAxesGrid.ZLabelColor = [0.0, 0.0, 0.0]

# init the 'PolarAxesRepresentation' selected for 'PolarAxes'
permeability_re100datDisplay.PolarAxes.PolarAxisTitleColor = [0.0, 0.0, 0.0]
permeability_re100datDisplay.PolarAxes.PolarAxisLabelColor = [0.0, 0.0, 0.0]
permeability_re100datDisplay.PolarAxes.LastRadialAxisTextColor = [0.0, 0.0, 0.0]
permeability_re100datDisplay.PolarAxes.SecondaryRadialAxesTextColor = [0.0, 0.0, 0.0]

# reset view to fit data
renderView2.ResetCamera()

#changing interaction mode based on data extents
renderView2.InteractionMode = '2D'
renderView2.CameraPosition = [0.4999999888241291, 0.1600000001490116, 10000.0]
renderView2.CameraFocalPoint = [0.4999999888241291, 0.1600000001490116, 0.0]

# update the view to ensure updated data information
renderView2.Update()

# Hide orientation axes
renderView2.OrientationAxesVisibility = 0

# Show orientation axes
renderView2.OrientationAxesVisibility = 1

# reset view to fit data
renderView2.ResetCamera()

# reset view to fit data
renderView2.ResetCamera()

# reset view to fit data
renderView2.ResetCamera()

# Hide orientation axes
renderView2.OrientationAxesVisibility = 0

# set active view
SetActiveView(renderView1)

# change scalar bar placement
pLUTColorBar.Position = [0.7865844402277038, 0.37463032340373825]

# change scalar bar placement
pLUTColorBar.Position = [0.7714041745730548, 0.37920698244263984]

# set active view
SetActiveView(renderView2)

# reset view to fit data
renderView2.ResetCamera()

# set scalar coloring
ColorBy(permeability_re100datDisplay, ('POINTS', 'U'))

# rescale color and/or opacity maps used to include current data range
permeability_re100datDisplay.RescaleTransferFunctionToDataRange(True, False)

# show color bar/color legend
permeability_re100datDisplay.SetScalarBarVisibility(renderView2, True)

# get color transfer function/color map for 'U'
uLUT = GetColorTransferFunction('U')

# get color legend/bar for uLUT in view renderView2
uLUTColorBar = GetScalarBar(uLUT, renderView2)

# change scalar bar placement
uLUTColorBar.Orientation = 'Vertical'
uLUTColorBar.Position = [0.7865844402277038, 0.3724027459954232]
uLUTColorBar.ScalarBarLength = 0.30000000000000027

# Properties modified on uLUT
uLUT.NumberOfTableValues = 50

# Properties modified on uLUT
uLUT.NumberOfTableValues = 30

# Properties modified on uLUT
uLUT.NumberOfTableValues = 25

# change scalar bar placement
uLUTColorBar.Position = [0.781840607210626, 0.3907093821510297]

# set active view
SetActiveView(renderView1)

# set active source
SetActiveSource(calculator2)

# set scalar coloring
ColorBy(calculator2Display, ('POINTS', 'U*', 'Magnitude'))

# Hide the scalar bar for this color map if no visible data is colored by it.
HideScalarBarIfNotNeeded(pLUT, renderView1)

# rescale color and/or opacity maps used to include current data range
calculator2Display.RescaleTransferFunctionToDataRange(True, False)

# show color bar/color legend
calculator2Display.SetScalarBarVisibility(renderView1, True)

# set scalar coloring
ColorBy(calculator2Display, ('POINTS', 'U*', 'X'))

# rescale color and/or opacity maps used to exactly fit the current data range
calculator2Display.RescaleTransferFunctionToDataRange(False, False)

# Update a scalar bar component title.
UpdateScalarBarsComponentTitle(uLUT, calculator2Display)

# get color legend/bar for uLUT in view renderView1
uLUTColorBar_1 = GetScalarBar(uLUT, renderView1)

# change scalar bar placement
uLUTColorBar_1.Orientation = 'Vertical'
uLUTColorBar_1.Position = [0.7726565464895636, 0.37011441647597254]
uLUTColorBar_1.ScalarBarLength = 0.29999999999999993

# set active view
SetActiveView(renderView2)

# set active source
SetActiveSource(permeability_re100dat)

# rescale color and/or opacity maps used to exactly fit the current data range
permeability_re100datDisplay.RescaleTransferFunctionToDataRange(False, True)

# set active view
SetActiveView(renderView1)

# set active view
SetActiveView(renderView2)

# rescale color and/or opacity maps used to exactly fit the current data range
permeability_re100datDisplay.RescaleTransferFunctionToDataRange(False, True)

# set active view
SetActiveView(renderView1)

# set active source
SetActiveSource(calculator2)

# rescale color and/or opacity maps used to exactly fit the current data range
calculator2Display.RescaleTransferFunctionToDataRange(False, True)

# reset view to fit data
renderView1.ResetCamera()

# rescale color and/or opacity maps used to exactly fit the current data range
calculator2Display.RescaleTransferFunctionToDataRange(False, True)

# set active source
SetActiveSource(permeability_re100dat)

# set active view
SetActiveView(renderView2)

# rescale color and/or opacity maps used to exactly fit the current data range
permeability_re100datDisplay.RescaleTransferFunctionToDataRange(False, True)

# set active view
SetActiveView(renderView1)

# set active source
SetActiveSource(calculator2)

# rescale color and/or opacity maps used to exactly fit the current data range
calculator2Display.RescaleTransferFunctionToDataRange(False, True)

# current camera placement for renderView1
renderView1.CameraPosition = [0.6352510417969459, -1.0004801010976068, 0.1600000001490116]
renderView1.CameraFocalPoint = [0.6352510417969459, 0.03999999910593033, 0.1600000001490116]
renderView1.CameraViewUp = [0.0, 0.0, 1.0]
renderView1.CameraParallelScale = 0.4770744079486521

# current camera placement for renderView2
renderView2.InteractionMode = '2D'
renderView2.CameraPosition = [0.6281622736785717, 0.13615114551114785, 1.8367835453775365]
renderView2.CameraFocalPoint = [0.6281622736785717, 0.13615114551114785, 0.0]
renderView2.CameraParallelScale = 0.26834783745783314

# save screenshot
SaveScreenshot('/mnt/bighome/nluminar/macromodel/zampogna_cavity_1000/u.png', layout1, SaveAllViews=1,
    ImageResolution=[1456, 930])

# set scalar coloring
ColorBy(calculator2Display, ('POINTS', 'U*', 'Z'))

# rescale color and/or opacity maps used to exactly fit the current data range
calculator2Display.RescaleTransferFunctionToDataRange(False, False)

# Update a scalar bar component title.
UpdateScalarBarsComponentTitle(uLUT, calculator2Display)

# rescale color and/or opacity maps used to exactly fit the current data range
calculator2Display.RescaleTransferFunctionToDataRange(False, True)

# set active view
SetActiveView(renderView2)

# set active source
SetActiveSource(permeability_re100dat)

# set scalar coloring
ColorBy(permeability_re100datDisplay, ('POINTS', 'V'))

# Hide the scalar bar for this color map if no visible data is colored by it.
HideScalarBarIfNotNeeded(uLUT, renderView2)

# rescale color and/or opacity maps used to include current data range
permeability_re100datDisplay.RescaleTransferFunctionToDataRange(True, False)

# show color bar/color legend
permeability_re100datDisplay.SetScalarBarVisibility(renderView2, True)

# get color transfer function/color map for 'V'
vLUT = GetColorTransferFunction('V')

# rescale color and/or opacity maps used to exactly fit the current data range
permeability_re100datDisplay.RescaleTransferFunctionToDataRange(False, True)

# Properties modified on vLUT
vLUT.NumberOfTableValues = 25

# get color legend/bar for vLUT in view renderView2
vLUTColorBar = GetScalarBar(vLUT, renderView2)

# change scalar bar placement
vLUTColorBar.Orientation = 'Vertical'
vLUTColorBar.Position = [0.7741379310344826, 0.41130434782608694]
vLUTColorBar.ScalarBarLength = 0.2999999999999994

# current camera placement for renderView1
renderView1.CameraPosition = [0.6352510417969459, -1.0004801010976068, 0.1600000001490116]
renderView1.CameraFocalPoint = [0.6352510417969459, 0.03999999910593033, 0.1600000001490116]
renderView1.CameraViewUp = [0.0, 0.0, 1.0]
renderView1.CameraParallelScale = 0.4770744079486521

# current camera placement for renderView2
renderView2.InteractionMode = '2D'
renderView2.CameraPosition = [0.6281622736785717, 0.13615114551114785, 1.8367835453775365]
renderView2.CameraFocalPoint = [0.6281622736785717, 0.13615114551114785, 0.0]
renderView2.CameraParallelScale = 0.26834783745783314

# save screenshot
SaveScreenshot('/mnt/bighome/nluminar/macromodel/zampogna_cavity_1000/w.png', layout1, SaveAllViews=1,
    ImageResolution=[1456, 930])

# set scalar coloring
ColorBy(permeability_re100datDisplay, ('POINTS', 'dPx'))

# Hide the scalar bar for this color map if no visible data is colored by it.
HideScalarBarIfNotNeeded(vLUT, renderView2)

# rescale color and/or opacity maps used to include current data range
permeability_re100datDisplay.RescaleTransferFunctionToDataRange(True, False)

# show color bar/color legend
permeability_re100datDisplay.SetScalarBarVisibility(renderView2, True)

# get color transfer function/color map for 'dPx'
dPxLUT = GetColorTransferFunction('dPx')

# Apply a preset using its name. Note this may not work as expected when presets have duplicate names.
dPxLUT.ApplyPreset('Cool to Warm', True)

# Properties modified on dPxLUT
dPxLUT.RGBPoints = [-0.017030425369739532, 0.23137254902, 0.298039215686, 0.752941176471, 0.0, 0.865, 0.865, 0.865, 0.08562164753675461, 0.705882352941, 0.0156862745098, 0.149019607843]

# Properties modified on dPxLUT
dPxLUT.NumberOfTableValues = 25

# get color legend/bar for dPxLUT in view renderView2
dPxLUTColorBar = GetScalarBar(dPxLUT, renderView2)

# change scalar bar placement
dPxLUTColorBar.Orientation = 'Vertical'
dPxLUTColorBar.Position = [0.788785578747628, 0.38155606407322645]
dPxLUTColorBar.ScalarBarLength = 0.3000000000000002

# set active source
SetActiveSource(calculator2)

# set active source
SetActiveSource(calculator2)

# show data in view
calculator2Display_1 = Show(calculator2, renderView2)
# trace defaults for the display properties.
calculator2Display_1.Representation = 'Surface'
calculator2Display_1.ColorArrayName = ['POINTS', 'p']
calculator2Display_1.LookupTable = pLUT
calculator2Display_1.OSPRayScaleArray = 'p'
calculator2Display_1.OSPRayScaleFunction = 'PiecewiseFunction'
calculator2Display_1.SelectOrientationVectors = 'grad_p*'
calculator2Display_1.ScaleFactor = 0.09199999794363976
calculator2Display_1.SelectScaleArray = 'p'
calculator2Display_1.GlyphType = 'Arrow'
calculator2Display_1.GlyphTableIndexArray = 'p'
calculator2Display_1.DataAxesGrid = 'GridAxesRepresentation'
calculator2Display_1.PolarAxes = 'PolarAxesRepresentation'
calculator2Display_1.ScalarOpacityFunction = pPWF
calculator2Display_1.ScalarOpacityUnitDistance = 0.07275057282595088
calculator2Display_1.GaussianRadius = 0.04599999897181988
calculator2Display_1.SetScaleArray = ['POINTS', 'p']
calculator2Display_1.ScaleTransferFunction = 'PiecewiseFunction'
calculator2Display_1.OpacityArray = ['POINTS', 'p']
calculator2Display_1.OpacityTransferFunction = 'PiecewiseFunction'

# init the 'PiecewiseFunction' selected for 'OSPRayScaleFunction'
calculator2Display_1.OSPRayScaleFunction.Points = [0.002180787269026041, 0.0, 0.5, 0.0, 0.01113197486847639, 1.0, 0.5, 0.0]

# init the 'GridAxesRepresentation' selected for 'DataAxesGrid'
calculator2Display_1.DataAxesGrid.XTitleColor = [0.0, 0.0, 0.0]
calculator2Display_1.DataAxesGrid.YTitleColor = [0.0, 0.0, 0.0]
calculator2Display_1.DataAxesGrid.ZTitleColor = [0.0, 0.0, 0.0]
calculator2Display_1.DataAxesGrid.XLabelColor = [0.0, 0.0, 0.0]
calculator2Display_1.DataAxesGrid.YLabelColor = [0.0, 0.0, 0.0]
calculator2Display_1.DataAxesGrid.ZLabelColor = [0.0, 0.0, 0.0]

# init the 'PolarAxesRepresentation' selected for 'PolarAxes'
calculator2Display_1.PolarAxes.PolarAxisTitleColor = [0.0, 0.0, 0.0]
calculator2Display_1.PolarAxes.PolarAxisLabelColor = [0.0, 0.0, 0.0]
calculator2Display_1.PolarAxes.LastRadialAxisTextColor = [0.0, 0.0, 0.0]
calculator2Display_1.PolarAxes.SecondaryRadialAxesTextColor = [0.0, 0.0, 0.0]

# init the 'PiecewiseFunction' selected for 'ScaleTransferFunction'
calculator2Display_1.ScaleTransferFunction.Points = [0.002180787269026041, 0.0, 0.5, 0.0, 0.01113197486847639, 1.0, 0.5, 0.0]

# init the 'PiecewiseFunction' selected for 'OpacityTransferFunction'
calculator2Display_1.OpacityTransferFunction.Points = [0.002180787269026041, 0.0, 0.5, 0.0, 0.01113197486847639, 1.0, 0.5, 0.0]

# show color bar/color legend
calculator2Display_1.SetScalarBarVisibility(renderView2, True)

# hide data in view
Hide(calculator2, renderView2)

# set active view
SetActiveView(renderView1)

# set scalar coloring
ColorBy(calculator2Display, ('POINTS', 'grad_p*', 'Magnitude'))

# Hide the scalar bar for this color map if no visible data is colored by it.
HideScalarBarIfNotNeeded(uLUT, renderView1)

# rescale color and/or opacity maps used to include current data range
calculator2Display.RescaleTransferFunctionToDataRange(True, False)

# show color bar/color legend
calculator2Display.SetScalarBarVisibility(renderView1, True)

# get color transfer function/color map for 'grad_p'
grad_pLUT = GetColorTransferFunction('grad_p')

# set scalar coloring
ColorBy(calculator2Display, ('POINTS', 'grad_p*', 'X'))

# rescale color and/or opacity maps used to exactly fit the current data range
calculator2Display.RescaleTransferFunctionToDataRange(False, False)

# Update a scalar bar component title.
UpdateScalarBarsComponentTitle(grad_pLUT, calculator2Display)

# Apply a preset using its name. Note this may not work as expected when presets have duplicate names.
grad_pLUT.ApplyPreset('Cool to Warm', True)

# Properties modified on grad_pLUT
grad_pLUT.RGBPoints = [-0.04665437458584165, 0.23137254902, 0.298039215686, 0.752941176471, 0.07700391113758087, 0.865, 0.865, 0.865, 0.20367825470657408, 0.705882352941, 0.0156862745098, 0.149019607843]

# Properties modified on grad_pLUT
grad_pLUT.RGBPoints = [-0.04665437458584165, 0.23137254902, 0.298039215686, 0.752941176471, 0.0, 0.865, 0.865, 0.865, 0.20367825470657408, 0.705882352941, 0.0156862745098, 0.149019607843]

# Properties modified on grad_pLUT
grad_pLUT.NumberOfTableValues = 25

# get color legend/bar for grad_pLUT in view renderView1
grad_pLUTColorBar = GetScalarBar(grad_pLUT, renderView1)

# change scalar bar placement
grad_pLUTColorBar.Orientation = 'Vertical'
grad_pLUTColorBar.Position = [0.7879310344827586, 0.3518077803203663]
grad_pLUTColorBar.ScalarBarLength = 0.2999999999999995

# current camera placement for renderView1
renderView1.CameraPosition = [0.6352510417969459, -1.0004801010976068, 0.1600000001490116]
renderView1.CameraFocalPoint = [0.6352510417969459, 0.03999999910593033, 0.1600000001490116]
renderView1.CameraViewUp = [0.0, 0.0, 1.0]
renderView1.CameraParallelScale = 0.4770744079486521

# current camera placement for renderView2
renderView2.InteractionMode = '2D'
renderView2.CameraPosition = [0.6281622736785717, 0.13615114551114785, 1.8367835453775365]
renderView2.CameraFocalPoint = [0.6281622736785717, 0.13615114551114785, 0.0]
renderView2.CameraParallelScale = 0.26834783745783314

# save screenshot
SaveScreenshot('/mnt/bighome/nluminar/macromodel/zampogna_cavity_1000/dpx.png', layout1, SaveAllViews=1,
    ImageResolution=[1456, 930])

# set scalar coloring
ColorBy(calculator2Display, ('POINTS', 'grad_p*', 'Z'))

# rescale color and/or opacity maps used to exactly fit the current data range
calculator2Display.RescaleTransferFunctionToDataRange(False, False)

# Update a scalar bar component title.
UpdateScalarBarsComponentTitle(grad_pLUT, calculator2Display)

# rescale color and/or opacity maps used to exactly fit the current data range
calculator2Display.RescaleTransferFunctionToDataRange(False, True)

# Properties modified on grad_pLUT
grad_pLUT.RGBPoints = [-0.055763475614867275, 0.23137254902, 0.298039215686, 0.752941176471, 0.0, 0.865, 0.865, 0.865, 0.08615062085937097, 0.705882352941, 0.0156862745098, 0.149019607843]

# set active view
SetActiveView(renderView2)

# set active source
SetActiveSource(permeability_re100dat)

# set scalar coloring
ColorBy(permeability_re100datDisplay, ('POINTS', 'dPy'))

# Hide the scalar bar for this color map if no visible data is colored by it.
HideScalarBarIfNotNeeded(dPxLUT, renderView2)

# rescale color and/or opacity maps used to include current data range
permeability_re100datDisplay.RescaleTransferFunctionToDataRange(True, False)

# show color bar/color legend
permeability_re100datDisplay.SetScalarBarVisibility(renderView2, True)

# get color transfer function/color map for 'dPy'
dPyLUT = GetColorTransferFunction('dPy')

# Apply a preset using its name. Note this may not work as expected when presets have duplicate names.
dPyLUT.ApplyPreset('Cool to Warm', True)

# Properties modified on dPyLUT
dPyLUT.NumberOfTableValues = 25

# Properties modified on dPyLUT
dPyLUT.RGBPoints = [-0.04860113561153412, 0.23137254902, 0.298039215686, 0.752941176471, 0.0, 0.865, 0.865, 0.865, 0.07777638733386993, 0.705882352941, 0.0156862745098, 0.149019607843]

# get color legend/bar for dPyLUT in view renderView2
dPyLUTColorBar = GetScalarBar(dPyLUT, renderView2)

# change scalar bar placement
dPyLUTColorBar.Orientation = 'Vertical'
dPyLUTColorBar.Position = [0.7906896551724139, 0.38384439359267714]
dPyLUTColorBar.ScalarBarLength = 0.30000000000000043

# current camera placement for renderView1
renderView1.CameraPosition = [0.6352510417969459, -1.0004801010976068, 0.1600000001490116]
renderView1.CameraFocalPoint = [0.6352510417969459, 0.03999999910593033, 0.1600000001490116]
renderView1.CameraViewUp = [0.0, 0.0, 1.0]
renderView1.CameraParallelScale = 0.4770744079486521

# current camera placement for renderView2
renderView2.InteractionMode = '2D'
renderView2.CameraPosition = [0.6281622736785717, 0.13615114551114785, 1.8367835453775365]
renderView2.CameraFocalPoint = [0.6281622736785717, 0.13615114551114785, 0.0]
renderView2.CameraParallelScale = 0.26834783745783314

# save screenshot
SaveScreenshot('/mnt/bighome/nluminar/macromodel/zampogna_cavity_1000/dpz.png', layout1, SaveAllViews=1,
    ImageResolution=[1456, 930])

# set scalar coloring
ColorBy(permeability_re100datDisplay, ('POINTS', 'K11'))

# Hide the scalar bar for this color map if no visible data is colored by it.
HideScalarBarIfNotNeeded(dPyLUT, renderView2)

# rescale color and/or opacity maps used to include current data range
permeability_re100datDisplay.RescaleTransferFunctionToDataRange(True, False)

# show color bar/color legend
permeability_re100datDisplay.SetScalarBarVisibility(renderView2, True)

# get color transfer function/color map for 'K11'
k11LUT = GetColorTransferFunction('K11')

# Apply a preset using its name. Note this may not work as expected when presets have duplicate names.
k11LUT.ApplyPreset('Magma (matplotlib)', True)

# Properties modified on k11LUT
k11LUT.NumberOfTableValues = 25

# get color legend/bar for k11LUT in view renderView2
k11LUTColorBar = GetScalarBar(k11LUT, renderView2)

# change scalar bar placement
k11LUTColorBar.Orientation = 'Vertical'
k11LUTColorBar.Position = [0.7844827586206896, 0.3838443935926774]
k11LUTColorBar.ScalarBarLength = 0.2999999999999998

# rescale color and/or opacity maps used to exactly fit the current data range
permeability_re100datDisplay.RescaleTransferFunctionToDataRange(False, True)

# Rescale transfer function
k11LUT.RescaleTransferFunction(0.026, 0.0266)

# get opacity transfer function/opacity map for 'K11'
k11PWF = GetOpacityTransferFunction('K11')

# Rescale transfer function
k11PWF.RescaleTransferFunction(0.026, 0.0266)

# rescale color and/or opacity maps used to exactly fit the current data range
permeability_re100datDisplay.RescaleTransferFunctionToDataRange(False, True)

# create a new 'Calculator'
calculator3 = Calculator(Input=permeability_re100dat)
calculator3.Function = ''

# Properties modified on calculator3
calculator3.ResultArrayName = 'k11'
calculator3.Function = 'abs(K11)'

# get color transfer function/color map for 'k11'
k11LUT_1 = GetColorTransferFunction('k11')

# get opacity transfer function/opacity map for 'k11'
k11PWF_1 = GetOpacityTransferFunction('k11')

# show data in view
calculator3Display = Show(calculator3, renderView2)
# trace defaults for the display properties.
calculator3Display.Representation = 'Surface'
calculator3Display.ColorArrayName = ['POINTS', 'k11']
calculator3Display.LookupTable = k11LUT_1
calculator3Display.OSPRayScaleArray = 'k11'
calculator3Display.OSPRayScaleFunction = 'PiecewiseFunction'
calculator3Display.SelectOrientationVectors = 'K11'
calculator3Display.ScaleFactor = 0.09199999794363976
calculator3Display.SelectScaleArray = 'k11'
calculator3Display.GlyphType = 'Arrow'
calculator3Display.GlyphTableIndexArray = 'k11'
calculator3Display.DataAxesGrid = 'GridAxesRepresentation'
calculator3Display.PolarAxes = 'PolarAxesRepresentation'
calculator3Display.ScalarOpacityFunction = k11PWF_1
calculator3Display.ScalarOpacityUnitDistance = 0.11590562517402621

# init the 'PiecewiseFunction' selected for 'OSPRayScaleFunction'
calculator3Display.OSPRayScaleFunction.Points = [0.002180787269026041, 0.0, 0.5, 0.0, 0.01113197486847639, 1.0, 0.5, 0.0]

# init the 'GridAxesRepresentation' selected for 'DataAxesGrid'
calculator3Display.DataAxesGrid.XTitleColor = [0.0, 0.0, 0.0]
calculator3Display.DataAxesGrid.YTitleColor = [0.0, 0.0, 0.0]
calculator3Display.DataAxesGrid.ZTitleColor = [0.0, 0.0, 0.0]
calculator3Display.DataAxesGrid.XLabelColor = [0.0, 0.0, 0.0]
calculator3Display.DataAxesGrid.YLabelColor = [0.0, 0.0, 0.0]
calculator3Display.DataAxesGrid.ZLabelColor = [0.0, 0.0, 0.0]

# init the 'PolarAxesRepresentation' selected for 'PolarAxes'
calculator3Display.PolarAxes.PolarAxisTitleColor = [0.0, 0.0, 0.0]
calculator3Display.PolarAxes.PolarAxisLabelColor = [0.0, 0.0, 0.0]
calculator3Display.PolarAxes.LastRadialAxisTextColor = [0.0, 0.0, 0.0]
calculator3Display.PolarAxes.SecondaryRadialAxesTextColor = [0.0, 0.0, 0.0]

# hide data in view
Hide(permeability_re100dat, renderView2)

# show color bar/color legend
calculator3Display.SetScalarBarVisibility(renderView2, True)

# update the view to ensure updated data information
renderView2.Update()

# Apply a preset using its name. Note this may not work as expected when presets have duplicate names.
k11LUT_1.ApplyPreset('Magma (matplotlib)', True)

# get color legend/bar for k11LUT_1 in view renderView2
k11LUT_1ColorBar = GetScalarBar(k11LUT_1, renderView2)

# change scalar bar placement
k11LUT_1ColorBar.Orientation = 'Vertical'
k11LUT_1ColorBar.Position = [0.7486206896551725, 0.3861327231121281]
k11LUT_1ColorBar.ScalarBarLength = 0.30000000000000004

# rescale color and/or opacity maps used to exactly fit the current data range
calculator3Display.RescaleTransferFunctionToDataRange(False, True)

# rescale color and/or opacity maps used to exactly fit the current data range
calculator3Display.RescaleTransferFunctionToDataRange(False, True)

# Rescale transfer function
k11LUT_1.RescaleTransferFunction(0.0025, 0.0027)

# Rescale transfer function
k11PWF_1.RescaleTransferFunction(0.0025, 0.0027)

# Rescale transfer function
k11LUT_1.RescaleTransferFunction(0.0023, 0.0027)

# Rescale transfer function
k11PWF_1.RescaleTransferFunction(0.0023, 0.0027)

# Rescale transfer function
k11LUT_1.RescaleTransferFunction(0.0023, 0.0025)

# Rescale transfer function
k11PWF_1.RescaleTransferFunction(0.0023, 0.0025)

# Rescale transfer function
k11LUT_1.RescaleTransferFunction(0.0022, 0.0025)

# Rescale transfer function
k11PWF_1.RescaleTransferFunction(0.0022, 0.0025)

# Rescale transfer function
k11LUT_1.RescaleTransferFunction(0.0018, 0.0025)

# Rescale transfer function
k11PWF_1.RescaleTransferFunction(0.0018, 0.0025)

# set active view
SetActiveView(renderView1)

# set active source
SetActiveSource(calculator2)

# create a new 'Calculator'
calculator4 = Calculator(Input=calculator2)
calculator4.Function = ''

# Properties modified on calculator4
calculator4.ResultArrayName = 'K11*'
calculator4.Function = '1/K_0'

# show data in view
calculator4Display = Show(calculator4, renderView1)
# trace defaults for the display properties.
calculator4Display.Representation = 'Surface'
calculator4Display.ColorArrayName = ['POINTS', 'K11*']
calculator4Display.LookupTable = k11LUT
calculator4Display.OSPRayScaleArray = 'K11*'
calculator4Display.OSPRayScaleFunction = 'PiecewiseFunction'
calculator4Display.SelectOrientationVectors = 'grad_p*'
calculator4Display.ScaleFactor = 0.09199999794363976
calculator4Display.SelectScaleArray = 'K11*'
calculator4Display.GlyphType = 'Arrow'
calculator4Display.GlyphTableIndexArray = 'K11*'
calculator4Display.DataAxesGrid = 'GridAxesRepresentation'
calculator4Display.PolarAxes = 'PolarAxesRepresentation'
calculator4Display.ScalarOpacityFunction = k11PWF
calculator4Display.ScalarOpacityUnitDistance = 0.07275057282595088
calculator4Display.GaussianRadius = 0.04599999897181988
calculator4Display.SetScaleArray = ['POINTS', 'K11*']
calculator4Display.ScaleTransferFunction = 'PiecewiseFunction'
calculator4Display.OpacityArray = ['POINTS', 'K11*']
calculator4Display.OpacityTransferFunction = 'PiecewiseFunction'

# init the 'PiecewiseFunction' selected for 'OSPRayScaleFunction'
calculator4Display.OSPRayScaleFunction.Points = [0.002180787269026041, 0.0, 0.5, 0.0, 0.01113197486847639, 1.0, 0.5, 0.0]

# init the 'GridAxesRepresentation' selected for 'DataAxesGrid'
calculator4Display.DataAxesGrid.XTitleColor = [0.0, 0.0, 0.0]
calculator4Display.DataAxesGrid.YTitleColor = [0.0, 0.0, 0.0]
calculator4Display.DataAxesGrid.ZTitleColor = [0.0, 0.0, 0.0]
calculator4Display.DataAxesGrid.XLabelColor = [0.0, 0.0, 0.0]
calculator4Display.DataAxesGrid.YLabelColor = [0.0, 0.0, 0.0]
calculator4Display.DataAxesGrid.ZLabelColor = [0.0, 0.0, 0.0]

# init the 'PolarAxesRepresentation' selected for 'PolarAxes'
calculator4Display.PolarAxes.PolarAxisTitleColor = [0.0, 0.0, 0.0]
calculator4Display.PolarAxes.PolarAxisLabelColor = [0.0, 0.0, 0.0]
calculator4Display.PolarAxes.LastRadialAxisTextColor = [0.0, 0.0, 0.0]
calculator4Display.PolarAxes.SecondaryRadialAxesTextColor = [0.0, 0.0, 0.0]

# init the 'PiecewiseFunction' selected for 'ScaleTransferFunction'
calculator4Display.ScaleTransferFunction.Points = [0.002180787269026041, 0.0, 0.5, 0.0, 0.01113197486847639, 1.0, 0.5, 0.0]

# init the 'PiecewiseFunction' selected for 'OpacityTransferFunction'
calculator4Display.OpacityTransferFunction.Points = [0.002180787269026041, 0.0, 0.5, 0.0, 0.01113197486847639, 1.0, 0.5, 0.0]

# hide data in view
Hide(calculator2, renderView1)

# show color bar/color legend
calculator4Display.SetScalarBarVisibility(renderView1, True)

# update the view to ensure updated data information
renderView1.Update()

# update the view to ensure updated data information
renderView2.Update()

# Rescale transfer function
k11LUT_1.RescaleTransferFunction(0.000590512703639, 0.0109498696402)

# Rescale transfer function
k11PWF_1.RescaleTransferFunction(0.000590512703639, 0.0109498696402)

# get color legend/bar for k11LUT in view renderView1
k11LUTColorBar_1 = GetScalarBar(k11LUT, renderView1)

# change scalar bar placement
k11LUTColorBar_1.Orientation = 'Vertical'
k11LUTColorBar_1.Position = [0.747241379310345, 0.3289244851258581]
k11LUTColorBar_1.ScalarBarLength = 0.2999999999999999

# rescale color and/or opacity maps used to exactly fit the current data range
calculator4Display.RescaleTransferFunctionToDataRange(False, True)

# set active source
SetActiveSource(calculator3)

# set active view
SetActiveView(renderView2)

# Rescale transfer function
k11LUT_1.RescaleTransferFunction(0.026, 0.029)

# Rescale transfer function
k11PWF_1.RescaleTransferFunction(0.026, 0.029)

# set active view
SetActiveView(renderView1)

# set active source
SetActiveSource(calculator4)

# rescale color and/or opacity maps used to exactly fit the current data range
calculator4Display.RescaleTransferFunctionToDataRange(False, True)

# rescale color and/or opacity maps used to exactly fit the current data range
calculator4Display.RescaleTransferFunctionToDataRange(False, True)

# Rescale transfer function
k11LUT.RescaleTransferFunction(0.018, 0.0286557)

# Rescale transfer function
k11PWF.RescaleTransferFunction(0.018, 0.0286557)

# set active view
SetActiveView(renderView2)

# set active source
SetActiveSource(calculator3)

# Rescale transfer function
k11LUT_1.RescaleTransferFunction(0.018, 0.029)

# Rescale transfer function
k11PWF_1.RescaleTransferFunction(0.018, 0.029)

# rescale color and/or opacity maps used to exactly fit the current data range
calculator3Display.RescaleTransferFunctionToDataRange(False, True)

# set active view
SetActiveView(renderView1)

# set active source
SetActiveSource(calculator4)

# rescale color and/or opacity maps used to exactly fit the current data range
calculator4Display.RescaleTransferFunctionToDataRange(False, True)

# set active view
SetActiveView(renderView2)

# set active source
SetActiveSource(calculator3)

# Rescale transfer function
k11LUT_1.RescaleTransferFunction(0.025, 0.03)

# Rescale transfer function
k11PWF_1.RescaleTransferFunction(0.025, 0.03)

# Rescale transfer function
k11LUT_1.RescaleTransferFunction(0.026, 0.029)

# Rescale transfer function
k11PWF_1.RescaleTransferFunction(0.026, 0.029)

# current camera placement for renderView1
renderView1.CameraPosition = [0.6352510417969459, -1.0004801010976068, 0.1600000001490116]
renderView1.CameraFocalPoint = [0.6352510417969459, 0.03999999910593033, 0.1600000001490116]
renderView1.CameraViewUp = [0.0, 0.0, 1.0]
renderView1.CameraParallelScale = 0.4770744079486521

# current camera placement for renderView2
renderView2.InteractionMode = '2D'
renderView2.CameraPosition = [0.6269341371227006, 0.13615114551114785, 1.8367835453775365]
renderView2.CameraFocalPoint = [0.6269341371227006, 0.13615114551114785, 0.0]
renderView2.CameraParallelScale = 0.26834783745783314

# save screenshot
SaveScreenshot('/mnt/bighome/nluminar/macromodel/zampogna_cavity_1000/k11.png', layout1, SaveAllViews=1,
    ImageResolution=[1456, 930])

# set scalar coloring
ColorBy(calculator3Display, ('POINTS', 'K33'))

# Hide the scalar bar for this color map if no visible data is colored by it.
HideScalarBarIfNotNeeded(k11LUT_1, renderView2)

# rescale color and/or opacity maps used to include current data range
calculator3Display.RescaleTransferFunctionToDataRange(True, False)

# show color bar/color legend
calculator3Display.SetScalarBarVisibility(renderView2, True)

# get color transfer function/color map for 'K33'
k33LUT = GetColorTransferFunction('K33')

# get color legend/bar for k33LUT in view renderView2
k33LUTColorBar = GetScalarBar(k33LUT, renderView2)

# change scalar bar placement
k33LUTColorBar.Orientation = 'Vertical'
k33LUTColorBar.Position = [0.8079310344827587, 0.39986270022883297]
k33LUTColorBar.ScalarBarLength = 0.2999999999999995

# set active view
SetActiveView(renderView1)

# set active source
SetActiveSource(calculator4)

# create a new 'Calculator'
calculator5 = Calculator(Input=calculator4)
calculator5.Function = ''

# Properties modified on calculator5
calculator5.ResultArrayName = 'K33*'
calculator5.Function = '1/K_8'

# get opacity transfer function/opacity map for 'K33'
k33PWF = GetOpacityTransferFunction('K33')

# show data in view
calculator5Display = Show(calculator5, renderView1)
# trace defaults for the display properties.
calculator5Display.Representation = 'Surface'
calculator5Display.ColorArrayName = ['POINTS', 'K33*']
calculator5Display.LookupTable = k33LUT
calculator5Display.OSPRayScaleArray = 'K33*'
calculator5Display.OSPRayScaleFunction = 'PiecewiseFunction'
calculator5Display.SelectOrientationVectors = 'grad_p*'
calculator5Display.ScaleFactor = 0.09199999794363976
calculator5Display.SelectScaleArray = 'K33*'
calculator5Display.GlyphType = 'Arrow'
calculator5Display.GlyphTableIndexArray = 'K33*'
calculator5Display.DataAxesGrid = 'GridAxesRepresentation'
calculator5Display.PolarAxes = 'PolarAxesRepresentation'
calculator5Display.ScalarOpacityFunction = k33PWF
calculator5Display.ScalarOpacityUnitDistance = 0.07275057282595088
calculator5Display.GaussianRadius = 0.04599999897181988
calculator5Display.SetScaleArray = ['POINTS', 'K33*']
calculator5Display.ScaleTransferFunction = 'PiecewiseFunction'
calculator5Display.OpacityArray = ['POINTS', 'K33*']
calculator5Display.OpacityTransferFunction = 'PiecewiseFunction'

# init the 'PiecewiseFunction' selected for 'OSPRayScaleFunction'
calculator5Display.OSPRayScaleFunction.Points = [0.002180787269026041, 0.0, 0.5, 0.0, 0.01113197486847639, 1.0, 0.5, 0.0]

# init the 'GridAxesRepresentation' selected for 'DataAxesGrid'
calculator5Display.DataAxesGrid.XTitleColor = [0.0, 0.0, 0.0]
calculator5Display.DataAxesGrid.YTitleColor = [0.0, 0.0, 0.0]
calculator5Display.DataAxesGrid.ZTitleColor = [0.0, 0.0, 0.0]
calculator5Display.DataAxesGrid.XLabelColor = [0.0, 0.0, 0.0]
calculator5Display.DataAxesGrid.YLabelColor = [0.0, 0.0, 0.0]
calculator5Display.DataAxesGrid.ZLabelColor = [0.0, 0.0, 0.0]

# init the 'PolarAxesRepresentation' selected for 'PolarAxes'
calculator5Display.PolarAxes.PolarAxisTitleColor = [0.0, 0.0, 0.0]
calculator5Display.PolarAxes.PolarAxisLabelColor = [0.0, 0.0, 0.0]
calculator5Display.PolarAxes.LastRadialAxisTextColor = [0.0, 0.0, 0.0]
calculator5Display.PolarAxes.SecondaryRadialAxesTextColor = [0.0, 0.0, 0.0]

# init the 'PiecewiseFunction' selected for 'ScaleTransferFunction'
calculator5Display.ScaleTransferFunction.Points = [0.002180787269026041, 0.0, 0.5, 0.0, 0.01113197486847639, 1.0, 0.5, 0.0]

# init the 'PiecewiseFunction' selected for 'OpacityTransferFunction'
calculator5Display.OpacityTransferFunction.Points = [0.002180787269026041, 0.0, 0.5, 0.0, 0.01113197486847639, 1.0, 0.5, 0.0]

# hide data in view
Hide(calculator4, renderView1)

# show color bar/color legend
calculator5Display.SetScalarBarVisibility(renderView1, True)

# update the view to ensure updated data information
renderView1.Update()

# update the view to ensure updated data information
renderView2.Update()

# Apply a preset using its name. Note this may not work as expected when presets have duplicate names.
k33LUT.ApplyPreset('Magma (matplotlib)', True)

# get color legend/bar for k33LUT in view renderView1
k33LUTColorBar_1 = GetScalarBar(k33LUT, renderView1)

# change scalar bar placement
k33LUTColorBar_1.Orientation = 'Vertical'
k33LUTColorBar_1.Position = [0.8106896551724138, 0.32892448512585803]
k33LUTColorBar_1.ScalarBarLength = 0.30000000000000016

# rescale color and/or opacity maps used to exactly fit the current data range
calculator5Display.RescaleTransferFunctionToDataRange(False, True)

# set active view
SetActiveView(renderView2)

# current camera placement for renderView1
renderView1.CameraPosition = [0.6352510417969459, -1.0004801010976068, 0.1600000001490116]
renderView1.CameraFocalPoint = [0.6352510417969459, 0.03999999910593033, 0.1600000001490116]
renderView1.CameraViewUp = [0.0, 0.0, 1.0]
renderView1.CameraParallelScale = 0.4770744079486521

# current camera placement for renderView2
renderView2.InteractionMode = '2D'
renderView2.CameraPosition = [0.6269341371227006, 0.13615114551114785, 1.8367835453775365]
renderView2.CameraFocalPoint = [0.6269341371227006, 0.13615114551114785, 0.0]
renderView2.CameraParallelScale = 0.26834783745783314

# save screenshot
SaveScreenshot('/mnt/bighome/nluminar/macromodel/zampogna_cavity_1000/k33.png', layout1, SaveAllViews=1,
    ImageResolution=[1456, 930])

# set active view
SetActiveView(renderView1)

# create a new 'Stream Tracer'
streamTracer1 = StreamTracer(Input=calculator5,
    SeedType='High Resolution Line Source')
streamTracer1.Vectors = ['POINTS', 'grad_p*']
streamTracer1.MaximumStreamlineLength = 0.9199999794363976

# init the 'High Resolution Line Source' selected for 'SeedType'
streamTracer1.SeedType.Point1 = [0.03999999910593033, 0.0, 0.03999999910593033]
streamTracer1.SeedType.Point2 = [0.9599999785423279, 0.07999999821186066, 0.2800000011920929]

# Properties modified on streamTracer1.SeedType
streamTracer1.SeedType.Resolution = 100

# Properties modified on streamTracer1.SeedType
streamTracer1.SeedType.Resolution = 100

# show data in view
streamTracer1Display = Show(streamTracer1, renderView1)
# trace defaults for the display properties.
streamTracer1Display.Representation = 'Surface'
streamTracer1Display.ColorArrayName = ['POINTS', 'K33*']
streamTracer1Display.LookupTable = k33LUT
streamTracer1Display.OSPRayScaleArray = 'K33*'
streamTracer1Display.OSPRayScaleFunction = 'PiecewiseFunction'
streamTracer1Display.SelectOrientationVectors = 'Normals'
streamTracer1Display.ScaleFactor = 0.09182000383734704
streamTracer1Display.SelectScaleArray = 'K33*'
streamTracer1Display.GlyphType = 'Arrow'
streamTracer1Display.GlyphTableIndexArray = 'K33*'
streamTracer1Display.DataAxesGrid = 'GridAxesRepresentation'
streamTracer1Display.PolarAxes = 'PolarAxesRepresentation'
streamTracer1Display.GaussianRadius = 0.04591000191867352
streamTracer1Display.SetScaleArray = ['POINTS', 'K33*']
streamTracer1Display.ScaleTransferFunction = 'PiecewiseFunction'
streamTracer1Display.OpacityArray = ['POINTS', 'K33*']
streamTracer1Display.OpacityTransferFunction = 'PiecewiseFunction'

# init the 'PiecewiseFunction' selected for 'OSPRayScaleFunction'
streamTracer1Display.OSPRayScaleFunction.Points = [0.002180787269026041, 0.0, 0.5, 0.0, 0.01113197486847639, 1.0, 0.5, 0.0]

# init the 'GridAxesRepresentation' selected for 'DataAxesGrid'
streamTracer1Display.DataAxesGrid.XTitleColor = [0.0, 0.0, 0.0]
streamTracer1Display.DataAxesGrid.YTitleColor = [0.0, 0.0, 0.0]
streamTracer1Display.DataAxesGrid.ZTitleColor = [0.0, 0.0, 0.0]
streamTracer1Display.DataAxesGrid.XLabelColor = [0.0, 0.0, 0.0]
streamTracer1Display.DataAxesGrid.YLabelColor = [0.0, 0.0, 0.0]
streamTracer1Display.DataAxesGrid.ZLabelColor = [0.0, 0.0, 0.0]

# init the 'PolarAxesRepresentation' selected for 'PolarAxes'
streamTracer1Display.PolarAxes.PolarAxisTitleColor = [0.0, 0.0, 0.0]
streamTracer1Display.PolarAxes.PolarAxisLabelColor = [0.0, 0.0, 0.0]
streamTracer1Display.PolarAxes.LastRadialAxisTextColor = [0.0, 0.0, 0.0]
streamTracer1Display.PolarAxes.SecondaryRadialAxesTextColor = [0.0, 0.0, 0.0]

# init the 'PiecewiseFunction' selected for 'ScaleTransferFunction'
streamTracer1Display.ScaleTransferFunction.Points = [0.002180787269026041, 0.0, 0.5, 0.0, 0.01113197486847639, 1.0, 0.5, 0.0]

# init the 'PiecewiseFunction' selected for 'OpacityTransferFunction'
streamTracer1Display.OpacityTransferFunction.Points = [0.002180787269026041, 0.0, 0.5, 0.0, 0.01113197486847639, 1.0, 0.5, 0.0]

# hide data in view
Hide(calculator5, renderView1)

# show color bar/color legend
streamTracer1Display.SetScalarBarVisibility(renderView1, True)

# update the view to ensure updated data information
renderView1.Update()

# update the view to ensure updated data information
renderView2.Update()

# Rescale transfer function
k33LUT.RescaleTransferFunction(-0.0148267531767, 0.0598306194397)

# Rescale transfer function
k33PWF.RescaleTransferFunction(-0.0148267531767, 0.0598306194397)

# set scalar coloring
ColorBy(streamTracer1Display, ('POINTS', 'U', 'Z'))

# Hide the scalar bar for this color map if no visible data is colored by it.
HideScalarBarIfNotNeeded(k33LUT, renderView1)

# rescale color and/or opacity maps used to include current data range
streamTracer1Display.RescaleTransferFunctionToDataRange(True, False)

# show color bar/color legend
streamTracer1Display.SetScalarBarVisibility(renderView1, True)

# set scalar coloring
ColorBy(streamTracer1Display, ('POINTS', 'Vorticity', 'Magnitude'))

# Hide the scalar bar for this color map if no visible data is colored by it.
HideScalarBarIfNotNeeded(uLUT, renderView1)

# rescale color and/or opacity maps used to include current data range
streamTracer1Display.RescaleTransferFunctionToDataRange(True, False)

# show color bar/color legend
streamTracer1Display.SetScalarBarVisibility(renderView1, True)

# get color transfer function/color map for 'Vorticity'
vorticityLUT = GetColorTransferFunction('Vorticity')

# hide color bar/color legend
streamTracer1Display.SetScalarBarVisibility(renderView1, False)

# toggle 3D widget visibility (only when running from the GUI)
Hide3DWidgets(proxy=streamTracer1.SeedType)

# set active source
SetActiveSource(calculator5)

# create a new 'Stream Tracer'
streamTracer2 = StreamTracer(Input=calculator5,
    SeedType='High Resolution Line Source')
streamTracer2.Vectors = ['POINTS', 'grad_p*']
streamTracer2.MaximumStreamlineLength = 0.9199999794363976

# init the 'High Resolution Line Source' selected for 'SeedType'
streamTracer2.SeedType.Point1 = [0.03999999910593033, 0.0, 0.03999999910593033]
streamTracer2.SeedType.Point2 = [0.9599999785423279, 0.07999999821186066, 0.2800000011920929]

# toggle 3D widget visibility (only when running from the GUI)
Hide3DWidgets(proxy=streamTracer2.SeedType)

# Properties modified on streamTracer2.SeedType
streamTracer2.SeedType.Point1 = [0.96, 0.0, 0.03999999910593033]
streamTracer2.SeedType.Point2 = [0.04, 0.07999999821186066, 0.2800000011920929]
streamTracer2.SeedType.Resolution = 100

# Properties modified on streamTracer2.SeedType
streamTracer2.SeedType.Point1 = [0.96, 0.0, 0.03999999910593033]
streamTracer2.SeedType.Point2 = [0.04, 0.07999999821186066, 0.2800000011920929]
streamTracer2.SeedType.Resolution = 100

# show data in view
streamTracer2Display = Show(streamTracer2, renderView1)
# trace defaults for the display properties.
streamTracer2Display.Representation = 'Surface'
streamTracer2Display.ColorArrayName = ['POINTS', 'K33*']
streamTracer2Display.LookupTable = k33LUT
streamTracer2Display.OSPRayScaleArray = 'K33*'
streamTracer2Display.OSPRayScaleFunction = 'PiecewiseFunction'
streamTracer2Display.SelectOrientationVectors = 'Normals'
streamTracer2Display.ScaleFactor = 0.09194389805197717
streamTracer2Display.SelectScaleArray = 'K33*'
streamTracer2Display.GlyphType = 'Arrow'
streamTracer2Display.GlyphTableIndexArray = 'K33*'
streamTracer2Display.DataAxesGrid = 'GridAxesRepresentation'
streamTracer2Display.PolarAxes = 'PolarAxesRepresentation'
streamTracer2Display.GaussianRadius = 0.045971949025988584
streamTracer2Display.SetScaleArray = ['POINTS', 'K33*']
streamTracer2Display.ScaleTransferFunction = 'PiecewiseFunction'
streamTracer2Display.OpacityArray = ['POINTS', 'K33*']
streamTracer2Display.OpacityTransferFunction = 'PiecewiseFunction'

# init the 'PiecewiseFunction' selected for 'OSPRayScaleFunction'
streamTracer2Display.OSPRayScaleFunction.Points = [0.002180787269026041, 0.0, 0.5, 0.0, 0.01113197486847639, 1.0, 0.5, 0.0]

# init the 'GridAxesRepresentation' selected for 'DataAxesGrid'
streamTracer2Display.DataAxesGrid.XTitleColor = [0.0, 0.0, 0.0]
streamTracer2Display.DataAxesGrid.YTitleColor = [0.0, 0.0, 0.0]
streamTracer2Display.DataAxesGrid.ZTitleColor = [0.0, 0.0, 0.0]
streamTracer2Display.DataAxesGrid.XLabelColor = [0.0, 0.0, 0.0]
streamTracer2Display.DataAxesGrid.YLabelColor = [0.0, 0.0, 0.0]
streamTracer2Display.DataAxesGrid.ZLabelColor = [0.0, 0.0, 0.0]

# init the 'PolarAxesRepresentation' selected for 'PolarAxes'
streamTracer2Display.PolarAxes.PolarAxisTitleColor = [0.0, 0.0, 0.0]
streamTracer2Display.PolarAxes.PolarAxisLabelColor = [0.0, 0.0, 0.0]
streamTracer2Display.PolarAxes.LastRadialAxisTextColor = [0.0, 0.0, 0.0]
streamTracer2Display.PolarAxes.SecondaryRadialAxesTextColor = [0.0, 0.0, 0.0]

# init the 'PiecewiseFunction' selected for 'ScaleTransferFunction'
streamTracer2Display.ScaleTransferFunction.Points = [0.002180787269026041, 0.0, 0.5, 0.0, 0.01113197486847639, 1.0, 0.5, 0.0]

# init the 'PiecewiseFunction' selected for 'OpacityTransferFunction'
streamTracer2Display.OpacityTransferFunction.Points = [0.002180787269026041, 0.0, 0.5, 0.0, 0.01113197486847639, 1.0, 0.5, 0.0]

# hide data in view
Hide(calculator5, renderView1)

# show color bar/color legend
streamTracer2Display.SetScalarBarVisibility(renderView1, True)

# update the view to ensure updated data information
renderView1.Update()

# set scalar coloring
ColorBy(streamTracer2Display, ('POINTS', 'Vorticity', 'Magnitude'))

# Hide the scalar bar for this color map if no visible data is colored by it.
HideScalarBarIfNotNeeded(k33LUT, renderView1)

# rescale color and/or opacity maps used to include current data range
streamTracer2Display.RescaleTransferFunctionToDataRange(True, False)

# show color bar/color legend
streamTracer2Display.SetScalarBarVisibility(renderView1, True)

# hide color bar/color legend
streamTracer2Display.SetScalarBarVisibility(renderView1, False)

# toggle 3D widget visibility (only when running from the GUI)
Show3DWidgets(proxy=streamTracer2.SeedType)

# Properties modified on streamTracer2
streamTracer2.SeedType = 'Point Source'

# update the view to ensure updated data information
renderView1.Update()

# Rescale transfer function
vorticityLUT.RescaleTransferFunction(1.87485938495e-06, 0.141643948134)

# get opacity transfer function/opacity map for 'Vorticity'
vorticityPWF = GetOpacityTransferFunction('Vorticity')

# Rescale transfer function
vorticityPWF.RescaleTransferFunction(1.87485938495e-06, 0.141643948134)

# toggle 3D widget visibility (only when running from the GUI)
Hide3DWidgets(proxy=streamTracer2.SeedType)

# toggle 3D widget visibility (only when running from the GUI)
Show3DWidgets(proxy=streamTracer2.SeedType)

# Properties modified on streamTracer2.SeedType
streamTracer2.SeedType.Center = [0.06, 0.03999999910593033, 0.2]

# Properties modified on streamTracer2.SeedType
streamTracer2.SeedType.Center = [0.06, 0.03999999910593033, 0.2]

# update the view to ensure updated data information
renderView1.Update()

# toggle 3D widget visibility (only when running from the GUI)
Hide3DWidgets(proxy=streamTracer2.SeedType)

# toggle 3D widget visibility (only when running from the GUI)
Show3DWidgets(proxy=streamTracer2.SeedType)

# Properties modified on streamTracer2.SeedType
streamTracer2.SeedType.Point1 = [0.14, 0.0, 0.03999999910593033]

# Properties modified on streamTracer2
streamTracer2.SeedType = 'High Resolution Line Source'

# Properties modified on streamTracer2.SeedType
streamTracer2.SeedType.Point1 = [0.14, 0.0, 0.03999999910593033]

# update the view to ensure updated data information
renderView1.Update()

# Properties modified on streamTracer2.SeedType
streamTracer2.SeedType.Resolution = 50

# Properties modified on streamTracer2.SeedType
streamTracer2.SeedType.Resolution = 50

# update the view to ensure updated data information
renderView1.Update()

# create a new 'Stream Tracer'
streamTracer3 = StreamTracer(Input=streamTracer2,
    SeedType='High Resolution Line Source')
streamTracer3.Vectors = ['POINTS', 'Normals']
streamTracer3.MaximumStreamlineLength = 0.24000000208616257

# init the 'High Resolution Line Source' selected for 'SeedType'
streamTracer3.SeedType.Point1 = [0.03999999910593033, 0.0, 0.03999999910593033]
streamTracer3.SeedType.Point2 = [0.20364375412464142, 0.07999999821186066, 0.2800000011920929]

# Properties modified on streamTracer3.SeedType
streamTracer3.SeedType.Point1 = [0.96, 0.0, 0.03999999910593033]
streamTracer3.SeedType.Point2 = [0.5, 0.07999999821186066, 0.2800000011920929]
streamTracer3.SeedType.Resolution = 100

# Properties modified on streamTracer3.SeedType
streamTracer3.SeedType.Point1 = [0.96, 0.0, 0.03999999910593033]
streamTracer3.SeedType.Point2 = [0.5, 0.07999999821186066, 0.2800000011920929]
streamTracer3.SeedType.Resolution = 100

# show data in view
streamTracer3Display = Show(streamTracer3, renderView1)
# trace defaults for the display properties.
streamTracer3Display.Representation = 'Surface'
streamTracer3Display.ColorArrayName = [None, '']
streamTracer3Display.OSPRayScaleFunction = 'PiecewiseFunction'
streamTracer3Display.SelectOrientationVectors = 'None'
streamTracer3Display.ScaleFactor = -2.0000000000000002e+298
streamTracer3Display.SelectScaleArray = 'None'
streamTracer3Display.GlyphType = 'Arrow'
streamTracer3Display.GlyphTableIndexArray = 'None'
streamTracer3Display.DataAxesGrid = 'GridAxesRepresentation'
streamTracer3Display.PolarAxes = 'PolarAxesRepresentation'
streamTracer3Display.GaussianRadius = -1.0000000000000001e+298
streamTracer3Display.SetScaleArray = [None, '']
streamTracer3Display.ScaleTransferFunction = 'PiecewiseFunction'
streamTracer3Display.OpacityArray = [None, '']
streamTracer3Display.OpacityTransferFunction = 'PiecewiseFunction'

# init the 'PiecewiseFunction' selected for 'OSPRayScaleFunction'
streamTracer3Display.OSPRayScaleFunction.Points = [0.002180787269026041, 0.0, 0.5, 0.0, 0.01113197486847639, 1.0, 0.5, 0.0]

# init the 'GridAxesRepresentation' selected for 'DataAxesGrid'
streamTracer3Display.DataAxesGrid.XTitleColor = [0.0, 0.0, 0.0]
streamTracer3Display.DataAxesGrid.YTitleColor = [0.0, 0.0, 0.0]
streamTracer3Display.DataAxesGrid.ZTitleColor = [0.0, 0.0, 0.0]
streamTracer3Display.DataAxesGrid.XLabelColor = [0.0, 0.0, 0.0]
streamTracer3Display.DataAxesGrid.YLabelColor = [0.0, 0.0, 0.0]
streamTracer3Display.DataAxesGrid.ZLabelColor = [0.0, 0.0, 0.0]

# init the 'PolarAxesRepresentation' selected for 'PolarAxes'
streamTracer3Display.PolarAxes.PolarAxisTitleColor = [0.0, 0.0, 0.0]
streamTracer3Display.PolarAxes.PolarAxisLabelColor = [0.0, 0.0, 0.0]
streamTracer3Display.PolarAxes.LastRadialAxisTextColor = [0.0, 0.0, 0.0]
streamTracer3Display.PolarAxes.SecondaryRadialAxesTextColor = [0.0, 0.0, 0.0]

# init the 'PiecewiseFunction' selected for 'ScaleTransferFunction'
streamTracer3Display.ScaleTransferFunction.Points = [0.002180787269026041, 0.0, 0.5, 0.0, 0.01113197486847639, 1.0, 0.5, 0.0]

# init the 'PiecewiseFunction' selected for 'OpacityTransferFunction'
streamTracer3Display.OpacityTransferFunction.Points = [0.002180787269026041, 0.0, 0.5, 0.0, 0.01113197486847639, 1.0, 0.5, 0.0]

# hide data in view
Hide(streamTracer2, renderView1)

# update the view to ensure updated data information
renderView1.Update()

# set active source
SetActiveSource(streamTracer2)

# show data in view
streamTracer2Display = Show(streamTracer2, renderView1)

# show color bar/color legend
streamTracer2Display.SetScalarBarVisibility(renderView1, True)

# set active source
SetActiveSource(streamTracer3)

# Properties modified on streamTracer3.SeedType
streamTracer3.SeedType.Point1 = [0.5, 0.03999999910593033, 0.03999999910593033]
streamTracer3.SeedType.Point2 = [0.5, 0.03999999910593033, 0.2800000011920929]

# Properties modified on streamTracer3.SeedType
streamTracer3.SeedType.Point1 = [0.5, 0.03999999910593033, 0.03999999910593033]
streamTracer3.SeedType.Point2 = [0.5, 0.03999999910593033, 0.2800000011920929]

# update the view to ensure updated data information
renderView1.Update()

# Properties modified on streamTracer3.SeedType
streamTracer3.SeedType.Resolution = 1000

# Properties modified on streamTracer3.SeedType
streamTracer3.SeedType.Resolution = 1000

# update the view to ensure updated data information
renderView1.Update()

# set active source
SetActiveSource(streamTracer2)

# hide data in view
Hide(streamTracer3, renderView1)

# show data in view
streamTracer2Display = Show(streamTracer2, renderView1)

# show color bar/color legend
streamTracer2Display.SetScalarBarVisibility(renderView1, True)

# destroy streamTracer3
Delete(streamTracer3)
del streamTracer3

# toggle 3D widget visibility (only when running from the GUI)
Hide3DWidgets(proxy=streamTracer2.SeedType)

# set active source
SetActiveSource(calculator5)

# create a new 'Stream Tracer'
streamTracer3 = StreamTracer(Input=calculator5,
    SeedType='High Resolution Line Source')
streamTracer3.Vectors = ['POINTS', 'grad_p*']
streamTracer3.MaximumStreamlineLength = 0.9199999794363976

# init the 'High Resolution Line Source' selected for 'SeedType'
streamTracer3.SeedType.Point1 = [0.03999999910593033, 0.0, 0.03999999910593033]
streamTracer3.SeedType.Point2 = [0.9599999785423279, 0.07999999821186066, 0.2800000011920929]

# Properties modified on streamTracer3.SeedType
streamTracer3.SeedType.Point1 = [0.96, 0.0, 0.03999999910593033]
streamTracer3.SeedType.Point2 = [0.5, 0.07999999821186066, 0.2800000011920929]
streamTracer3.SeedType.Resolution = 100

# Properties modified on streamTracer3.SeedType
streamTracer3.SeedType.Point1 = [0.96, 0.0, 0.03999999910593033]
streamTracer3.SeedType.Point2 = [0.5, 0.07999999821186066, 0.2800000011920929]
streamTracer3.SeedType.Resolution = 100

# show data in view
streamTracer3Display = Show(streamTracer3, renderView1)
# trace defaults for the display properties.
streamTracer3Display.Representation = 'Surface'
streamTracer3Display.ColorArrayName = ['POINTS', 'K33*']
streamTracer3Display.LookupTable = k33LUT
streamTracer3Display.OSPRayScaleArray = 'K33*'
streamTracer3Display.OSPRayScaleFunction = 'PiecewiseFunction'
streamTracer3Display.SelectOrientationVectors = 'Normals'
streamTracer3Display.ScaleFactor = 0.0771355852484703
streamTracer3Display.SelectScaleArray = 'K33*'
streamTracer3Display.GlyphType = 'Arrow'
streamTracer3Display.GlyphTableIndexArray = 'K33*'
streamTracer3Display.DataAxesGrid = 'GridAxesRepresentation'
streamTracer3Display.PolarAxes = 'PolarAxesRepresentation'
streamTracer3Display.GaussianRadius = 0.03856779262423515
streamTracer3Display.SetScaleArray = ['POINTS', 'K33*']
streamTracer3Display.ScaleTransferFunction = 'PiecewiseFunction'
streamTracer3Display.OpacityArray = ['POINTS', 'K33*']
streamTracer3Display.OpacityTransferFunction = 'PiecewiseFunction'

# init the 'PiecewiseFunction' selected for 'OSPRayScaleFunction'
streamTracer3Display.OSPRayScaleFunction.Points = [0.002180787269026041, 0.0, 0.5, 0.0, 0.01113197486847639, 1.0, 0.5, 0.0]

# init the 'GridAxesRepresentation' selected for 'DataAxesGrid'
streamTracer3Display.DataAxesGrid.XTitleColor = [0.0, 0.0, 0.0]
streamTracer3Display.DataAxesGrid.YTitleColor = [0.0, 0.0, 0.0]
streamTracer3Display.DataAxesGrid.ZTitleColor = [0.0, 0.0, 0.0]
streamTracer3Display.DataAxesGrid.XLabelColor = [0.0, 0.0, 0.0]
streamTracer3Display.DataAxesGrid.YLabelColor = [0.0, 0.0, 0.0]
streamTracer3Display.DataAxesGrid.ZLabelColor = [0.0, 0.0, 0.0]

# init the 'PolarAxesRepresentation' selected for 'PolarAxes'
streamTracer3Display.PolarAxes.PolarAxisTitleColor = [0.0, 0.0, 0.0]
streamTracer3Display.PolarAxes.PolarAxisLabelColor = [0.0, 0.0, 0.0]
streamTracer3Display.PolarAxes.LastRadialAxisTextColor = [0.0, 0.0, 0.0]
streamTracer3Display.PolarAxes.SecondaryRadialAxesTextColor = [0.0, 0.0, 0.0]

# init the 'PiecewiseFunction' selected for 'ScaleTransferFunction'
streamTracer3Display.ScaleTransferFunction.Points = [0.002180787269026041, 0.0, 0.5, 0.0, 0.01113197486847639, 1.0, 0.5, 0.0]

# init the 'PiecewiseFunction' selected for 'OpacityTransferFunction'
streamTracer3Display.OpacityTransferFunction.Points = [0.002180787269026041, 0.0, 0.5, 0.0, 0.01113197486847639, 1.0, 0.5, 0.0]

# hide data in view
Hide(calculator5, renderView1)

# show color bar/color legend
streamTracer3Display.SetScalarBarVisibility(renderView1, True)

# update the view to ensure updated data information
renderView1.Update()

# set scalar coloring
ColorBy(streamTracer3Display, ('POINTS', 'Vorticity', 'Magnitude'))

# Hide the scalar bar for this color map if no visible data is colored by it.
HideScalarBarIfNotNeeded(k33LUT, renderView1)

# rescale color and/or opacity maps used to include current data range
streamTracer3Display.RescaleTransferFunctionToDataRange(True, False)

# show color bar/color legend
streamTracer3Display.SetScalarBarVisibility(renderView1, True)

# hide color bar/color legend
streamTracer3Display.SetScalarBarVisibility(renderView1, False)

# toggle 3D widget visibility (only when running from the GUI)
Hide3DWidgets(proxy=streamTracer3.SeedType)

# Properties modified on streamTracer3.SeedType
streamTracer3.SeedType.Resolution = 50

# Properties modified on streamTracer3.SeedType
streamTracer3.SeedType.Resolution = 50

# update the view to ensure updated data information
renderView1.Update()

# set active source
SetActiveSource(permeability_re100dat)

# set active view
SetActiveView(renderView2)

# set active source
SetActiveSource(calculator3)

# set active source
SetActiveSource(permeability_re100dat)

# create a new 'Calculator'
calculator6 = Calculator(Input=permeability_re100dat)
calculator6.Function = ''

# Properties modified on calculator6
calculator6.ResultArrayName = 'UV'
calculator6.Function = 'U.V'

# show data in view
calculator6Display = Show(calculator6, renderView2)
# trace defaults for the display properties.
calculator6Display.Representation = 'Surface'
calculator6Display.ColorArrayName = ['POINTS', 'K11']
calculator6Display.LookupTable = k11LUT
calculator6Display.OSPRayScaleArray = 'K11'
calculator6Display.OSPRayScaleFunction = 'PiecewiseFunction'
calculator6Display.SelectOrientationVectors = 'K11'
calculator6Display.ScaleFactor = 0.09199999794363976
calculator6Display.SelectScaleArray = 'K11'
calculator6Display.GlyphType = 'Arrow'
calculator6Display.GlyphTableIndexArray = 'K11'
calculator6Display.DataAxesGrid = 'GridAxesRepresentation'
calculator6Display.PolarAxes = 'PolarAxesRepresentation'
calculator6Display.ScalarOpacityFunction = k11PWF
calculator6Display.ScalarOpacityUnitDistance = 0.11590562517402621

# init the 'PiecewiseFunction' selected for 'OSPRayScaleFunction'
calculator6Display.OSPRayScaleFunction.Points = [0.002180787269026041, 0.0, 0.5, 0.0, 0.01113197486847639, 1.0, 0.5, 0.0]

# init the 'GridAxesRepresentation' selected for 'DataAxesGrid'
calculator6Display.DataAxesGrid.XTitleColor = [0.0, 0.0, 0.0]
calculator6Display.DataAxesGrid.YTitleColor = [0.0, 0.0, 0.0]
calculator6Display.DataAxesGrid.ZTitleColor = [0.0, 0.0, 0.0]
calculator6Display.DataAxesGrid.XLabelColor = [0.0, 0.0, 0.0]
calculator6Display.DataAxesGrid.YLabelColor = [0.0, 0.0, 0.0]
calculator6Display.DataAxesGrid.ZLabelColor = [0.0, 0.0, 0.0]

# init the 'PolarAxesRepresentation' selected for 'PolarAxes'
calculator6Display.PolarAxes.PolarAxisTitleColor = [0.0, 0.0, 0.0]
calculator6Display.PolarAxes.PolarAxisLabelColor = [0.0, 0.0, 0.0]
calculator6Display.PolarAxes.LastRadialAxisTextColor = [0.0, 0.0, 0.0]
calculator6Display.PolarAxes.SecondaryRadialAxesTextColor = [0.0, 0.0, 0.0]

# hide data in view
Hide(permeability_re100dat, renderView2)

# show color bar/color legend
calculator6Display.SetScalarBarVisibility(renderView2, True)

# update the view to ensure updated data information
renderView1.Update()

# update the view to ensure updated data information
renderView2.Update()

# set active source
SetActiveSource(permeability_re100dat)

# hide data in view
Hide(calculator6, renderView2)

# show data in view
permeability_re100datDisplay = Show(permeability_re100dat, renderView2)

# show color bar/color legend
permeability_re100datDisplay.SetScalarBarVisibility(renderView2, True)

# destroy calculator6
Delete(calculator6)
del calculator6

# set active source
SetActiveSource(calculator3)

# set active source
SetActiveSource(permeability_re100dat)

# create a new 'Calculator'
calculator6 = Calculator(Input=permeability_re100dat)
calculator6.Function = ''

# Properties modified on calculator6
calculator6.ResultArrayName = 'UV'
calculator6.Function = 'U*iHat +V*jHat'

# show data in view
calculator6Display = Show(calculator6, renderView2)
# trace defaults for the display properties.
calculator6Display.Representation = 'Surface'
calculator6Display.ColorArrayName = ['POINTS', 'K11']
calculator6Display.LookupTable = k11LUT
calculator6Display.OSPRayScaleArray = 'K11'
calculator6Display.OSPRayScaleFunction = 'PiecewiseFunction'
calculator6Display.SelectOrientationVectors = 'UV'
calculator6Display.ScaleFactor = 0.09199999794363976
calculator6Display.SelectScaleArray = 'K11'
calculator6Display.GlyphType = 'Arrow'
calculator6Display.GlyphTableIndexArray = 'K11'
calculator6Display.DataAxesGrid = 'GridAxesRepresentation'
calculator6Display.PolarAxes = 'PolarAxesRepresentation'
calculator6Display.ScalarOpacityFunction = k11PWF
calculator6Display.ScalarOpacityUnitDistance = 0.11590562517402621

# init the 'PiecewiseFunction' selected for 'OSPRayScaleFunction'
calculator6Display.OSPRayScaleFunction.Points = [0.002180787269026041, 0.0, 0.5, 0.0, 0.01113197486847639, 1.0, 0.5, 0.0]

# init the 'GridAxesRepresentation' selected for 'DataAxesGrid'
calculator6Display.DataAxesGrid.XTitleColor = [0.0, 0.0, 0.0]
calculator6Display.DataAxesGrid.YTitleColor = [0.0, 0.0, 0.0]
calculator6Display.DataAxesGrid.ZTitleColor = [0.0, 0.0, 0.0]
calculator6Display.DataAxesGrid.XLabelColor = [0.0, 0.0, 0.0]
calculator6Display.DataAxesGrid.YLabelColor = [0.0, 0.0, 0.0]
calculator6Display.DataAxesGrid.ZLabelColor = [0.0, 0.0, 0.0]

# init the 'PolarAxesRepresentation' selected for 'PolarAxes'
calculator6Display.PolarAxes.PolarAxisTitleColor = [0.0, 0.0, 0.0]
calculator6Display.PolarAxes.PolarAxisLabelColor = [0.0, 0.0, 0.0]
calculator6Display.PolarAxes.LastRadialAxisTextColor = [0.0, 0.0, 0.0]
calculator6Display.PolarAxes.SecondaryRadialAxesTextColor = [0.0, 0.0, 0.0]

# hide data in view
Hide(permeability_re100dat, renderView2)

# show color bar/color legend
calculator6Display.SetScalarBarVisibility(renderView2, True)

# update the view to ensure updated data information
renderView2.Update()

# create a new 'Stream Tracer'
streamTracer4 = StreamTracer(Input=calculator6,
    SeedType='High Resolution Line Source')
streamTracer4.Vectors = ['POINTS', 'UV']
streamTracer4.MaximumStreamlineLength = 0.9199999794363976

# init the 'High Resolution Line Source' selected for 'SeedType'
streamTracer4.SeedType.Point1 = [0.03999999910593033, 0.03999999910593033, 0.0]
streamTracer4.SeedType.Point2 = [0.9599999785423279, 0.2800000011920929, 0.0]

# Properties modified on streamTracer4.SeedType
streamTracer4.SeedType.Resolution = 100

# Properties modified on streamTracer4.SeedType
streamTracer4.SeedType.Resolution = 100

# show data in view
streamTracer4Display = Show(streamTracer4, renderView2)
# trace defaults for the display properties.
streamTracer4Display.Representation = 'Surface'
streamTracer4Display.ColorArrayName = ['POINTS', 'K11']
streamTracer4Display.LookupTable = k11LUT
streamTracer4Display.OSPRayScaleArray = 'AngularVelocity'
streamTracer4Display.OSPRayScaleFunction = 'PiecewiseFunction'
streamTracer4Display.SelectOrientationVectors = 'Normals'
streamTracer4Display.ScaleFactor = 0.09199573025107384
streamTracer4Display.SelectScaleArray = 'AngularVelocity'
streamTracer4Display.GlyphType = 'Arrow'
streamTracer4Display.GlyphTableIndexArray = 'AngularVelocity'
streamTracer4Display.DataAxesGrid = 'GridAxesRepresentation'
streamTracer4Display.PolarAxes = 'PolarAxesRepresentation'
streamTracer4Display.GaussianRadius = 0.04599786512553692
streamTracer4Display.SetScaleArray = ['POINTS', 'AngularVelocity']
streamTracer4Display.ScaleTransferFunction = 'PiecewiseFunction'
streamTracer4Display.OpacityArray = ['POINTS', 'AngularVelocity']
streamTracer4Display.OpacityTransferFunction = 'PiecewiseFunction'

# init the 'PiecewiseFunction' selected for 'OSPRayScaleFunction'
streamTracer4Display.OSPRayScaleFunction.Points = [0.002180787269026041, 0.0, 0.5, 0.0, 0.01113197486847639, 1.0, 0.5, 0.0]

# init the 'GridAxesRepresentation' selected for 'DataAxesGrid'
streamTracer4Display.DataAxesGrid.XTitleColor = [0.0, 0.0, 0.0]
streamTracer4Display.DataAxesGrid.YTitleColor = [0.0, 0.0, 0.0]
streamTracer4Display.DataAxesGrid.ZTitleColor = [0.0, 0.0, 0.0]
streamTracer4Display.DataAxesGrid.XLabelColor = [0.0, 0.0, 0.0]
streamTracer4Display.DataAxesGrid.YLabelColor = [0.0, 0.0, 0.0]
streamTracer4Display.DataAxesGrid.ZLabelColor = [0.0, 0.0, 0.0]

# init the 'PolarAxesRepresentation' selected for 'PolarAxes'
streamTracer4Display.PolarAxes.PolarAxisTitleColor = [0.0, 0.0, 0.0]
streamTracer4Display.PolarAxes.PolarAxisLabelColor = [0.0, 0.0, 0.0]
streamTracer4Display.PolarAxes.LastRadialAxisTextColor = [0.0, 0.0, 0.0]
streamTracer4Display.PolarAxes.SecondaryRadialAxesTextColor = [0.0, 0.0, 0.0]

# init the 'PiecewiseFunction' selected for 'ScaleTransferFunction'
streamTracer4Display.ScaleTransferFunction.Points = [0.002180787269026041, 0.0, 0.5, 0.0, 0.01113197486847639, 1.0, 0.5, 0.0]

# init the 'PiecewiseFunction' selected for 'OpacityTransferFunction'
streamTracer4Display.OpacityTransferFunction.Points = [0.002180787269026041, 0.0, 0.5, 0.0, 0.01113197486847639, 1.0, 0.5, 0.0]

# hide data in view
Hide(calculator6, renderView2)

# show color bar/color legend
streamTracer4Display.SetScalarBarVisibility(renderView2, True)

# update the view to ensure updated data information
renderView2.Update()

# hide data in view
Hide(calculator3, renderView2)

# set scalar coloring
ColorBy(streamTracer4Display, ('POINTS', 'Vorticity', 'Magnitude'))

# Hide the scalar bar for this color map if no visible data is colored by it.
HideScalarBarIfNotNeeded(k11LUT, renderView2)

# rescale color and/or opacity maps used to include current data range
streamTracer4Display.RescaleTransferFunctionToDataRange(True, False)

# show color bar/color legend
streamTracer4Display.SetScalarBarVisibility(renderView2, True)

# hide color bar/color legend
streamTracer4Display.SetScalarBarVisibility(renderView2, False)

# toggle 3D widget visibility (only when running from the GUI)
Hide3DWidgets(proxy=streamTracer4.SeedType)

# set active source
SetActiveSource(calculator6)

# create a new 'Stream Tracer'
streamTracer5 = StreamTracer(Input=calculator6,
    SeedType='High Resolution Line Source')
streamTracer5.Vectors = ['POINTS', 'UV']
streamTracer5.MaximumStreamlineLength = 0.9199999794363976

# init the 'High Resolution Line Source' selected for 'SeedType'
streamTracer5.SeedType.Point1 = [0.03999999910593033, 0.03999999910593033, 0.0]
streamTracer5.SeedType.Point2 = [0.9599999785423279, 0.2800000011920929, 0.0]

# set active source
SetActiveSource(streamTracer2)

# set active source
SetActiveSource(streamTracer5)

# toggle 3D widget visibility (only when running from the GUI)
Hide3DWidgets(proxy=streamTracer5.SeedType)

# Properties modified on streamTracer5.SeedType
streamTracer5.SeedType.Point1 = [0.14, 0.03999999910593033, 0.0]
streamTracer5.SeedType.Point2 = [0.04, 0.2800000011920929, 0.0]
streamTracer5.SeedType.Resolution = 50

# Properties modified on streamTracer5.SeedType
streamTracer5.SeedType.Point1 = [0.14, 0.03999999910593033, 0.0]
streamTracer5.SeedType.Point2 = [0.04, 0.2800000011920929, 0.0]
streamTracer5.SeedType.Resolution = 50

# show data in view
streamTracer5Display = Show(streamTracer5, renderView2)
# trace defaults for the display properties.
streamTracer5Display.Representation = 'Surface'
streamTracer5Display.ColorArrayName = ['POINTS', 'K11']
streamTracer5Display.LookupTable = k11LUT
streamTracer5Display.OSPRayScaleArray = 'AngularVelocity'
streamTracer5Display.OSPRayScaleFunction = 'PiecewiseFunction'
streamTracer5Display.SelectOrientationVectors = 'Normals'
streamTracer5Display.ScaleFactor = 0.024000000208616257
streamTracer5Display.SelectScaleArray = 'AngularVelocity'
streamTracer5Display.GlyphType = 'Arrow'
streamTracer5Display.GlyphTableIndexArray = 'AngularVelocity'
streamTracer5Display.DataAxesGrid = 'GridAxesRepresentation'
streamTracer5Display.PolarAxes = 'PolarAxesRepresentation'
streamTracer5Display.GaussianRadius = 0.012000000104308128
streamTracer5Display.SetScaleArray = ['POINTS', 'AngularVelocity']
streamTracer5Display.ScaleTransferFunction = 'PiecewiseFunction'
streamTracer5Display.OpacityArray = ['POINTS', 'AngularVelocity']
streamTracer5Display.OpacityTransferFunction = 'PiecewiseFunction'

# init the 'PiecewiseFunction' selected for 'OSPRayScaleFunction'
streamTracer5Display.OSPRayScaleFunction.Points = [0.002180787269026041, 0.0, 0.5, 0.0, 0.01113197486847639, 1.0, 0.5, 0.0]

# init the 'GridAxesRepresentation' selected for 'DataAxesGrid'
streamTracer5Display.DataAxesGrid.XTitleColor = [0.0, 0.0, 0.0]
streamTracer5Display.DataAxesGrid.YTitleColor = [0.0, 0.0, 0.0]
streamTracer5Display.DataAxesGrid.ZTitleColor = [0.0, 0.0, 0.0]
streamTracer5Display.DataAxesGrid.XLabelColor = [0.0, 0.0, 0.0]
streamTracer5Display.DataAxesGrid.YLabelColor = [0.0, 0.0, 0.0]
streamTracer5Display.DataAxesGrid.ZLabelColor = [0.0, 0.0, 0.0]

# init the 'PolarAxesRepresentation' selected for 'PolarAxes'
streamTracer5Display.PolarAxes.PolarAxisTitleColor = [0.0, 0.0, 0.0]
streamTracer5Display.PolarAxes.PolarAxisLabelColor = [0.0, 0.0, 0.0]
streamTracer5Display.PolarAxes.LastRadialAxisTextColor = [0.0, 0.0, 0.0]
streamTracer5Display.PolarAxes.SecondaryRadialAxesTextColor = [0.0, 0.0, 0.0]

# init the 'PiecewiseFunction' selected for 'ScaleTransferFunction'
streamTracer5Display.ScaleTransferFunction.Points = [0.002180787269026041, 0.0, 0.5, 0.0, 0.01113197486847639, 1.0, 0.5, 0.0]

# init the 'PiecewiseFunction' selected for 'OpacityTransferFunction'
streamTracer5Display.OpacityTransferFunction.Points = [0.002180787269026041, 0.0, 0.5, 0.0, 0.01113197486847639, 1.0, 0.5, 0.0]

# hide data in view
Hide(calculator6, renderView2)

# show color bar/color legend
streamTracer5Display.SetScalarBarVisibility(renderView2, True)

# update the view to ensure updated data information
renderView1.Update()

# update the view to ensure updated data information
renderView2.Update()

# hide color bar/color legend
streamTracer5Display.SetScalarBarVisibility(renderView2, False)

# set scalar coloring
ColorBy(streamTracer5Display, ('POINTS', 'Vorticity', 'Magnitude'))

# Hide the scalar bar for this color map if no visible data is colored by it.
HideScalarBarIfNotNeeded(k11LUT, renderView2)

# rescale color and/or opacity maps used to include current data range
streamTracer5Display.RescaleTransferFunctionToDataRange(True, False)

# show color bar/color legend
streamTracer5Display.SetScalarBarVisibility(renderView2, True)

# hide color bar/color legend
streamTracer5Display.SetScalarBarVisibility(renderView2, False)

# set active source
SetActiveSource(streamTracer3)

# set active source
SetActiveSource(calculator6)

# create a new 'Stream Tracer'
streamTracer6 = StreamTracer(Input=calculator6,
    SeedType='High Resolution Line Source')
streamTracer6.Vectors = ['POINTS', 'UV']
streamTracer6.MaximumStreamlineLength = 0.9199999794363976

# init the 'High Resolution Line Source' selected for 'SeedType'
streamTracer6.SeedType.Point1 = [0.03999999910593033, 0.03999999910593033, 0.0]
streamTracer6.SeedType.Point2 = [0.9599999785423279, 0.2800000011920929, 0.0]

# toggle 3D widget visibility (only when running from the GUI)
Hide3DWidgets(proxy=streamTracer6.SeedType)

# Properties modified on streamTracer6.SeedType
streamTracer6.SeedType.Point1 = [0.96, 0.03999999910593033, 0.0]
streamTracer6.SeedType.Point2 = [0.5, 0.2800000011920929, 0.0]
streamTracer6.SeedType.Resolution = 50

# Properties modified on streamTracer6.SeedType
streamTracer6.SeedType.Point1 = [0.96, 0.03999999910593033, 0.0]
streamTracer6.SeedType.Point2 = [0.5, 0.2800000011920929, 0.0]
streamTracer6.SeedType.Resolution = 50

# show data in view
streamTracer6Display = Show(streamTracer6, renderView2)
# trace defaults for the display properties.
streamTracer6Display.Representation = 'Surface'
streamTracer6Display.ColorArrayName = ['POINTS', 'K11']
streamTracer6Display.LookupTable = k11LUT
streamTracer6Display.OSPRayScaleArray = 'AngularVelocity'
streamTracer6Display.OSPRayScaleFunction = 'PiecewiseFunction'
streamTracer6Display.SelectOrientationVectors = 'Normals'
streamTracer6Display.ScaleFactor = 0.06874738931655884
streamTracer6Display.SelectScaleArray = 'AngularVelocity'
streamTracer6Display.GlyphType = 'Arrow'
streamTracer6Display.GlyphTableIndexArray = 'AngularVelocity'
streamTracer6Display.DataAxesGrid = 'GridAxesRepresentation'
streamTracer6Display.PolarAxes = 'PolarAxesRepresentation'
streamTracer6Display.GaussianRadius = 0.03437369465827942
streamTracer6Display.SetScaleArray = ['POINTS', 'AngularVelocity']
streamTracer6Display.ScaleTransferFunction = 'PiecewiseFunction'
streamTracer6Display.OpacityArray = ['POINTS', 'AngularVelocity']
streamTracer6Display.OpacityTransferFunction = 'PiecewiseFunction'

# init the 'PiecewiseFunction' selected for 'OSPRayScaleFunction'
streamTracer6Display.OSPRayScaleFunction.Points = [0.002180787269026041, 0.0, 0.5, 0.0, 0.01113197486847639, 1.0, 0.5, 0.0]

# init the 'GridAxesRepresentation' selected for 'DataAxesGrid'
streamTracer6Display.DataAxesGrid.XTitleColor = [0.0, 0.0, 0.0]
streamTracer6Display.DataAxesGrid.YTitleColor = [0.0, 0.0, 0.0]
streamTracer6Display.DataAxesGrid.ZTitleColor = [0.0, 0.0, 0.0]
streamTracer6Display.DataAxesGrid.XLabelColor = [0.0, 0.0, 0.0]
streamTracer6Display.DataAxesGrid.YLabelColor = [0.0, 0.0, 0.0]
streamTracer6Display.DataAxesGrid.ZLabelColor = [0.0, 0.0, 0.0]

# init the 'PolarAxesRepresentation' selected for 'PolarAxes'
streamTracer6Display.PolarAxes.PolarAxisTitleColor = [0.0, 0.0, 0.0]
streamTracer6Display.PolarAxes.PolarAxisLabelColor = [0.0, 0.0, 0.0]
streamTracer6Display.PolarAxes.LastRadialAxisTextColor = [0.0, 0.0, 0.0]
streamTracer6Display.PolarAxes.SecondaryRadialAxesTextColor = [0.0, 0.0, 0.0]

# init the 'PiecewiseFunction' selected for 'ScaleTransferFunction'
streamTracer6Display.ScaleTransferFunction.Points = [0.002180787269026041, 0.0, 0.5, 0.0, 0.01113197486847639, 1.0, 0.5, 0.0]

# init the 'PiecewiseFunction' selected for 'OpacityTransferFunction'
streamTracer6Display.OpacityTransferFunction.Points = [0.002180787269026041, 0.0, 0.5, 0.0, 0.01113197486847639, 1.0, 0.5, 0.0]

# hide data in view
Hide(calculator6, renderView2)

# show color bar/color legend
streamTracer6Display.SetScalarBarVisibility(renderView2, True)

# update the view to ensure updated data information
renderView2.Update()

# set scalar coloring
ColorBy(streamTracer6Display, ('POINTS', 'Vorticity', 'Magnitude'))

# Hide the scalar bar for this color map if no visible data is colored by it.
HideScalarBarIfNotNeeded(k11LUT, renderView2)

# rescale color and/or opacity maps used to include current data range
streamTracer6Display.RescaleTransferFunctionToDataRange(True, False)

# show color bar/color legend
streamTracer6Display.SetScalarBarVisibility(renderView2, True)

# hide color bar/color legend
streamTracer6Display.SetScalarBarVisibility(renderView2, False)

# set active view
SetActiveView(renderView1)

# set active source
SetActiveSource(streamTracer1)

# Hide the scalar bar for this color map if no visible data is colored by it.
HideScalarBarIfNotNeeded(vorticityLUT, renderView1)

# set scalar coloring
ColorBy(streamTracer1Display, ('POINTS', 'K', 'Magnitude'))

# rescale color and/or opacity maps used to include current data range
streamTracer1Display.RescaleTransferFunctionToDataRange(True, False)

# show color bar/color legend
streamTracer1Display.SetScalarBarVisibility(renderView1, True)

# get color transfer function/color map for 'K'
kLUT = GetColorTransferFunction('K')

# set scalar coloring
ColorBy(streamTracer1Display, ('POINTS', 'K11*'))

# Hide the scalar bar for this color map if no visible data is colored by it.
HideScalarBarIfNotNeeded(kLUT, renderView1)

# rescale color and/or opacity maps used to include current data range
streamTracer1Display.RescaleTransferFunctionToDataRange(True, False)

# show color bar/color legend
streamTracer1Display.SetScalarBarVisibility(renderView1, True)

# set scalar coloring
ColorBy(streamTracer1Display, ('POINTS', 'K33*'))

# Hide the scalar bar for this color map if no visible data is colored by it.
HideScalarBarIfNotNeeded(k11LUT, renderView1)

# rescale color and/or opacity maps used to include current data range
streamTracer1Display.RescaleTransferFunctionToDataRange(True, False)

# show color bar/color legend
streamTracer1Display.SetScalarBarVisibility(renderView1, True)

# set scalar coloring
ColorBy(streamTracer1Display, ('POINTS', 'p'))

# Hide the scalar bar for this color map if no visible data is colored by it.
HideScalarBarIfNotNeeded(k33LUT, renderView1)

# rescale color and/or opacity maps used to include current data range
streamTracer1Display.RescaleTransferFunctionToDataRange(True, False)

# show color bar/color legend
streamTracer1Display.SetScalarBarVisibility(renderView1, True)

# set scalar coloring
ColorBy(streamTracer1Display, ('POINTS', 'Vorticity', 'Magnitude'))

# Hide the scalar bar for this color map if no visible data is colored by it.
HideScalarBarIfNotNeeded(pLUT, renderView1)

# rescale color and/or opacity maps used to include current data range
streamTracer1Display.RescaleTransferFunctionToDataRange(True, False)

# show color bar/color legend
streamTracer1Display.SetScalarBarVisibility(renderView1, True)

# hide color bar/color legend
streamTracer1Display.SetScalarBarVisibility(renderView1, False)

# Apply a preset using its name. Note this may not work as expected when presets have duplicate names.
vorticityLUT.ApplyPreset('X Ray', True)

# Apply a preset using its name. Note this may not work as expected when presets have duplicate names.
vorticityLUT.ApplyPreset('Viridis (matplotlib)', True)

# current camera placement for renderView1
renderView1.CameraPosition = [0.6352510417969459, -1.0004801010976068, 0.1600000001490116]
renderView1.CameraFocalPoint = [0.6352510417969459, 0.03999999910593033, 0.1600000001490116]
renderView1.CameraViewUp = [0.0, 0.0, 1.0]
renderView1.CameraParallelScale = 0.4770744079486521

# current camera placement for renderView2
renderView2.InteractionMode = '2D'
renderView2.CameraPosition = [0.6269341371227006, 0.13615114551114785, 1.8367835453775365]
renderView2.CameraFocalPoint = [0.6269341371227006, 0.13615114551114785, 0.0]
renderView2.CameraParallelScale = 0.26834783745783314

# save screenshot
SaveScreenshot('/mnt/bighome/nluminar/macromodel/zampogna_cavity_1000/stream.png', layout1, SaveAllViews=1,
    ImageResolution=[1456, 930])

#### saving camera placements for all active views

# current camera placement for renderView1
renderView1.CameraPosition = [0.6352510417969459, -1.0004801010976068, 0.1600000001490116]
renderView1.CameraFocalPoint = [0.6352510417969459, 0.03999999910593033, 0.1600000001490116]
renderView1.CameraViewUp = [0.0, 0.0, 1.0]
renderView1.CameraParallelScale = 0.4770744079486521

# current camera placement for renderView2
renderView2.InteractionMode = '2D'
renderView2.CameraPosition = [0.6269341371227006, 0.13615114551114785, 1.8367835453775365]
renderView2.CameraFocalPoint = [0.6269341371227006, 0.13615114551114785, 0.0]
renderView2.CameraParallelScale = 0.26834783745783314

#### uncomment the following to render all views
# RenderAllViews()
# alternatively, if you want to write images, you can use SaveScreenshot(...).

# 
#  This file is part of Herschel Common Science System (HCSS).
#  Copyright 2001-2011 Herschel Science Ground Segment Consortium
# 
#  HCSS is free software: you can redistribute it and/or modify
#  it under the terms of the GNU Lesser General Public License as
#  published by the Free Software Foundation, either version 3 of
#  the License, or (at your option) any later version.
# 
#  HCSS is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
#  GNU Lesser General Public License for more details.
# 
#  You should have received a copy of the GNU Lesser General
#  Public License along with HCSS.
#  If not, see <http://www.gnu.org/licenses/>.
# 


"""

this is the calling script for the automatic spectroscopy pipeline. 
      It calls and runs the ipipe/spec scripts that also can be run interactively.
      Especially, for the level2 generation this script might be helpful for the 
      general user in case that there are more than one spectral line. 
<br>
AUTHOR
   Juergen Schreiber <schreiber@mpia.de>, Jeroen de jong <jdejong@mpe.mpg.de>
<br>
WARNING: <br>
   Do not edit this file! This is the reference copy for your current 
   installation of HIPE. We recommend you first copy it to a different  
   location before editing.
<br>

"""

from java.util.logging import Logger, Level

# Select the ipipe scripts based on the observation mode
from herschel.pacs.spg.pipeline   import SelectPacsPipeline
from herschel.pacs.signal         import SlicedFrames
from herschel.pacs.signal.context import PacsContext
from herschel.pacs.spg.common     import PacsPropagateMetaKeywordsTask
from herschel.pacs.spg.pipeline.ProductSinkHandling import *
from herschel.pacs.spg.pipeline.spg_spec_tools import *
from herschel.ia.pal              import *
from herschel.pacs.cal import *
from herschel.pacs.cal import GetPacsCalDataTask
from herschel.ia.obs import ObservationContext
from herschel.ia.numeric.toolbox.basic import *
from herschel.pacs.spg.common.util import PacsProcessingExceptionHandler
from java.lang import Throwable

_logger = Logger.getLogger("pacsspectro_pipeline")

# Cameras to reduce
try:
    cameraList
except NameError:
    cameraList = ['red','blue']

# Check that we have data for all camera's
for camera in list(cameraList):
    if obs.level0.getCamera(camera).available == False:
        _logger.warning("There is no level 0 data for camera: "+camera)
        cameraList.remove(camera)

maxErrors = len(cameraList)
if maxErrors == 0:
    raise Exception("No data available in ObservationContext")

# get the calibration tree
calTree = obs.calibration

#SPR 1552 FOR ESAC PIPELINE 
GetPacsCalDataTask.setDefaultCalTree(calTree)

# selects the pipeline scripts
selector = SelectPacsPipeline(obs,True)

# reduce from level 0 to level 2 for red and blue array
exceptionHandler = PacsProcessingExceptionHandler(obs,maxErrors)
for camera in cameraList:
    try:
        exec(selector.level05Script)
    except Throwable, e:
        exceptionHandler.handle("camera "+camera,e)
    saveToProductSink(obs)
    
#obs.setObsState(ObservationContext.OBS_STATE_LEVEL0_5_PROCESSED)
#add trend analysis product to ObservationContext
addTrendProducts(obs)

maxErrors = 0
for camera in cameraList:
    if obs.level0_5.fitted.getCamera(camera).available:
       maxErrors += 1

exceptionHandler = PacsProcessingExceptionHandler(obs,maxErrors)
for camera in cameraList:
    if obs.level0_5.fitted.getCamera(camera).available:
        try:
            exec(selector.level1Script)
        except Throwable, e:
            exceptionHandler.handle("camera "+camera,e)
        saveToProductSink(obs)
    else:
        _logger.warning("There is no "+camera+" Frames in the level 0.5 context!")

obs.setObsState(ObservationContext.OBS_STATE_LEVEL1_PROCESSED)

level1 = PacsContext(obs.level1)

maxErrors = 0
for camera in cameraList:
    if obs.level1.cube.getCamera(camera).available:
       maxErrors += 1

exceptionHandler = PacsProcessingExceptionHandler(obs,maxErrors)
for camera in cameraList:
    if level1.cube.getCamera(camera).available:
        try:
            exec(selector.level2Script)
        except Throwable, e:
            exceptionHandler.handle("camera "+camera,e)
        saveToProductSink(obs)            
    else:
        _logger.warning("There is no "+camera+" PacsCube in the level 1 context!")


# copy average RA/Dec to level-2 and observation context
if obs.level2 != None:
    # extractRaDecToObs(obs)
    print "Set Spectrometer Pipeline Level 2"
    obs.setObsState(ObservationContext.OBS_STATE_LEVEL2_PROCESSED)


# obs.setObsState(ObservationContext.OBS_STATE_LEVEL2_PROCESSED)

# restore old sink state 
restoreOldSinkState()

del calTree, selector, level1, exceptionHandler, _logger, maxErrors, camera
del sink, currentIsUsedState
del LOGGER, sliceSaveMode
try:
    del e
except:
    pass

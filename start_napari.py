import numpy as np

import napari
from napari_train_cellpose import AnnotateWidget

# create a Viewer and add an image here

viewer = napari.view_image(np.random.random((100, 100)))

# create our widget, passing in the viewer
my_widget = AnnotateWidget(viewer)

my_widget.path_ann_project_widg.value = "/Users/alberto-mac/EMBL_ATeam/projects/napari-train-cellpose/sample-proj-dirs/napari-train-cellpose/test2"

viewer.window.add_dock_widget(my_widget, area='right',
                                              name="ROI labeling")

# viewer = napari.view_image(np.random.random((100, 100)))

# custom code to add data here
# viewer.add_points(my_points_data)

# start the event loop and show the viewer
napari.run()

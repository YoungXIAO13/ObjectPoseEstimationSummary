import os, sys
import bpy
from mathutils import Matrix, Vector


# Create directory if not existed
def create_dir(dir):
    if not os.path.isdir(dir):
        os.makedirs(dir)


# Compute the calibration matrix K of camera
def get_calibration_matrix_K_from_blender(camd):
    f_in_mm = camd.lens
    scene = bpy.context.scene
    resolution_x_in_px = scene.render.resolution_x
    resolution_y_in_px = scene.render.resolution_y
    scale = scene.render.resolution_percentage / 100
    sensor_width_in_mm = camd.sensor_width
    sensor_height_in_mm = camd.sensor_height
    pixel_aspect_ratio = scene.render.pixel_aspect_x / scene.render.pixel_aspect_y
    if (camd.sensor_fit == 'VERTICAL'):
        # the sensor height is fixed (sensor fit is horizontal), the sensor width is effectively changed with the pixel aspect ratio
        s_u = resolution_x_in_px * scale / sensor_width_in_mm / pixel_aspect_ratio
        s_v = resolution_y_in_px * scale / sensor_height_in_mm
    else: # 'HORIZONTAL' and 'AUTO'
        # the sensor width is fixed (sensor fit is horizontal),
        # the sensor height is effectively changed with the pixel aspect ratio
        pixel_aspect_ratio = scene.render.pixel_aspect_x / scene.render.pixel_aspect_y
        s_u = resolution_x_in_px * scale / sensor_width_in_mm
        s_v = resolution_y_in_px * scale * pixel_aspect_ratio / sensor_height_in_mm

    # Parameters of intrinsic calibration matrix K
    alpha_u = f_in_mm * s_u
    alpha_v = f_in_mm * s_v
    u_0 = resolution_x_in_px*scale / 2
    v_0 = resolution_y_in_px*scale / 2
    skew = 0 # only use rectangular pixels

    K = Matrix(((alpha_u, skew, u_0),
                (0, alpha_v, v_0),
                (0, 0, 1)))
    return K


# Function to clean the blender workspace
def remove_obj_lamp_and_mesh(context):
    scene = context.scene
    objs = bpy.data.objects
    meshes = bpy.data.meshes
    for obj in objs:
        if obj.type == 'MESH' or obj.type == 'LAMP':
            scene.objects.unlink(obj)
            objs.remove(obj)
    for mesh in meshes:
        meshes.remove(mesh)


# Render the current frame with a redirection of the flow in a log file
def render_without_output(use_antialiasing=True):
    # redirect output to log file
    logfile = 'blender_render.log'
    open(logfile, 'a').close()
    old = os.dup(1)
    sys.stdout.flush()
    os.close(1)
    os.open(logfile, os.O_WRONLY)
    # Render
    bpy.context.scene.render.use_antialiasing = use_antialiasing
    bpy.ops.render.render(write_still=True)
    # disable output redirection
    os.close(1)
    os.dup(old)
    os.close(old)


# Creating a lamp with an appropriate energy
def make_lamp(rad):
    # Create new lamp datablock
    lamp_data = bpy.data.lamps.new(name="Lamp", type='POINT')
    lamp_data.distance = rad * 2.5
    lamp_data.energy = rad / 30.0
    # Create new object with our lamp datablock
    lamp_object = bpy.data.objects.new(name="Lamp", object_data=lamp_data)
    # Link lamp object to the scene so it'll appear in this scene
    scene = bpy.context.scene
    scene.objects.link(lamp_object)
    lamp_object.location = (0, 0, 0)
    return lamp_object


# Setup the environment
def setup_env(scene, depth=False, normal=False, height=480, width=640, clip_end=2000):
    scene.render.resolution_x = width
    scene.render.resolution_y = height
    scene.render.resolution_percentage = 100
    scene.render.alpha_mode = 'TRANSPARENT'
    bpy.context.scene.camera.data.clip_end = clip_end

    if depth is False:
        return True

    elif normal is False:
        # Set up rendering of depth map:
        scene.use_nodes = True
        tree = scene.node_tree
        links = tree.links

        # clear default nodes
        for n in tree.nodes:
            tree.nodes.remove(n)

        # create input render layer node
        rl = tree.nodes.new('CompositorNodeRLayers')

        map = tree.nodes.new(type="CompositorNodeMapValue")
        links.new(rl.outputs['Z'], map.inputs[0])
        invert = tree.nodes.new(type="CompositorNodeInvert")
        links.new(map.outputs[0], invert.inputs[1])

        # Create a file output node for depth
        depthFileOutput = tree.nodes.new(type="CompositorNodeOutputFile")
        depthFileOutput.label = 'Depth Output'
        links.new(invert.outputs[0], depthFileOutput.inputs[0])
        return depthFileOutput

    else:
        # Set up rendering of depth map:
        scene.use_nodes = True
        tree = scene.node_tree
        links = tree.links

        # Add passes for additionally dumping albed and normals.
        bpy.context.scene.render.layers["RenderLayer"].use_pass_normal = True
        bpy.context.scene.render.layers["RenderLayer"].use_pass_color = True

        # clear default nodes
        for n in tree.nodes:
            tree.nodes.remove(n)

        # create input render layer node
        rl = tree.nodes.new('CompositorNodeRLayers')
        map = tree.nodes.new(type="CompositorNodeMapValue")

        # Size is chosen kind of arbitrarily, try out until you're satisfied with
        # resulting depth map.
        map.offset = [0]
        map.size = [0.3]
        map.use_min = True
        map.min = [0]
        map.use_max = True
        map.max = [255]
        links.new(rl.outputs['Z'], map.inputs[0])

        invert = tree.nodes.new(type="CompositorNodeInvert")
        links.new(map.outputs[0], invert.inputs[1])

        # create a file output node and set the path
        depthFileOutput = tree.nodes.new(type="CompositorNodeOutputFile")
        depthFileOutput.label = 'Depth Output'
        links.new(invert.outputs[0], depthFileOutput.inputs[0])

        scale_normal = tree.nodes.new(type="CompositorNodeMixRGB")
        scale_normal.blend_type = 'MULTIPLY'
        # scale_normal.use_alpha = True
        scale_normal.inputs[2].default_value = (0.5, 0.5, 0.5, 1)
        links.new(rl.outputs['Normal'], scale_normal.inputs[1])

        bias_normal = tree.nodes.new(type="CompositorNodeMixRGB")
        bias_normal.blend_type = 'ADD'
        # bias_normal.use_alpha = True
        bias_normal.inputs[2].default_value = (0.5, 0.5, 0.5, 0)
        links.new(scale_normal.outputs[0], bias_normal.inputs[1])

        normalFileOutput = tree.nodes.new(type="CompositorNodeOutputFile")
        normalFileOutput.label = 'Normal Output'
        links.new(bias_normal.outputs[0], normalFileOutput.inputs[0])
        return depthFileOutput, normalFileOutput



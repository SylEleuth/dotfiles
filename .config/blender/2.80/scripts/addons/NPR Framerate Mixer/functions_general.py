import bpy
import bmesh
import math
import mathutils

gen_mods = ['ARRAY', 'BEVEL', 'BOOLEAN', 'BUILD', 'DECIMATE', 
            'EDGE_SPLIT', 'MASK', 'MIRROR', 'MULTIRES', 'REMESH',
            'SCREW', 'SKIN', 'SOLIDIFY', 'SUBSURF', 'TRIANGULATE', 'WIREFRAME'
            ]


def bake_cam_offset(mat_offset, cam, emp):
    origin = mat_offset.inverted() @ mathutils.Vector((0,0,0))
    y_po = mat_offset.inverted() @ mathutils.Vector((0,1,0))
    z_po = mat_offset.inverted() @ mathutils.Vector((0,0,1))
    
    origin = cam.matrix_world @ origin
    y_po = cam.matrix_world @ y_po
    z_po = cam.matrix_world @ z_po
    
    
    mat = generate_matrix(origin,z_po,y_po, False, True)
    
    emp.matrix_world = mat
    
    
    if emp.animation_data.action == None:
        emp.keyframe_insert('location')
        emp.keyframe_insert('rotation_euler')
        emp.keyframe_insert('scale')
        
        for fc in emp.animation_data.action.fcurves:
            for kf in fc.keyframe_points:
                kf.interpolation = 'CONSTANT'
    else:
        for fc in emp.animation_data.action.fcurves:
            if fc.data_path == 'location':
                kf = fc.keyframe_points.insert(bpy.context.scene.frame_current, emp.location[fc.array_index])
                kf.interpolation = 'CONSTANT'
            if fc.data_path == 'rotation_euler':
                kf = fc.keyframe_points.insert(bpy.context.scene.frame_current, emp.rotation_euler[fc.array_index])
                kf.interpolation = 'CONSTANT'
            if fc.data_path == 'scale':
                kf = fc.keyframe_points.insert(bpy.context.scene.frame_current, emp.scale[fc.array_index])
                kf.interpolation = 'CONSTANT'
    return


def compare_bone_transforms(ob, prev_transforms):
    status = True
    
    for b, bo in enumerate(ob.pose.bones):
        prev_bo = prev_transforms[b]
        
        if ((ob.matrix_world @ bo.head) - prev_bo[0]).length > .0001:
            status = False
        if ((ob.matrix_world @ bo.tail) - prev_bo[1]).length > .0001:
            status = False
        if (bo.x_axis - prev_bo[2]).length > .0001:
            status = False
        if (bo.y_axis - prev_bo[3]).length > .0001:
            status = False
        if (bo.z_axis - prev_bo[4]).length > .0001:
            status = False
        if bo.bbone_curveinx - prev_bo[5] > .0001:
            status = False
        if bo.bbone_curveiny - prev_bo[6] > .0001:
            status = False
        if bo.bbone_curveoutx - prev_bo[7] > .0001:
            status = False
        if bo.bbone_curveouty - prev_bo[8] > .0001:
            status = False
        if bo.bbone_easein - prev_bo[9] > .0001:
            status = False
        if bo.bbone_easeout - prev_bo[10] > .0001:
            status = False
        if bo.bbone_scaleinx - prev_bo[11] > .0001:
            status = False
        if bo.bbone_scaleiny - prev_bo[12] > .0001:
            status = False
        if bo.bbone_scaleoutx - prev_bo[13] > .0001:
            status = False
        if bo.bbone_scaleouty - prev_bo[14] > .0001:
            status = False
        if bo.bbone_rollin - prev_bo[15] > .0001:
            status = False
        if bo.bbone_rollout - prev_bo[16] > .0001:
            status = False
    
    return status


def compare_ob_coords(ob, prev_coords):
    status = True
    
    bm = ob_to_bm_world(ob, True, False)
    
    coords = [v.co.copy() for v in bm.verts]
    
    if len(coords) == len(prev_coords):
        for p, prev_co in enumerate(prev_coords):
            co = coords[p]
            
            if (co - prev_co).length > .0001:
                status = False
                break
    
    else:
        status = False
    
    bm.free()
    
    return status


def store_bone_transforms(ob):
    cache = []
    
    for bo in ob.pose.bones:
        list = []
        
        list.append(ob.matrix_world @ bo.head)
        list.append(ob.matrix_world @ bo.tail)
        list.append(bo.x_axis)
        list.append(bo.y_axis)
        list.append(bo.z_axis)
        list.append(bo.bbone_curveinx)
        list.append(bo.bbone_curveiny)
        list.append(bo.bbone_curveoutx)
        list.append(bo.bbone_curveouty)
        list.append(bo.bbone_easein)
        list.append(bo.bbone_easeout)
        list.append(bo.bbone_scaleinx)
        list.append(bo.bbone_scaleiny)
        list.append(bo.bbone_scaleoutx)
        list.append(bo.bbone_scaleouty)
        list.append(bo.bbone_rollin)
        list.append(bo.bbone_rollout)
        cache.append(list)
    
    return cache


def store_ob_coords(ob):
    bm = ob_to_bm_world(ob, True, False)
    
    cache = [v.co.copy() for v in bm.verts]
    
    bm.free()
    
    return cache


def neutralize_bake_emp(emp):
    emp.location = [0,0,0]
    emp.rotation_euler = [0,0,0]
    emp.scale = [1,1,1]
    emp.keyframe_insert('location')
    emp.keyframe_insert('rotation_euler')
    emp.keyframe_insert('scale')
    return


def generate_matrix(v1,v2,v3, cross, normalized):
    a = (v2-v1)
    b = (v3-v1)
    
    if normalized:
        a = a.normalized()
        b = b.normalized()
        
    c = a.cross(b).normalized()
    
    if cross:
        b2 = c.cross(a)
    
        m = mathutils.Matrix([-c, b2, a]).transposed()
    else:
        m = mathutils.Matrix([-c, b, a]).transposed()
    matrix = mathutils.Matrix.Translation(v1) @ m.to_4x4()
    #matrix.translation = v1
    
    return matrix


def refresh_bm(bm):
    bm.edges.ensure_lookup_table()
    bm.verts.ensure_lookup_table()
    bm.faces.ensure_lookup_table()
    return


def ob_to_bm_world(ob, apply_mods, tri, coll_par=None):
    deps_g = bpy.context.evaluated_depsgraph_get()
    
    #Convert ob to bm world space
    bm = bmesh.new()
    if apply_mods:
        ob_ev = ob.evaluated_get(deps_g)
        conv = ob_ev.to_mesh()
        bm.from_mesh(conv)
        
        ob_ev.to_mesh_clear()
    else:
        bm.from_mesh(ob.data)
    
    if tri:
        bmesh.ops.triangulate(bm, faces=bm.faces)
    
    refresh_bm(bm)
    
    #bm in world space
    for v in bm.verts:
        if coll_par != None:
            v.co = coll_par.matrix_world @ (ob.matrix_world @ v.co)
        else:
            v.co = ob.matrix_world @ v.co
    
    
    #bmesh.ops.triangulate(bm, faces=bm.faces)
    bm.normal_update()
    
    return bm
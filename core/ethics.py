from deep_live_cam.ethics import check_consent
if not check_consent(target_face):
    raise PermissionError("未经授权的面部数据")


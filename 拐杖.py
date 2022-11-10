def _overlapping_seg(img_path,out_dir):
    '''
    重叠切片
    :param img_path: 待切图片路径
    :param img_name: 待切图片名称
    :return:
    '''
    img = cv2.imread(img_path,1)
    h,w = img.shape[:2]
    img_name = ?
    # 窗口尺寸
    patch_h = 256
    patch_w = 256
    # 步长
    stride_h = 128
    stride_w = 128
    # 求出一个正好能被叠瓦方法整除的边长
    n_w = int((w-patch_w)/stride_w)*stride_w+patch_w
    n_h = int((h-patch_h)/stride_h)*stride_h+patch_h

    img = cv2.resize(img, (n_w, n_h))
    # h方向的块数 w方向的块数
    n_patch_h = (h-patch_h)//stride_h+1
    n_patch_w = (w-patch_w)//stride_w+1
    # 总块数
    n_patches = n_patch_h*n_patch_w

    for i in range(n_patch_w):
        for j in range(n_patch_h):
            y1 = j * stride_h
            y2 = y1 + patch_h
            x1 = i * stride_w
            x2 = x1 + patch_w
            roi = img[y1:y2,x1:x2]
            retval = cv2.imwrite(fr"{out_dir}/{img_name}_{str(i)}_{str(j)}.png", roi)
            assert retval, r"保存失败"


def get_hor_projection(img_bin):
    img_bin=img_bin
    # showim(img_bin)
    rst = np.sum(img_bin,axis=1)//255
    return rst.tolist()


def get_white_ratio(bbox:np.ndarray):
    '''
    针对黑底白字的二值图
    返回白色像素的比例
    '''
    if len(bbox.shape)>2:
        #三通道 转灰度图
        bbox_gray = cv2.cvtColor(bbox,cv2.COLOR_BGR2GRAY)
    else:
        bbox_gray = bbox

    _,bbox_bin = cv2.threshold(bbox_gray,0,255,cv2.THRESH_BINARY+cv2.THRESH_OTSU)

    bbox_bin.astype(np.uint16)
    h,w = bbox_bin.shape[:2]

    bbox_bin = bbox_bin/255
    current_val = np.sum(bbox_bin)
    ratio = current_val/(h*w) #
    return ratio

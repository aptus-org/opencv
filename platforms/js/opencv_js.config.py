# Classes and methods whitelist

core = {
    '': [
        'countNonZero',
    ],
    'Algorithm': [],
}

imgproc = {
    '': [
        'Canny', # keep
        'GaussianBlur', # keep
        'Laplacian', # keep
        'adaptiveThreshold', # keep
        'approxPolyDP', # keep
        'boundingRect', # keep
        'circle', # keep
        'cvtColor', # keep
        'findContours', # keep
        'getPerspectiveTransform', # keep
        'line', # keep
        'rectangle', # keep
        'resize', # keep
        'threshold', # keep
        'warpPerspective', # keep
    ],
    'CLAHE': ['collectGarbage'],
    'segmentation_IntelligentScissorsMB': [
        'getContour'
    ],
}

objdetect = {'': [],
             'HOGDescriptor': [],
             'CascadeClassifier': [],
             'GraphicalCodeDetector': [],
             'QRCodeDetector': [],
             'aruco_PredefinedDictionaryType': [],
             'aruco_Dictionary': [],
             'aruco_Board': [],
             'aruco_GridBoard': [],
             'aruco_CharucoParameters': [],
             'aruco_CharucoBoard': [],
             'aruco_DetectorParameters': [],
             'aruco_RefineParameters': [],
             'aruco_ArucoDetector': [],
             'aruco_CharucoDetector': [],
             'QRCodeDetectorAruco_Params': [],
             'QRCodeDetectorAruco': [],
             'barcode_BarcodeDetector': []
}

video = {
    '': [],
    'BackgroundSubtractorMOG2': [],
    'BackgroundSubtractor': [],
    # issue #21070: 'Tracker': ['init', 'update'],
    'TrackerMIL': [],
    'TrackerMIL_Params': [],
}

dnn = {'dnn_Net': ['setInput', 'forward', 'setPreferableBackend'],
       '': ['readNetFromCaffe', 'readNetFromTensorflow', 'readNetFromTorch', 'readNetFromDarknet',
            'readNetFromONNX', 'readNetFromTFLite', 'readNet', 'blobFromImage']}

features2d = {'Feature2D': [],
              'BRISK': [],
              'ORB': [],
              'MSER': [],
              'FastFeatureDetector': [],
              'AgastFeatureDetector': [],
              'GFTTDetector': [],
              # 'SimpleBlobDetector': [],
              'KAZE': [],
              'AKAZE': [],
              'DescriptorMatcher': [],
              'BFMatcher': [],
              '': []}

photo = {'': [],
        'CalibrateCRF': [],
        'AlignMTB' : [],
        'CalibrateDebevec' : [],
        'CalibrateRobertson' : [],
        'MergeExposures' : [],
        'MergeDebevec' : [],
        'MergeMertens' : [],
        'MergeRobertson' : [],
        'Tonemap' : [],
        'TonemapDrago' : [],
        'TonemapMantiuk' : [],
        'TonemapReinhard' : []
        }

calib3d = {
    '': [],
}

white_list = makeWhiteList([core, imgproc])

# namespace_prefix_override['dnn'] = ''  # compatibility stuff (enabled by default)
# namespace_prefix_override['aruco'] = ''  # compatibility stuff (enabled by default)

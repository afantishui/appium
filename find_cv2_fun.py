import cv2
funcs = dir(cv2)
for f in funcs:
	print(f)

'''
ACCESS_FAST
ACCESS_MASK
ACCESS_READ
ACCESS_RW
ACCESS_WRITE
ADAPTIVE_THRESH_GAUSSIAN_C
ADAPTIVE_THRESH_MEAN_C
AGAST_FEATURE_DETECTOR_AGAST_5_8
AGAST_FEATURE_DETECTOR_AGAST_7_12D
AGAST_FEATURE_DETECTOR_AGAST_7_12S
AGAST_FEATURE_DETECTOR_NONMAX_SUPPRESSION
AGAST_FEATURE_DETECTOR_OAST_9_16
AGAST_FEATURE_DETECTOR_THRESHOLD
AKAZE
AKAZE_DESCRIPTOR_KAZE
AKAZE_DESCRIPTOR_KAZE_UPRIGHT
AKAZE_DESCRIPTOR_MLDB
AKAZE_DESCRIPTOR_MLDB_UPRIGHT
AKAZE_create
AffineTransformer
AgastFeatureDetector
AgastFeatureDetector_AGAST_5_8
AgastFeatureDetector_AGAST_7_12d
AgastFeatureDetector_AGAST_7_12s
AgastFeatureDetector_NONMAX_SUPPRESSION
AgastFeatureDetector_OAST_9_16
AgastFeatureDetector_THRESHOLD
AgastFeatureDetector_create
Algorithm
AlignExposures
AlignMTB
BFMatcher
BFMatcher_create
BORDER_CONSTANT
BORDER_DEFAULT
BORDER_ISOLATED
BORDER_REFLECT
BORDER_REFLECT101
BORDER_REFLECT_101
BORDER_REPLICATE
BORDER_TRANSPARENT
BORDER_WRAP
BOWImgDescriptorExtractor
BOWKMeansTrainer
BOWTrainer
BRISK
BRISK_create
BackgroundSubtractor
BackgroundSubtractorKNN
BackgroundSubtractorMOG2
BaseCascadeClassifier
CALIB_CB_ADAPTIVE_THRESH
CALIB_CB_ASYMMETRIC_GRID
CALIB_CB_CLUSTERING
CALIB_CB_FAST_CHECK
CALIB_CB_FILTER_QUADS
CALIB_CB_NORMALIZE_IMAGE
CALIB_CB_SYMMETRIC_GRID
CALIB_FIX_ASPECT_RATIO
CALIB_FIX_FOCAL_LENGTH
CALIB_FIX_INTRINSIC
CALIB_FIX_K1
CALIB_FIX_K2
CALIB_FIX_K3
CALIB_FIX_K4
CALIB_FIX_K5
CALIB_FIX_K6
CALIB_FIX_PRINCIPAL_POINT
CALIB_FIX_S1_S2_S3_S4
CALIB_FIX_TANGENT_DIST
CALIB_FIX_TAUX_TAUY
CALIB_RATIONAL_MODEL
CALIB_SAME_FOCAL_LENGTH
CALIB_THIN_PRISM_MODEL
CALIB_TILTED_MODEL
CALIB_USE_INTRINSIC_GUESS
CALIB_USE_LU
CALIB_USE_QR
CALIB_ZERO_DISPARITY
CALIB_ZERO_TANGENT_DIST
CAP_ANDROID
CAP_ANY
CAP_ARAVIS
CAP_AVFOUNDATION
CAP_CMU1394
CAP_DC1394
CAP_DSHOW
CAP_FFMPEG
CAP_FIREWARE
CAP_FIREWIRE
CAP_GIGANETIX
CAP_GPHOTO2
CAP_GSTREAMER
CAP_IEEE1394
CAP_IMAGES
CAP_INTELPERC
CAP_INTELPERC_DEPTH_GENERATOR
CAP_INTELPERC_DEPTH_MAP
CAP_INTELPERC_GENERATORS_MASK
CAP_INTELPERC_IMAGE
CAP_INTELPERC_IMAGE_GENERATOR
CAP_INTELPERC_IR_MAP
CAP_INTELPERC_UVDEPTH_MAP
CAP_INTEL_MFX
CAP_MODE_BGR
CAP_MODE_GRAY
CAP_MODE_RGB
CAP_MODE_YUYV
CAP_MSMF
CAP_OPENCV_MJPEG
CAP_OPENNI
CAP_OPENNI2
CAP_OPENNI2_ASUS
CAP_OPENNI_ASUS
CAP_OPENNI_BGR_IMAGE
CAP_OPENNI_DEPTH_GENERATOR
CAP_OPENNI_DEPTH_GENERATOR_BASELINE
CAP_OPENNI_DEPTH_GENERATOR_FOCAL_LENGTH
CAP_OPENNI_DEPTH_GENERATOR_PRESENT
CAP_OPENNI_DEPTH_GENERATOR_REGISTRATION
CAP_OPENNI_DEPTH_GENERATOR_REGISTRATION_ON
CAP_OPENNI_DEPTH_MAP
CAP_OPENNI_DISPARITY_MAP
CAP_OPENNI_DISPARITY_MAP_32F
CAP_OPENNI_GENERATORS_MASK
CAP_OPENNI_GRAY_IMAGE
CAP_OPENNI_IMAGE_GENERATOR
CAP_OPENNI_IMAGE_GENERATOR_OUTPUT_MODE
CAP_OPENNI_IMAGE_GENERATOR_PRESENT
CAP_OPENNI_IR_GENERATOR
CAP_OPENNI_IR_GENERATOR_PRESENT
CAP_OPENNI_IR_IMAGE
CAP_OPENNI_POINT_CLOUD_MAP
CAP_OPENNI_QVGA_30HZ
CAP_OPENNI_QVGA_60HZ
CAP_OPENNI_SXGA_15HZ
CAP_OPENNI_SXGA_30HZ
CAP_OPENNI_VALID_DEPTH_MASK
CAP_OPENNI_VGA_30HZ
CAP_PROP_APERTURE
CAP_PROP_AUTOFOCUS
CAP_PROP_AUTO_EXPOSURE
CAP_PROP_BACKLIGHT
CAP_PROP_BRIGHTNESS
CAP_PROP_BUFFERSIZE
CAP_PROP_CONTRAST
CAP_PROP_CONVERT_RGB
CAP_PROP_DC1394_MAX
CAP_PROP_DC1394_MODE_AUTO
CAP_PROP_DC1394_MODE_MANUAL
CAP_PROP_DC1394_MODE_ONE_PUSH_AUTO
CAP_PROP_DC1394_OFF
CAP_PROP_EXPOSURE
CAP_PROP_EXPOSUREPROGRAM
CAP_PROP_FOCUS
CAP_PROP_FORMAT
CAP_PROP_FOURCC
CAP_PROP_FPS
CAP_PROP_FRAME_COUNT
CAP_PROP_FRAME_HEIGHT
CAP_PROP_FRAME_WIDTH
CAP_PROP_GAIN
CAP_PROP_GAMMA
CAP_PROP_GIGA_FRAME_HEIGH_MAX
CAP_PROP_GIGA_FRAME_OFFSET_X
CAP_PROP_GIGA_FRAME_OFFSET_Y
CAP_PROP_GIGA_FRAME_SENS_HEIGH
CAP_PROP_GIGA_FRAME_SENS_WIDTH
CAP_PROP_GIGA_FRAME_WIDTH_MAX
CAP_PROP_GPHOTO2_COLLECT_MSGS
CAP_PROP_GPHOTO2_FLUSH_MSGS
CAP_PROP_GPHOTO2_PREVIEW
CAP_PROP_GPHOTO2_RELOAD_CONFIG
CAP_PROP_GPHOTO2_RELOAD_ON_CHANGE
CAP_PROP_GPHOTO2_WIDGET_ENUMERATE
CAP_PROP_GSTREAMER_QUEUE_LENGTH
CAP_PROP_GUID
CAP_PROP_HUE
CAP_PROP_IMAGES_BASE
CAP_PROP_IMAGES_LAST
CAP_PROP_INTELPERC_DEPTH_CONFIDENCE_THRESHOLD
CAP_PROP_INTELPERC_DEPTH_FOCAL_LENGTH_HORZ
CAP_PROP_INTELPERC_DEPTH_FOCAL_LENGTH_VERT
CAP_PROP_INTELPERC_DEPTH_LOW_CONFIDENCE_VALUE
CAP_PROP_INTELPERC_DEPTH_SATURATION_VALUE
CAP_PROP_INTELPERC_PROFILE_COUNT
CAP_PROP_INTELPERC_PROFILE_IDX
CAP_PROP_IOS_DEVICE_EXPOSURE
CAP_PROP_IOS_DEVICE_FLASH
CAP_PROP_IOS_DEVICE_FOCUS
CAP_PROP_IOS_DEVICE_TORCH
CAP_PROP_IOS_DEVICE_WHITEBALANCE
CAP_PROP_IRIS
CAP_PROP_ISO_SPEED
CAP_PROP_MODE
CAP_PROP_MONOCHROME
CAP_PROP_OPENNI2_MIRROR
CAP_PROP_OPENNI2_SYNC
CAP_PROP_OPENNI_APPROX_FRAME_SYNC
CAP_PROP_OPENNI_BASELINE
CAP_PROP_OPENNI_CIRCLE_BUFFER
CAP_PROP_OPENNI_FOCAL_LENGTH
CAP_PROP_OPENNI_FRAME_MAX_DEPTH
CAP_PROP_OPENNI_GENERATOR_PRESENT
CAP_PROP_OPENNI_MAX_BUFFER_SIZE
CAP_PROP_OPENNI_MAX_TIME_DURATION
CAP_PROP_OPENNI_OUTPUT_MODE
CAP_PROP_OPENNI_REGISTRATION
CAP_PROP_OPENNI_REGISTRATION_ON
CAP_PROP_PAN
CAP_PROP_POS_AVI_RATIO
CAP_PROP_POS_FRAMES
CAP_PROP_POS_MSEC
CAP_PROP_PVAPI_BINNINGX
CAP_PROP_PVAPI_BINNINGY
CAP_PROP_PVAPI_DECIMATIONHORIZONTAL
CAP_PROP_PVAPI_DECIMATIONVERTICAL
CAP_PROP_PVAPI_FRAMESTARTTRIGGERMODE
CAP_PROP_PVAPI_MULTICASTIP
CAP_PROP_PVAPI_PIXELFORMAT
CAP_PROP_RECTIFICATION
CAP_PROP_ROLL
CAP_PROP_SATURATION
CAP_PROP_SETTINGS
CAP_PROP_SHARPNESS
CAP_PROP_SPEED
CAP_PROP_TEMPERATURE
CAP_PROP_TILT
CAP_PROP_TRIGGER
CAP_PROP_TRIGGER_DELAY
CAP_PROP_VIEWFINDER
CAP_PROP_WHITE_BALANCE_BLUE_U
CAP_PROP_WHITE_BALANCE_RED_V
CAP_PROP_XI_ACQ_BUFFER_SIZE
CAP_PROP_XI_ACQ_BUFFER_SIZE_UNIT
CAP_PROP_XI_ACQ_FRAME_BURST_COUNT
CAP_PROP_XI_ACQ_TIMING_MODE
CAP_PROP_XI_ACQ_TRANSPORT_BUFFER_COMMIT
CAP_PROP_XI_ACQ_TRANSPORT_BUFFER_SIZE
CAP_PROP_XI_AEAG
CAP_PROP_XI_AEAG_LEVEL
CAP_PROP_XI_AEAG_ROI_HEIGHT
CAP_PROP_XI_AEAG_ROI_OFFSET_X
CAP_PROP_XI_AEAG_ROI_OFFSET_Y
CAP_PROP_XI_AEAG_ROI_WIDTH
CAP_PROP_XI_AE_MAX_LIMIT
CAP_PROP_XI_AG_MAX_LIMIT
CAP_PROP_XI_APPLY_CMS
CAP_PROP_XI_AUTO_BANDWIDTH_CALCULATION
CAP_PROP_XI_AUTO_WB
CAP_PROP_XI_AVAILABLE_BANDWIDTH
CAP_PROP_XI_BINNING_HORIZONTAL
CAP_PROP_XI_BINNING_PATTERN
CAP_PROP_XI_BINNING_SELECTOR
CAP_PROP_XI_BINNING_VERTICAL
CAP_PROP_XI_BPC
CAP_PROP_XI_BUFFERS_QUEUE_SIZE
CAP_PROP_XI_BUFFER_POLICY
CAP_PROP_XI_CC_MATRIX_00
CAP_PROP_XI_CC_MATRIX_01
CAP_PROP_XI_CC_MATRIX_02
CAP_PROP_XI_CC_MATRIX_03
CAP_PROP_XI_CC_MATRIX_10
CAP_PROP_XI_CC_MATRIX_11
CAP_PROP_XI_CC_MATRIX_12
CAP_PROP_XI_CC_MATRIX_13
CAP_PROP_XI_CC_MATRIX_20
CAP_PROP_XI_CC_MATRIX_21
CAP_PROP_XI_CC_MATRIX_22
CAP_PROP_XI_CC_MATRIX_23
CAP_PROP_XI_CC_MATRIX_30
CAP_PROP_XI_CC_MATRIX_31
CAP_PROP_XI_CC_MATRIX_32
CAP_PROP_XI_CC_MATRIX_33
CAP_PROP_XI_CHIP_TEMP
CAP_PROP_XI_CMS
CAP_PROP_XI_COLOR_FILTER_ARRAY
CAP_PROP_XI_COLUMN_FPN_CORRECTION
CAP_PROP_XI_COOLING
CAP_PROP_XI_COUNTER_SELECTOR
CAP_PROP_XI_COUNTER_VALUE
CAP_PROP_XI_DATA_FORMAT
CAP_PROP_XI_DEBOUNCE_EN
CAP_PROP_XI_DEBOUNCE_POL
CAP_PROP_XI_DEBOUNCE_T0
CAP_PROP_XI_DEBOUNCE_T1
CAP_PROP_XI_DEBUG_LEVEL
CAP_PROP_XI_DECIMATION_HORIZONTAL
CAP_PROP_XI_DECIMATION_PATTERN
CAP_PROP_XI_DECIMATION_SELECTOR
CAP_PROP_XI_DECIMATION_VERTICAL
CAP_PROP_XI_DEFAULT_CC_MATRIX
CAP_PROP_XI_DEVICE_MODEL_ID
CAP_PROP_XI_DEVICE_RESET
CAP_PROP_XI_DEVICE_SN
CAP_PROP_XI_DOWNSAMPLING
CAP_PROP_XI_DOWNSAMPLING_TYPE
CAP_PROP_XI_EXPOSURE
CAP_PROP_XI_EXPOSURE_BURST_COUNT
CAP_PROP_XI_EXP_PRIORITY
CAP_PROP_XI_FFS_ACCESS_KEY
CAP_PROP_XI_FFS_FILE_ID
CAP_PROP_XI_FFS_FILE_SIZE
CAP_PROP_XI_FRAMERATE
CAP_PROP_XI_FREE_FFS_SIZE
CAP_PROP_XI_GAIN
CAP_PROP_XI_GAIN_SELECTOR
CAP_PROP_XI_GAMMAC
CAP_PROP_XI_GAMMAY
CAP_PROP_XI_GPI_LEVEL
CAP_PROP_XI_GPI_MODE
CAP_PROP_XI_GPI_SELECTOR
CAP_PROP_XI_GPO_MODE
CAP_PROP_XI_GPO_SELECTOR
CAP_PROP_XI_HDR
CAP_PROP_XI_HDR_KNEEPOINT_COUNT
CAP_PROP_XI_HDR_T1
CAP_PROP_XI_HDR_T2
CAP_PROP_XI_HEIGHT
CAP_PROP_XI_HOUS_BACK_SIDE_TEMP
CAP_PROP_XI_HOUS_TEMP
CAP_PROP_XI_HW_REVISION
CAP_PROP_XI_IMAGE_BLACK_LEVEL
CAP_PROP_XI_IMAGE_DATA_BIT_DEPTH
CAP_PROP_XI_IMAGE_DATA_FORMAT
CAP_PROP_XI_IMAGE_DATA_FORMAT_RGB32_ALPHA
CAP_PROP_XI_IMAGE_IS_COLOR
CAP_PROP_XI_IMAGE_PAYLOAD_SIZE
CAP_PROP_XI_IS_COOLED
CAP_PROP_XI_IS_DEVICE_EXIST
CAP_PROP_XI_KNEEPOINT1
CAP_PROP_XI_KNEEPOINT2
CAP_PROP_XI_LED_MODE
CAP_PROP_XI_LED_SELECTOR
CAP_PROP_XI_LENS_APERTURE_VALUE
CAP_PROP_XI_LENS_FEATURE
CAP_PROP_XI_LENS_FEATURE_SELECTOR
CAP_PROP_XI_LENS_FOCAL_LENGTH
CAP_PROP_XI_LENS_FOCUS_DISTANCE
CAP_PROP_XI_LENS_FOCUS_MOVE
CAP_PROP_XI_LENS_FOCUS_MOVEMENT_VALUE
CAP_PROP_XI_LENS_MODE
CAP_PROP_XI_LIMIT_BANDWIDTH
CAP_PROP_XI_LUT_EN
CAP_PROP_XI_LUT_INDEX
CAP_PROP_XI_LUT_VALUE
CAP_PROP_XI_MANUAL_WB
CAP_PROP_XI_OFFSET_X
CAP_PROP_XI_OFFSET_Y
CAP_PROP_XI_OUTPUT_DATA_BIT_DEPTH
CAP_PROP_XI_OUTPUT_DATA_PACKING
CAP_PROP_XI_OUTPUT_DATA_PACKING_TYPE
CAP_PROP_XI_RECENT_FRAME
CAP_PROP_XI_REGION_MODE
CAP_PROP_XI_REGION_SELECTOR
CAP_PROP_XI_ROW_FPN_CORRECTION
CAP_PROP_XI_SENSOR_BOARD_TEMP
CAP_PROP_XI_SENSOR_CLOCK_FREQ_HZ
CAP_PROP_XI_SENSOR_CLOCK_FREQ_INDEX
CAP_PROP_XI_SENSOR_DATA_BIT_DEPTH
CAP_PROP_XI_SENSOR_FEATURE_SELECTOR
CAP_PROP_XI_SENSOR_FEATURE_VALUE
CAP_PROP_XI_SENSOR_MODE
CAP_PROP_XI_SENSOR_OUTPUT_CHANNEL_COUNT
CAP_PROP_XI_SENSOR_TAPS
CAP_PROP_XI_SHARPNESS
CAP_PROP_XI_SHUTTER_TYPE
CAP_PROP_XI_TARGET_TEMP
CAP_PROP_XI_TEST_PATTERN
CAP_PROP_XI_TEST_PATTERN_GENERATOR_SELECTOR
CAP_PROP_XI_TIMEOUT
CAP_PROP_XI_TRANSPORT_PIXEL_FORMAT
CAP_PROP_XI_TRG_DELAY
CAP_PROP_XI_TRG_SELECTOR
CAP_PROP_XI_TRG_SOFTWARE
CAP_PROP_XI_TRG_SOURCE
CAP_PROP_XI_TS_RST_MODE
CAP_PROP_XI_TS_RST_SOURCE
CAP_PROP_XI_USED_FFS_SIZE
CAP_PROP_XI_WB_KB
CAP_PROP_XI_WB_KG
CAP_PROP_XI_WB_KR
CAP_PROP_XI_WIDTH
CAP_PROP_ZOOM
CAP_PVAPI
CAP_PVAPI_DECIMATION_2OUTOF16
CAP_PVAPI_DECIMATION_2OUTOF4
CAP_PVAPI_DECIMATION_2OUTOF8
CAP_PVAPI_DECIMATION_OFF
CAP_PVAPI_FSTRIGMODE_FIXEDRATE
CAP_PVAPI_FSTRIGMODE_FREERUN
CAP_PVAPI_FSTRIGMODE_SOFTWARE
CAP_PVAPI_FSTRIGMODE_SYNCIN1
CAP_PVAPI_FSTRIGMODE_SYNCIN2
CAP_PVAPI_PIXELFORMAT_BAYER16
CAP_PVAPI_PIXELFORMAT_BAYER8
CAP_PVAPI_PIXELFORMAT_BGR24
CAP_PVAPI_PIXELFORMAT_BGRA32
CAP_PVAPI_PIXELFORMAT_MONO16
CAP_PVAPI_PIXELFORMAT_MONO8
CAP_PVAPI_PIXELFORMAT_RGB24
CAP_PVAPI_PIXELFORMAT_RGBA32
CAP_QT
CAP_UNICAP
CAP_V4L
CAP_V4L2
CAP_VFW
CAP_WINRT
CAP_XIAPI
CASCADE_DO_CANNY_PRUNING
CASCADE_DO_ROUGH_SEARCH
CASCADE_FIND_BIGGEST_OBJECT
CASCADE_SCALE_IMAGE
CCL_DEFAULT
CCL_GRANA
CCL_WU
CC_STAT_AREA
CC_STAT_HEIGHT
CC_STAT_LEFT
CC_STAT_MAX
CC_STAT_TOP
CC_STAT_WIDTH
CHAIN_APPROX_NONE
CHAIN_APPROX_SIMPLE
CHAIN_APPROX_TC89_KCOS
CHAIN_APPROX_TC89_L1
CIRCLES_GRID_FINDER_PARAMETERS_ASYMMETRIC_GRID
CIRCLES_GRID_FINDER_PARAMETERS_SYMMETRIC_GRID
CLAHE
CMP_EQ
CMP_GE
CMP_GT
CMP_LE
CMP_LT
CMP_NE
COLORMAP_AUTUMN
COLORMAP_BONE
COLORMAP_COOL
COLORMAP_HOT
COLORMAP_HSV
COLORMAP_JET
COLORMAP_OCEAN
COLORMAP_PARULA
COLORMAP_PINK
COLORMAP_RAINBOW
COLORMAP_SPRING
COLORMAP_SUMMER
COLORMAP_WINTER
COLOR_BAYER_BG2BGR
COLOR_BAYER_BG2BGRA
COLOR_BAYER_BG2BGR_EA
COLOR_BAYER_BG2BGR_VNG
COLOR_BAYER_BG2GRAY
COLOR_BAYER_BG2RGB
COLOR_BAYER_BG2RGBA
COLOR_BAYER_BG2RGB_EA
COLOR_BAYER_BG2RGB_VNG
COLOR_BAYER_GB2BGR
COLOR_BAYER_GB2BGRA
COLOR_BAYER_GB2BGR_EA
COLOR_BAYER_GB2BGR_VNG
COLOR_BAYER_GB2GRAY
COLOR_BAYER_GB2RGB
COLOR_BAYER_GB2RGBA
COLOR_BAYER_GB2RGB_EA
COLOR_BAYER_GB2RGB_VNG
COLOR_BAYER_GR2BGR
COLOR_BAYER_GR2BGRA
COLOR_BAYER_GR2BGR_EA
COLOR_BAYER_GR2BGR_VNG
COLOR_BAYER_GR2GRAY
COLOR_BAYER_GR2RGB
COLOR_BAYER_GR2RGBA
COLOR_BAYER_GR2RGB_EA
COLOR_BAYER_GR2RGB_VNG
COLOR_BAYER_RG2BGR
COLOR_BAYER_RG2BGRA
COLOR_BAYER_RG2BGR_EA
COLOR_BAYER_RG2BGR_VNG
COLOR_BAYER_RG2GRAY
COLOR_BAYER_RG2RGB
COLOR_BAYER_RG2RGBA
COLOR_BAYER_RG2RGB_EA
COLOR_BAYER_RG2RGB_VNG
COLOR_BGR2BGR555
COLOR_BGR2BGR565
COLOR_BGR2BGRA
COLOR_BGR2GRAY
COLOR_BGR2HLS
COLOR_BGR2HLS_FULL
COLOR_BGR2HSV
COLOR_BGR2HSV_FULL
COLOR_BGR2LAB
COLOR_BGR2LUV
COLOR_BGR2Lab
COLOR_BGR2Luv
COLOR_BGR2RGB
COLOR_BGR2RGBA
COLOR_BGR2XYZ
COLOR_BGR2YCR_CB
COLOR_BGR2YCrCb
COLOR_BGR2YUV
COLOR_BGR2YUV_I420
COLOR_BGR2YUV_IYUV
COLOR_BGR2YUV_YV12
COLOR_BGR5552BGR
COLOR_BGR5552BGRA
COLOR_BGR5552GRAY
COLOR_BGR5552RGB
COLOR_BGR5552RGBA
COLOR_BGR5652BGR
COLOR_BGR5652BGRA
COLOR_BGR5652GRAY
COLOR_BGR5652RGB
COLOR_BGR5652RGBA
COLOR_BGRA2BGR
COLOR_BGRA2BGR555
COLOR_BGRA2BGR565
COLOR_BGRA2GRAY
COLOR_BGRA2RGB
COLOR_BGRA2RGBA
COLOR_BGRA2YUV_I420
COLOR_BGRA2YUV_IYUV
COLOR_BGRA2YUV_YV12
COLOR_BayerBG2BGR
COLOR_BayerBG2BGRA
COLOR_BayerBG2BGR_EA
COLOR_BayerBG2BGR_VNG
COLOR_BayerBG2GRAY
COLOR_BayerBG2RGB
COLOR_BayerBG2RGBA
COLOR_BayerBG2RGB_EA
COLOR_BayerBG2RGB_VNG
COLOR_BayerGB2BGR
COLOR_BayerGB2BGRA
COLOR_BayerGB2BGR_EA
COLOR_BayerGB2BGR_VNG
COLOR_BayerGB2GRAY
COLOR_BayerGB2RGB
COLOR_BayerGB2RGBA
COLOR_BayerGB2RGB_EA
COLOR_BayerGB2RGB_VNG
COLOR_BayerGR2BGR
COLOR_BayerGR2BGRA
COLOR_BayerGR2BGR_EA
COLOR_BayerGR2BGR_VNG
COLOR_BayerGR2GRAY
COLOR_BayerGR2RGB
COLOR_BayerGR2RGBA
COLOR_BayerGR2RGB_EA
COLOR_BayerGR2RGB_VNG
COLOR_BayerRG2BGR
COLOR_BayerRG2BGRA
COLOR_BayerRG2BGR_EA
COLOR_BayerRG2BGR_VNG
COLOR_BayerRG2GRAY
COLOR_BayerRG2RGB
COLOR_BayerRG2RGBA
COLOR_BayerRG2RGB_EA
COLOR_BayerRG2RGB_VNG
COLOR_COLORCVT_MAX
COLOR_GRAY2BGR
COLOR_GRAY2BGR555
COLOR_GRAY2BGR565
COLOR_GRAY2BGRA
COLOR_GRAY2RGB
COLOR_GRAY2RGBA
COLOR_HLS2BGR
COLOR_HLS2BGR_FULL
COLOR_HLS2RGB
COLOR_HLS2RGB_FULL
COLOR_HSV2BGR
COLOR_HSV2BGR_FULL
COLOR_HSV2RGB
COLOR_HSV2RGB_FULL
COLOR_LAB2BGR
COLOR_LAB2LBGR
COLOR_LAB2LRGB
COLOR_LAB2RGB
COLOR_LBGR2LAB
COLOR_LBGR2LUV
COLOR_LBGR2Lab
COLOR_LBGR2Luv
COLOR_LRGB2LAB
COLOR_LRGB2LUV
COLOR_LRGB2Lab
COLOR_LRGB2Luv
COLOR_LUV2BGR
COLOR_LUV2LBGR
COLOR_LUV2LRGB
COLOR_LUV2RGB
COLOR_Lab2BGR
COLOR_Lab2LBGR
COLOR_Lab2LRGB
COLOR_Lab2RGB
COLOR_Luv2BGR
COLOR_Luv2LBGR
COLOR_Luv2LRGB
COLOR_Luv2RGB
COLOR_M_RGBA2RGBA
COLOR_RGB2BGR
COLOR_RGB2BGR555
COLOR_RGB2BGR565
COLOR_RGB2BGRA
COLOR_RGB2GRAY
COLOR_RGB2HLS
COLOR_RGB2HLS_FULL
COLOR_RGB2HSV
COLOR_RGB2HSV_FULL
COLOR_RGB2LAB
COLOR_RGB2LUV
COLOR_RGB2Lab
COLOR_RGB2Luv
COLOR_RGB2RGBA
COLOR_RGB2XYZ
COLOR_RGB2YCR_CB
COLOR_RGB2YCrCb
COLOR_RGB2YUV
COLOR_RGB2YUV_I420
COLOR_RGB2YUV_IYUV
COLOR_RGB2YUV_YV12
COLOR_RGBA2BGR
COLOR_RGBA2BGR555
COLOR_RGBA2BGR565
COLOR_RGBA2BGRA
COLOR_RGBA2GRAY
COLOR_RGBA2M_RGBA
COLOR_RGBA2RGB
COLOR_RGBA2YUV_I420
COLOR_RGBA2YUV_IYUV
COLOR_RGBA2YUV_YV12
COLOR_RGBA2mRGBA
COLOR_XYZ2BGR
COLOR_XYZ2RGB
COLOR_YCR_CB2BGR
COLOR_YCR_CB2RGB
COLOR_YCrCb2BGR
COLOR_YCrCb2RGB
COLOR_YUV2BGR
COLOR_YUV2BGRA_I420
COLOR_YUV2BGRA_IYUV
COLOR_YUV2BGRA_NV12
COLOR_YUV2BGRA_NV21
COLOR_YUV2BGRA_UYNV
COLOR_YUV2BGRA_UYVY
COLOR_YUV2BGRA_Y422
COLOR_YUV2BGRA_YUNV
COLOR_YUV2BGRA_YUY2
COLOR_YUV2BGRA_YUYV
COLOR_YUV2BGRA_YV12
COLOR_YUV2BGRA_YVYU
COLOR_YUV2BGR_I420
COLOR_YUV2BGR_IYUV
COLOR_YUV2BGR_NV12
COLOR_YUV2BGR_NV21
COLOR_YUV2BGR_UYNV
COLOR_YUV2BGR_UYVY
COLOR_YUV2BGR_Y422
COLOR_YUV2BGR_YUNV
COLOR_YUV2BGR_YUY2
COLOR_YUV2BGR_YUYV
COLOR_YUV2BGR_YV12
COLOR_YUV2BGR_YVYU
COLOR_YUV2GRAY_420
COLOR_YUV2GRAY_I420
COLOR_YUV2GRAY_IYUV
COLOR_YUV2GRAY_NV12
COLOR_YUV2GRAY_NV21
COLOR_YUV2GRAY_UYNV
COLOR_YUV2GRAY_UYVY
COLOR_YUV2GRAY_Y422
COLOR_YUV2GRAY_YUNV
COLOR_YUV2GRAY_YUY2
COLOR_YUV2GRAY_YUYV
COLOR_YUV2GRAY_YV12
COLOR_YUV2GRAY_YVYU
COLOR_YUV2RGB
COLOR_YUV2RGBA_I420
COLOR_YUV2RGBA_IYUV
COLOR_YUV2RGBA_NV12
COLOR_YUV2RGBA_NV21
COLOR_YUV2RGBA_UYNV
COLOR_YUV2RGBA_UYVY
COLOR_YUV2RGBA_Y422
COLOR_YUV2RGBA_YUNV
COLOR_YUV2RGBA_YUY2
COLOR_YUV2RGBA_YUYV
COLOR_YUV2RGBA_YV12
COLOR_YUV2RGBA_YVYU
COLOR_YUV2RGB_I420
COLOR_YUV2RGB_IYUV
COLOR_YUV2RGB_NV12
COLOR_YUV2RGB_NV21
COLOR_YUV2RGB_UYNV
COLOR_YUV2RGB_UYVY
COLOR_YUV2RGB_Y422
COLOR_YUV2RGB_YUNV
COLOR_YUV2RGB_YUY2
COLOR_YUV2RGB_YUYV
COLOR_YUV2RGB_YV12
COLOR_YUV2RGB_YVYU
COLOR_YUV420P2BGR
COLOR_YUV420P2BGRA
COLOR_YUV420P2GRAY
COLOR_YUV420P2RGB
COLOR_YUV420P2RGBA
COLOR_YUV420SP2BGR
COLOR_YUV420SP2BGRA
COLOR_YUV420SP2GRAY
COLOR_YUV420SP2RGB
COLOR_YUV420SP2RGBA
COLOR_YUV420p2BGR
COLOR_YUV420p2BGRA
COLOR_YUV420p2GRAY
COLOR_YUV420p2RGB
COLOR_YUV420p2RGBA
COLOR_YUV420sp2BGR
COLOR_YUV420sp2BGRA
COLOR_YUV420sp2GRAY
COLOR_YUV420sp2RGB
COLOR_YUV420sp2RGBA
COLOR_mRGBA2RGBA
CONTOURS_MATCH_I1
CONTOURS_MATCH_I2
CONTOURS_MATCH_I3
COVAR_COLS
COVAR_NORMAL
COVAR_ROWS
COVAR_SCALE
COVAR_SCRAMBLED
COVAR_USE_AVG
CV_16S
CV_16SC1
CV_16SC2
CV_16SC3
CV_16SC4
CV_16U
CV_16UC1
CV_16UC2
CV_16UC3
CV_16UC4
CV_32F
CV_32FC1
CV_32FC2
CV_32FC3
CV_32FC4
CV_32S
CV_32SC1
CV_32SC2
CV_32SC3
CV_32SC4
CV_64F
CV_64FC1
CV_64FC2
CV_64FC3
CV_64FC4
CV_8S
CV_8SC1
CV_8SC2
CV_8SC3
CV_8SC4
CV_8U
CV_8UC1
CV_8UC2
CV_8UC3
CV_8UC4
CV_FEATURE_PARAMS_HAAR
CV_FEATURE_PARAMS_HOG
CV_FEATURE_PARAMS_LBP
CalibrateCRF
CalibrateDebevec
CalibrateRobertson
CamShift
Canny
CascadeClassifier
CascadeClassifier_convert
ChiHistogramCostExtractor
CirclesGridFinderParameters
CirclesGridFinderParameters2
CirclesGridFinderParameters_ASYMMETRIC_GRID
CirclesGridFinderParameters_SYMMETRIC_GRID
CvFeatureParams_HAAR
CvFeatureParams_HOG
CvFeatureParams_LBP
DCT_INVERSE
DCT_ROWS
DECOMP_CHOLESKY
DECOMP_EIG
DECOMP_LU
DECOMP_NORMAL
DECOMP_QR
DECOMP_SVD
DESCRIPTOR_MATCHER_BRUTEFORCE
DESCRIPTOR_MATCHER_BRUTEFORCE_HAMMING
DESCRIPTOR_MATCHER_BRUTEFORCE_HAMMINGLUT
DESCRIPTOR_MATCHER_BRUTEFORCE_L1
DESCRIPTOR_MATCHER_BRUTEFORCE_SL2
DESCRIPTOR_MATCHER_FLANNBASED
DFT_COMPLEX_INPUT
DFT_COMPLEX_OUTPUT
DFT_INVERSE
DFT_REAL_OUTPUT
DFT_ROWS
DFT_SCALE
DIST_C
DIST_FAIR
DIST_HUBER
DIST_L1
DIST_L12
DIST_L2
DIST_LABEL_CCOMP
DIST_LABEL_PIXEL
DIST_MASK_3
DIST_MASK_5
DIST_MASK_PRECISE
DIST_USER
DIST_WELSCH
DMatch
DRAW_MATCHES_FLAGS_DEFAULT
DRAW_MATCHES_FLAGS_DRAW_OVER_OUTIMG
DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS
DRAW_MATCHES_FLAGS_NOT_DRAW_SINGLE_POINTS
DenseOpticalFlow
DescriptorMatcher
DescriptorMatcher_BRUTEFORCE
DescriptorMatcher_BRUTEFORCE_HAMMING
DescriptorMatcher_BRUTEFORCE_HAMMINGLUT
DescriptorMatcher_BRUTEFORCE_L1
DescriptorMatcher_BRUTEFORCE_SL2
DescriptorMatcher_FLANNBASED
DescriptorMatcher_create
DrawMatchesFlags_DEFAULT
DrawMatchesFlags_DRAW_OVER_OUTIMG
DrawMatchesFlags_DRAW_RICH_KEYPOINTS
DrawMatchesFlags_NOT_DRAW_SINGLE_POINTS
DualTVL1OpticalFlow
DualTVL1OpticalFlow_create
EMD
EMDHistogramCostExtractor
EMDL1HistogramCostExtractor
EVENT_FLAG_ALTKEY
EVENT_FLAG_CTRLKEY
EVENT_FLAG_LBUTTON
EVENT_FLAG_MBUTTON
EVENT_FLAG_RBUTTON
EVENT_FLAG_SHIFTKEY
EVENT_LBUTTONDBLCLK
EVENT_LBUTTONDOWN
EVENT_LBUTTONUP
EVENT_MBUTTONDBLCLK
EVENT_MBUTTONDOWN
EVENT_MBUTTONUP
EVENT_MOUSEHWHEEL
EVENT_MOUSEMOVE
EVENT_MOUSEWHEEL
EVENT_RBUTTONDBLCLK
EVENT_RBUTTONDOWN
EVENT_RBUTTONUP
Error
FAST_FEATURE_DETECTOR_FAST_N
FAST_FEATURE_DETECTOR_NONMAX_SUPPRESSION
FAST_FEATURE_DETECTOR_THRESHOLD
FAST_FEATURE_DETECTOR_TYPE_5_8
FAST_FEATURE_DETECTOR_TYPE_7_12
FAST_FEATURE_DETECTOR_TYPE_9_16
FILE_NODE_EMPTY
FILE_NODE_FLOAT
FILE_NODE_FLOW
FILE_NODE_INT
FILE_NODE_MAP
FILE_NODE_NAMED
FILE_NODE_NONE
FILE_NODE_REAL
FILE_NODE_REF
FILE_NODE_SEQ
FILE_NODE_STR
FILE_NODE_STRING
FILE_NODE_TYPE_MASK
FILE_NODE_USER
FILE_STORAGE_APPEND
FILE_STORAGE_BASE64
FILE_STORAGE_FORMAT_AUTO
FILE_STORAGE_FORMAT_JSON
FILE_STORAGE_FORMAT_MASK
FILE_STORAGE_FORMAT_XML
FILE_STORAGE_FORMAT_YAML
FILE_STORAGE_INSIDE_MAP
FILE_STORAGE_MEMORY
FILE_STORAGE_NAME_EXPECTED
FILE_STORAGE_READ
FILE_STORAGE_UNDEFINED
FILE_STORAGE_VALUE_EXPECTED
FILE_STORAGE_WRITE
FILE_STORAGE_WRITE_BASE64
FILLED
FLOODFILL_FIXED_RANGE
FLOODFILL_MASK_ONLY
FM_7POINT
FM_8POINT
FM_LMEDS
FM_RANSAC
FONT_HERSHEY_COMPLEX
FONT_HERSHEY_COMPLEX_SMALL
FONT_HERSHEY_DUPLEX
FONT_HERSHEY_PLAIN
FONT_HERSHEY_SCRIPT_COMPLEX
FONT_HERSHEY_SCRIPT_SIMPLEX
FONT_HERSHEY_SIMPLEX
FONT_HERSHEY_TRIPLEX
FONT_ITALIC
FORMATTER_FMT_C
FORMATTER_FMT_CSV
FORMATTER_FMT_DEFAULT
FORMATTER_FMT_MATLAB
FORMATTER_FMT_NUMPY
FORMATTER_FMT_PYTHON
FarnebackOpticalFlow
FarnebackOpticalFlow_create
FastFeatureDetector
FastFeatureDetector_FAST_N
FastFeatureDetector_NONMAX_SUPPRESSION
FastFeatureDetector_THRESHOLD
FastFeatureDetector_TYPE_5_8
FastFeatureDetector_TYPE_7_12
FastFeatureDetector_TYPE_9_16
FastFeatureDetector_create
Feature2D
FileNode
FileNode_EMPTY
FileNode_FLOAT
FileNode_FLOW
FileNode_INT
FileNode_MAP
FileNode_NAMED
FileNode_NONE
FileNode_REAL
FileNode_REF
FileNode_SEQ
FileNode_STR
FileNode_STRING
FileNode_TYPE_MASK
FileNode_USER
FileStorage
FileStorage_APPEND
FileStorage_BASE64
FileStorage_FORMAT_AUTO
FileStorage_FORMAT_JSON
FileStorage_FORMAT_MASK
FileStorage_FORMAT_XML
FileStorage_FORMAT_YAML
FileStorage_INSIDE_MAP
FileStorage_MEMORY
FileStorage_NAME_EXPECTED
FileStorage_READ
FileStorage_UNDEFINED
FileStorage_VALUE_EXPECTED
FileStorage_WRITE
FileStorage_WRITE_BASE64
FlannBasedMatcher
FlannBasedMatcher_create
Formatter_FMT_C
Formatter_FMT_CSV
Formatter_FMT_DEFAULT
Formatter_FMT_MATLAB
Formatter_FMT_NUMPY
Formatter_FMT_PYTHON
GC_BGD
GC_EVAL
GC_FGD
GC_INIT_WITH_MASK
GC_INIT_WITH_RECT
GC_PR_BGD
GC_PR_FGD
GEMM_1_T
GEMM_2_T
GEMM_3_T
GFTTDetector
GFTTDetector_create
GaussianBlur
HAMMING_NORM_TYPE
HISTCMP_BHATTACHARYYA
HISTCMP_CHISQR
HISTCMP_CHISQR_ALT
HISTCMP_CORREL
HISTCMP_HELLINGER
HISTCMP_INTERSECT
HISTCMP_KL_DIV
HOGDESCRIPTOR_DEFAULT_NLEVELS
HOGDESCRIPTOR_L2HYS
HOGDescriptor
HOGDescriptor_DEFAULT_NLEVELS
HOGDescriptor_L2Hys
HOGDescriptor_getDaimlerPeopleDetector
HOGDescriptor_getDefaultPeopleDetector
HOUGH_GRADIENT
HOUGH_MULTI_SCALE
HOUGH_PROBABILISTIC
HOUGH_STANDARD
Hamming_normType
HausdorffDistanceExtractor
HistogramCostExtractor
HoughCircles
HoughLines
HoughLinesP
HuMoments
IMREAD_ANYCOLOR
IMREAD_ANYDEPTH
IMREAD_COLOR
IMREAD_GRAYSCALE
IMREAD_IGNORE_ORIENTATION
IMREAD_LOAD_GDAL
IMREAD_REDUCED_COLOR_2
IMREAD_REDUCED_COLOR_4
IMREAD_REDUCED_COLOR_8
IMREAD_REDUCED_GRAYSCALE_2
IMREAD_REDUCED_GRAYSCALE_4
IMREAD_REDUCED_GRAYSCALE_8
IMREAD_UNCHANGED
IMWRITE_EXR_TYPE
IMWRITE_EXR_TYPE_FLOAT
IMWRITE_EXR_TYPE_HALF
IMWRITE_JPEG_CHROMA_QUALITY
IMWRITE_JPEG_LUMA_QUALITY
IMWRITE_JPEG_OPTIMIZE
IMWRITE_JPEG_PROGRESSIVE
IMWRITE_JPEG_QUALITY
IMWRITE_JPEG_RST_INTERVAL
IMWRITE_PAM_FORMAT_BLACKANDWHITE
IMWRITE_PAM_FORMAT_GRAYSCALE
IMWRITE_PAM_FORMAT_GRAYSCALE_ALPHA
IMWRITE_PAM_FORMAT_NULL
IMWRITE_PAM_FORMAT_RGB
IMWRITE_PAM_FORMAT_RGB_ALPHA
IMWRITE_PAM_TUPLETYPE
IMWRITE_PNG_BILEVEL
IMWRITE_PNG_COMPRESSION
IMWRITE_PNG_STRATEGY
IMWRITE_PNG_STRATEGY_DEFAULT
IMWRITE_PNG_STRATEGY_FILTERED
IMWRITE_PNG_STRATEGY_FIXED
IMWRITE_PNG_STRATEGY_HUFFMAN_ONLY
IMWRITE_PNG_STRATEGY_RLE
IMWRITE_PXM_BINARY
IMWRITE_WEBP_QUALITY
INPAINT_NS
INPAINT_TELEA
INTERSECT_FULL
INTERSECT_NONE
INTERSECT_PARTIAL
INTER_AREA
INTER_BITS
INTER_BITS2
INTER_CUBIC
INTER_LANCZOS4
INTER_LINEAR
INTER_LINEAR_EXACT
INTER_MAX
INTER_NEAREST
INTER_TAB_SIZE
INTER_TAB_SIZE2
KAZE
KAZE_DIFF_CHARBONNIER
KAZE_DIFF_PM_G1
KAZE_DIFF_PM_G2
KAZE_DIFF_WEICKERT
KAZE_create
KMEANS_PP_CENTERS
KMEANS_RANDOM_CENTERS
KMEANS_USE_INITIAL_LABELS
KalmanFilter
KeyPoint
KeyPoint_convert
KeyPoint_overlap
LDR_SIZE
LINE_4
LINE_8
LINE_AA
LMEDS
LSD_REFINE_ADV
LSD_REFINE_NONE
LSD_REFINE_STD
LUT
Laplacian
LineSegmentDetector
MARKER_CROSS
MARKER_DIAMOND
MARKER_SQUARE
MARKER_STAR
MARKER_TILTED_CROSS
MARKER_TRIANGLE_DOWN
MARKER_TRIANGLE_UP
MAT_AUTO_STEP
MAT_CONTINUOUS_FLAG
MAT_DEPTH_MASK
MAT_MAGIC_MASK
MAT_MAGIC_VAL
MAT_SUBMATRIX_FLAG
MAT_TYPE_MASK
MIXED_CLONE
MONOCHROME_TRANSFER
MORPH_BLACKHAT
MORPH_CLOSE
MORPH_CROSS
MORPH_DILATE
MORPH_ELLIPSE
MORPH_ERODE
MORPH_GRADIENT
MORPH_HITMISS
MORPH_OPEN
MORPH_RECT
MORPH_TOPHAT
MOTION_AFFINE
MOTION_EUCLIDEAN
MOTION_HOMOGRAPHY
MOTION_TRANSLATION
MSER
MSER_create
Mahalanobis
Mat_AUTO_STEP
Mat_CONTINUOUS_FLAG
Mat_DEPTH_MASK
Mat_MAGIC_MASK
Mat_MAGIC_VAL
Mat_SUBMATRIX_FLAG
Mat_TYPE_MASK
MergeDebevec
MergeExposures
MergeMertens
MergeRobertson
MultiTracker
MultiTracker_create
NORMAL_CLONE
NORMCONV_FILTER
NORM_HAMMING
NORM_HAMMING2
NORM_INF
NORM_L1
NORM_L2
NORM_L2SQR
NORM_MINMAX
NORM_RELATIVE
NORM_TYPE_MASK
NormHistogramCostExtractor
OPTFLOW_FARNEBACK_GAUSSIAN
OPTFLOW_LK_GET_MIN_EIGENVALS
OPTFLOW_USE_INITIAL_FLOW
ORB
ORB_FAST_SCORE
ORB_HARRIS_SCORE
ORB_K_BYTES
ORB_create
ORB_kBytes
PARAM_ALGORITHM
PARAM_BOOLEAN
PARAM_FLOAT
PARAM_INT
PARAM_MAT
PARAM_MAT_VECTOR
PARAM_REAL
PARAM_STRING
PARAM_UCHAR
PARAM_UINT64
PARAM_UNSIGNED_INT
PCABackProject
PCACompute
PCAProject
PCA_DATA_AS_COL
PCA_DATA_AS_ROW
PCA_USE_AVG
PROJ_SPHERICAL_EQRECT
PROJ_SPHERICAL_ORTHO
PSNR
Param_ALGORITHM
Param_BOOLEAN
Param_FLOAT
Param_INT
Param_MAT
Param_MAT_VECTOR
Param_REAL
Param_STRING
Param_UCHAR
Param_UINT64
Param_UNSIGNED_INT
QT_CHECKBOX
QT_FONT_BLACK
QT_FONT_BOLD
QT_FONT_DEMIBOLD
QT_FONT_LIGHT
QT_FONT_NORMAL
QT_NEW_BUTTONBAR
QT_PUSH_BUTTON
QT_RADIOBOX
QT_STYLE_ITALIC
QT_STYLE_NORMAL
QT_STYLE_OBLIQUE
RANSAC
RECURS_FILTER
REDUCE_AVG
REDUCE_MAX
REDUCE_MIN
REDUCE_SUM
RETR_CCOMP
RETR_EXTERNAL
RETR_FLOODFILL
RETR_LIST
RETR_TREE
RHO
RNG_NORMAL
RNG_UNIFORM
ROTATE_180
ROTATE_90_CLOCKWISE
ROTATE_90_COUNTERCLOCKWISE
RQDecomp3x3
Rodrigues
SOLVELP_MULTI
SOLVELP_SINGLE
SOLVELP_UNBOUNDED
SOLVELP_UNFEASIBLE
SOLVEPNP_AP3P
SOLVEPNP_DLS
SOLVEPNP_EPNP
SOLVEPNP_ITERATIVE
SOLVEPNP_MAX_COUNT
SOLVEPNP_P3P
SOLVEPNP_UPNP
SORT_ASCENDING
SORT_DESCENDING
SORT_EVERY_COLUMN
SORT_EVERY_ROW
SPARSE_MAT_HASH_BIT
SPARSE_MAT_HASH_SCALE
SPARSE_MAT_MAGIC_VAL
SPARSE_MAT_MAX_DIM
STEREO_BM_PREFILTER_NORMALIZED_RESPONSE
STEREO_BM_PREFILTER_XSOBEL
STEREO_MATCHER_DISP_SCALE
STEREO_MATCHER_DISP_SHIFT
STEREO_SGBM_MODE_HH
STEREO_SGBM_MODE_HH4
STEREO_SGBM_MODE_SGBM
STEREO_SGBM_MODE_SGBM_3WAY
STITCHER_ERR_CAMERA_PARAMS_ADJUST_FAIL
STITCHER_ERR_HOMOGRAPHY_EST_FAIL
STITCHER_ERR_NEED_MORE_IMGS
STITCHER_OK
STITCHER_ORIG_RESOL
STITCHER_PANORAMA
STITCHER_SCANS
SUBDIV2D_NEXT_AROUND_DST
SUBDIV2D_NEXT_AROUND_LEFT
SUBDIV2D_NEXT_AROUND_ORG
SUBDIV2D_NEXT_AROUND_RIGHT
SUBDIV2D_PREV_AROUND_DST
SUBDIV2D_PREV_AROUND_LEFT
SUBDIV2D_PREV_AROUND_ORG
SUBDIV2D_PREV_AROUND_RIGHT
SUBDIV2D_PTLOC_ERROR
SUBDIV2D_PTLOC_INSIDE
SUBDIV2D_PTLOC_ON_EDGE
SUBDIV2D_PTLOC_OUTSIDE_RECT
SUBDIV2D_PTLOC_VERTEX
SVBackSubst
SVD_FULL_UV
SVD_MODIFY_A
SVD_NO_UV
SVDecomp
Scharr
ShapeContextDistanceExtractor
ShapeDistanceExtractor
ShapeTransformer
SimpleBlobDetector
SimpleBlobDetector_Params
SimpleBlobDetector_create
Sobel
SparseMat_HASH_BIT
SparseMat_HASH_SCALE
SparseMat_MAGIC_VAL
SparseMat_MAX_DIM
SparseOpticalFlow
SparsePyrLKOpticalFlow
SparsePyrLKOpticalFlow_create
StereoBM
StereoBM_PREFILTER_NORMALIZED_RESPONSE
StereoBM_PREFILTER_XSOBEL
StereoBM_create
StereoMatcher
StereoMatcher_DISP_SCALE
StereoMatcher_DISP_SHIFT
StereoSGBM
StereoSGBM_MODE_HH
StereoSGBM_MODE_HH4
StereoSGBM_MODE_SGBM
StereoSGBM_MODE_SGBM_3WAY
StereoSGBM_create
Stitcher
Stitcher_ERR_CAMERA_PARAMS_ADJUST_FAIL
Stitcher_ERR_HOMOGRAPHY_EST_FAIL
Stitcher_ERR_NEED_MORE_IMGS
Stitcher_OK
Stitcher_ORIG_RESOL
Stitcher_PANORAMA
Stitcher_SCANS
Subdiv2D
Subdiv2D_NEXT_AROUND_DST
Subdiv2D_NEXT_AROUND_LEFT
Subdiv2D_NEXT_AROUND_ORG
Subdiv2D_NEXT_AROUND_RIGHT
Subdiv2D_PREV_AROUND_DST
Subdiv2D_PREV_AROUND_LEFT
Subdiv2D_PREV_AROUND_ORG
Subdiv2D_PREV_AROUND_RIGHT
Subdiv2D_PTLOC_ERROR
Subdiv2D_PTLOC_INSIDE
Subdiv2D_PTLOC_ON_EDGE
Subdiv2D_PTLOC_OUTSIDE_RECT
Subdiv2D_PTLOC_VERTEX
TERM_CRITERIA_COUNT
TERM_CRITERIA_EPS
TERM_CRITERIA_MAX_ITER
THRESH_BINARY
THRESH_BINARY_INV
THRESH_MASK
THRESH_OTSU
THRESH_TOZERO
THRESH_TOZERO_INV
THRESH_TRIANGLE
THRESH_TRUNC
TM_CCOEFF
TM_CCOEFF_NORMED
TM_CCORR
TM_CCORR_NORMED
TM_SQDIFF
TM_SQDIFF_NORMED
TRACKER_KCF_CN
TRACKER_KCF_CUSTOM
TRACKER_KCF_GRAY
TRACKER_SAMPLER_CSC_MODE_DETECT
TRACKER_SAMPLER_CSC_MODE_INIT_NEG
TRACKER_SAMPLER_CSC_MODE_INIT_POS
TRACKER_SAMPLER_CSC_MODE_TRACK_NEG
TRACKER_SAMPLER_CSC_MODE_TRACK_POS
TRACKER_SAMPLER_CS_MODE_CLASSIFY
TRACKER_SAMPLER_CS_MODE_NEGATIVE
TRACKER_SAMPLER_CS_MODE_POSITIVE
TermCriteria_COUNT
TermCriteria_EPS
TermCriteria_MAX_ITER
ThinPlateSplineShapeTransformer
TickMeter
Tonemap
TonemapDrago
TonemapDurand
TonemapMantiuk
TonemapReinhard
Tracker
TrackerBoosting
TrackerBoosting_create
TrackerGOTURN
TrackerGOTURN_create
TrackerKCF
TrackerKCF_CN
TrackerKCF_CUSTOM
TrackerKCF_GRAY
TrackerKCF_create
TrackerMIL
TrackerMIL_create
TrackerMOSSE
TrackerMOSSE_create
TrackerMedianFlow
TrackerMedianFlow_create
TrackerSamplerCSC_MODE_DETECT
TrackerSamplerCSC_MODE_INIT_NEG
TrackerSamplerCSC_MODE_INIT_POS
TrackerSamplerCSC_MODE_TRACK_NEG
TrackerSamplerCSC_MODE_TRACK_POS
TrackerSamplerCS_MODE_CLASSIFY
TrackerSamplerCS_MODE_NEGATIVE
TrackerSamplerCS_MODE_POSITIVE
TrackerTLD
TrackerTLD_create
UMAT_AUTO_STEP
UMAT_CONTINUOUS_FLAG
UMAT_DATA_ASYNC_CLEANUP
UMAT_DATA_COPY_ON_MAP
UMAT_DATA_DEVICE_COPY_OBSOLETE
UMAT_DATA_DEVICE_MEM_MAPPED
UMAT_DATA_HOST_COPY_OBSOLETE
UMAT_DATA_TEMP_COPIED_UMAT
UMAT_DATA_TEMP_UMAT
UMAT_DATA_USER_ALLOCATED
UMAT_DEPTH_MASK
UMAT_MAGIC_MASK
UMAT_MAGIC_VAL
UMAT_SUBMATRIX_FLAG
UMAT_TYPE_MASK
UMat
UMatData_ASYNC_CLEANUP
UMatData_COPY_ON_MAP
UMatData_DEVICE_COPY_OBSOLETE
UMatData_DEVICE_MEM_MAPPED
UMatData_HOST_COPY_OBSOLETE
UMatData_TEMP_COPIED_UMAT
UMatData_TEMP_UMAT
UMatData_USER_ALLOCATED
UMat_AUTO_STEP
UMat_CONTINUOUS_FLAG
UMat_DEPTH_MASK
UMat_MAGIC_MASK
UMat_MAGIC_VAL
UMat_SUBMATRIX_FLAG
UMat_TYPE_MASK
USAGE_ALLOCATE_DEVICE_MEMORY
USAGE_ALLOCATE_HOST_MEMORY
USAGE_ALLOCATE_SHARED_MEMORY
USAGE_DEFAULT
VIDEOWRITER_PROP_FRAMEBYTES
VIDEOWRITER_PROP_NSTRIPES
VIDEOWRITER_PROP_QUALITY
VideoCapture
VideoWriter
VideoWriter_fourcc
WARP_FILL_OUTLIERS
WARP_INVERSE_MAP
WINDOW_AUTOSIZE
WINDOW_FREERATIO
WINDOW_FULLSCREEN
WINDOW_GUI_EXPANDED
WINDOW_GUI_NORMAL
WINDOW_KEEPRATIO
WINDOW_NORMAL
WINDOW_OPENGL
WND_PROP_ASPECT_RATIO
WND_PROP_AUTOSIZE
WND_PROP_FULLSCREEN
WND_PROP_OPENGL
WND_PROP_VISIBLE
_INPUT_ARRAY_CUDA_GPU_MAT
_INPUT_ARRAY_CUDA_HOST_MEM
_INPUT_ARRAY_EXPR
_INPUT_ARRAY_FIXED_SIZE
_INPUT_ARRAY_FIXED_TYPE
_INPUT_ARRAY_KIND_MASK
_INPUT_ARRAY_KIND_SHIFT
_INPUT_ARRAY_MAT
_INPUT_ARRAY_MATX
_INPUT_ARRAY_NONE
_INPUT_ARRAY_OPENGL_BUFFER
_INPUT_ARRAY_STD_ARRAY
_INPUT_ARRAY_STD_ARRAY_MAT
_INPUT_ARRAY_STD_BOOL_VECTOR
_INPUT_ARRAY_STD_VECTOR
_INPUT_ARRAY_STD_VECTOR_CUDA_GPU_MAT
_INPUT_ARRAY_STD_VECTOR_MAT
_INPUT_ARRAY_STD_VECTOR_UMAT
_INPUT_ARRAY_STD_VECTOR_VECTOR
_INPUT_ARRAY_UMAT
_InputArray_CUDA_GPU_MAT
_InputArray_CUDA_HOST_MEM
_InputArray_EXPR
_InputArray_FIXED_SIZE
_InputArray_FIXED_TYPE
_InputArray_KIND_MASK
_InputArray_KIND_SHIFT
_InputArray_MAT
_InputArray_MATX
_InputArray_NONE
_InputArray_OPENGL_BUFFER
_InputArray_STD_ARRAY
_InputArray_STD_ARRAY_MAT
_InputArray_STD_BOOL_VECTOR
_InputArray_STD_VECTOR
_InputArray_STD_VECTOR_CUDA_GPU_MAT
_InputArray_STD_VECTOR_MAT
_InputArray_STD_VECTOR_UMAT
_InputArray_STD_VECTOR_VECTOR
_InputArray_UMAT
_OUTPUT_ARRAY_DEPTH_MASK_16S
_OUTPUT_ARRAY_DEPTH_MASK_16U
_OUTPUT_ARRAY_DEPTH_MASK_32F
_OUTPUT_ARRAY_DEPTH_MASK_32S
_OUTPUT_ARRAY_DEPTH_MASK_64F
_OUTPUT_ARRAY_DEPTH_MASK_8S
_OUTPUT_ARRAY_DEPTH_MASK_8U
_OUTPUT_ARRAY_DEPTH_MASK_ALL
_OUTPUT_ARRAY_DEPTH_MASK_ALL_BUT_8S
_OUTPUT_ARRAY_DEPTH_MASK_FLT
_OutputArray_DEPTH_MASK_16S
_OutputArray_DEPTH_MASK_16U
_OutputArray_DEPTH_MASK_32F
_OutputArray_DEPTH_MASK_32S
_OutputArray_DEPTH_MASK_64F
_OutputArray_DEPTH_MASK_8S
_OutputArray_DEPTH_MASK_8U
_OutputArray_DEPTH_MASK_ALL
_OutputArray_DEPTH_MASK_ALL_BUT_8S
_OutputArray_DEPTH_MASK_FLT
__UMAT_USAGE_FLAGS_32BIT
__builtins__
__cached__
__doc__
__file__
__loader__
__name__
__package__
__path__
__spec__
__version__
absdiff
accumulate
accumulateProduct
accumulateSquare
accumulateWeighted
adaptiveThreshold
add
addText
addWeighted
applyColorMap
approxPolyDP
arcLength
arrowedLine
aruco
aruco_Board
aruco_CharucoBoard
aruco_DetectorParameters
aruco_Dictionary
aruco_GridBoard
batchDistance
bgsegm
bgsegm_BackgroundSubtractorCNT
bgsegm_BackgroundSubtractorGMG
bgsegm_BackgroundSubtractorGSOC
bgsegm_BackgroundSubtractorLSBP
bgsegm_BackgroundSubtractorLSBPDesc
bgsegm_BackgroundSubtractorMOG
bgsegm_SyntheticSequenceGenerator
bilateralFilter
bioinspired
bioinspired_Retina
bioinspired_RetinaFastToneMapping
bioinspired_TransientAreasSegmentationModule
bitwise_and
bitwise_not
bitwise_or
bitwise_xor
blur
borderInterpolate
boundingRect
boxFilter
boxPoints
buildOpticalFlowPyramid
calcBackProject
calcCovarMatrix
calcHist
calcOpticalFlowFarneback
calcOpticalFlowPyrLK
calibrateCamera
calibrateCameraExtended
calibrationMatrixValues
cartToPolar
checkHardwareSupport
checkRange
circle
clipLine
colorChange
compare
compareHist
completeSymm
composeRT
computeCorrespondEpilines
connectedComponents
connectedComponentsWithAlgorithm
connectedComponentsWithStats
connectedComponentsWithStatsWithAlgorithm
contourArea
convertFp16
convertMaps
convertPointsFromHomogeneous
convertPointsToHomogeneous
convertScaleAbs
convexHull
convexityDefects
copyMakeBorder
cornerEigenValsAndVecs
cornerHarris
cornerMinEigenVal
cornerSubPix
correctMatches
countNonZero
createAffineTransformer
createAlignMTB
createBackgroundSubtractorKNN
createBackgroundSubtractorMOG2
createButton
createCLAHE
createCalibrateDebevec
createCalibrateRobertson
createChiHistogramCostExtractor
createEMDHistogramCostExtractor
createEMDL1HistogramCostExtractor
createHanningWindow
createHausdorffDistanceExtractor
createLineSegmentDetector
createMergeDebevec
createMergeMertens
createMergeRobertson
createNormHistogramCostExtractor
createOptFlow_DualTVL1
createShapeContextDistanceExtractor
createStitcher
createThinPlateSplineShapeTransformer
createTonemap
createTonemapDrago
createTonemapDurand
createTonemapMantiuk
createTonemapReinhard
createTrackbar
cubeRoot
cuda
cv2
cvtColor
data
datasets
dct
decolor
decomposeEssentialMat
decomposeHomographyMat
decomposeProjectionMatrix
demosaicing
denoise_TVL1
destroyAllWindows
destroyWindow
detail
detailEnhance
determinant
dft
dilate
displayOverlay
displayStatusBar
distanceTransform
distanceTransformWithLabels
divide
dnn
dnn_DictValue
dnn_Layer
dnn_Net
dpm_DPMDetector
dpm_DPMDetector_ObjectDetection
drawChessboardCorners
drawContours
drawKeypoints
drawMarker
drawMatches
drawMatchesKnn
edgePreservingFilter
eigen
eigenNonSymmetric
ellipse
ellipse2Poly
equalizeHist
erode
error
estimateAffine2D
estimateAffine3D
estimateAffinePartial2D
estimateRigidTransform
exp
extractChannel
face
face_BIF
face_BasicFaceRecognizer
face_EigenFaceRecognizer
face_FaceRecognizer
face_Facemark
face_FacemarkAAM
face_FacemarkKazemi
face_FacemarkLBF
face_FisherFaceRecognizer
face_LBPHFaceRecognizer
face_PredictCollector
face_StandardCollector
fastAtan2
fastNlMeansDenoising
fastNlMeansDenoisingColored
fastNlMeansDenoisingColoredMulti
fastNlMeansDenoisingMulti
fillConvexPoly
fillPoly
filter2D
filterSpeckles
findChessboardCorners
findCirclesGrid
findCirclesGrid2
findContours
findEssentialMat
findFundamentalMat
findHomography
findNonZero
findTransformECC
fisheye
fitEllipse
fitEllipseAMS
fitEllipseDirect
fitLine
flann
flann_Index
flip
floodFill
ft
gemm
getAffineTransform
getBuildInformation
getCPUTickCount
getDefaultNewCameraMatrix
getDerivKernels
getGaborKernel
getGaussianKernel
getNumThreads
getNumberOfCPUs
getOptimalDFTSize
getOptimalNewCameraMatrix
getPerspectiveTransform
getRectSubPix
getRotationMatrix2D
getStructuringElement
getTextSize
getThreadNum
getTickCount
getTickFrequency
getTrackbarPos
getValidDisparityROI
getWindowProperty
goodFeaturesToTrack
grabCut
groupRectangles
haarcascades
haveOpenVX
hconcat
idct
idft
illuminationChange
imdecode
imencode
img_hash
img_hash_AverageHash
img_hash_BlockMeanHash
img_hash_ColorMomentHash
img_hash_ImgHashBase
img_hash_MarrHildrethHash
img_hash_PHash
img_hash_RadialVarianceHash
importlib
imread
imreadmulti
imshow
imwrite
inRange
initCameraMatrix2D
initUndistortRectifyMap
initWideAngleProjMap
inpaint
insertChannel
instr
integral
integral2
integral3
intersectConvexConvex
invert
invertAffineTransform
ipp
isContourConvex
kmeans
line
line_descriptor
linearPolar
linemod
linemod_Detector
linemod_Feature
linemod_Match
linemod_Modality
linemod_QuantizedPyramid
linemod_Template
log
logPolar
magnitude
matMulDeriv
matchShapes
matchTemplate
max
mean
meanShift
meanStdDev
medianBlur
merge
min
minAreaRect
minEnclosingCircle
minEnclosingTriangle
minMaxLoc
mixChannels
ml
ml_ANN_MLP
ml_ANN_MLP_ANNEAL
ml_Boost
ml_DTrees
ml_EM
ml_KNearest
ml_LogisticRegression
ml_NormalBayesClassifier
ml_ParamGrid
ml_RTrees
ml_SVM
ml_SVMSGD
ml_StatModel
ml_TrainData
moments
morphologyEx
motempl
moveWindow
mulSpectrums
mulTransposed
multicalib
multiply
namedWindow
norm
normalize
ocl
ogl
omnidir
optflow
optflow_DISOpticalFlow
optflow_GPCDetails
optflow_GPCPatchDescriptor
optflow_GPCPatchSample
optflow_GPCTrainingSamples
optflow_GPCTree
optflow_OpticalFlowPCAFlow
optflow_PCAPrior
optflow_VariationalRefinement
os
patchNaNs
pencilSketch
perspectiveTransform
phase
phaseCorrelate
phase_unwrapping_HistogramPhaseUnwrapping
phase_unwrapping_PhaseUnwrapping
plot
plot_Plot2d
pointPolygonTest
polarToCart
polylines
pow
ppf_match_3d
ppf_match_3d_ICP
ppf_match_3d_PPF3DDetector
ppf_match_3d_PoseCluster3D
preCornerDetect
projectPoints
putText
pyrDown
pyrMeanShiftFiltering
pyrUp
randShuffle
randn
randu
recoverPose
rectangle
rectify3Collinear
reduce
reg
reg_Map
reg_MapAffine
reg_MapProjec
reg_MapShift
reg_MapTypeCaster
reg_Mapper
reg_MapperGradAffine
reg_MapperGradEuclid
reg_MapperGradProj
reg_MapperGradShift
reg_MapperGradSimilar
reg_MapperPyramid
remap
repeat
reprojectImageTo3D
resize
resizeWindow
rgbd
rgbd_DepthCleaner
rgbd_ICPOdometry
rgbd_Odometry
rgbd_OdometryFrame
rgbd_RgbdFrame
rgbd_RgbdICPOdometry
rgbd_RgbdNormals
rgbd_RgbdOdometry
rgbd_RgbdPlane
rotate
rotatedRectangleIntersection
saliency
saliency_MotionSaliency
saliency_MotionSaliencyBinWangApr2014
saliency_Objectness
saliency_ObjectnessBING
saliency_Saliency
saliency_StaticSaliency
saliency_StaticSaliencyFineGrained
saliency_StaticSaliencySpectralResidual
sampsonDistance
scaleAdd
seamlessClone
selectROI
selectROIs
sepFilter2D
setIdentity
setMouseCallback
setNumThreads
setRNGSeed
setTrackbarMax
setTrackbarMin
setTrackbarPos
setUseOpenVX
setUseOptimized
setWindowProperty
setWindowTitle
solve
solveCubic
solveLP
solveP3P
solvePnP
solvePnPRansac
solvePoly
sort
sortIdx
spatialGradient
split
sqrBoxFilter
sqrt
startWindowThread
stereoCalibrate
stereoRectify
stereoRectifyUncalibrated
structured_light
structured_light_GrayCodePattern
structured_light_SinusoidalPattern
structured_light_SinusoidalPattern_Params
structured_light_StructuredLightPattern
stylization
subtract
sumElems
text
text_BaseOCR
text_ERFilter
text_ERFilter_Callback
text_OCRBeamSearchDecoder
text_OCRBeamSearchDecoder_ClassifierCallback
text_OCRHMMDecoder
text_OCRHMMDecoder_ClassifierCallback
text_OCRTesseract
text_TextDetector
text_TextDetectorCNN
textureFlattening
threshold
trace
transform
transpose
triangulatePoints
undistort
undistortPoints
undistortPointsIter
useOpenVX
useOptimized
validateDisparity
vconcat
videostab
waitKey
waitKeyEx
warpAffine
warpPerspective
watershed
xfeatures2d
xfeatures2d_BoostDesc
xfeatures2d_BriefDescriptorExtractor
xfeatures2d_DAISY
xfeatures2d_FREAK
xfeatures2d_HarrisLaplaceFeatureDetector
xfeatures2d_LATCH
xfeatures2d_LUCID
xfeatures2d_MSDDetector
xfeatures2d_PCTSignatures
xfeatures2d_PCTSignaturesSQFD
xfeatures2d_SIFT
xfeatures2d_SURF
xfeatures2d_StarDetector
xfeatures2d_VGG
ximgproc
ximgproc_AdaptiveManifoldFilter
ximgproc_ContourFitting
ximgproc_DTFilter
ximgproc_DisparityFilter
ximgproc_DisparityWLSFilter
ximgproc_EdgeAwareInterpolator
ximgproc_EdgeBoxes
ximgproc_FastGlobalSmootherFilter
ximgproc_FastLineDetector
ximgproc_GuidedFilter
ximgproc_RFFeatureGetter
ximgproc_RidgeDetectionFilter
ximgproc_SparseMatchInterpolator
ximgproc_StructuredEdgeDetection
ximgproc_SuperpixelLSC
ximgproc_SuperpixelSEEDS
ximgproc_SuperpixelSLIC
ximgproc_segmentation_GraphSegmentation
ximgproc_segmentation_SelectiveSearchSegmentation
ximgproc_segmentation_SelectiveSearchSegmentationStrategy
ximgproc_segmentation_SelectiveSearchSegmentationStrategyColor
ximgproc_segmentation_SelectiveSearchSegmentationStrategyFill
ximgproc_segmentation_SelectiveSearchSegmentationStrategyMultiple
ximgproc_segmentation_SelectiveSearchSegmentationStrategySize
ximgproc_segmentation_SelectiveSearchSegmentationStrategyTexture
xphoto
xphoto_GrayworldWB
xphoto_LearningBasedWB
xphoto_SimpleWB
xphoto_WhiteBalancer
'''
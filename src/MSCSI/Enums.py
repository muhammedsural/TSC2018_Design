from enum import Enum

class eComboType(Enum):
    LinearAdditive   = 0
    Envelope         = 1
    AbsoluteAdditive = 2
    SRSS             = 3
    RangeAdditive    = 4
class e2DFrameType(Enum):
    PortalFrame      = 0  
    ConcentricBraced = 1  
    EccentricBraced  = 2 

class e3DFrameType(Enum):
    OpenFrame       = 0  
    PerimeterFrame  = 1  
    BeamSlab        = 2  
    FlatPlate       = 3 

class eAreaDesignOrientation(Enum):
    Wall             = 1  
    Floor            = 2  
    Ramp_DO_NOT_USE  = 3  
    Null             = 4  
    Other            = 5 

class eCNameType(Enum):
    LoadCase  = 0  
    LoadCombo = 1 

class eConstraintAxis(Enum):
    X        = 1  
    Y        = 2  
    Z        = 3  
    AutoAxis = 4 

class eConstraintType(Enum):
    Body      = 1  
    Diaphragm = 2  
    Plate     = 3  
    Rod       = 4  
    Beam      = 5  
    Equal     = 6  
    Local     = 7  
    Weld      = 8  
    Line      = 13 

class eDeckType(Enum):
    Filled    = 1  
    Unfilled  = 2  
    SolidSlab = 3 

class eDesignActionType(Enum):
    NonComposite        = 1  
    ShortTermComposite  = 2  
    LongTermComposite   = 3  
    Staged              = 4  
    Other               = 5 

class eDiaphragmOption(Enum):
    Disconnect        = 1  
    FromShellObject   = 2  
    DefinedDiaphragm  = 3 

class eForce(Enum):
    """Kuvvet birimi için enum sınıfı"""

    NotApplicable = 0  
    lb   = 1  
    kip  = 2  
    N    = 3  
    kN   = 4  
    kgf  = 5  
    tonf = 6 

class eFrameDesignOrientation(Enum):
    Column = 1  
    Beam   = 2  
    Brace  = 3  
    Null   = 4  
    Other  = 5 

class eFramePropType(Enum):
    I                       = 1  
    Channel                 = 2  
    T                       = 3  
    Angle                   = 4  
    DblAngle                = 5  
    Box                     = 6  
    Pipe                    = 7  
    Rectangular             = 8  
    Circle                  = 9  
    General                 = 10  
    DbChannel               = 11  
    Auto                    = 12  
    SD                      = 13  
    Variable                = 14  
    Joist                   = 15  
    Bridge                  = 16  
    Cold_C                  = 17  
    Cold_2C                 = 18  
    Cold_Z                  = 19  
    Cold_L                  = 20  
    Cold_2L                 = 21  
    Cold_Hat                = 22  
    BuiltupICoverplate      = 23  
    PCCGirderI              = 24  
    PCCGirderU              = 25  
    BuiltupIHybrid          = 26  
    BuiltupUHybrid          = 27  
    Concrete_L              = 28  
    FilledTube              = 29  
    FilledPipe              = 30  
    EncasedRectangle        = 31  
    EncasedCircle           = 32  
    BucklingRestrainedBrace = 33  
    CoreBrace_BRB           = 34  
    ConcreteTee             = 35  
    ConcreteBox             = 36  
    ConcretePipe            = 37  
    ConcreteCross           = 38  
    SteelPlate              = 39  
    SteelRod                = 40  
    PCCGirderSuperT         = 41  
    Cold_Box                = 42  
    Cold_I                  = 43  
    Cold_Pipe               = 44  
    Cold_T                  = 45  
    Trapezoidal             = 46 

class eHingeLocationType(Enum):
    RelativeDistance = 1  
    OffsetFromIEnd   = 2  
    OffsetFromJEnd   = 3 

class eItemType(Enum):
    Objects         = 0  
    Group           = 1  
    SelectedObjects = 2 

class eItemTypeElm(Enum):
    ObjectElm    = 0  
    Element      = 1  
    GroupElm     = 2  
    SelectionElm = 3 

class eLength(Enum):
    NotApplicable = 0  
    inch          = 1  
    ft            = 2  
    micron        = 3  
    mm            = 4  
    cm            = 5  
    m             = 6 

class eLinkPropType(Enum):
    Linear              = 1  
    Damper              = 2  
    Gap                 = 3  
    Hook                = 4  
    PlasticWen          = 5  
    Isolator1           = 6  
    Isolator2           = 7  
    MultilinearElastic  = 8  
    MultilinearPlastic  = 9  
    Isolator3           = 10 

class eLoadCaseType(Enum):
    LinearStatic            = 1  
    NonlinearStatic         = 2  
    Modal                   = 3  
    ResponseSpectrum        = 4  
    LinearHistory           = 5  
    NonlinearHistory        = 6  
    LinearDynamic           = 7  
    NonlinearDynamic        = 8  
    MovingLoad              = 9  
    Buckling                = 10  
    SteadyState             = 11  
    PowerSpectralDensity    = 12  
    LinearStaticMultiStep   = 13  
    HyperStatic             = 14 

class eLoadPatternType(Enum):
    Dead              = 1  
    SuperDead         = 2  
    Live              = 3  
    ReduceLive        = 4  
    Quake             = 5  
    Wind              = 6  
    Snow              = 7  
    Other             = 8 
    Temperature       = 10  
    Rooflive          = 11  
    Notional          = 12 
    PrestressTransfer = 59  
    PatternAuto       = 60  
    QuakeDrift        = 61 

class eMatCoupledType(Enum):
    NNone                           = 1  
    VonMisesPlasticity              = 2  
    ModifiedDarwinPecknoldConcrete  = 3 

class eMatType(Enum):
    Steel       = 1  
    Concrete    = 2  
    NoDesign    = 3  
    Aluminum    = 4  
    ColdFormed  = 5  
    Rebar       = 6  
    Tendon      = 7  
    Masonry     = 8 

class eMatTypeAluminum(Enum):
    SubType_6061_T6     = 1  
    SubType_6063_T6     = 2  
    SubType_5052_H34    = 3 

class eMatTypeColdFormed(Enum):
    ASTM_A653SQGr33 = 1  
    ASTM_A653SQGr50 = 2 

class eMatTypeConcrete(Enum):
    FC3000_NormalWeight         = 1  
    FC4000_NormalWeight         = 2  
    FC5000_NormalWeight         = 3  
    FC6000_NormalWeight         = 4  
    FC3000_LightWeight          = 5  
    FC4000_LightWeight          = 6  
    FC5000_LightWeight          = 7  
    FC6000_LightWeight          = 8  
    Chinese_C20_NormalWeight    = 9  
    Chinese_C30_NormalWeight    = 10  
    Chinese_C40_NormalWeight    = 11  
    Indian_M15_NormalWeight     = 12  
    Indian_M20_NormalWeight     = 13  
    Indian_M25_NormalWeight     = 14  
    Indian_M30_NormalWeight     = 15  
    Indian_M35_NormalWeight     = 16  
    Indian_M40_NormalWeight     = 17  
    Indian_M45_NormalWeight     = 18  
    Indian_M50_NormalWeight     = 19  
    Indian_M55_NormalWeight     = 20  
    Indian_M60_NormalWeight     = 21  
    EN_C12_NormalWeight         = 22  
    EN_C16_NormalWeight         = 23  
    EN_C20_NormalWeight         = 24  
    EN_C25_NormalWeight         = 25  
    EN_C30_NormalWeight         = 26  
    EN_C35_NormalWeight         = 27  
    EN_C40_NormalWeight         = 28  
    EN_C45_NormalWeight         = 29  
    EN_C50_NormalWeight         = 30  
    EN_C55_NormalWeight         = 31  
    EN_C60_NormalWeight         = 32  
    EN_C70_NormalWeight         = 33  
    EN_C80_NormalWeight         = 34  
    EN_C90_NormalWeight         = 35 

class eMatTypeRebar(Enum):
    ASTM_A615Gr40   = 1  
    ASTM_A615Gr60   = 2  
    ASTM_A615Gr75   = 3  
    ASTM_A706       = 4  
    Chinese_HPB235  = 5  
    Chinese_HRB335  = 6  
    Chinese_HRB400  = 7  
    Indian_Mild250  = 8  
    Indian_HYSD415  = 9  
    Indian_HYSD500  = 10  
    Indian_HYSD550  = 11 

class eMatTypeSteel(Enum):
    ASTM_A36            = 1  
    ASTM_A53GrB         = 2  
    ASTM_A500GrB_Fy42   = 3  
    ASTM_A500GrB_Fy46   = 4  
    ASTM_A572Gr50       = 5  
    ASTM_A913Gr50       = 6  
    ASTM_A992_Fy50      = 7  
    Chinese_Q235        = 8  
    Chinese_Q345        = 9  
    Indian_Fe250        = 10  
    Indian_Fe345        = 11  
    EN100252_S235       = 12  
    EN100252_S275       = 13  
    EN100252_S355       = 14  
    EN100252_S450       = 15  
    Chinese_Q355        = 16 

class eMatTypeTendon(Enum):
    ASTM_A416Gr250 = 1  
    ASTM_A416Gr270 = 2 

class eNamedSetType(Enum):
    All                             = 0  
    UpdateBridgeObject              = 1  
    RunAnalysis                     = 2  
    RunBridgeDesignSuperstructure   = 3  
    RunBridgeDesignSubstructure     = 4  
    RunBridgeDesignSeismic          = 5  
    RunBridgeRatingSuperstructure   = 6  
    RunMemberRating                 = 7  
    JointTHResponseSpectra          = 8  
    NamedDisplay                    = 9  
    PlotFunctionTraces              = 10  
    PushoverCurve                   = 11  
    VirtualWork                     = 12  
    TableSet                        = 13  
    TableGroupSuperset              = 14  
    BridgeSeismicReport             = 15  
    BridgeSuperstructureResponse    = 16  
    BridgeCalculationReport         = 17  
    BridgeCalculationReportSub      = 18 

class eObjType(Enum):
    Point   = 1  
    Frame   = 2  
    Area    = 3  
    Solid   = 6 

class eReturnCode(Enum):
    NotApplicable      = -100  
    NotImplemented     = -99  
    NoError            = 0  
    UnspecifiedError   = 1  
    Deprecated         = -98  
    TableIsObsolete    = -97  
    TableDoesNotExist  = -96 

class eShellType(Enum):
    ShellThin               = 1  
    ShellThick              = 2  
    Membrane                = 3  
    PlateThin_DO_NOT_USE    = 4  
    PlateThick_DO_NOT_USE   = 5  
    Layered                 = 6 

class eSlabType(Enum):
    Slab               = 0  
    Drop               = 1  
    Stiff_DO_NOT_USE   = 2  
    Ribbed             = 3  
    Waffle             = 4  
    Mat                = 5  
    Footing            = 6 

class eSuperObjectClass(Enum):
    NNone               = 0  
    SuperObject         = 1  
    Foundation          = 2  
    BridgeFoundation    = 3 

class eTempurature(Enum):
    NotApplicable = 0  
    F             = 1  
    C             = 2 

class eTemplateType(Enum):
    Grid                = 0  
    Clear               = 1  
    Beam                = 2  
    SlopedTruss         = 3  
    VerticalTruss       = 4  
    SpaceTruss          = 5  
    PortalFrame         = 6  
    BracedFrame         = 7  
    EccentricFrame      = 8  
    PerimeterFrame      = 9  
    SpaceFrame          = 10  
    Bridge              = 11  
    Barrel              = 12  
    Cylinder            = 13  
    Dome                = 14  
    ShearWall           = 15  
    Floor               = 16  
    Advanced            = 17  
    UndergoundConcrete  = 18  
    Truss2D             = 19  
    Truss3D             = 20  
    Frame2D             = 21  
    Frame3D             = 22  
    BridgeWizard        = 23  
    PipesAndPlates      = 24  
    Shells              = 25  
    SolidModels         = 26  
    StorageStructures   = 27  
    Staircases          = 28  
    CableBridges        = 29 

class eUnits(Enum):
    lb_in_F   =  1  
    lb_ft_F   =  2  
    kip_in_F  =  3  
    kip_ft_F  =  4  
    kN_mm_C   =  5  
    kN_m_C    =  6  
    kgf_mm_C  =  7  
    kgf_m_C   =  8  
    N_mm_C    =  9  
    N_m_C     = 10  
    Ton_mm_C  = 11  
    Ton_m_C   = 12  
    kN_cm_C   = 13  
    kgf_cm_C  = 14  
    N_cm_C    = 15  
    Ton_cm_C  = 16 

class eWallPierRebarLayerType(Enum):
    Vertical_Distributed_MiddleZone_Eachface   = 1  
    Horizontal_Distributed_MiddleZone_Eachface = 2  
    Vertical_Distributed_EndZoneI_Total        = 3  
    Vertical_Distributed_EndZoneJ_Total        = 4  
    Confinement_EndZoneI                       = 5  
    Confinement_EndZoneJ                       = 6  
    Diagonal_Each                              = 7 

class eWallPropType(Enum):
   Specified      = 1  
   AutoSelectList = 2 

class eWallSpandrelRebarLayerType(Enum):
    Horizontal_Top_Total             = 1  
    Horizontal_Bottom_Total          = 2  
    Horizontal_Distributed_Eachface  = 3  
    Vertical_Ties_Distributed        = 4  
    Diagonal_Each                    = 5 


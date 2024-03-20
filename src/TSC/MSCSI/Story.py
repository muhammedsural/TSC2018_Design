
from dataclasses import asdict, dataclass, field
from pandas import DataFrame
from TSC.MSCSI.ErrorHandler import CustomCommentError


@dataclass
class Story:
    """Class for story information"""
    BaseElevation   : float       = None
    NumberStories   : int         = None
    StoryNames      : list[str]   = field(default_factory = list)
    StoryElevations : list[float] = field(default_factory = list)
    StoryHeights    : list[float] = field(default_factory = list)
    IsMasterStory   : list[bool]  = field(default_factory = list)
    SimilarToStory  : list[str]   = field(default_factory = list)
    SpliceAbove     : list[bool]  = field(default_factory = list)
    SpliceHeight    : list[float] = field(default_factory = list)
    Color           : list[int]   = field(default_factory = list)
    Successfulvalue : int         = field(default=0.0)

    def to_dict(self) -> dict:
        return asdict(self)
    
    def to_dataframe(self) -> DataFrame:
        dumydict = self.to_dict()
        return DataFrame([dumydict])

@dataclass
class StoryManager:
    ModelRef : object
    story    : None = field(default_factory=Story())

    def GetInfo(self) -> None:
        [self.story.BaseElevation  ,
         self.story.NumberStories  ,
         self.story.StoryNames     ,
         self.story.StoryElevations,
         self.story.StoryHeights   ,
         self.story.IsMasterStory  ,
         self.story.SimilarToStory ,
         self.story.SpliceAbove    ,
         self.story.SpliceHeight   ,
         self.story.Color,
         self.story.Successfulvalue ] = self.ModelRef.Story.GetStories_2()
        if self.story.Successfulvalue != 0.0:
             return CustomCommentError(self.story.Successfulvalue,"Kat bilgileri alınamadı...")
        
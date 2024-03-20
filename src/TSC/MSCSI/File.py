from dataclasses import dataclass
from TSC.MSCSI.ErrorHandler import CustomCommentError


@dataclass
class FileManeger:
    RefApi : object

    def GetFilePath(self,FilePath : str) -> None:
        val = self.RefApi.GetFilePath(FilePath)
        if val != 0.0:
            return CustomCommentError(val,"Dosya yolu alınamadı...")
    
    def NewBlank(self) -> None:
        val = self.RefApi.NewBlank()
        if val != 0.0:
            return CustomCommentError(val,"Boş model oluşturulamadı...")

    def NewGridOnly(self,NumberStorys : int,
                    TypicalStoryHeight : float,
                    BottomStoryHeight : float,
                    NumberLinesX : int,
                    NumberLinesY : int,
                    SpacingX : float,
                    SpacingY : float) -> None:
        val = self.RefApi.NewGridOnly(NumberStorys,TypicalStoryHeight,BottomStoryHeight,NumberLinesX,NumberLinesY,SpacingX,SpacingY)
        if val != 0.0:
            return CustomCommentError(val,"Sadece gridlerden oluşan model oluşturulamadı...")
    
    def NewSteelDeck(self,NumberStorys : int,
                     TypicalStoryHeight : float,
                     BottomStoryHeight : float,
                     NumberLinesX : int,
                     NumberLinesY : int,
                     SpacingX : float,
                     SpacingY : float) -> None:
            val = self.RefApi.File.NewSteelDeck(NumberStorys,TypicalStoryHeight,BottomStoryHeight,NumberLinesX,NumberLinesY,SpacingX,SpacingY)
            if val != 0.0:
                return CustomCommentError(val,"SteelDeck model oluşturulamadı...")
    
    def OpenFile(self,FileName : str) -> None:
            val = self.RefApi.OpenFile(FileName)
            if val != 0.0:
                return CustomCommentError(val,"Model açılamadı...")
    
    def Save(self,FileName : str) -> None:
            val = self.RefApi.Save(FileName)
            if val != 0.0:
                return CustomCommentError(val,"Model kayıt edilemedi...")

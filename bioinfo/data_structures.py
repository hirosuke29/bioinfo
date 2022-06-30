import abc
from enum import Enum


class BaseEnum(Enum):
    A: int = 0
    T: int = 1
    G: int = 2
    C: int = 3
    U: int = 5
    N: int = 99


DNA_BASE_COMPLEMENTALITY: dict[int, int] = {
    BaseEnum.A: BaseEnum.T,
    BaseEnum.T: BaseEnum.A,
    BaseEnum.C: BaseEnum.G,
    BaseEnum.G: BaseEnum.C
}


class AbstractSequence:
    def __init__(self, str_sequence: list[str], acid_type: str = "DNA", **kwargs) -> None:
        self.acid_type = acid_type
        self.sequence: list[int] = self.__interpret_sequence(str_sequence, **kwargs)

    def __getitem__(self, idx: int) -> int:
        return self.sequence[idx]

    @abc.abstractstaticmethod
    def __interpret_sequence(str_sequnece: list[str]) -> list[int]:
        raise NotImplementedError


class Read(AbstractSequence):
    def get_complemental(self) -> list[int]:
        if self.acid_type != "DNA":
            raise Exception("acid type must be DNA")
        complemental_sequence: list[int] = []
        for base in reversed(self.sequence):
            complemental_sequence.append(DNA_BASE_COMPLEMENTALITY[base])
        return complemental_sequence
    
    @staticmethod
    def __interpret_sequence(str_sequnece: list[str]) -> list[int]:
        sequnece: list[int] = []
        for base in str_sequnece:
            if base == "A":
                sequnece.append(BaseEnum.A)
            elif base == "T":
                sequnece.append(BaseEnum.T)
            elif base == "G":
                sequnece.append(BaseEnum.G)
            elif base == "C":
                sequnece.append(BaseEnum.C)
            elif base == "N":
                sequnece.append(BaseEnum.N)
        return sequnece


class Quiality(AbstractSequence):
    @staticmethod
    def __interpret_sequence(str_sequnece: list[str], phred: int = 33) -> list[int]:
        sequnece: list[int] = []
        for quality in str_sequnece:
            q: int = ord(quality) - phred
            sequnece.append(q)
        return sequnece
from typing import List


class ResultElement:
    ui: str
    rootSource: str
    uri: str
    name: str

    def __init__(self, ui: str, rootSource: str, uri: str, name: str) -> None:
        self.ui = ui
        self.rootSource = rootSource
        self.uri = uri
        self.name = name


class UMLSSearchResponseResult:
    classType: str
    results: List[ResultElement]
    recCount: int

    def __init__(self, classType: str, results: List[ResultElement], recCount: int) -> None:
        self.classType = classType
        self.results = results
        self.recCount = recCount


class UMLSSearchResponse:
    pageSize: int
    pageNumber: int
    result: UMLSSearchResponseResult

    def __init__(self, pageSize: int, pageNumber: int, result: UMLSSearchResponseResult) -> None:
        self.pageSize = pageSize
        self.pageNumber = pageNumber
        self.result = result

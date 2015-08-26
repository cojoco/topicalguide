
from sys import path
path.insert(0, 'import_tool/analysis/interfaces')
from .mallet_analysis import MalletLdaAnalysis, MalletHldaAnalysis
from .mallet_itm_analysis import MalletItmAnalysis
from .random_analysis import RandomAnalysis

analyses = {
    "MalletITM": MalletItmAnalysis,
    "MalletLDA": MalletLdaAnalysis,
    "MalletHLDA": MalletHldaAnalysis,
    "Random": RandomAnalysis,
}

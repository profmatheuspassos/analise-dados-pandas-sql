from pathlib import Path
import sqlite3
import pandas as pd

caminhoArquivoOriginal = Path(__file__).parent / "arquivos" / "bd_data.csv"
caminhoArquivoBD = Path(__file__).parent / "arquivos" / "web.db"

conexao = sqlite3.connect(str(caminhoArquivoBD))
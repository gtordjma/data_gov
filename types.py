import datetime
from enum import Enum


class AssetTypes(Enum):
    ADL = 'ADL'
    AERODOM = 'AERODOM'
    AGO = 'AGO'
    AMA = 'AMA'
    ANA = 'ANA'
    BEG = 'BEG'
    BFS = 'BFS'
    CVA = 'CVA'
    KAP = 'KAP'
    LGW = 'LGW'
    LIR = 'LIR'
    OMA = 'OMA'
    SCA = 'SCA'
    SCL = 'SCL'
    SSA = 'SSA'
    
class FileTypes(Enum):
    FINANCE_BUDGET = 'finance_budget'
    FINANCE_CAPEX = 'finance_capex'
    FINANCE_CAPEX_FORECAST = 'finance_capex_forecast'
    FINANCE_CAPEX_FORECAST_LONGTERM = 'finance_capex_forecast_longterm'
    FINANCE_REF_CAPEX_PROJECTS = 'finance_ref_capex_projects'
    FINANCE_CAPEX_DETAILED = 'finance_capex_detailed'
    FINANCE_COCKPIT_BUDGET = 'finance_cockpit_budget'
    FINANCE_COCKPIT_FTE_BUDGET = 'finance_cockpit_fte_budget'
    FINANCE_COCKPIT_FTE_RH = 'finance_cockpit_fte_rh'
    FINANCE_COCKPIT_GENERAL_LEDGER = 'finance_cockpit_general_ledger'
    FINANCE_COCKPIT_MAPPING_LOCAL = 'finance_cockpit_mapping_local'
    FINANCE_COCKPIT_PAX = 'finance_cockpit_pax'
    FINANCE_COCKPIT_TRAFFIC = 'finance_cockpit_traffic'
    FINANCE_COCKPIT_TRAFFIC_BUDGET = 'finance_cockpit_traffic_budget'
    FINANCE_CUSTOMER_REVENUES = 'finance_customer_revenues'
    FINANCE_DEPOSITS = 'finance_deposits'
    FINANCE_GENERAL_LEDGER = 'finance_general_ledger'
    FINANCE_GUARANTEES = 'finance_guarantees'
    FINANCE_MAPPING_USECASE = 'finance_mapping_usecase'
    FINANCE_MAPPING_LOCAL = 'finance_mapping_local'
    FINANCE_PROCUREMENTS = 'finance_procurements'
    FINANCE_PROVISIONS = 'finance_provisions'
    FINANCE_RECEIVABLES = 'finance_receivables'
    FINANCE_SUPPLIER_OPEX = 'finance_supplier_opex'
    FINANCE_PIGMENT_TRAFFIC_CONSO = 'finance_pigment_traffic_conso'
    FINANCE_PIGMENT_HR_CONSO = 'finance_pigment_hr_conso'
    FINANCE_PIGMENT_EURO = 'finance_pigment_euro'
    FINANCE_PIGMENT_GL_LOCAL = 'finance_pigment_gl_local'
    FINANCE_PIGMENT_MAPPING_LOCAL = 'finance_pigment_mapping_local'

class Versions(Enum):
    B0 = 'B0'
    R1 = 'R1'
    R2 = 'R2'
    R3 = 'R3'
    
class FileStepStatus(str):
    PENDING = 'pending'
    RUNNING = 'running'
    FINISHED = 'finished'
    ERROR = 'error'

class ParquetFile:
    def __init__(self, asset: AssetTypes, use_case: str, file_name: str, file_source: str, parquet_file_path: str, classic_file_path: str | None):
        self.asset = asset
        self.use_case = use_case
        self.file_name = file_name
        self.file_source = file_source
        self.parquet_file_path = parquet_file_path
        self.classic_file_path = classic_file_path
        self.timestamp = datetime.now()
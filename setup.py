setting = {
    "filepath": __file__,
    "use_db": True,
    "use_default_setting": True,
    "home_module": None,
    "menu": {
        "uri": __package__,
        "name": "쿠팡플레이",
        "list": [
            {
                "uri": "main/setting",
                "name": "설정",
            },
            {
                "uri": "main/list",
                "name": "목록",
            },
            {
                "uri": "main/cpl",
                "name": "방송 예정 목록",
            },
            {
                "uri": "log",
                "name": "로그",
            },
        ],
    },
    "setting_menu": None,
    "default_route": "normal",
}

from plugin import *

P = create_plugin_instance(setting)
try:
    if os.path.exists(os.path.join(os.path.dirname(__file__), "mod_main.py")):
        from .mod_main import ModuleMain
    else:
        from support import SupportSC

        ModuleMain = SupportSC.load_module_P(P, "mod_main").ModuleMain

    P.set_module_list([ModuleMain])
except Exception as e:
    P.logger.error(f"Exception:{str(e)}")
    P.logger.error(traceback.format_exc())

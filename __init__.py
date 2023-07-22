import os

try:
    import yaml
except:
    os.system("pip install pyyaml")

try:
    if os.path.exists(os.path.join(os.path.dirname(__file__), "souce_cpp_handler.py")):
        from .souce_cpp_handler import CPP_Handler

    else:
        from support import SupportSC

        CPP_Handler = SupportSC.load_module_f(__file__, "souce_cpp_handler").CPP_Handler
except:
    pass

try:
    if os.path.exists(os.path.join(os.path.dirname(__file__), "souce_cpp_service.py")):
        from .souce_cpp_service import CPP_Service
    else:
        from support import SupportSC

        CPP_Service = SupportSC.load_module_f(__file__, "souce_cpp_service").CPP_Service
except:
    pass

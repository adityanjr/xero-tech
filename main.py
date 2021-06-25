from dotenv import load_dotenv
import os
import settings
import take_user_inputs

take_user_inputs.taking_inputs_and_update_env()
global_variables = settings.load_global_variables()
print(global_variables)



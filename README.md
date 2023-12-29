# Repository containg a notebooks I used for training models for function name prediction
I used following formulation of the task:
Given the function signature without the docstring predict a function name
I only used a python code.

## Structure
- evaluation.ipynb (contains jupyter with error analysis and comparisson of approaches to proble)
- datasets_exploration.ipynb (contain code for creating datase from code search net)
- scripts, recipes (scripts and recipes taken from hf alignment repistory, which I used for LoRA SFT and QLora trianing, with my modifications)
- For QLoRA I have used Axoltl, because the alignment repoistory dones't have QLoRA correctly implement, thus it's not possible to run in on 3090 with reasonable batch size.

## Environment
- all the work was done on runpod with RTX3090

## Training Logs
https://wandb.ai/hynky/func_name_code_llama?workspace=user-kydlicek-hynek

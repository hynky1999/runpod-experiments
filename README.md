# Repository containg a notebooks I used for training models for function name prediction
I used following formulation of the task:
Given the function signature without the docstring predict a function name
I only used a python code.

## Structure
- evaluation.ipynb (contains jupyter with error analysis and comparisson of approaches to proble)
- datasets_exploration.ipynb (contain code for creating datase from code search net)
- scripts, recipes (scripts and recipes taken from hf alignment repistory, which I used for LoRA SFT and QLora trianing, with my modifications)
- For QLoRA I have used Axoltl, because the alignment repoistory dones't have QLoRA correctly implement, thus it's not possible to run in on 3090 with reasonable batch size.

### Dataset design choices
I decideded to create the inputs in format

```
def x(signature):
    NO doc string
    xxxx
    xxxx
```
As same was done in https://arxiv.org/abs/2007.04973.
I removed the class names from the function name, as in my eyes
that's essentialy almost impossible to predict and in python
it's never even in a function name itself.



### Prompt choices
I decided to utilize also the system prompt, hoping that it would help the perfromance

### Hyperparametrs choices
- I have finetune both models using SFT only, simply because DPO would require way more resouces and time. Secondly I didn't have a dataset
with preferences. But it would certainly be benfical
- I have used Lora for the same reason as there is no other way to put the gradients + Adam momentum on the RTX3090, and secondly the method is way faster than the full-training.
- I have use QLora to showcase it as I think it's provides great performance in terms of size compared to it small downside in performance
- For Lora I have used the standard settings, however for Lora I forgot to target of Linears (down/up gate proj), secondly for r and alpha I have used the recommendation by [Rashka](https://magazine.sebastianraschka.com/p/practical-tips-for-finetuning-llms)
- I half precission training with bf16, which is pretty stable and very cheap on memory
- For batch size I tried to set the max that will get on gpu, while targetting effective batch size of 32 (using grad accumulation)
- Lastly I used packing in both cases and training on inputs in case of Axoltl as it has super easy set-up there.

## Environment
- all the work was done on runpod with RTX3090

## Training Logs
https://wandb.ai/hynky/func_name_code_llama?workspace=user-kydlicek-hynek

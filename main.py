import os

os.environ['OPENAI_API_KEY'] = 'your_openai_api_key_here'

from openai import OpenAI
client = OpenAI()


response = client.files.create(
  file=open("game_lore_dataset.jsonl", "rb"),
  purpose="fine-tune"
)

print(response)

# get id from response:
file_id = response.id

response = client.fine_tuning.jobs.create(
  training_file=file_id,
  model="gpt-3.5-turbo" #change to gpt-4-0613 if you have access
)
print(response)

# Example output:
# FileObject(id='file-FDxAUGtaVmTLHKuPNa8ZwQ', bytes=1667, created_at=1750245638, filename='game_lore_dataset.jsonl', object='file', purpose='fine-tune', status='processed', expires_at=None, status_details=None)
# FineTuningJob(id='ftjob-9dD7SotEdES0xy7ac3dbcHSv', created_at=1750245639, error=Error(code=None, message=None, param=None), fine_tuned_model=None, finished_at=None, hyperparameters=Hyperparameters(batch_size='auto', learning_rate_multiplier='auto', n_epochs='auto'), model='gpt-3.5-turbo-0125', object='fine_tuning.job', organization_id='org-bZ9KN2rdozJ7snHuVnypRDGM', result_files=[], seed=1473300658, status='validating_files', trained_tokens=None, training_file='file-FDxAUGtaVmTLHKuPNa8ZwQ', validation_file=None, estimated_finish=None, integrations=[], metadata=None, method=Method(type='supervised', dpo=None, reinforcement=None, supervised=SupervisedMethod(hyperparameters=SupervisedHyperparameters(batch_size='auto', learning_rate_multiplier='auto', n_epochs='auto'))), user_provided_suffix=None, usage_metrics=None, shared_with_openai=False, eval_id=None)

print(client.fine_tuning.jobs.list(limit=10))

print(client.fine_tuning.jobs.retrieve("ftjob-2TJ5ZZX1WPvithAFu9zrSPUT"))

response = client.chat.completions.create(
    model="ft:gpt-3.5-turbo-0125:personal::BjlIyXNp",
    messages=[
        {"role": "system", "content": "You are a wise bard well-versed in the lore of games. "
                                      "You help adventurers understand the mysteries of gaming."},
        {"role": "user", "content": "What is an RPG?"}
    ]
)

print(response.choices[0].message.content)
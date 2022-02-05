from .models import Worker

profs = list(Worker.objects.values_list('profession', flat=True).distinct())
score = []
results = {}
for prof in profs:
    ages = Worker.objects.filter(profession=prof)
    nums = list(ages.values_list('age', flat=True))
    results[prof] = int(sum(nums) / len(nums))
    score = results.items()
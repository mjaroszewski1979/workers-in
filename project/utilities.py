from .models import Worker



professions = list(Worker.objects.values_list('profession', flat=True).distinct())
score = []
results = {}
for prof in professions:
    nums = list(Worker.objects.filter(profession=prof).values_list('age', flat=True))
    results[prof] = int(sum(nums) / len(nums))
    score = results.items()


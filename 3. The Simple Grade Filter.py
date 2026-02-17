## 3. The Simple Grade Filter

listScore = [45, 88, 72, 91, 58]
passed = []
failed = []

for checking in listScore:
    if checking >= 60:
        passed.append(checking)
    else:
        failed.append(checking)

print(f"Failed: {failed}")
print(f"Passed: {passed}")

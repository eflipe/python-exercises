iterableObj = range(3)

print(iterableObj)

iterableObj = iter(iterableObj)

print(iterableObj)
print(type(iterableObj))
print(dir(iterableObj))

i = next(iterableObj)
print(i)
i = next(iterableObj)
print(i)
i = next(iterableObj)
print(i)
i = next(iterableObj)
print(i)
i = next(iterableObj)

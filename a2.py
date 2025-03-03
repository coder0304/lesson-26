class employee:
    def __init__(self):
        print('Employee created')
    def __del__(self):
        print("destructive called")
def Create_obj():
    print('Making object.......')
    obj=employee()
    print=('function end......')
    del obj
print('calling Create_obj()function.....')
obj=Create_obj()
print('Program End.......')
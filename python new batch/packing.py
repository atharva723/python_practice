#### packing is done to take 0 to n number of argument

#### single * only take positional args, single start packing is called tuple packing because it will pack in tuple
def n_positional_args(*args):
    return args

print(n_positional_args())
print(n_positional_args(2))
print(n_positional_args(1,2,3,4,5,6,7,8,9,))
print(n_positional_args(2,8.9,'hello',[1,2]))



#### double star ** only take keyword arguments
def n_kwargs(**kwargs):
    return kwargs
print(list(n_kwargs(a=1,b=2,c=4)))
print(n_kwargs(a=1,v=4))




#### to collect 0 to n number of argumnet of any type of argumnet we should use *args first args and then followed by ** kwargs is known as variable argumnets
def var_args(*args,**kwargs):
    return args, kwargs
print(var_args(1,2,3,a=3,b=5))
print(var_args(1,7.5))

if __name__ == "__main__":
    module_name = "variable_load_2"
    module_file = f"{module_name}.py"
    
    module_code = compile(open(module_file).read(), module_file, 'exec')
    module_namespace = {}
    exec(module_code, module_namespace)
    
    if 'a' in module_namespace:
        print("Value of 'a':", module_namespace['a'])
    else:
        print("Variable 'a' not found in the imported module.")
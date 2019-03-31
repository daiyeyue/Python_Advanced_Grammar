# 1. 模块
- 一个模块就是包含python代码的文件，后缀名是.py就可以，模块就是个python文件
- 为什么要用模块
    - 程序太大，编程维护不方便，需要拆分
    - 模块可以增加代码重复利用的方式
    - 当做命名空间使用，避免命名冲突
- 如何定义模块
    - 模块就是一个普通文件，所以任何代码可以直接书写
    - 不过根据模块的规范，最好在模块中编写以下内容
        - 函数（单一功能）
        - 类（相似功能的组合，或者类似业务模块）
        - 测试代码
- 如何使用模块
    - 模块直接导入
    - 语法
        - import module_name
        - 借助于importlib包可以实现导入以数字开头的模块名称   
    -使用
        import module_name
        module_name.function_name
        module_name.class_name
        案例p01,p02
        import mudule_name as 别名
        案例p03
        
        - from module_name import func_name, class_name
           - 按上述方法有选择性的导入
           - 使用的时候可以直接使用导入的内容，不需要前缀
           - 案例 p04
           
        - from module_name import *
            - 导入模块的所有内容
            - 案例p05
            - 使用的时候不用前缀，但是会带来命名污染的情况
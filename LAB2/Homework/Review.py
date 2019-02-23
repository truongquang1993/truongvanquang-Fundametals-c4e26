# 1. Why should we use functions at all?
# 
    # Các hàm do người dùng định nghĩa là các khối mã có thể tái sử dụng; chúng chỉ cần được viết một lần, sau đó chúng có thể được sử dụng nhiều lần.
    # Chúng có thể được sử dụng trong các ứng dụng khác.
    # Các chức năng này cũng có thể được sửa đổi theo yêu cầu.
    # Mã này thường được tổ chức tốt, dễ bảo trì và thân thiện với nhà phát triển. Có nghĩa là nó có thể hỗ trợ phương pháp thiết kế mô-đun.
    # Vì các hàm do người dùng định nghĩa có thể được viết độc lập, các tác vụ của dự án có thể được phân phối để phát triển ứng dụng nhanh chóng.
    # Một chức năng do người dùng xác định rõ và được viết cẩn thận có thể dễ dàng cho quá trình phát triển ứng dụng.

# 2. How to define/declare a function?
# 
    # Step 1: Declare the function with the keyword def followed by the function name.
    # Step 2: Write the arguments inside the opening and closing parentheses of the function, and end the declaration with a colon.
    # Step 3: Add the program statements to be executed.
    # Step 4: End the function with/without return statement.

# 3. How to call/use a function?
# 
    # with example:
    # Function definition: def polygon(n, side_length):
    # Function call: polygon(5, 200)
    # ...

# What is return, why and how do we use it?
# 
    # return use to give a result, it is user want to back up the program. We can use a result when it was assign values to a variable
# Do we have to use return in every function?
# 
    # No. We can't use return in every function. Example:
        # def Hello():
        #     s = print("hello")
        #     return s
        # a = s

        # print(a)

# What are function arguments/parameters, why and how we use it?
# 
    # with example:
    # Function definition: def polygon(n, side_length):
    # in this case, n and side_length are function arguments. And they can use for programs in function

# How to use function from a different file other than our currently working file?
# 
    # We can use the following syntax: from *name_file* import *name_function*

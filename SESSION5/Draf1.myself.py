teencode = {
    "oy": "Rồi. Ý nói đã xác nhận một điều gì đó",
    "NĐ": "Nam Định. Quê tôi",
    "FW": "Chuyển tiếp. Chuyển tiếp mail trên gmail",
    "rpl": "Reply. Trả lời câu hỏi nào đó",
    "Wth": "What the hell. Cái chuyện gì thế?"
}
print(*teencode.keys())

# a = input("Bạn muốn biết nghĩa từ nào?(Nhập từ khóa hoặc nhập ext để thoát ra")
a = "yes"

while a != "ext":
    a = input("Bạn muốn biết nghĩa từ nào?(Nhập từ khóa hoặc nhập ext để thoát ra)")
    if a in teencode:
        print(teencode[a])
    else:
        print("Từ khóa", a, "chưa có trong tư mục" )
        b = input("Bạn có muốn đóng góp từ khóa mới này (yes/no)")
        if b == "yes":
            val = input("Nhập ý nghĩa từ khóa mới:")
            teencode.get(a)
            teencode[a] = val
            print(*teencode.keys())
        else:
            print(*teencode.keys())
            a = input("Bạn muốn biết nghĩa từ nào?(Nhập từ khóa hoặc nhập ext để thoát ra)")

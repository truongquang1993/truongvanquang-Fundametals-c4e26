teencode = {
    "oy": "Rồi. Ý nói đã xác nhận một điều gì đó",
    "NĐ": "Nam Định. Quê tôi",
    "FW": "Chuyển tiếp. Chuyển tiếp mail trên gmail",
    "rpl": "Reply. Trả lời câu hỏi nào đó",
    "Wth": "What the hell. Cái chuyện gì thế?"
}
print(*teencode.keys())

a = input("Bạn muốn biết nghĩa từ nào?")

if a in teencode:
    print(teencode[a])
else:
    print("Not found")
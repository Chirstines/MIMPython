# week04_assignment04
""" Bài tập 1. (sort a list)
Một list được gọi là ổn nếu nó chỉ chứa các số thực và có ít nhất một phần tử. Cho một list gồm
các list con ổn. Viết một chương trình sắp xếp list này theo thứ tự tăng dẫn của tổng các số 
trong mỗi list con. Ví dụ:
A = [[1,2], [3,0,4], [2], [4,5]] # input
B = [[2], [1,2], [3,0,4], [4,5]] # output
Yêu cầu bổ sung: đặt ra thêm tiêu chí để so sánh hai list ổn bất kỳ và áp dụng tiêu chí này để sắp xếp list đầu vào.
"""
# Sắp xếp hàm list theo thứ tự tăng dần theo tổng các list con
def Sort_by_condition01(inputList):
    for turn in range(len(inputList)):
        for index in range(len(inputList)-1):
            if sum(inputList[index]) > sum(inputList[index+1]):
                tempList = inputList[index]
                inputList[index] = inputList[index+1]
                inputList[index+1] = tempList
        
# Hàm sắp xếp list theo thứ tự tăng dần của giá trị mỗi list trong mỗi list con
def Sort_by_condition02(inputList):
    for turn in range(len(inputList)):
        for index in range (len(inputList)-1):
            if max(inputList[index]) > max(inputList[index+1]):
                tempList = inputList[index]
                inputList[index] = inputList[index+1]
                inputList[index+1] = tempList
        
if __name__ == '__main__':
    inputList01 = [[1,2], [3,0,4], [2], [4,5]]
    Sort_by_condition01(inputList01)
    print(inputList01) #[[2], [1, 2], [3, 0, 4], [4, 5]]
    
    inputList02 = [[0,1], [4,0,3], [2,0,1,2], [2]]
    Sort_by_condition01(inputList02)
    print(inputList02) #[[0, 1], [2], [2, 0, 1, 2], [4, 0, 3]]
    
#đặt ra thêm tiêu chí để so sánh hai list ổn bất kỳ và áp dụng tiêu chí này để sắp xếp list đầu vào.
    inputList03 = [[1,2], [3,0,4], [2], [4,5]]
    Sort_by_condition02(inputList03)
    print(inputList03) # [[1, 2], [2], [3, 0, 4], [4, 5]]  
    
    inputList04 =  [[0,1], [4,0,3], [2,0,1,2], [2]]
    Sort_by_condition02(inputList04)
    print(inputList04) # [[0, 1], [2, 0, 1, 2], [2], [4, 0, 3]]
    
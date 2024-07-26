import csv
import json
import math
import re
from collections import Counter
import glob
import shlex
import subprocess


def checkPasswordComplexity(password):
  # 长度计算
  if len(password)<8:
    print("密码长度小于8位,太不安全")
  elif len(password)>=16:
    print("密码长度超过16位,对某些网站可能不合法")
    
  # 字符类型计算（虽然字符类型 字符集不会显著影响密码复杂度 但还是写了一下）
  type_count = 0
  if re.search(r'[a-z]', password):
    type_count += 1
  if re.search(r'[A-Z]', password):
    type_count += 1
  if re.search(r'\d', password):
    type_count += 1
  if re.search(r'[!@#$%^&*()-=_+]', password):
    type_count +=1
  print("密码包含"+str(type_count)+"种字符类型")
  
  # 调用pydictor 根据已知参数生成字典库，方便撞库攻击
  # 构造命令
  # 使用 shlex.split 来安全地构建命令行参数，防止命令注入
  # 注意：这里我们不直接使用 password 的内容，而是使用其长度，但仍遵循安全实践
  command = shlex.split(f"python ./pydictor/pydictor.py -base L --len {len(password)} {len(password)} -output D:\\code\\res.txt")
  print(command)
  # 使用subprocess.run执行命令
  try:
      subprocess.run(command, check=True)
  except subprocess.CalledProcessError as e:
      print(f"Command execution failed with error code {e.returncode}")
  
  input("press any key to continue")
  
  # 进行撞库攻击（利用pyditor）
  with open("D:\code\res.txt", "r") as f:
    for line in f:
      if line.strip() in password:
        print("撞库攻击成功")
        break
  
  # 计算熵值：密码长度和各个字符的组合
  print("密码长度为"+str(len(password)),end="")
  print("your password: "+password,end='')
  # 计算不同字符的数量
  unique_chars = set(password)
  num_unique_chars = len(unique_chars)
  print("不同字符的数量为"+str(num_unique_chars),end="")
  # 计算熵
  entropy = math.log2(num_unique_chars ** len(password))
  print("熵值为"+str(entropy))
  return entropy
  

def readFromCSV():
  # 匹配任意一个 CSV 文件 ，假设有很多个csv file
  csv_files = glob.glob('*.csv')

  # 循环处理每个 CSV 文件
  for csv_file in csv_files:
      print(f'处理文件: {csv_file}')
      
      # 读取 CSV 文件并提取密码
      passwords = []
      with open(csv_file, newline='', encoding='utf-8') as csvfile:
          reader = csv.DictReader(csvfile)
          for row in reader:
              if 'password' in row:
                  # 检查密码安全性
                  checkPasswordComplexity(row['password'])
                  passwords.append(row['password'])

      # 将密码拼接成一个字符串
      passwords_str = ' '.join(passwords)

      # 使用正则表达式找出所有连续的字母子串
      substrings = re.findall(r'[a-zA-Z]+', passwords_str)

      # 计算每个子串的频率
      substrings_freq = Counter(substrings)

      # 按照频率高低排序
      sorted_substrings = sorted(substrings_freq.items(), key=lambda x: x[1], reverse=True)

      # 打印子串名字和频率
      print("子串名字和频率:")
      for substring, frequency in sorted_substrings:
          print(f'子串名字: {substring}, 频率: {frequency}')
      print('\n')


def main():
    while(True):
      print("请输入密码，检查安全性：(按esc退出)")
      password=input()
      if password=='\x1b':
        break
      checkPasswordComplexity(password)

if __name__ == '__main__':
    main()
import os

# 작업 디렉토리에서 모든 파일과 디렉토리의 경로를 가져옵니다.
file_sizes = []
for root, dirs, files in os.walk("E:\Program Files (x86)\Python311"):
    for filename in files:
        filepath = os.path.join(root, filename)
        file_size = os.path.getsize(filepath)
        file_sizes.append((file_size, filepath))

# 파일 크기순으로 정렬합니다.
file_sizes.sort(reverse=True)

# 결과를 report.txt 파일에 저장합니다.
with open("report.txt", "w") as f:
    for size, path in file_sizes:
        f.write(f"{size}    {path}\n")

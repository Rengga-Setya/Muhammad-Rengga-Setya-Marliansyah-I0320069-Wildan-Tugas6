banyak_data = int(input('Masukan banyaknya data nilai : '))
data = []
i = 1
for i in range(banyak_data):
    nilai = float(input('nilai ke-{} : '.format(i + 1)))
    data.append(float(nilai))
    i += 1
mean = sum(data)/banyak_data
print('Nilai rata-rata = ', mean)
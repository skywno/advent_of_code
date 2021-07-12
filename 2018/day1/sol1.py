from typing import List

def sum_frequency(freqs: List[int]) -> int:
  return sum(freqs)

def find_freq_twice(freqs: List[int]) -> int:
  sum = 0
  sum_set = {0}

  while True:
    for freq in freqs:
      sum = sum + freq
      if sum in sum_set:
        return sum
      else:
        sum_set.add(sum)
  


if __name__ =='__main__':
  with open('input.txt') as f:
    freqs = f.readlines()
  freqs = list(map(int, freqs))
  print(sum_frequency(freqs))
  print(find_freq_twice(freqs))
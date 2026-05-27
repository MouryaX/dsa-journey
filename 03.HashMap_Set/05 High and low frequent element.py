#Without using max and min
class FrequencyCounter:
    def Frequency(self, arr):
        freq_map = {}                # Dictionary to store frequency of each element

        # Count frequencies
        for num in arr:
            freq_map[num] = freq_map.get(num, 0) + 1

        maxFreq = 0
        minFreq = len(arr)
        maxEle = 0
        minEle = 0

        # Iterate through dictionary to find max and min frequency elements
        for element, count in freq_map.items():
            if count > maxFreq:
                maxFreq = count
                maxEle = element

            if count < minFreq:
                minFreq = count
                minEle = element

        # Print results
        print("The highest frequency element is:", maxEle)
        print("The lowest frequency element is:", minEle)


if __name__ == "__main__":
    fc = FrequencyCounter()
    arr = [10, 5, 10, 15, 10, 5]
    fc.Frequency(arr)

#Time: O(n) HashMap + O(n) Tarversal = O(n)
#Space: O(n) HashMap

'''freq = {'a':4, 'b':1, 'c':7}

print(min(freq, key=freq.get))

print(max(freq, key=freq.get))'''
class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
          

        hashmap = Counter(tasks)

        time = 0

        heap = []     

        for count in hashmap.values():

            heapq.heappush(heap, -count)  # Negative for max heap

        queue = deque()  # Stores (available_time, remaining_count)

        while heap or queue:
            time += 1
            
            # Step 1: Process most frequent task from heap
            if heap:
                count = heapq.heappop(heap)  # Negative value
                count += 1  # Increment (one use consumed)
                
                # Step 2: If task still has more uses, add to cooldown queue
                if count != 0:  # Still has uses left

                    available_time = time + n  # Can use again after cooldown

                    queue.append((available_time, count))

            if queue and queue[0][0] == time:  # Front task ready?

                available_time, count = queue.popleft()

                heapq.heappush(heap, count)  # Back to heap for next use

        return time  # ✅ Return AFTER loop completes
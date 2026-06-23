import heapq
from collections import defaultdict
from typing import List

class Twitter:
    def __init__(self):
        self.following = defaultdict(set)
        self.tweets = defaultdict(list)
        self.time = 0

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.tweets[userId].append([tweetId, self.time])
        self.time += 1

    def getNewsFeed(self, userId: int) -> List[int]:
        feed = []
        heap = []
        users = self.following[userId] | {userId}

        # Seed the heap with each user's NEWEST tweet only
        for u in users:
            if self.tweets[u]:
                idx = len(self.tweets[u]) - 1          # last = most recent
                tweetId, time = self.tweets[u][idx]    # storage is [tweetId, time]
                heapq.heappush(heap, (-time, tweetId, u, idx))

        # Pop the newest, then refill from that same user
        while heap and len(feed) < 10:
            neg_time, tweetId, u, idx = heapq.heappop(heap)
            feed.append(tweetId)
            if idx > 0:                                # that user has an older tweet
                idx -= 1
                tid, time = self.tweets[u][idx]        # match storage order here too
                heapq.heappush(heap, (-time, tid, u, idx))

        return feed

    def follow(self, followerId: int, followeeId: int) -> None:
        self.following[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        self.following[followerId].discard(followeeId)
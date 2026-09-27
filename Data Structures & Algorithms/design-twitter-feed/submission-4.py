from collections import defaultdict
from typing import List
import heapq


class Twitter:

    def __init__(self):
        self.user_tweets = defaultdict(list)

        # followerId -> set of people they follow
        self.following = defaultdict(set)

        self.time = 0


    def postTweet(self, userId: int, tweetId: int) -> None:
        self.time += 1

        self.user_tweets[userId].append(
            (self.time, tweetId)
        )


    def getNewsFeed(self, userId: int) -> List[int]:

        result = []
        heap = []

        # people whose tweets should appear in feed
        users = self.following[userId] | {userId}

        # Put the latest tweet from every relevant user into heap
        for uid in users:

            if self.user_tweets[uid]:

                index = len(self.user_tweets[uid]) - 1

                time, tweetId = self.user_tweets[uid][index]

                heapq.heappush(
                    heap,
                    (-time, tweetId, uid, index)
                )


        # Get at most 10 latest tweets
        while heap and len(result) < 10:

            neg_time, tweetId, uid, index = heapq.heappop(heap)

            result.append(tweetId)

            # Add previous tweet from same user
            if index - 1 >= 0:

                prev_time, prev_tweetId = self.user_tweets[uid][index - 1]

                heapq.heappush(
                    heap,
                    (-prev_time, prev_tweetId, uid, index - 1)
                )

        return result


    def follow(self, followerId: int, followeeId: int) -> None:

        if followerId != followeeId:
            self.following[followerId].add(followeeId)


    def unfollow(self, followerId: int, followeeId: int) -> None:

        self.following[followerId].discard(followeeId)
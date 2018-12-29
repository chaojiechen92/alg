import heapq


class Twitter:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.users = {}
        self.i = 0

    def postTweet(self, userId, tweetId):
        """
        Compose a new tweet.
        :type userId: int
        :type tweetId: int
        :rtype: void
        """
        if userId in self.users:
            if len(self.users[userId]["tweets"]) == 10:
                self.users[userId]["tweets"].pop(0)
            self.users[userId]["tweets"].append((self.i, tweetId))
            self.i += 1
            return

        self.users[userId] = {
            "follow": set(),
            "tweets": [(self.i, tweetId)]
        }
        self.users[userId]["follow"].add(userId)
        self.i += 1
        return

    #
    def getNewsFeed(self, userId):
        """
        Retrieve the 10 most recent tweet ids in the user's news feed. Each item in the news feed must be posted by users who the user followed or by the user herself. Tweets must be ordered from most recent to least recent.
        :type userId: int
        :rtype: List[int]
        """
        if userId not in self.users:
            return []
        h = []
        for followee in self.users[userId]["follow"]:
            if followee in self.users and self.users[followee]["tweets"]:
                for tweet in self.users[followee]["tweets"]:
                    if len(h) < 10:
                        heapq.heappush(h, tweet)
                    elif tweet[0] > h[0][0]:
                        heapq.heappushpop(h, tweet)
        ret = []
        while h:
            ret.append(heapq.heappop(h)[1])
        ret.reverse()
        return ret

    def follow(self, followerId, followeeId):
        """
        Follower follows a followee. If the operation is invalid, it should be a no-op.
        :type followerId: int
        :type followeeId: int
        :rtype: void
        """
        if followerId not in self.users:
            self.users[followerId] = {
                "follow": set(),
                "tweets": []
            }
            self.users[followerId]["follow"].add(followerId)

        self.users[followerId]["follow"].add(followeeId)
        return

    def unfollow(self, followerId, followeeId):
        """
        Follower unfollows a followee. If the operation is invalid, it should be a no-op.
        :type followerId: int
        :type followeeId: int
        :rtype: void
        """
        if followerId not in self.users or followerId==followeeId:
            return
        if followeeId in self.users[followerId]["follow"]:
            self.users[followerId]["follow"].remove(followeeId)
        return

    def __str__(self):
        return str(self.users)

if __name__ == "__main__":
    t = Twitter()

    t.postTweet(1,5)
    print(t.getNewsFeed(1))
    t.follow(1,2)
    t.postTweet(2,6)
    print(t.getNewsFeed(1))
    t.unfollow(1,2)
    print(t.getNewsFeed(1))


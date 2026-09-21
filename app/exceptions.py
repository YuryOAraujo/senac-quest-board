class QuestAlreadyCompletedError(Exception):
  pass

class QuestAssignmentNotFoundError(Exception):
  pass

class RewardAlreadyClaimedError(Exception):
  pass

class QuestNotCompleted(Exception):
  pass
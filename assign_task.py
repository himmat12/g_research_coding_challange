def assign_tasks(factor, arrival, bonus, reward, duration, time_bonus):


    processorArray = []

    for processors in factor:

        for processor in processors:

            processorArray[processor] = -1 # -1 denotes that processor is currently not being used.

    

    print(processorArray)


    maxTick = 0

    for i in range(0, len(arrival)):

        if maxTick < (arrival[i] + duration[i]):

            maxTick = arrival[i] + duration[i]


    print(maxTick)


    tick = 0

    while tick <= maxTick:

        noTasksToAssign = False


        while noTasksToAssign:

            maxScore = 0

            maxScoreIndex = 0

            bestProcessorIndex = -1

            for i in range(0, len(factor)): # Checks all tasks for their scores.

                # Checks for the score produced for each task by processor.

                for processor in factor[i]:

                    if processorArray[processor] <= tick:

                        if tick < arrival[i] + time_bonus[i]: # Checks that the processor is not in use.

                            tempScore = factor[i][processor] * (bonus[i] + reward[i] * duration[i] / (duration[i] + tick - arrival[i]))

                        else:

                            tempScore = factor[i][processor] * reward[i] * duration[i] / (duration[i] + tick - arrival[i])


                        if tempScore > maxScore:

                            maxScore = tempScore

                            maxScoreIndex = i

                            bestProcessorIndex = processor

            

            # Set the processor as being in use until the time when the task is done.

            processorArray[bestProcessorIndex] = tick + duration[maxScoreIndex]


            factor.remove(factor[maxScoreIndex])

            arrival.remove(arrival[maxScoreIndex])

            bonus.remove(bonus[maxScoreIndex])

            reward.remove(reward[maxScoreIndex])

            duration.remove(duration[maxScoreIndex])

            time_bonus.remove[time_bonus[maxScoreIndex]]

    





    tick += 1



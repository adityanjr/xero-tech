#!/usr/bin/env python
# coding: utf-8

# In[ ]:


def DayOrNight(img):     #return dayOrNight (1 -> day  0-> night)

    th = 0.75

    #if dayOrNight == 1 ---> day
    #if dayOrNight == 0 ---> night
    dayOrNight = 1

    #time.sleep(2)
    img = cv2.resize(img, (640, 480))
    
    #img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    #img = cv2.cvtColor(img, cv2.COLOR_GRAY2BGR)
    


    cntEqualChannelVal = 0
    cntUnequalChannelVal = 0
    for i in range(img.shape[0]):
        for j in range(img.shape[1]):
            pixel = img[i, j]
            if pixel[0] == pixel[1] and pixel[1] == pixel[2]:
                cntEqualChannelVal += 1
            else:
                cntUnequalChannelVal += 1
            
    if cntEqualChannelVal/(cntEqualChannelVal + cntUnequalChannelVal) >= th:
        dayOrNight = 0
        print("night time video")
        
    else:
        dayOrNight = 1
        print("day time video")

    cv2.imshow("image", img)
  
    cv2.waitKey(0)
    #if k == 27:
        #break
    
        
    #vid.release()
    cv2.destroyAllWindows()
    
    return dayOrNight


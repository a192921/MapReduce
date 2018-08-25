# MapReduce

## 介紹
- MapReduce，最早是由 Google 提出，後來也運用在開源的雲端技術 Hadoop 中。

- MapReduce 是雲端運算的關鍵技術，將要執行的問題，拆解成 Map 和 Reduce 的方式來執行，以達到分散運算的效果。

![](https://github.com/a192921/MapReduce/blob/master/MapReduce.jpg)



## Mapping
- 從主節點(master node)輸入一組input，此input是一組key/value，將這組輸入切分成好幾個小的子部分，分散到各個工作節點(worker nodes)去做運算。

![](https://github.com/a192921/MapReduce/blob/master/%E5%9C%96%E7%89%871.png)



## Reducing
- 主節點(master node)收回處理完的子部分，將子部分重新組合產生輸出。

![](https://github.com/a192921/MapReduce/blob/master/%E5%9C%96%E7%89%872.png)



## Hadoop
- Hadoop 不但讓你儲存超過一個伺服器所能容納的超大檔案，還能同時儲存、處理、分析幾千幾萬份這種超大檔案，所以每每提到大數據，便會提到 Hadoop 這套技術。
- 能夠儲存並管理大量資料的雲端平台，為 Apache 軟體基金會底下的一個開放原始碼、社群基礎、而且完全免費的軟體。


## HDFS分散式檔案系統
- Hadoop Distributed File System
- 在分散式儲存環境中，提供單一的目錄系統。
- 資料以Write-once-read-many 存取，一旦建立、寫入，就不允許修改。
- 每個檔案被分割成許多block，每個block複製許多複本(replica)，並分散儲存於不同的DataNode上。
- NameNode：負責維護HDFS的檔案名稱空間 (File System Namespace)。
- DataNode：實際儲存檔案區塊(Blocks)的伺服器。
![](https://github.com/a192921/MapReduce/blob/master/HDFS.jpg)

引用自：http://images.cnblogs.com/cnblogs_com/wayne1017/HDFSArch.JPG


## 資料來源
- Jewel，2015年3月12日。大數據、數位學習、雲端運算、      數據、科技、網路、網路技術、雲端運算，認識大數據的黃色小象幫手-Hadoop 。2018年8月25日，取自  https://www.inside.com.tw/2015/03/12/big-data-4-hadoop
- Wea，2008年9月25日。5. MapReduce, Hadoop。2018年8月25日，取自https://sls.weco.net/CollectiveNote20/MR
- 顏孜羲，2015年5月19日。MapReduce 簡單介紹與練習。2018年8月26日，取自  https://www.slideshare.net/d2207197/mapreduce-48359655

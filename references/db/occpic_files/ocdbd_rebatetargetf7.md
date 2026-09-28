# 政策目标F7-ocdbd_rebatetargetf7

## 政策目标F7-主表 t_occpic_rebatetarget

- **表名称：** 政策目标F7-主表
- **表名：** t_occpic_rebatetarget

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fenablecaltime | fenablecaltime | timestamp | 0 |  |  | null |  |
| 3 | factivityplanid | factivityplanid | int8 | 64 |  | √ | 0 |  |
| 4 | faccrualformulaid | faccrualformulaid | int8 | 64 |  | √ | 0 |  |
| 5 | fnrebateclassid | fnrebateclassid | int8 | 64 |  | √ | 0 |  |
| 6 | fmodifytime | fmodifytime | timestamp | 0 |  |  | null |  |
| 7 | fbnfcustomerid | fbnfcustomerid | int8 | 64 |  | √ | 0 |  |
| 8 | fcreatorid | fcreatorid | int8 | 64 |  | √ | 0 |  |
| 9 | fbizorgid | fbizorgid | int8 | 64 |  | √ | 0 |  |
| 10 | fpushtype | fpushtype | bpchar | 1 |  | √ | 'A' |  |
| 11 | fgroupkey | fgroupkey | int8 | 64 |  | √ | 0 |  |
| 12 | fcustomdaterange | fcustomdaterange | varchar | 2000 |  | √ | ' ' |  |
| 13 | fexpensetypeid | fexpensetypeid | int8 | 64 |  | √ | 0 |  |
| 14 | fpresettle | fpresettle | bpchar | 1 |  | √ | '0' |  |
| 15 | fbaselineamount | fbaselineamount | numeric | 23 | 10 | √ | 0 |  |
| 16 | fbillno | 编码 | varchar | 80 |  | √ | ' ' | 编码 |
| 17 | fname | 名称 | varchar | 255 |  | √ | ' ' | 名称 |
| 18 | fmodifierid | fmodifierid | int8 | 64 |  | √ | 0 |  |
| 19 | fsettperiod | fsettperiod | bpchar | 1 |  | √ | ' ' |  |
| 20 | fbaselineqty | fbaselineqty | numeric | 23 | 10 | √ | 0 |  |
| 21 | fnladdertypeid | fnladdertypeid | int8 | 64 |  | √ | 0 |  |
| 22 | fbillstatus | 单据状态 | bpchar | 1 |  | √ | 'A' | 单据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 23 | fcalculatestatus | fcalculatestatus | bpchar | 1 |  | √ | 'A' |  |
| 24 | fcreatetime | fcreatetime | timestamp | 0 |  |  | null |  |
| 25 | funitid | funitid | int8 | 64 |  | √ | 0 |  |
| 26 | fbnfchannelclassid | fbnfchannelclassid | int8 | 64 |  | √ | 0 |  |
| 27 | fdescription | fdescription | varchar | 255 |  | √ | ' ' |  |
| 28 | fauditdate | fauditdate | timestamp | 0 |  |  | null |  |
| 29 | fpolicyid | fpolicyid | int8 | 64 |  | √ | 0 |  |
| 30 | fstarttime | fstarttime | timestamp | 0 |  |  | null |  |
| 31 | fcalscopetype | fcalscopetype | bpchar | 1 |  | √ | ' ' |  |
| 32 | fbnfchannelid | fbnfchannelid | int8 | 64 |  | √ | 0 |  |
| 33 | fbalanceorgid | fbalanceorgid | int8 | 64 |  | √ | 0 |  |
| 34 | fcalbilltypeid | fcalbilltypeid | int8 | 64 |  | √ | 0 |  |
| 35 | fnrebatetypeid | fnrebatetypeid | int8 | 64 |  | √ | 0 |  |
| 36 | fendtime | fendtime | timestamp | 0 |  |  | null |  |
| 37 | fcurrencyid | fcurrencyid | int8 | 64 |  | √ | 0 |  |
| 38 | fauditorid | fauditorid | int8 | 64 |  | √ | 0 |  |
| 39 | fbnfcustomerclassid | fbnfcustomerclassid | int8 | 64 |  | √ | 0 |  |
| 40 | fkpiid | fkpiid | int8 | 64 |  | √ | 0 |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_occpic_rebatetarget |  | fid |
| 2 | idx_occpic_rbtgt_chl |  | fbnfchannelid |
| 3 | idx_occpic_rbtgt_efftime |  | fstarttime,fendtime |
| 4 | idx_occpic_rbtgt_policy |  | fpolicyid |
| 5 | idx_occpic_rbtgt_bno |  | fbillno |

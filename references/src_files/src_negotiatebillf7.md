# 议价单F7-src_negotiatebillf7

## 议价单F7-主表 t_src_negotiatebill

- **表名称：** 议价单F7-主表
- **表名：** t_src_negotiatebill

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | forgid | forgid | int8 | 64 |  | √ | 0 |  |
| 3 | fbizstatus | fbizstatus | bpchar | 1 |  | √ | ' ' |  |
| 4 | fnote | fnote | varchar | 255 |  | √ | ' ' |  |
| 5 | fbilldate | 发布时间 | timestamp | 0 |  |  | null | 发布时间 |
| 6 | fpurdeptid | fpurdeptid | int8 | 64 |  | √ | 0 |  |
| 7 | freplenishtype | freplenishtype | bpchar | 1 |  | √ | ' ' |  |
| 8 | fmodifytime | fmodifytime | timestamp | 0 |  |  | null |  |
| 9 | fcreatorid | fcreatorid | int8 | 64 |  | √ | 0 |  |
| 10 | fopentype | 开标方式 | bpchar | 1 |  | √ | ' ' | 开标方式,枚举: 1 :截止时间手动开标 |
| 11 | fturns | 议价轮次 | varchar | 2 |  | √ | ' ' | 议价轮次,枚举: 1 :首轮 2 :议价(1) 3 :议价(2) 4 :议价(3) 5 :议价(4) 6 :议价(5) 7 :议价(6) 8 :议价(7) 9 :议价(8) 10 :议价(9) 11 :议价(10) 12 :议价(11) 13 :议价(12) 14 :议价(13) 15 :议价(14) |
| 12 | fpurgroupid | fpurgroupid | int8 | 64 |  | √ | 0 |  |
| 13 | fbillno | 议价单号 | varchar | 30 |  | √ | ' ' | 议价单号 |
| 14 | fmodifierid | fmodifierid | int8 | 64 |  | √ | 0 |  |
| 15 | ftemplateid | ftemplateid | int8 | 64 |  | √ | 0 |  |
| 16 | fprojectid | 招标项目 | int8 | 64 |  | √ | 0 | 招标项目F7 src_projectf7 |
| 17 | fbillstatus | 单据状态 | bpchar | 1 |  | √ | ' ' | 单据状态,枚举: A :创建 B :审核中 C :已审核 D :重新审核 |
| 18 | fparentid | fparentid | varchar | 50 |  | √ | ' ' |  |
| 19 | fcreatetime | fcreatetime | timestamp | 0 |  |  | null |  |
| 20 | fbidcount | fbidcount | int4 | 32 |  | √ | 0 |  |
| 21 | flastupdateuserid | flastupdateuserid | int8 | 64 |  | √ | 0 |  |
| 22 | fauditdate | fauditdate | timestamp | 0 |  |  | null |  |
| 23 | fbizpartnerid | fbizpartnerid | int8 | 64 |  | √ | 0 |  |
| 24 | fsupplierid | fsupplierid | int8 | 64 |  | √ | 0 |  |
| 25 | flastupdatetime | flastupdatetime | timestamp | 0 |  |  | null |  |
| 26 | fquotenum | fquotenum | bpchar | 1 |  | √ | '1' |  |
| 27 | fsuppliertype | fsuppliertype | varchar | 30 |  | √ | ' ' |  |
| 28 | fcontent_tag | fcontent_tag | text | 0 |  |  | null |  |
| 29 | fdeadline | 报价截止时间 | timestamp | 0 |  |  | null | 报价截止时间 |
| 30 | fisnotice | fisnotice | bpchar | 1 |  | √ | '0' |  |
| 31 | fcontent | fcontent | varchar | 255 |  | √ | ' ' |  |
| 32 | fcurrentnode | fcurrentnode | int8 | 64 |  | √ | 0 |  |
| 33 | fnegotiatetype | 议价方式 | bpchar | 1 |  | √ | ' ' | 议价方式,枚举: 1 :线上议价 2 :线下议价(标的) 3 :线下议价(标段) 4 :电子竞价 |
| 34 | fisreplenish | fisreplenish | bpchar | 1 |  | √ | '0' |  |
| 35 | fauditorid | fauditorid | int8 | 64 |  | √ | 0 |  |
| 36 | fisquotebidopen | 已议标开标 | bpchar | 1 |  | √ | '0' | 已议标开标 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_src_negotiatebill_billdata |  | fbilldate |
| 2 | idx_src_negotiatebill_billno |  | fbillno |
| 3 | idx_src_negotiatebill_proid |  | fprojectid |
| 4 | idx_src_negotiatebill_supid |  | fsupplierid |
| 5 | idx_src_negotiatebill_parentid |  | fparentid |
| 6 | pk_src_negotiatebill |  | fid |

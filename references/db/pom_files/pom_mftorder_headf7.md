# 生产工单单据头F7-pom_mftorder_headf7

## 生产工单单据头F7-主表 t_pom_mftorder

- **表名称：** 生产工单单据头F7-主表
- **表名：** t_pom_mftorder

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | 单据id | int8 | 64 |  | √ | 0 | 单据id |
| 2 | fk_bj73_basedatafield | fk_bj73_basedatafield | int8 | 64 |  | √ | 0 |  |
| 3 | forgid | 生产组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 4 | ftransactiontype | ftransactiontype | int8 | 64 |  | √ | 0 |  |
| 5 | fasyncstatuspom | fasyncstatuspom | varchar | 50 |  | √ | ' ' |  |
| 6 | finterprocess | finterprocess | bpchar | 1 |  | √ | '0' |  |
| 7 | fbilldate | fbilldate | timestamp | 0 |  |  | null |  |
| 8 | fisinit | fisinit | bpchar | 1 |  | √ | '0' |  |
| 9 | fmodifytime | fmodifytime | timestamp | 0 |  |  | null |  |
| 10 | fentrustdept | fentrustdept | int8 | 64 |  | √ | 0 |  |
| 11 | fisrework | fisrework | bpchar | 1 |  | √ | '0' |  |
| 12 | fbiztype | fbiztype | varchar | 50 |  | √ | ' ' |  |
| 13 | fcreatorid | fcreatorid | int8 | 64 |  | √ | 0 |  |
| 14 | fbillno | 单据编号 | varchar | 30 |  | √ | ' ' | 单据编号 |
| 15 | fremark | fremark | varchar | 500 |  | √ | ' ' |  |
| 16 | fmodifierid | fmodifierid | int8 | 64 |  | √ | 0 |  |
| 17 | fbillstatus | 单据状态 | varchar | 30 |  | √ | ' ' | 单据状态,枚举: A :暂存 B :已提交 C :已审核 D :作废 |
| 18 | fcreatetime | fcreatetime | timestamp | 0 |  |  | null |  |
| 19 | fasyncstatussfc | fasyncstatussfc | varchar | 50 |  | √ | ' ' |  |
| 20 | fauditdate | fauditdate | timestamp | 0 |  |  | null |  |
| 21 | fbillcretype | fbillcretype | varchar | 5 |  | √ | ' ' |  |
| 22 | fisdevproduce | 研发试制 | bpchar | 1 |  | √ | '0' | 研发试制 |
| 23 | fk_bj73_textareafield | fk_bj73_textareafield | varchar | 500 |  | √ | ' ' |  |
| 24 | fauditorid | fauditorid | int8 | 64 |  | √ | 0 |  |
| 25 | fbilltype | 单据类型 | int8 | 64 |  | √ | 0 | 单据类型 bos_billtype |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_pom_mftorder_fk |  | fbillno |
| 2 | idx_mftorder_createtime |  | fcreatetime |
| 3 | idx_pom_mftorder_orgidfid |  | forgid,fid |
| 4 | t_pom_mftorder_pkey |  | fid |

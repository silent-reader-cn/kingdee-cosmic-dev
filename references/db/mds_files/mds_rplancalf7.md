# 需求计划方案F7-mds_rplancalf7

## 需求计划方案F7-主表 t_mds_rplancal

- **表名称：** 需求计划方案F7-主表
- **表名：** t_mds_rplancal

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fdeduct_h | fdeduct_h | int8 | 64 |  | √ | 0 |  |
| 3 | fpredversion | fpredversion | int8 | 64 |  | √ | 0 |  |
| 4 | fopenlv | fopenlv | int8 | 64 |  | √ | 0 |  |
| 5 | forgid | forgid | int8 | 64 |  | √ | 0 |  |
| 6 | frepeat | 重复运算 | bpchar | 1 |  | √ | '0' | 重复运算 |
| 7 | frunninglog_tag | frunninglog_tag | text | 0 |  |  | null |  |
| 8 | fpredtime | 预约时间 | int8 | 64 |  | √ | 0 | 预约时间 |
| 9 | fdeduct_t | fdeduct_t | int8 | 64 |  | √ | 0 |  |
| 10 | frunningtype | 运行时间类型 | varchar | 30 |  | √ | ' ' | 运行时间类型,枚举: |
| 11 | fmodifytime | fmodifytime | timestamp | 0 |  |  | null |  |
| 12 | fplanid | fplanid | varchar | 50 |  | √ | ' ' |  |
| 13 | fcreatorid | fcreatorid | int8 | 64 |  | √ | 0 |  |
| 14 | fdaysofmon | 月 | varchar | 100 |  | √ | ' ' | 月 |
| 15 | fsourcetype | fsourcetype | varchar | 30 |  | √ | ' ' |  |
| 16 | fchangeway | 改写方式 | varchar | 30 |  | √ | ' ' | 改写方式,枚举: 0 :全部覆盖 1 :仅更新增加 2 :仅覆盖相同来源数据 |
| 17 | fend | fend | timestamp | 0 |  |  | null |  |
| 18 | fdummysiteid | fdummysiteid | int8 | 64 |  | √ | 0 |  |
| 19 | fbillno | 需求计划方案编码 | varchar | 30 |  | √ | ' ' | 需求计划方案编码 |
| 20 | fstype | 计划来源类型 | varchar | 20 |  | √ | ' ' | 计划来源类型,枚举: 0 :指定需求计划 1 :需求计划关联关系 2 :指定预测 3 :冲减结果 |
| 21 | fdaysofweek | 周 | varchar | 100 |  | √ | ' ' | 周 |
| 22 | fcalstatus | 使用状态 | varchar | 30 |  | √ | ' ' | 使用状态,枚举: A :禁用 B :可用 |
| 23 | foutlookperiod | foutlookperiod | numeric | 23 | 10 | √ | 0.0000000000 |  |
| 24 | fdatetype | fdatetype | varchar | 30 |  | √ | ' ' |  |
| 25 | fmodifierid | fmodifierid | int8 | 64 |  | √ | 0 |  |
| 26 | fbillstatus | 单据状态 | varchar | 30 |  | √ | ' ' | 单据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 27 | fcreatetime | fcreatetime | timestamp | 0 |  |  | null |  |
| 28 | fstart | fstart | timestamp | 0 |  |  | null |  |
| 29 | fjobid | fjobid | varchar | 50 |  | √ | ' ' |  |
| 30 | fsourcename | fsourcename | int8 | 64 |  | √ | 0 |  |
| 31 | fauditdate | fauditdate | timestamp | 0 |  |  | null |  |
| 32 | fmod | fmod | numeric | 23 | 10 | √ | 0.0000000000 |  |
| 33 | frepeattype | 时间重复类型 | varchar | 30 |  | √ | ' ' | 时间重复类型,枚举: |
| 34 | fplangrp | fplangrp | int8 | 64 |  | √ | 0 |  |
| 35 | fsetoffverid | fsetoffverid | int8 | 64 |  | √ | 0 |  |
| 36 | ftype | ftype | int8 | 64 |  | √ | 0 |  |
| 37 | fdeduct | fdeduct | bpchar | 1 |  | √ | '0' |  |
| 38 | famounttype | famounttype | varchar | 30 |  | √ | ' ' |  |
| 39 | fisquota | fisquota | bpchar | 1 |  | √ | '0' |  |
| 40 | flosedate | 失效时间 | timestamp | 0 |  |  | null | 失效时间 |
| 41 | fauditorid | fauditorid | int8 | 64 |  | √ | 0 |  |
| 42 | fdtype | fdtype | int8 | 64 |  | √ | 0 |  |
| 43 | fbillstatuscheckbox | fbillstatuscheckbox | bpchar | 1 |  | √ | '0' |  |
| 44 | frunninglog | frunninglog | varchar | 500 |  | √ | ' ' |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_mds_rplancal |  | fbillno,forgid |
| 2 | t_mds_rplancal_pkey |  | fid |

---

## 需求计划方案F7-多语言表 t_mds_rplancal_l

- **表名称：** 需求计划方案F7-多语言表
- **表名：** t_mds_rplancal_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fname | 需求计划方案名称 | varchar | 100 |  | √ | ' ' | 需求计划方案名称 |
| 3 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 4 | fpkid | fpkid | varchar | 36 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_mds_rplancal_l |  | fpkid |

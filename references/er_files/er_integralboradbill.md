# 低碳积分单据-er_integralboradbill

## 低碳积分单据-主表 t_ep_userscore

- **表名称：** 低碳积分单据-主表
- **表名：** t_ep_userscore

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | frank | frank | int8 | 64 |  | √ | 0 |  |
| 3 | fcreateorgid | fcreateorgid | int8 | 64 |  | √ | 0 |  |
| 4 | fmodifierid | fmodifierid | int8 | 64 |  | √ | 0 |  |
| 5 | fcreatetime | fcreatetime | timestamp | 0 |  |  | null |  |
| 6 | fdisabledate | fdisabledate | timestamp | 0 |  |  | null |  |
| 7 | fuserid | 用户 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 8 | fpraisecount | 点赞数量 | varchar | 44 |  | √ | ' ' | 点赞数量 |
| 9 | fcontrolstatus | fcontrolstatus | bpchar | 1 |  | √ | '0' |  |
| 10 | fmodifytime | fmodifytime | timestamp | 0 |  |  | null |  |
| 11 | fstatus | fstatus | varchar | 25 |  | √ | ' ' |  |
| 12 | fcreatorid | fcreatorid | int8 | 64 |  | √ | 0 |  |
| 13 | fmasterid | fmasterid | int8 | 64 |  | √ | 0 |  |
| 14 | fyearscore | 年度积分 | int8 | 64 |  | √ | 0 | 年度积分 |
| 15 | fnowdate | fnowdate | timestamp | 0 |  |  | null |  |
| 16 | fyear | 年度 | int8 | 64 |  | √ | 0 | 年度 |
| 17 | fenable | fenable | bpchar | 1 |  | √ | '0' |  |
| 18 | fnumber | 单据编号 | varchar | 25 |  | √ | ' ' | 单据编号 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_er_us_fuserid |  | fuserid |
| 2 | t_ep_userscore_pkey |  | fid |

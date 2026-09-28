# 尾盘调整日志单据(暂存)-tcret_tdzzswp_edit_tp

## 尾盘调整日志单据(暂存)-主表 t_tcret_tdzzswp_edit_tp

- **表名称：** 尾盘调整日志单据(暂存)-主表
- **表名：** t_tcret_tdzzswp_edit_tp

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fpreadjust | 调整数值前 | numeric | 23 | 10 | √ | 0 | 调整数值前 |
| 3 | fyjxmid | 预缴项目id | int8 | 64 |  | √ | 0 | 预缴项目id |
| 4 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 5 | forgid | 取数组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 6 | fadjustexplain | 调整说明 | varchar | 1000 |  | √ | ' ' | 调整说明 |
| 7 | fskssqq | 开始日期 | timestamp | 0 |  |  | null | 开始日期 |
| 8 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 9 | fadjusttype | 调整类型 | varchar | 50 |  | √ | ' ' | 调整类型,枚举: 1 :数据源调整 2 :手工录入调整 |
| 10 | fpostadjust | 调整数值后 | numeric | 23 | 10 | √ | 0 | 调整数值后 |
| 11 | fskssqz | 结束日期 | timestamp | 0 |  |  | null | 结束日期 |
| 12 | frowindex | 调整行 | int8 | 64 |  | √ | 0 | 调整行 |
| 13 | fsbbid | 申报表ID | int8 | 64 |  | √ | 0 | 申报表ID |
| 14 | fcolumntype | 调整列 | varchar | 50 |  | √ | ' ' | 调整列,枚举: hbsr :货币收入 swjqtsr :实物收入及其他收入 stxssr :视同销售收入 |
| 15 | fruleid | 规则id | int8 | 64 |  | √ | 0 | 规则id |
| 16 | fitemname | 业务名称 | varchar | 200 |  | √ | ' ' | 业务名称 |
| 17 | ftitlename | 调整项目 | varchar | 50 |  | √ | ' ' | 调整项目 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_tcret_tdzzswp_edit_tp |  | fid |
| 2 | idx_tcret_tdzzswp_edit_tp |  | forgid,fskssqq,fskssqz |

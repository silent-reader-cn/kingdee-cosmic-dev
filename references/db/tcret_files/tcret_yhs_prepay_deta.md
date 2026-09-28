# 印花税预缴底稿取数明细-tcret_yhs_prepay_deta

## 印花税预缴底稿取数明细-主表 t_tcret_yhs_prepay_deta

- **表名称：** 印花税预缴底稿取数明细-主表
- **表名：** t_tcret_yhs_prepay_deta

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fadjustamount | 调整数值 | numeric | 23 | 10 | √ | 0 | 调整数值 |
| 3 | fskssqz | 日期范围.结束 | timestamp | 0 |  |  | null | 日期范围.结束 |
| 4 | ftzsm | 调整说明 | varchar | 1000 |  | √ | ' ' | 调整说明 |
| 5 | fprepayitem | 预征项目 | varchar | 50 |  | √ | ' ' | 预征项目,枚举: jzfw :建筑服务 xsbdc :销售不动产 czbdc :出租不动产 |
| 6 | forgid | 组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 7 | ftotalamount | 总数 | numeric | 23 | 10 | √ | 0 | 总数 |
| 8 | ftaxaccountserialno | 台账流水号 | varchar | 50 |  | √ | ' ' | 台账流水号 |
| 9 | ftaxorgid | 取数组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 10 | famount | 数值 | numeric | 23 | 10 | √ | 0 | 数值 |
| 11 | fskssqq | 日期范围.开始 | timestamp | 0 |  |  | null | 日期范围.开始 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_tcret_yhs_prepay_deta |  | fid |
| 2 | idx_tcret_yhs_prepay_deta |  | forgid,ftaxaccountserialno,fskssqq,fskssqz |

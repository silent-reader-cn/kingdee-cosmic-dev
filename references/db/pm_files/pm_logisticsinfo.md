# 物流信息-pm_logisticsinfo

## 物流信息-主表 t_pm_logisticsinfo

- **表名称：** 物流信息-主表
- **表名：** t_pm_logisticsinfo

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fbillno | 单据编号 | varchar | 80 |  | √ | ' ' | 单据编号 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | t_pm_logisticsinfo_pkey |  | fid |
| 2 | idx_pm_logisticsinfo_no |  | fbillno |

---

## 单据体-子表 t_pm_logisticsinfoentry

- **表名称：** 单据体-子表
- **表名：** t_pm_logisticsinfoentry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | freceivephone | 收件人电话 | varchar | 50 |  | √ | ' ' | 收件人电话 |
| 3 | flogisticscompid | 物流公司 | int8 | 64 |  | √ | 0 | 物流公司 bd_logisticcomp |
| 4 | flogisticsnum | 物流单号 | varchar | 80 |  | √ | ' ' | 物流单号 |
| 5 | fsenderphone | 寄件人电话 | varchar | 50 |  | √ | ' ' | 寄件人电话 |
| 6 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 7 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | t_pm_logisticsinfoentry_pkey |  | fentryid |
| 2 | idx_pm_loginfoentry_fid |  | fid |

# 抄报税管理-sim_copy_tax_returns

## 抄报税管理-主表 t_sim_copy_tax_return

- **表名称：** 抄报税管理-主表
- **表名：** t_sim_copy_tax_return

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | ftaxcopytime | 抄报时间 | timestamp | 0 |  |  | null | 抄报时间 |
| 3 | fequipment | 设备信息 | int8 | 64 |  | √ | 0 | [开票设备 bdm_tax_equipment](../bdm_files/bdm_tax_equipment.md) |
| 4 | ftaxreturnenddate | 数据报税终止日期 | timestamp | 0 |  |  | null | 数据报税终止日期 |
| 5 | fequipmentstatus | 设备状态 | varchar | 30 |  | √ | ' ' | 设备状态,枚举: 1 :正常 2 :不可用 |
| 6 | fresetandunlocktime | 清零解锁时间 | timestamp | 0 |  |  | null | 清零解锁时间 |
| 7 | fcopysuccessdate | 抄报成功月份 | varchar | 50 |  | √ | ' ' | 抄报成功月份 |
| 8 | finv_end_date | 开票截止日期 | timestamp | 0 |  |  | null | 开票截止日期 |
| 9 | forg | 组织信息 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 10 | fepinfo | 企业信息 | int8 | 64 |  | √ | 0 | [企业基础信息 bdm_enterprise_baseinfo](../bdm_files/bdm_enterprise_baseinfo.md) |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_sim_copy_tax_return |  | fid |
| 2 | idx_sim_copy_tax_return |  | fequipment |

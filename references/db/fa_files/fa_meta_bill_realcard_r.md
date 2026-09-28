# 单据元数据实物基础资料关系-fa_meta_bill_realcard_r

## 单据元数据实物基础资料关系-主表 t_fa_meta_bill_realcard_r

- **表名称：** 单据元数据实物基础资料关系-主表
- **表名：** t_fa_meta_bill_realcard_r

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | frealentity | 分录标志（实物卡片基础资料所在分录） | varchar | 30 |  | √ | ' ' | 分录标志（实物卡片基础资料所在分录） |
| 3 | fbillentityname | 单据标识 | varchar | 30 |  | √ | ' ' | 单据标识 |
| 4 | frealfield | 实物卡片基础资料名称 | varchar | 30 |  | √ | ' ' | 实物卡片基础资料名称 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_fa_meta_bill_realcard_r |  | fbillentityname |
| 2 | pk_t_fa_meta_bill_realcard_r |  | fid |

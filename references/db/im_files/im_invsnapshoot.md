# 库存余额快照表-im_invsnapshoot

## 库存余额快照表-主表 t_im_invsnapshoot

- **表名称：** 库存余额快照表-主表
- **表名：** t_im_invsnapshoot

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fdimstr | 维度 | varchar | 1200 |  | √ | ' ' | 维度 |
| 3 | fbillid | 单据内码 | int8 | 64 |  | √ | 0 | 单据内码 |
| 4 | fdimmd5str | 维度加密串 | varchar | 36 |  | √ | ' ' | 维度加密串 |
| 5 | fbiztime | 业务日期 | timestamp | 0 |  |  | null | 业务日期 |
| 6 | fformid | 单据标识 | varchar | 100 |  | √ | ' ' | 单据标识 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_im_ivnsn_ffid |  | fformid |
| 2 | t_im_invsnapshoot_pkey |  | fid |
| 3 | idx_im_ivnsn_fbid |  | fbillid |

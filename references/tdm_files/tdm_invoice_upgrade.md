# 发票主键数据升级专用(勿删)-tdm_invoice_upgrade

## 发票主键数据升级专用(勿删)-主表 t_tdm_invoice_upgrade

- **表名称：** 发票主键数据升级专用(勿删)-主表
- **表名：** t_tdm_invoice_upgrade

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | foldid | 旧主键ID | varchar | 50 |  | √ | ' ' | 旧主键ID |
| 3 | fcreatedate | 创建日期 | timestamp | 0 |  |  | null | 创建日期 |
| 4 | fmodifydate | 修改日期 | timestamp | 0 |  |  | null | 修改日期 |
| 5 | fnewid | 新主键ID | varchar | 50 |  | √ | ' ' | 新主键ID |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_tdm_invoice_upgrade |  | foldid,fnewid |
| 2 | pk_tdm_invoice_upgrade |  | fid |

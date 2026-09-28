# 反归档记录-bos_cbs_archi_reversercd

## 反归档记录-主表 t_cbs_archi_reversercd

- **表名称：** 反归档记录-主表
- **表名：** t_cbs_archi_reversercd

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | farchi_entityid | 归档表单id | int8 | 64 |  | √ | 0 | 归档表单id |
| 3 | fcreatetime | 创建日期 | timestamp | 0 |  |  | null | 创建日期 |
| 4 | fbatchnum | 批次号 | varchar | 50 |  | √ | ' ' | 批次号 |
| 5 | fdesc | 操作描述 | varchar | 1000 |  | √ | ' ' | 操作描述 |
| 6 | freversecount | 反归档记录总数 | int8 | 64 |  | √ | 0 | 反归档记录总数 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_cbs_archi_reversercd |  | fid |
| 2 | idx_cbs_archi_reversercd |  | farchi_entityid |

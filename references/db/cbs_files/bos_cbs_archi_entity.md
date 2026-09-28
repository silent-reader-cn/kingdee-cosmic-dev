# 已归档单据（反归档）-bos_cbs_archi_entity

## 已归档单据（反归档）-主表 t_cbs_archi_entity

- **表名称：** 已归档单据（反归档）-主表
- **表名：** t_cbs_archi_entity

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | farchiveroute | 归档库 | varchar | 50 |  | √ | ' ' | 归档库 |
| 3 | fcreatetime | 创建日期 | timestamp | 0 |  |  | null | 创建日期 |
| 4 | fdatabase_type | 归档库类型 | varchar | 50 |  | √ | ' ' | 归档库类型,枚举: db :数据库 es :Elasticsearch |
| 5 | farchivecount | 已归档总数 | int8 | 64 |  | √ | 0 | 已归档总数 |
| 6 | fentitynumber | 表单 | varchar | 36 |  | √ | ' ' | 主实体对象 bos_entityobject |
| 7 | freversecount | 反归档总数 | int8 | 64 |  | √ | 0 | 反归档总数 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_cbs_archi_entity |  | fentitynumber |
| 2 | pk_cbs_archi_entity |  | fid |

# 已同步基础资料-bos_cbs_archi_basedata

## 已同步基础资料-主表 t_cbs_archi_basedata

- **表名称：** 已同步基础资料-主表
- **表名：** t_cbs_archi_basedata

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | farchiveroute | 归档库 | varchar | 50 |  | √ | ' ' | 归档库 |
| 3 | fcreatetime | 创建日期 | timestamp | 0 |  |  | null | 创建日期 |
| 4 | fentitynumber | 基础资料 | varchar | 36 |  | √ | ' ' | 主实体对象 bos_entityobject |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_cbs_archi_basedata |  | fid |
| 2 | idx_cbs_archi_bd_number |  | fentitynumber |

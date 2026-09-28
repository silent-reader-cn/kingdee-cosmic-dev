# 进项统计刷新日期-rim_idb_task_param

## 进项统计刷新日期-主表 t_rim_idb_task_param

- **表名称：** 进项统计刷新日期-主表
- **表名：** t_rim_idb_task_param

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | forg_id | 组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 3 | fcreate_time | 创建日期 | timestamp | 0 |  |  | null | 创建日期 |
| 4 | fquery_type | 统计类型 | varchar | 20 |  | √ | ' ' | 统计类型,枚举: fcreatetime :采集日期 finvoice_date :开票日期 fauthenticate_time :认证日期 |
| 5 | fdata_date | 数据日期 | timestamp | 0 |  |  | null | 数据日期 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_rim_idb_task_param |  | fquery_type,fdata_date |
| 2 | pk_t_rim_idb_task_param |  | fid |

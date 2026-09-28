# 比较结果-dbc_table_diff

## 单据体-子表 t_dbc_table_diff_items

- **表名称：** 单据体-子表
- **表名：** t_dbc_table_diff_items

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | ftable_name | 数据表 | varchar | 150 |  | √ | ' ' | 数据表 |
| 3 | fcomp_state | 比较结果 | varchar | 30 |  | √ | ' ' | 比较结果,枚举: SUCCESS :不兼容 FAILED :失败 OMITTED :兼容 READY :就绪 ABORTED :撤销 RUNNING :执行中 |
| 4 | ftable_remark_tag | 备注_详情 | text | 0 |  |  | null | 备注_详情 |
| 5 | fsyn_state | 同步状态 | varchar | 30 |  | √ | ' ' | 同步状态,枚举: SUCCESS :已同步 FAILED :失败 OMITTED :忽略 READY :就绪 ABORTED :撤销 RUNNING :执行中 |
| 6 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 7 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 8 | ftable_remark | 备注 | varchar | 300 |  | √ | ' ' | 备注 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_dbc_table_diff_items_0 |  | fid |
| 2 | pk_t_dbc_table_diff_items |  | fentryid |

---

## 比较结果-主表 t_dbc_table_diff

- **表名称：** 比较结果-主表
- **表名：** t_dbc_table_diff

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fhost | 执行服务器 | varchar | 50 |  | √ | ' ' | 执行服务器 |
| 3 | fremark | 备注 | varchar | 300 |  | √ | ' ' | 备注 |
| 4 | fsrc_db_id | 来源数据库 | int8 | 64 |  | √ | 0 | [数据库 dbc_database](../dbc_files/dbc_database.md) |
| 5 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 6 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 7 | fomitted_count | 兼容数据表个数 | int4 | 32 |  | √ | 0 | 兼容数据表个数 |
| 8 | ftotal_elapsed_time | 总耗时（秒） | numeric | 10 | 1 | √ | 0.0 | 总耗时（秒） |
| 9 | fremark_tag | 备注_详情 | text | 0 |  |  | null | 备注_详情 |
| 10 | fend_time | 结束时间 | timestamp | 0 |  |  | null | 结束时间 |
| 11 | fstart_time | 开始时间 | timestamp | 0 |  |  | null | 开始时间 |
| 12 | fmodifytime | 状态更新时间 | timestamp | 0 |  |  | null | 状态更新时间 |
| 13 | fstate | 状态 | varchar | 30 |  | √ | ' ' | 状态,枚举: READY :创建 RUNNING :执行中 COMPARED :已比较 SYNCHRONIZED :已同步 FAILED :失败 ABORTED :已撤销 |
| 14 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 15 | fsuccess_count | 不兼容数据表个数 | int4 | 32 |  | √ | 0 | 不兼容数据表个数 |
| 16 | ftable_copy_id | 数据表复制 | int8 | 64 |  | √ | 0 | [数据表复制 dbc_table_copy](../dbc_files/dbc_table_copy.md) |
| 17 | ftar_db_id | 目标数据库 | int8 | 64 |  | √ | 0 | [数据库 dbc_database](../dbc_files/dbc_database.md) |
| 18 | ffailed_count | 失败数据表个数 | int4 | 32 |  | √ | 0 | 失败数据表个数 |
| 19 | fnumber | 编码 | varchar | 50 |  | √ | ' ' | 编码 |
| 20 | ftable_count | 数据表总数 | int4 | 32 |  | √ | 0 | 数据表总数 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_dbc_table_diff_2 |  | ftable_copy_id |
| 2 | idx_dbc_table_diff_1 |  | fcreatetime |
| 3 | pk_t_dbc_table_diff |  | fid |
| 4 | idx_dbc_table_diff_0 |  | fnumber |

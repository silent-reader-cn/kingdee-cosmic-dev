# 上下文实例数据表-plm_ipd_contextual_ins

## 上下文实例数据表-分表 t_plm_ipd_contextual_ins_s

- **表名称：** 上下文实例数据表-分表
- **表名：** t_plm_ipd_contextual_ins_s

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fsnapshot | 快照 | varchar | 255 |  | √ | ' ' | 快照 |
| 3 | fsnapshot_tag | 快照_详情 | text | 0 |  |  | null | 快照_详情 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_plm_ipd_contextual_ins_s |  | fid |
| 2 | idx_t_plm_ipd_ctx_inss |  | fsnapshot |

---

## 上下文实例数据表-主表 t_plm_ipd_contextual_ins

- **表名称：** 上下文实例数据表-主表
- **表名：** t_plm_ipd_contextual_ins

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fcreator | 创建人 | varchar | 50 |  | √ | ' ' | 创建人 |
| 3 | fchargeperson | 负责人 | varchar | 50 |  | √ | ' ' | 负责人 |
| 4 | fdatanumber | 编码 | varchar | 200 |  | √ | ' ' | 编码 |
| 5 | fdatamodel | 实例工作项 | varchar | 36 |  | √ | ' ' | [业务对象列表_可多选 bos_flydb_objlist](../superquery_files/bos_flydb_objlist.md) |
| 6 | fsourcemasterid | 源实例内码 | int8 | 64 |  | √ | 0 | 源实例内码 |
| 7 | fdataid | 实例ID | int8 | 64 |  | √ | 0 | 实例ID |
| 8 | fpriority | 优先级 | varchar | 50 |  | √ | ' ' | 优先级 |
| 9 | fmodelnumber | 实例工作项编码 | varchar | 100 |  | √ | ' ' | 实例工作项编码 |
| 10 | fsourceversion | 源实例版本 | varchar | 50 |  | √ | ' ' | 源实例版本 |
| 11 | fcreatedatefield | 创建日期 | timestamp | 0 |  |  | null | 创建日期 |
| 12 | flcstatus | 生命周期状态 | varchar | 50 |  | √ | ' ' | 生命周期状态 |
| 13 | ftargetmodel | 目标工作项 | varchar | 36 |  | √ | ' ' | [业务对象列表_可多选 bos_flydb_objlist](../superquery_files/bos_flydb_objlist.md) |
| 14 | fpicturefield | 图片字段 | varchar | 255 |  | √ | ' ' | 图片字段 |
| 15 | fversion | 版本 | varchar | 50 |  | √ | ' ' | 版本 |
| 16 | fsourcehash | 源实例Hash码 | int8 | 64 |  | √ | 0 | 源实例Hash码 |
| 17 | fdataname | 名称 | varchar | 500 |  | √ | ' ' | 名称 |
| 18 | ftargetmasterid | 目标实例内码 | int8 | 64 |  | √ | 0 | 目标实例内码 |
| 19 | ftargethash | 目标实例Hash码 | int8 | 64 |  | √ | 0 | 目标实例Hash码 |
| 20 | fmodifierfield | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 21 | fdatamasterid | 实例内码 | int8 | 64 |  | √ | 0 | 实例内码 |
| 22 | ftargetversion | 目标实例版本 | varchar | 50 |  | √ | ' ' | 目标实例版本 |
| 23 | fcreaterfield | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 24 | fdataversion | 实例版本 | varchar | 50 |  | √ | ' ' | 实例版本 |
| 25 | fmodifydatefield | 修改日期 | timestamp | 0 |  |  | null | 修改日期 |
| 26 | fsourcemodel | 源工作项 | varchar | 36 |  | √ | ' ' | [业务对象列表_可多选 bos_flydb_objlist](../superquery_files/bos_flydb_objlist.md) |
| 27 | fislockversion | 是否定版 | bpchar | 1 |  | √ | '0' | 是否定版 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_plm_ipd_contextual_ins |  | fid |
| 2 | idx_t_plm_ipd_ctx_ins_t |  | ftargetmodel,ftargetmasterid,ftargetversion |
| 3 | idx_t_plm_ipd_ctx_ins_s |  | fsourcemodel,fsourcemasterid,fsourceversion |
| 4 | idx_t_plm_ipd_ctx_shash |  | fsourcehash |
| 5 | idx_t_plm_ipd_ctx_thash |  | ftargethash |

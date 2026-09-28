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
| 1 | fid | fid,fsnapshot |
| 2 | fsnapshot | fid,fsnapshot |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_plm_ipd_contextual_ins_s |  | fid,fsnapshot |
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
| 5 | fdatamodel | 实例工作项 | varchar | 50 |  | √ | ' ' | 业务对象列表_可多选 bos_flydb_objlist |
| 6 | fsourcemasterid | 源实例内码 | int8 | 64 |  | √ | 0 | 源实例内码 |
| 7 | fdataid | 实例ID | int8 | 64 |  | √ | 0 | 实例ID |
| 8 | fpriority | 优先级 | varchar | 50 |  | √ | ' ' | 优先级 |
| 9 | fmodelnumber | 实例工作项编码 | varchar | 100 |  | √ | ' ' | 实例工作项编码 |
| 10 | fdataname | 名称 | varchar | 500 |  | √ | ' ' | 名称 |
| 11 | fsourceversion | 源实例版本 | varchar | 50 |  | √ | ' ' | 源实例版本 |
| 12 | fcreatedatefield | 创建日期 | timestamp | 0 |  |  | null | 创建日期 |
| 13 | ftargetmasterid | 目标实例内码 | int8 | 64 |  | √ | 0 | 目标实例内码 |
| 14 | fmodifierfield | 修改人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 15 | fdatamasterid | 实例内码 | int8 | 64 |  | √ | 0 | 实例内码 |
| 16 | ftargetversion | 目标实例版本 | varchar | 50 |  | √ | ' ' | 目标实例版本 |
| 17 | fcreaterfield | 创建人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 18 | fdataversion | 实例版本 | varchar | 50 |  | √ | ' ' | 实例版本 |
| 19 | fmodifydatefield | 修改日期 | timestamp | 0 |  |  | null | 修改日期 |
| 20 | flcstatus | 生命周期状态 | varchar | 50 |  | √ | ' ' | 生命周期状态 |
| 21 | fsourcemodel | 源工作项 | varchar | 50 |  | √ | ' ' | 业务对象列表_可多选 bos_flydb_objlist |
| 22 | ftargetmodel | 目标工作项 | varchar | 50 |  | √ | ' ' | 业务对象列表_可多选 bos_flydb_objlist |
| 23 | fpicturefield | 图片字段 | varchar | 255 |  | √ | ' ' | 图片字段 |
| 24 | fversion | 版本 | varchar | 50 |  | √ | ' ' | 版本 |

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

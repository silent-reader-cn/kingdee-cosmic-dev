# 需求下文关系-plm_rm_contextual_rel

## 需求下文关系-主表 t_plm_rm_contextual_ins

- **表名称：** 需求下文关系-主表
- **表名：** t_plm_rm_contextual_ins

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fchargeperson | 负责人 | varchar | 50 |  | √ | ' ' | 负责人 |
| 2 | fcreator | 创建人 | varchar | 50 |  | √ | ' ' | 创建人 |
| 3 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 4 | fdatanumber | 编码 | varchar | 200 |  | √ | ' ' | 编码 |
| 5 | fdatamodel | 实例工作项 | varchar | 36 |  | √ | ' ' | 业务对象列表_可多选 bos_flydb_objlist |
| 6 | fpriority | 优先级 | varchar | 50 |  | √ | ' ' | 优先级 |
| 7 | fdataid | 实例ID | int8 | 64 |  | √ | 0 | 实例ID |
| 8 | fsourcemasterid | 源实例内码 | int8 | 64 |  | √ | 0 | 源实例内码 |
| 9 | fmodelnumber | 实例工作项编码 | varchar | 100 |  | √ | ' ' | 实例工作项编码 |
| 10 | fcreatedatefield | 创建日期 | timestamp | 0 |  |  | null | 创建日期 |
| 11 | fsourceversion | 源实例版本 | varchar | 50 |  | √ | ' ' | 源实例版本 |
| 12 | ftextfield | 标题 | varchar | 50 |  | √ | ' ' | 标题 |
| 13 | flcstatus | 生命周期状态 | varchar | 50 |  | √ | ' ' | 生命周期状态 |
| 14 | ftargetmodel | 目标工作项 | varchar | 36 |  | √ | ' ' | 业务对象列表_可多选 bos_flydb_objlist |
| 15 | fpicturefield | 图片字段 | varchar | 255 |  | √ | ' ' | 图片字段 |
| 16 | findustry | 所属行业 | varchar | 50 |  | √ | ' ' | 所属行业 |
| 17 | fversion | 版本 | varchar | 50 |  | √ | ' ' | 版本 |
| 18 | fexceptedrealiztime1 | 期望实现时间 | varchar | 50 |  | √ | ' ' | 期望实现时间 |
| 19 | fdataname | 名称 | varchar | 500 |  | √ | ' ' | 名称 |
| 20 | fdescription | 描述 | varchar | 50 |  | √ | ' ' | 描述 |
| 21 | ftargetmasterid | 目标实例内码 | int8 | 64 |  | √ | 0 | 目标实例内码 |
| 22 | fmodifierfield | 修改人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 23 | ftargetversion | 目标实例版本 | varchar | 50 |  | √ | ' ' | 目标实例版本 |
| 24 | fdatamasterid | 实例内码 | int8 | 64 |  | √ | 0 | 实例内码 |
| 25 | fcreaterfield | 创建人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 26 | fmodifydatefield | 修改日期 | timestamp | 0 |  |  | null | 修改日期 |
| 27 | fdataversion | 实例版本 | varchar | 50 |  | √ | ' ' | 实例版本 |
| 28 | fgroup | 需求分类 | varchar | 50 |  | √ | ' ' | 需求分类 |
| 29 | fsourcemodel | 源工作项 | varchar | 36 |  | √ | ' ' | 业务对象列表_可多选 bos_flydb_objlist |
| 30 | frelateproject | 关联项目 | varchar | 50 |  | √ | ' ' | 关联项目 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_plm_rm_contextual_ins_m0 |  | findustry |
| 2 | pk_plm_rm_contextual_ins |  | fid |

---

## 需求下文关系-分表 t_plm_rm_contextual_ins_s

- **表名称：** 需求下文关系-分表
- **表名：** t_plm_rm_contextual_ins_s

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
| 1 | pk_plm_rm_contextual_ins_s |  | fid |

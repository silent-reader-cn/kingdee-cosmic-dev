# 包需求详细信息-plm_rm_contextual

## 包需求详细信息-分表 t_plm_rm_contextual_ins_s

- **表名称：** 包需求详细信息-分表
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

---

## 关联PRD-多选基础资料表 t_plm_rm_relateprd

- **表名称：** 关联PRD-多选基础资料表
- **表名：** t_plm_rm_relateprd

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fbasedataid | fbasedataid | int8 | 64 |  | √ | 0 | [PRD产品包需求 plm_rm_prd](../plmrm_files/plm_rm_prd.md) |
| 3 | fpkid | fpkid | int8 | 64 |  | √ | 0 | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_plm_rm_relateprd_fk |  | fid |
| 2 | pk_plm_rm_relateprd |  | fpkid |

---

## 关联任务-多选基础资料表 t_plm_rm_relatetask

- **表名称：** 关联任务-多选基础资料表
- **表名：** t_plm_rm_relatetask

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fbasedataid | fbasedataid | int8 | 64 |  | √ | 0 | [任务 plm_ipd_task](../plmpm_files/plm_ipd_task.md) |
| 3 | fpkid | fpkid | int8 | 64 |  | √ | 0 | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_plm_rm_relatetask_fk |  | fid |
| 2 | pk_plm_rm_relatetask |  | fpkid |

---

## 关联MRD-多选基础资料表 t_plm_rm_relatemrd

- **表名称：** 关联MRD-多选基础资料表
- **表名：** t_plm_rm_relatemrd

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fbasedataid | fbasedataid | int8 | 64 |  | √ | 0 | [MRD市场包需求 plm_rm_mrd](../plmrm_files/plm_rm_mrd.md) |
| 3 | fpkid | fpkid | int8 | 64 |  | √ | 0 | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_plm_rm_relatemrd_fk |  | fid |
| 2 | pk_plm_rm_relatemrd |  | fpkid |

---

## 包需求详细信息-主表 t_plm_rm_contextual_ins

- **表名称：** 包需求详细信息-主表
- **表名：** t_plm_rm_contextual_ins

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fchargeperson | 负责人 | varchar | 50 |  | √ | ' ' | 负责人 |
| 2 | fcreator | 创建人 | varchar | 50 |  | √ | ' ' | 创建人 |
| 3 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 4 | fdatanumber | 编码 | varchar | 200 |  | √ | ' ' | 编码 |
| 5 | fdatamodel | 实例工作项 | varchar | 36 |  | √ | ' ' | [业务对象列表_可多选 bos_flydb_objlist](../superquery_files/bos_flydb_objlist.md) |
| 6 | fpriority | 优先级 | varchar | 50 |  | √ | ' ' | 优先级 |
| 7 | fdataid | 实例ID | int8 | 64 |  | √ | 0 | 实例ID |
| 8 | fsourcemasterid | 源实例内码 | int8 | 64 |  | √ | 0 | 源实例内码 |
| 9 | fmodelnumber | 实例工作项编码 | varchar | 100 |  | √ | ' ' | 实例工作项编码 |
| 10 | fcreatedatefield | 创建日期 | timestamp | 0 |  |  | null | 创建日期 |
| 11 | fsourceversion | 源实例版本 | varchar | 50 |  | √ | ' ' | 源实例版本 |
| 12 | ftextfield | 标题 | varchar | 50 |  | √ | ' ' | 标题 |
| 13 | flcstatus | 生命周期状态 | varchar | 50 |  | √ | ' ' | 生命周期状态 |
| 14 | ftargetmodel | 目标工作项 | varchar | 36 |  | √ | ' ' | [业务对象列表_可多选 bos_flydb_objlist](../superquery_files/bos_flydb_objlist.md) |
| 15 | fpicturefield | 图片字段 | varchar | 255 |  | √ | ' ' | 图片字段 |
| 16 | findustry | 所属行业 | varchar | 50 |  | √ | ' ' | 所属行业 |
| 17 | fversion | 版本 | varchar | 50 |  | √ | ' ' | 版本 |
| 18 | fexceptedrealiztime1 | 期望实现时间 | varchar | 50 |  | √ | ' ' | 期望实现时间 |
| 19 | fsourcehash | 源实例Hash码 | int8 | 64 |  | √ | 0 | 源实例Hash码 |
| 20 | fdataname | 名称 | varchar | 500 |  | √ | ' ' | 名称 |
| 21 | fdescription | fdescription | varchar | 50 |  | √ | ' ' |  |
| 22 | ftargetmasterid | 目标实例内码 | int8 | 64 |  | √ | 0 | 目标实例内码 |
| 23 | ftargethash | 目标实例Hash码 | int8 | 64 |  | √ | 0 | 目标实例Hash码 |
| 24 | fmodifierfield | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 25 | ftargetversion | 目标实例版本 | varchar | 50 |  | √ | ' ' | 目标实例版本 |
| 26 | fdatamasterid | 实例内码 | int8 | 64 |  | √ | 0 | 实例内码 |
| 27 | fcreaterfield | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 28 | fmodifydatefield | 修改日期 | timestamp | 0 |  |  | null | 修改日期 |
| 29 | fdataversion | 实例版本 | varchar | 50 |  | √ | ' ' | 实例版本 |
| 30 | fgroup | 需求分类 | varchar | 50 |  | √ | ' ' | 需求分类 |
| 31 | ftextareafield | 备注 | varchar | 255 |  | √ | ' ' | 备注 |
| 32 | fsourcemodel | 源工作项 | varchar | 36 |  | √ | ' ' | [业务对象列表_可多选 bos_flydb_objlist](../superquery_files/bos_flydb_objlist.md) |
| 33 | fislockversion | 是否定版 | bpchar | 1 |  | √ | '0' | 是否定版 |
| 34 | frelateproject | frelateproject | varchar | 50 |  | √ | ' ' |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_plm_rm_contextual_ins_m0 |  | findustry |
| 2 | idx_plm_rm_contextual_thash |  | ftargethash |
| 3 | idx_plm_rm_contextual_shash |  | fsourcehash |
| 4 | pk_plm_rm_contextual_ins |  | fid |

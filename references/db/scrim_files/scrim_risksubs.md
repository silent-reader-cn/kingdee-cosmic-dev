# 风险订阅-scrim_risksubs

## 适用组织-子表 t_scrim_risksubs_org

- **表名称：** 适用组织-子表
- **表名：** t_scrim_risksubs_org

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 3 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 4 | forg | 组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_scrim_risksubs_org |  | fentryid |
| 2 | idx_scrim_risksubs_org_fid |  | fid |

---

## 维度字段映射-子表 t_scrim_risksubs_mapping

- **表名称：** 维度字段映射-子表
- **表名：** t_scrim_risksubs_mapping

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fctrlbillfield | 控制单据字段 | varchar | 50 |  | √ | ' ' | 控制单据字段,枚举: |
| 2 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 3 | fdetailid | fdetailid | int8 | 64 |  | √ | 0 | id |
| 4 | fcomparetype | 条件 | varchar | 50 |  | √ | ' ' | 条件,枚举: equals :等于 not_equals :不等于 large_than :大于 large_equals :大于等于 less_than :小于 less_equals :小于等于 is_null :为空 |
| 5 | fentryid | fentryid | int8 | 64 |  | √ | 0 |  |
| 6 | fmetrics | 指标编码 | int8 | 64 |  | √ | 0 | [数据指标 sbs_datametrics](../sbs_files/sbs_datametrics.md) |
| 7 | fmetricsfield | 指标维度字段值 | varchar | 50 |  | √ | ' ' | 指标维度字段值 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fdetailid | fdetailid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_scrim_risksubs_mapping |  | fdetailid |
| 2 | idx_scrim_risksubs_mapping_eid |  | fentryid |

---

## 风险事件-子表 t_scrim_risksubs_event

- **表名称：** 风险事件-子表
- **表名：** t_scrim_risksubs_event

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | friskevent | 事件编码 | int8 | 64 |  | √ | 0 | [风险事件 scrim_riskevent](../scrim_files/scrim_riskevent.md) |
| 3 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 4 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_scrim_risksubs_event_fid |  | fid |
| 2 | pk_t_scrim_risksubs_event |  | fentryid |

---

## 风险级别控制-子表 t_scrim_risksubs_level

- **表名称：** 风险级别控制-子表
- **表名：** t_scrim_risksubs_level

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | frisklevel | 风险级别 | varchar | 50 |  | √ | ' ' | 风险级别,枚举: high :高风险 middle :中风险 low :低风险 |
| 2 | fctrltype | 控制方式 | varchar | 50 |  | √ | ' ' | 控制方式,枚举: strict :严格控制 warning :预警提示 ignore :不控制 |
| 3 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 4 | fdetailid | fdetailid | int8 | 64 |  | √ | 0 | id |
| 5 | fentryid | fentryid | int8 | 64 |  | √ | 0 |  |
| 6 | fctrlops | 控制操作 | varchar | 2000 |  | √ | ' ' | 控制操作,枚举: |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fdetailid | fdetailid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_scrim_risksubs_level |  | fdetailid |
| 2 | idx_scrim_risksubs_level_eid |  | fentryid |

---

## 风险订阅-主表 t_scrim_risksubs

- **表名称：** 风险订阅-主表
- **表名：** t_scrim_risksubs

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fname | 名称 | varchar | 50 |  | √ | ' ' | 名称 |
| 3 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 4 | fgroupid | 订阅分组 | int8 | 64 |  | √ | 0 | [风险订阅分组 scrim_risksubs_group](../scrim_files/scrim_risksubs_group.md) |
| 5 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 6 | fsubstarget | 订阅对象 | varchar | 50 |  | √ | ' ' | [主实体对象 bos_entityobject](../mdl_files/bos_entityobject.md) |
| 7 | fdisabledate | 禁用时间 | timestamp | 0 |  |  | null | 禁用时间 |
| 8 | fdisablerid | 禁用人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 9 | fdescription | 备注 | varchar | 512 |  | √ | ' ' | 备注 |
| 10 | fauditdate | 审核时间 | timestamp | 0 |  |  | null | 审核时间 |
| 11 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 12 | fappid | 所属应用 | varchar | 36 |  | √ | ' ' | [业务应用实体 bos_devportal_bizapp](../mdl_files/bos_devportal_bizapp.md) |
| 13 | fstatus | 数据状态 | bpchar | 1 |  | √ | ' ' | 数据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 14 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 15 | fmasterid | 主数据内码 | int8 | 64 |  | √ | 0 | 主数据内码 |
| 16 | fauditor | 审核人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 17 | ftriggerpoint | 触发时点 | varchar | 50 |  | √ | ' ' | 触发时点,枚举: save :保存 submit :提交 audit :审核 |
| 18 | fenable | 可用状态 | bpchar | 1 |  | √ | ' ' | 可用状态,枚举: 0 :禁用 1 :可用 |
| 19 | fsubstype | 订阅类型 | varchar | 50 |  | √ | ' ' | 订阅类型,枚举: bos_entityobject :单据 |
| 20 | fnumber | 编码 | varchar | 30 |  | √ | ' ' | 编码 |
| 21 | fissyspreset | 系统预设 | bpchar | 1 |  | √ | ' ' | 系统预设 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_scrim_risksubs |  | fid |
| 2 | idx_scrim_risksubs_fnumber |  | fnumber |

---

## 风险订阅-多语言表 t_scrim_risksubs_l

- **表名称：** 风险订阅-多语言表
- **表名：** t_scrim_risksubs_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fname | 名称 | varchar | 255 |  | √ | ' ' | 名称 |
| 3 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 4 | fdescription | 备注 | varchar | 512 |  | √ | ' ' | 备注 |
| 5 | fpkid | fpkid | varchar | 36 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_scrim_risksubs_l_fid |  | fid |
| 2 | pk_t_scrim_risksubs_l |  | fpkid |

# 风险事件-scrim_riskevent

## 风险事件-主表 t_scrim_riskevent

- **表名称：** 风险事件-主表
- **表名：** t_scrim_riskevent

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fname | 事件名称 | varchar | 50 |  | √ | ' ' | 事件名称 |
| 3 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 4 | fgroupid | 事件分组 | int8 | 64 |  | √ | 0 | [风险事件分组 scrim_riskevent_group](../scrim_files/scrim_riskevent_group.md) |
| 5 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 6 | fdisabledate | 禁用时间 | timestamp | 0 |  |  | null | 禁用时间 |
| 7 | fdisablerid | 禁用人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 8 | fdescription | 备注 | varchar | 512 |  | √ | ' ' | 备注 |
| 9 | fauditdate | 审核时间 | timestamp | 0 |  |  | null | 审核时间 |
| 10 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 11 | fappid | 所属应用 | varchar | 36 |  | √ | ' ' | [业务应用实体 bos_devportal_bizapp](../mdl_files/bos_devportal_bizapp.md) |
| 12 | fstatus | 数据状态 | bpchar | 1 |  | √ | ' ' | 数据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 13 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 14 | fmasterid | 主数据内码 | int8 | 64 |  | √ | 0 | 主数据内码 |
| 15 | fauditor | 审核人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 16 | fenable | 可用状态 | bpchar | 1 |  | √ | ' ' | 可用状态,枚举: 0 :禁用 1 :可用 |
| 17 | fnumber | 事件编码 | varchar | 30 |  | √ | ' ' | 事件编码 |
| 18 | fissyspreset | 系统预设 | bpchar | 1 |  | √ | ' ' | 系统预设 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_scrim_riskevent_fnumber |  | fnumber |
| 2 | pk_t_scrim_riskevent |  | fid |

---

## 指标明细-子表 t_scrim_riskevententry

- **表名称：** 指标明细-子表
- **表名：** t_scrim_riskevententry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fcondition_tag | 数据范围_详情 | text | 0 |  |  | null | 数据范围_详情 |
| 3 | fmetricscard | 指标卡片 | int8 | 64 |  | √ | 0 | [指标卡片 sbs_topiccard](../sbs_files/sbs_topiccard.md) |
| 4 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 5 | fcondition | 数据范围 | varchar | 2000 |  | √ | ' ' | 数据范围 |
| 6 | fdataplugin | 数据插件 | varchar | 512 |  | √ | ' ' | 数据插件 |
| 7 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 8 | fmetrics | 指标编码 | int8 | 64 |  | √ | 0 | [数据指标 sbs_datametrics](../sbs_files/sbs_datametrics.md) |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_t_scrim_riskevententry_fid |  | fid |
| 2 | pk_t_scrim_riskevententry |  | fentryid |

---

## 风险事件-多语言表 t_scrim_riskevent_l

- **表名称：** 风险事件-多语言表
- **表名：** t_scrim_riskevent_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fname | 事件名称 | varchar | 255 |  | √ | ' ' | 事件名称 |
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
| 1 | idx_scrim_riskevent_l_fid |  | fid |
| 2 | pk_t_scrim_riskevent_l |  | fpkid |

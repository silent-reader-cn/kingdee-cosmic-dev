# 风险预警设置-scrim_riskwarning

## 风险预警设置-多语言表 t_scrim_riskwarning_l

- **表名称：** 风险预警设置-多语言表
- **表名：** t_scrim_riskwarning_l

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
| 1 | pk_t_scrim_riskwarning_l |  | fpkid |
| 2 | idx_scrim_riskwarning_l_fid |  | fid |

---

## 风险规则-子表 t_scrim_riskwarningentry

- **表名称：** 风险规则-子表
- **表名：** t_scrim_riskwarningentry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fleftbracket | 左括号 | varchar | 10 |  | √ | ' ' | 左括号,枚举: ( :( (( :(( ((( :((( |
| 3 | faccording | 依据 | varchar | 50 |  | √ | ' ' | 依据,枚举: metrics :指标值 |
| 4 | frightbracket | 右括号 | varchar | 10 |  | √ | ' ' | 右括号,枚举: ) :) )) :)) ))) :))) |
| 5 | fmetricsvalue | 指标值 | varchar | 255 |  | √ | ' ' | 指标值 |
| 6 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 7 | fcomparetype | 条件 | varchar | 50 |  | √ | ' ' | 条件,枚举: equals :等于 not_equals :不等于 large_than :大于 large_equals :大于等于 less_than :小于 less_equals :小于等于 is_null :为空 |
| 8 | flogic | 逻辑 | varchar | 10 |  | √ | ' ' | 逻辑,枚举: 0 :并且 1 :或者 |
| 9 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 10 | fmetrics | 指标编码 | int8 | 64 |  | √ | 0 | [数据指标 sbs_datametrics](../sbs_files/sbs_datametrics.md) |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_scrim_riskwarningentry_fid |  | fid |
| 2 | pk_t_scrim_riskwarningentry |  | fentryid |

---

## 风险预警设置-主表 t_scrim_riskwarning

- **表名称：** 风险预警设置-主表
- **表名：** t_scrim_riskwarning

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fname | 名称 | varchar | 50 |  | √ | ' ' | 名称 |
| 3 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 4 | fgroupid | 预警分组 | int8 | 64 |  | √ | 0 | [风险预警分组 scrim_riskwarning_group](../scrim_files/scrim_riskwarning_group.md) |
| 5 | friskevent | 风险事件 | int8 | 64 |  | √ | 0 | [风险事件 scrim_riskevent](../scrim_files/scrim_riskevent.md) |
| 6 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 7 | fdisabledate | 禁用时间 | timestamp | 0 |  |  | null | 禁用时间 |
| 8 | fdisablerid | 禁用人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 9 | fdescription | 备注 | varchar | 512 |  | √ | ' ' | 备注 |
| 10 | fauditdate | 审核时间 | timestamp | 0 |  |  | null | 审核时间 |
| 11 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 12 | fappid | 所属应用 | varchar | 36 |  | √ | ' ' | [业务应用实体 bos_devportal_bizapp](../mdl_files/bos_devportal_bizapp.md) |
| 13 | fstatus | 数据状态 | bpchar | 1 |  | √ | ' ' | 数据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 14 | flevel | 风险级别 | varchar | 50 |  | √ | ' ' | 风险级别,枚举: high :高风险 middle :中风险 low :低风险 |
| 15 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 16 | fmasterid | 主数据内码 | int8 | 64 |  | √ | 0 | 主数据内码 |
| 17 | fauditor | 审核人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 18 | fenable | 可用状态 | bpchar | 1 |  | √ | ' ' | 可用状态,枚举: 0 :禁用 1 :可用 |
| 19 | fnumber | 编码 | varchar | 30 |  | √ | ' ' | 编码 |
| 20 | fissyspreset | 系统预设 | bpchar | 1 |  | √ | ' ' | 系统预设 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_scrim_riskwarning |  | fid |
| 2 | idx_scrim_riskwarning_fnumber |  | fnumber |

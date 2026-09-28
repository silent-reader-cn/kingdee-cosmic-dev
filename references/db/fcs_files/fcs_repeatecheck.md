# 重复控制设置-fcs_repeatecheck

## 重复控制设置-多语言表 t_fcs_repeatecheck_l

- **表名称：** 重复控制设置-多语言表
- **表名：** t_fcs_repeatecheck_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |

---

## 重复控制设置-主表 t_fcs_repeatecheck

- **表名称：** 重复控制设置-主表
- **表名：** t_fcs_repeatecheck

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |

---

## 规则单据体-子表 t_fcs_checkctrl_amtctrl

- **表名称：** 规则单据体-子表
- **表名：** t_fcs_checkctrl_amtctrl

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fistargetabs | 目标单金额是否使用绝对值 | bpchar | 1 |  | √ | '0' | 目标单金额是否使用绝对值 |
| 3 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 4 | ftargetamtruledesc | 目标单金额字段规则 | varchar | 512 |  | √ | ' ' | 目标单金额字段规则 |
| 5 | ftargetcondition | 目标单条件 | varchar | 255 |  | √ | ' ' | 目标单条件 |
| 6 | fistargetmulamt | 目标单多个金额参与计算 | bpchar | 1 |  | √ | '0' | 目标单多个金额参与计算 |
| 7 | ftargetamtfieldname | 目标单金额字段名称 | varchar | 50 |  | √ | ' ' | 目标单金额字段名称 |
| 8 | ftargetrule | 目标单采集规则 | varchar | 50 |  | √ | ' ' | 目标单采集规则,枚举: Head :单据头 EntrySingle :单据体逐一 EntrySum :单据体合计 |
| 9 | ftargetmulamt | 目标单多金额采集 | varchar | 255 |  | √ | ' ' | 目标单多金额采集 |
| 10 | fissrcabs | 源单金额是否使用绝对值 | bpchar | 1 |  | √ | '0' | 源单金额是否使用绝对值 |
| 11 | ftargetamtrule | 目标单金额字段规则 | varchar | 255 |  | √ | ' ' | 目标单金额字段规则 |
| 12 | ftargetmulamt_tag | 目标单多金额采集_详情 | varchar | 2000 |  | √ | ' ' | 目标单多金额采集_详情 |
| 13 | ftargetconditiondesc | 目标单条件 | varchar | 50 |  | √ | ' ' | 目标单条件 |
| 14 | fsrcconditiondesc | 源单条件 | varchar | 50 |  | √ | ' ' | 源单条件 |
| 15 | fistargetamtrule | 使用目标单金额字段规则 | bpchar | 1 |  | √ | '0' | 使用目标单金额字段规则 |
| 16 | fsrcrule | 源单采集规则 | varchar | 50 |  | √ | ' ' | 源单采集规则,枚举: Head :单据头 EntrySingle :单据体逐一 EntrySum :单据体合计 |
| 17 | ftargetamtfield | 目标单金额字段 | varchar | 50 |  | √ | ' ' | 目标单金额字段 |
| 18 | ftargetcondition_tag | 目标单条件_详情 | text | 0 |  |  | null | 目标单条件_详情 |
| 19 | fsrcamtfieldname | 源单金额字段名称 | varchar | 50 |  | √ | ' ' | 源单金额字段名称 |
| 20 | fsrccondition | 源单条件 | varchar | 255 |  | √ | ' ' | 源单条件 |
| 21 | fsrcamtfield | 源单金额字段 | varchar | 50 |  | √ | ' ' | 源单金额字段 |
| 22 | ftargetmulamtdesc | 目标单多金额采集 | varchar | 512 |  | √ | ' ' | 目标单多金额采集 |
| 23 | fsrccondition_tag | 源单条件_详情 | text | 0 |  |  | null | 源单条件_详情 |
| 24 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 25 | ftargetamtrule_tag | 目标单金额字段规则_详情 | varchar | 4000 |  | √ | ' ' | 目标单金额字段规则_详情 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_fcs_checkctrl_amtctrl |  | fid |
| 2 | pk_t_fcs_checkctrl_amtctrl |  | fentryid |

---

## 子单据体-子表 t_fcs_checkctrl_subamt

- **表名称：** 子单据体-子表
- **表名：** t_fcs_checkctrl_subamt

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fisothermulamt | 目标单多个金额参与计算 | bpchar | 1 |  | √ | '0' | 目标单多个金额参与计算 |
| 2 | fothercondition | 目标单条件 | varchar | 255 |  | √ | ' ' | 目标单条件 |
| 3 | fothermulamt | 目标单多金额采集 | varchar | 255 |  | √ | ' ' | 目标单多金额采集 |
| 4 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 5 | fothermulamt_tag | 目标单多金额采集_详情 | varchar | 2000 |  | √ | ' ' | 目标单多金额采集_详情 |
| 6 | fotherconditiondesc | 目标单条件 | varchar | 50 |  | √ | ' ' | 目标单条件 |
| 7 | fothercondition_tag | 目标单条件_详情 | text | 0 |  |  | null | 目标单条件_详情 |
| 8 | fothertargetamtfieldname | 目标单金额字段名称 | varchar | 50 |  | √ | ' ' | 目标单金额字段名称 |
| 9 | fothertargetentity | 目标单据 | varchar | 50 |  | √ | ' ' | [单据主实体 bos_billmainentity](../mdl_files/bos_billmainentity.md) |
| 10 | fothertargetamtfield | 目标单金额字段 | varchar | 50 |  | √ | ' ' | 目标单金额字段 |
| 11 | fdetailid | fdetailid | int8 | 64 |  | √ | 0 | id |
| 12 | fisotherabs | 目标单金额是否使用绝对值 | bpchar | 1 |  | √ | '0' | 目标单金额是否使用绝对值 |
| 13 | fentryid | fentryid | int8 | 64 |  | √ | 0 |  |
| 14 | fothermulamtdesc | 目标单多金额采集 | varchar | 512 |  | √ | ' ' | 目标单多金额采集 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fdetailid | fdetailid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_fcs_checkctrl_subamt |  | fentryid |
| 2 | pk_t_fcs_checkctrl_subamt |  | fdetailid |

---

## 消息接收人-多选基础资料表 t_repeateccheckuser

- **表名称：** 消息接收人-多选基础资料表
- **表名：** t_repeateccheckuser

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |

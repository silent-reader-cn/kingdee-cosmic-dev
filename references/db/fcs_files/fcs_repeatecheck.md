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
| 2 | ftargetconditiondesc | 目标单条件 | varchar | 50 |  | √ | ' ' | 目标单条件 |
| 3 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 4 | fsrcconditiondesc | 源单条件 | varchar | 50 |  | √ | ' ' | 源单条件 |
| 5 | fsrcrule | 源单采集规则 | varchar | 50 |  | √ | ' ' | 源单采集规则,枚举: Head :单据头 EntrySingle :单据体逐一 EntrySum :单据体合计 |
| 6 | ftargetamtfield | 目标单金额字段 | varchar | 50 |  | √ | ' ' | 目标单金额字段 |
| 7 | ftargetcondition_tag | 目标单条件_详情 | text | 0 |  |  | null | 目标单条件_详情 |
| 8 | fsrcamtfieldname | 源单金额字段名称 | varchar | 50 |  | √ | ' ' | 源单金额字段名称 |
| 9 | fsrccondition | 源单条件 | varchar | 255 |  | √ | ' ' | 源单条件 |
| 10 | ftargetcondition | 目标单条件 | varchar | 255 |  | √ | ' ' | 目标单条件 |
| 11 | ftargetamtfieldname | 目标单金额字段名称 | varchar | 50 |  | √ | ' ' | 目标单金额字段名称 |
| 12 | fsrcamtfield | 源单金额字段 | varchar | 50 |  | √ | ' ' | 源单金额字段 |
| 13 | fsrccondition_tag | 源单条件_详情 | text | 0 |  |  | null | 源单条件_详情 |
| 14 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 15 | ftargetrule | 目标单采集规则 | varchar | 50 |  | √ | ' ' | 目标单采集规则,枚举: Head :单据头 EntrySingle :单据体逐一 EntrySum :单据体合计 |

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
| 1 | fothercondition | 目标单条件 | varchar | 255 |  | √ | ' ' | 目标单条件 |
| 2 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 3 | fothertargetentity | 目标单据 | varchar | 50 |  | √ | ' ' | 单据主实体 bos_billmainentity |
| 4 | fothertargetamtfield | 目标单金额字段 | varchar | 50 |  | √ | ' ' | 目标单金额字段 |
| 5 | fdetailid | fdetailid | int8 | 64 |  | √ | 0 | id |
| 6 | fotherconditiondesc | 目标单条件 | varchar | 50 |  | √ | ' ' | 目标单条件 |
| 7 | fothercondition_tag | 目标单条件_详情 | text | 0 |  |  | null | 目标单条件_详情 |
| 8 | fentryid | fentryid | int8 | 64 |  | √ | 0 |  |
| 9 | fothertargetamtfieldname | 目标单金额字段名称 | varchar | 50 |  | √ | ' ' | 目标单金额字段名称 |

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

# 支付防重-fcs_checkctrl

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

## 支付防重-主表 t_fcs_checkctrl

- **表名称：** 支付防重-主表
- **表名：** t_fcs_checkctrl

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fisctrlamt | 防超额控制 | bpchar | 1 |  | √ | '0' | 防超额控制 |
| 3 | fdisabledate | 禁用日期 | timestamp | 0 |  |  | null | 禁用日期 |
| 4 | fispreset | 是否系统预置 | bpchar | 1 |  | √ | '0' | 是否系统预置 |
| 5 | fmodifytime | 最后更新时间 | timestamp | 0 |  |  | null | 最后更新时间 |
| 6 | frepeatmessage | 重复提示信息 | varchar | 255 |  | √ | ' ' | 重复提示信息 |
| 7 | fstatus | 数据状态 | varchar | 30 |  | √ | ' ' | 数据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 8 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 9 | fmasterid | 主数据内码 | int8 | 64 |  | √ | 0 | 主数据内码 |
| 10 | fpayaccessid | 资金安全支付准入对象 | int8 | 64 |  | √ | 0 | 支付准入 fcs_payaccess |
| 11 | fctrlrule | 超额规则 | varchar | 50 |  | √ | ' ' | 超额规则,枚举: LargerOrEqual :源单金额>=目标单金额 |
| 12 | fsrcentityid | 源单 | varchar | 50 |  | √ | ' ' | 单据主实体 bos_billmainentity |
| 13 | fenablerid | 启用人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 14 | frepeatop | 目标单注册操作 | varchar | 50 |  | √ | ' ' | 目标单注册操作,枚举: |
| 15 | fisload | 按支付链路匹配 | bpchar | 1 |  | √ | '0' | 按支付链路匹配 |
| 16 | ffilter | 数据过滤条件 | varchar | 255 |  | √ | ' ' | 数据过滤条件 |
| 17 | fsrcbillidfield | 源单唯一值保存字段 | varchar | 50 |  | √ | ' ' | 源单唯一值保存字段 |
| 18 | fctrlentityid | 目标单 | varchar | 50 |  | √ | ' ' | 单据主实体 bos_billmainentity |
| 19 | fname | 名称 | varchar | 255 |  | √ | ' ' | 名称 |
| 20 | fmodifierid | 最后更新人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 21 | fismatch | fismatch | bpchar | 1 |  | √ | '0' |  |
| 22 | fcomment | fcomment | varchar | 255 |  | √ | ' ' |  |
| 23 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 24 | fctrlamtop | 目标单注册操作 | varchar | 50 |  | √ | ' ' | 目标单注册操作,枚举: |
| 25 | fopreat | 注册操作合集 | varchar | 50 |  | √ | ' ' | 注册操作合集 |
| 26 | fenabledate | 启用日期 | timestamp | 0 |  |  | null | 启用日期 |
| 27 | fdisablerid | 禁用人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 28 | ffilter_tag | 数据过滤条件_详情 | text | 0 |  |  | null | 数据过滤条件_详情 |
| 29 | fisbyrecord | 按支付链路查重 | bpchar | 1 |  | √ | '0' | 按支付链路查重 |
| 30 | fcustomsign | 自定义实体 | varchar | 50 |  | √ | ' ' | 自定义实体 |
| 31 | fisbotp | fisbotp | bpchar | 1 |  | √ | '0' |  |
| 32 | fisrepeat | 防重推控制 | bpchar | 1 |  | √ | '0' | 防重推控制 |
| 33 | fctrlmessage | 超额提示信息 | varchar | 255 |  | √ | ' ' | 超额提示信息 |
| 34 | fenable | 使用状态 | varchar | 30 |  | √ | ' ' | 使用状态,枚举: 0 :禁用 1 :可用 |
| 35 | fnumber | 编码 | varchar | 80 |  | √ | ' ' | 编码 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_fcs_checkctrl |  | fid |
| 2 | idx_t_fcs_checkctrl |  | fenable,fctrlentityid |

---

## 支付防重-多语言表 t_fcs_checkctrl_l

- **表名称：** 支付防重-多语言表
- **表名：** t_fcs_checkctrl_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | frepeatmessage | 重复提示信息 | varchar | 255 |  | √ | ' ' | 重复提示信息 |
| 3 | fname | 名称 | varchar | 255 |  | √ | ' ' | 名称 |
| 4 | fcomment | 备注 | varchar | 255 |  | √ | ' ' | 备注 |
| 5 | fctrlmessage | 超额提示信息 | varchar | 255 |  | √ | ' ' | 超额提示信息 |
| 6 | flocaleid | flocaleid | varchar | 30 |  | √ | ' ' | localeid |
| 7 | fpkid | fpkid | varchar | 30 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_fcs_checkctrl_l |  | fpkid |
| 2 | idx_t_fcs_checkctrl_l |  | fid,flocaleid |

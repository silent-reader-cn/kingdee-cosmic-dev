# 库存查询显示设置-mscm_iminventorycfg

## 库存明细-子表 t_mscm_imcfgshowlist

- **表名称：** 库存明细-子表
- **表名：** t_mscm_imcfgshowlist

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 3 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 4 | fshowlist | 明细字段 | varchar | 36 |  | √ | ' ' | 明细字段,枚举: |
| 5 | fshowlistenable | 是否显示 | bpchar | 1 |  | √ | '0' | 是否显示 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_mscm_imcfgshowlist_fid |  | fid |
| 2 | pk_mscm_imcfgshowlist |  | fentryid |

---

## 筛选条件-子表 t_mscm_imcfgfilter

- **表名称：** 筛选条件-子表
- **表名：** t_mscm_imcfgfilter

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 3 | ffilter | 筛选列表 | varchar | 36 |  | √ | ' ' | 筛选列表,枚举: |
| 4 | ffilterenable | 启用 | bpchar | 1 |  | √ | '0' | 启用 |
| 5 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_mscm_imcfgfilter_fid |  | fid |
| 2 | pk_mscm_imcfgfilter |  | fentryid |

---

## 汇总方式-子表 t_mscm_imcfgsummary

- **表名称：** 汇总方式-子表
- **表名：** t_mscm_imcfgsummary

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fsummaryshow | 是否显示 | bpchar | 1 |  | √ | '0' | 是否显示 |
| 3 | fsummaryenable | 是否汇总 | bpchar | 1 |  | √ | '0' | 是否汇总 |
| 4 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 5 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 6 | fsummary | 汇总字段 | varchar | 36 |  | √ | ' ' | 汇总字段,枚举: |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_mscm_imcfgsummary |  | fentryid |
| 2 | idx_mscm_imcfgsummary_fid |  | fid |

---

## 库存查询显示设置-主表 t_mscm_iminventorycfg

- **表名称：** 库存查询显示设置-主表
- **表名：** t_mscm_iminventorycfg

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fallowmodify | 允许用户修改 | bpchar | 1 |  | √ | '0' | 允许用户修改 |
| 3 | fname | 单据名称 | varchar | 100 |  | √ | ' ' | 单据名称 |
| 4 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 5 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 6 | fnote | 备注 | varchar | 512 |  | √ | ' ' | 备注 |
| 7 | fdisabledate | 禁用时间 | timestamp | 0 |  |  | null | 禁用时间 |
| 8 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 9 | fstatus | 数据状态 | varchar | 10 |  | √ | ' ' | 数据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 10 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 11 | fmasterid | 主数据内码 | int8 | 64 |  | √ | 0 | 主数据内码 |
| 12 | fpreset | 系统预设 | bpchar | 1 |  | √ | '0' | 系统预设 |
| 13 | fenable | 使用状态 | bpchar | 1 |  | √ | '0' | 使用状态,枚举: 0 :禁用 1 :可用 |
| 14 | fdisabler | 禁用人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 15 | fnumber | 编码 | varchar | 100 |  | √ | ' ' | 编码 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_mscm_iminventorycfg |  | fid |
| 2 | idx_mscm_invcfg_enable |  | fenable |

---

## 库存查询显示设置-多语言表 t_mscm_iminventorycfg_l

- **表名称：** 库存查询显示设置-多语言表
- **表名：** t_mscm_iminventorycfg_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fname | 单据名称 | varchar | 100 |  | √ | ' ' | 单据名称 |
| 3 | fnote | 备注 | varchar | 512 |  | √ | ' ' | 备注 |
| 4 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 5 | fpkid | fpkid | varchar | 36 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_mscm_iminventorycfg_l |  | fpkid |
| 2 | idx_mscm_invcfg_l_idloc |  | fid,flocaleid |

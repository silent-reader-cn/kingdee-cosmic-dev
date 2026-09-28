# 可发量计算规则-sm_expectqtycalrules

## 预计出-子表 t_sm_expectqtyout

- **表名称：** 预计出-子表
- **表名：** t_sm_expectqtyout

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fbillstatus | 单据状态 | bpchar | 1 |  | √ | ' ' | 单据状态,枚举: 0 :已保存 1 :已提交 2 :已审核 |
| 3 | fisinvbill | 是否库存单据 | bpchar | 1 |  | √ | '0' | 是否库存单据 |
| 4 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 5 | fenable | 是否启用 | bpchar | 1 |  | √ | '0' | 是否启用 |
| 6 | foutbillid | 预计出单据名称 | int8 | 64 |  | √ | 0 | 可发量单据配置 sm_expectqtybillsetting |
| 7 | fsameprocessprebill | 同一流程的前置单据 | bpchar | 1 |  | √ | '0' | 同一流程的前置单据 |
| 8 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 9 | fbilltypeid | 单据类型 | int8 | 64 |  | √ | 0 | 单据类型 bos_billtype |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_sm_expectqtyout |  | fid |
| 2 | pk_sm_expectqtyout |  | fentryid |

---

## 可发量计算规则-多语言表 t_sm_expectqtycalrules_l

- **表名称：** 可发量计算规则-多语言表
- **表名：** t_sm_expectqtycalrules_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fname | 名称 | varchar | 100 |  | √ | ' ' | 名称 |
| 3 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 4 | fdescription | 备注 | varchar | 500 |  | √ | ' ' | 备注 |
| 5 | fpkid | fpkid | varchar | 36 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_sm_expectqtycalrules_l |  | fpkid |
| 2 | idx_sm_expectqtycalrules_l |  | fid,flocaleid |

---

## 可发量计算规则-主表 t_sm_expectqtycalrules

- **表名称：** 可发量计算规则-主表
- **表名：** t_sm_expectqtycalrules

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fname | 名称 | varchar | 50 |  | √ | ' ' | 名称 |
| 3 | fmodifierid | 修改人 | int8 | 64 |  |  | 0 | 人员 bos_user |
| 4 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 5 | fdisabledate | 禁用时间 | timestamp | 0 |  |  | null | 禁用时间 |
| 6 | fdisablerid | 禁用人 | int8 | 64 |  |  | 0 | 人员 bos_user |
| 7 | fdescription | 备注 | varchar | 500 |  | √ | ' ' | 备注 |
| 8 | faudittime | 审核时间 | timestamp | 0 |  |  | null | 审核时间 |
| 9 | fshelflifedays | 天数 | int8 | 64 |  |  | 0 | 天数 |
| 10 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 11 | fdisplaysafetyinv | 安全库存仅显示 | bpchar | 1 |  | √ | '0' | 安全库存仅显示 |
| 12 | ftimerangedays | 时间范围天数 | int8 | 64 |  |  | 0 | 时间范围天数 |
| 13 | fstatus | 数据状态 | bpchar | 1 |  | √ | ' ' | 数据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 14 | ftimerangetype | 预计出\预计入统计时间范围（天） | varchar | 50 |  | √ | ' ' | 预计出\预计入统计时间范围（天）,枚举: 0 :30 1 :60 2 :90 3 :180 4 :365 -1 :自定义 |
| 15 | fcreatorid | 创建人 | int8 | 64 |  |  | 0 | 人员 bos_user |
| 16 | fmasterid | 主数据内码 | int8 | 64 |  |  | 0 | 主数据内码 |
| 17 | fexpectinonlydisplay | 预计入仅显示 | bpchar | 1 |  | √ | '0' | 预计入仅显示 |
| 18 | fenable | 使用状态 | bpchar | 1 |  | √ | ' ' | 使用状态,枚举: 0 :禁用 1 :可用 |
| 19 | fcalqtybyrequiredate | 按需求日期统计可发量 | bpchar | 1 |  | √ | '0' | 按需求日期统计可发量 |
| 20 | fdeductsafetyinv | 扣减安全库存 | bpchar | 1 |  | √ | '0' | 扣减安全库存 |
| 21 | fnumber | 编码 | varchar | 30 |  | √ | ' ' | 编码 |
| 22 | fissyspreset | 系统预置 | bpchar | 1 |  | √ | '0' | 系统预置 |
| 23 | fauditorid | 审核人 | int8 | 64 |  |  | 0 | 人员 bos_user |
| 24 | fdeductshelflifeinv | 扣减保质期临时 | bpchar | 1 |  | √ | '0' | 扣减保质期临时 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_sm_expectqtycalrules |  | fnumber |
| 2 | pk_sm_expectqtycalrules |  | fid |

---

## 库存维度-子表 t_sm_statinvdimension

- **表名称：** 库存维度-子表
- **表名：** t_sm_statinvdimension

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | finvdimension | 库存维度 | varchar | 50 |  | √ | ' ' | 库存维度 |
| 3 | finvdimensionname | finvdimensionname | varchar | 50 |  | √ | ' ' |  |
| 4 | fisstat | 是否统计 | bpchar | 1 |  | √ | '0' | 是否统计 |
| 5 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 6 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_sm_statinvdimension |  | fentryid |
| 2 | idx_sm_statinvdimension |  | fid |

---

## 预计入-子表 t_sm_expectqtyin

- **表名称：** 预计入-子表
- **表名：** t_sm_expectqtyin

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fbillstatus | 单据状态 | bpchar | 1 |  | √ | ' ' | 单据状态,枚举: 0 :已保存 1 :已提交 2 :已审核 |
| 3 | fisinvbill | 是否库存单据 | bpchar | 1 |  | √ | '0' | 是否库存单据 |
| 4 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 5 | fenable | 是否启用 | bpchar | 1 |  | √ | '0' | 是否启用 |
| 6 | fsameprocessprebill | 同一流程的前置单据 | bpchar | 1 |  | √ | '0' | 同一流程的前置单据 |
| 7 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 8 | finbillid | 预计入单据名称 | int8 | 64 |  | √ | 0 | 可发量单据配置 sm_expectqtybillsetting |
| 9 | fbilltypeid | 单据类型 | int8 | 64 |  | √ | 0 | 单据类型 bos_billtype |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_sm_expectqtyin |  | fid |
| 2 | pk_sm_expectqtyin |  | fentryid |

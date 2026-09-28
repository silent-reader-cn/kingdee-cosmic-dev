# 计划方案-pm_planschemeconfig

## 计划方案-多语言表 t_pm_planschemeconfig_l

- **表名称：** 计划方案-多语言表
- **表名：** t_pm_planschemeconfig_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fname | 方案名称 | varchar | 100 |  | √ | ' ' | 方案名称 |
| 3 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 4 | fpkid | fpkid | varchar | 36 |  | √ | ' ' | pkid |
| 5 | fschemedesc | 方案说明 | varchar | 512 |  | √ | ' ' | 方案说明 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_pm_planschemeconfig_l |  | fpkid |
| 2 | idx_pm_planschemeconfig_l_fid |  | fid |

---

## 供给需求参数-子表 t_pm_plansdparamentry

- **表名称：** 供给需求参数-子表
- **表名：** t_pm_plansdparamentry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fentity | 单据名称 | int8 | 64 |  | √ | 0 | 计划方案供需参数 pm_plansdparamdefault |
| 3 | fbillformuladesc | 计算公式配置 | varchar | 512 |  | √ | ' ' | 计算公式配置 |
| 4 | fbillstatus | 生效状态 | varchar | 36 |  | √ | ' ' | 生效状态,枚举: A :暂存 B :已提交 C :已审核 |
| 5 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 6 | fbillformula | 计算公式 | varchar | 512 |  | √ | ' ' | 计算公式 |
| 7 | fdesc | 供货说明 | varchar | 512 |  | √ | ' ' | 供货说明 |
| 8 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 9 | fstockoutintype | 出入库类型 | varchar | 5 |  | √ | ' ' | 出入库类型,枚举: A :预计出+ B :预计出- C :预计入+ D :预计入- |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_pm_plansdparamentry_fid |  | fid |
| 2 | pk_t_pm_plansdparamentry |  | fentryid |

---

## 计划方案-主表 t_pm_planschemeconfig

- **表名称：** 计划方案-主表
- **表名：** t_pm_planschemeconfig

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fenablematerialmerge | 物料 | bpchar | 1 |  | √ | '1' | 物料 |
| 3 | fenableavailablestock | 考虑现有库存 | bpchar | 1 |  | √ | '0' | 考虑现有库存 |
| 4 | fdisableor | 禁用人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 5 | fdisabledate | 禁用时间 | timestamp | 0 |  |  | null | 禁用时间 |
| 6 | fenablematvermerge | 物料版本 | bpchar | 1 |  | √ | '1' | 物料版本 |
| 7 | fenableauxmerge | 辅助属性 | bpchar | 1 |  | √ | '0' | 辅助属性 |
| 8 | fispreset | 系统预设 | bpchar | 1 |  | √ | '0' | 系统预设 |
| 9 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 10 | fstatus | 数据状态 | varchar | 5 |  | √ | ' ' | 数据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 11 | fmasterid | 主数据内码 | int8 | 64 |  | √ | 0 | 主数据内码 |
| 12 | fperiodordermerge | 期间订货合并 | varchar | 5 |  | √ | ' ' | 期间订货合并,枚举: A :合并到当前日期 B :合并至周期内的第一笔净需求日期 |
| 13 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 14 | fname | 方案名称 | varchar | 100 |  | √ | ' ' | 方案名称 |
| 15 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 16 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 17 | fenablesafestock | 考虑安全库存 | bpchar | 1 |  | √ | '0' | 考虑安全库存 |
| 18 | frequirereleaseway | 需求下达方式 | varchar | 5 |  | √ | ' ' | 需求下达方式,枚举: A :合并下达 B :独立下达 |
| 19 | frequiredaterange | 需求日期范围 | varchar | 5 |  | √ | ' ' | 需求日期范围,枚举: M_3 :三个月 M_6 :半年 M_12 :一年 |
| 20 | fenabletotalrequire | 计算总需求 | bpchar | 1 |  | √ | '0' | 计算总需求 |
| 21 | fauditdate | 审核时间 | timestamp | 0 |  |  | null | 审核时间 |
| 22 | fsupplydaterange | 供应日期范围 | varchar | 5 |  | √ | ' ' | 供应日期范围,枚举: M_3 :三个月 M_6 :半年 M_12 :一年 |
| 23 | fenabledayup | 采购提前期 | bpchar | 1 |  | √ | '0' | 采购提前期 |
| 24 | fenable | 使用状态 | varchar | 5 |  | √ | ' ' | 使用状态,枚举: 0 :禁用 1 :可用 |
| 25 | fnumber | 方案编码 | varchar | 80 |  | √ | ' ' | 方案编码 |
| 26 | fenablenegativestock | 负库存作为需求 | bpchar | 1 |  | √ | '0' | 负库存作为需求 |
| 27 | fschemedesc | 方案说明 | varchar | 512 |  | √ | ' ' | 方案说明 |
| 28 | fauditorid | 审核人 | int8 | 64 |  | √ | 0 | 人员 bos_user |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_pm_planschemeconfig_fnum |  | fnumber |
| 2 | pk_t_pm_planschemeconfig |  | fid |

---

## 单据状态-多选基础资料表 t_pm_plansdparamentry_s

- **表名称：** 单据状态-多选基础资料表
- **表名：** t_pm_plansdparamentry_s

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fbasedataid | fbasedataid | int8 | 64 |  | √ | 0 | 单据状态 pm_billstatus |
| 2 | fpkid | fpkid | int8 | 64 |  | √ | 0 | pkid |
| 3 | fentryid | fentryid | int8 | 64 |  | √ | 0 |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_pm_plansdparamentry_s_fe |  | fentryid |
| 2 | pk_t_pm_plansdparamentry_s |  | fpkid |

---

## 单据类型-多选基础资料表 t_pm_plansdparamentry_r

- **表名称：** 单据类型-多选基础资料表
- **表名：** t_pm_plansdparamentry_r

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fbasedataid | fbasedataid | int8 | 64 |  | √ | 0 | 单据类型 bos_billtype |
| 2 | fpkid | fpkid | int8 | 64 |  | √ | 0 | pkid |
| 3 | fentryid | fentryid | int8 | 64 |  | √ | 0 |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_pm_plansdparamentry_r |  | fpkid |
| 2 | idx_pm_plansdparamentry_r_fe |  | fentryid |

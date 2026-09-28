# 调整表自动创建方案-xkbm_adjustrptscheme

## 调整表自动创建方案-多语言表 t_xkbm_rptautoscheme_l

- **表名称：** 调整表自动创建方案-多语言表
- **表名：** t_xkbm_rptautoscheme_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fname | 名称 | varchar | 255 |  | √ | ' ' | 名称 |
| 3 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 4 | fdescription | 描述 | varchar | 255 |  | √ | ' ' | 描述 |
| 5 | fpkid | fpkid | varchar | 36 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_xkbm_rptautoscheme_l |  | fpkid |
| 2 | idx_xkbm_rptautoscheme_l |  | fid,flocaleid |

---

## 子单据体-多语言表 t_xkbm_autoschemesubentry_l

- **表名称：** 子单据体-多语言表
- **表名：** t_xkbm_autoschemesubentry_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fdetailid | fdetailid | int8 | 64 |  | √ | 0 |  |
| 2 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 3 | ffilterdescription | 描述 | varchar | 2000 |  | √ | ' ' | 描述 |
| 4 | fpkid | fpkid | varchar | 36 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_xkbm_autoschemesubentry_l |  | fpkid |
| 2 | idx_xkbm_autosubentry_l |  | fdetailid,flocaleid |

---

## 单据体-子表 t_xkbm_rptautoschemeentry

- **表名称：** 单据体-子表
- **表名：** t_xkbm_rptautoschemeentry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fprimarydimensionvalue | 多个维度类型值 | varchar | 1000 |  | √ | ' ' | 多个维度类型值 |
| 3 | fallowreload | 报表重新加载 | bpchar | 1 |  | √ | '0' | 报表重新加载 |
| 4 | fadjustmaindimvalue | 维度值 | varchar | 1000 |  | √ | ' ' | 维度值 |
| 5 | famountunit | 金额单位 | int8 | 64 |  | √ | 0 | [金额单位 xkbd_amountunit](../fibd_files/xkbd_amountunit.md) |
| 6 | fbwbcurrencyid | 本位币 | int8 | 64 |  | √ | 0 | [币种 bd_currency](../base_files/bd_currency.md) |
| 7 | fcontainformula | 保留报表金蝶公式 | bpchar | 1 |  | √ | ' ' | 保留报表金蝶公式 |
| 8 | fadjustmaindimname | 维度值 | varchar | 2000 |  | √ | ' ' | 维度值 |
| 9 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 10 | fmaindim | 主维度 | varchar | 1000 |  | √ | ' ' | 主维度 |
| 11 | fmaindimrange | 维度范围 | varchar | 1000 |  | √ | ' ' | 维度范围 |
| 12 | fiscurrencybwb | 本位币 | bpchar | 1 |  | √ | '0' | 本位币 |
| 13 | fadjusttype | 调整类型 | bpchar | 1 |  | √ | ' ' | 调整类型,枚举: 1 :计划外调整(计入调整数) 2 :计划内调整(计入原始数) |
| 14 | fmaindimgroup | 主维度维度值 | varchar | 1000 |  | √ | ' ' | 主维度维度值 |
| 15 | factualsampleid | 实际数模板 | varchar | 36 |  | √ | ' ' | [预算报表 xkbm_report](../xkbm_files/xkbm_report.md) |
| 16 | ffillway | 主维度填充方式 | varchar | 10 |  | √ | '0' | 主维度填充方式,枚举: 0 :交叉 1 :组合 |
| 17 | feffectdescription | 条件描述 | varchar | 2000 |  | √ | ' ' | 条件描述 |
| 18 | fadjustreason | 调整事由 | varchar | 255 |  | √ | ' ' | 调整事由 |
| 19 | fadjustdepot | 调整部门 | int8 | 64 |  | √ | 0 | [行政组织（部门） bos_adminorg](../base_files/bos_adminorg.md) |
| 20 | forglayersum | 逐层汇总 | bpchar | 1 |  | √ | '0' | 逐层汇总 |
| 21 | fcontaindimvalue | 包含原始预算表外的维度值 | bpchar | 1 |  | √ | '0' | 包含原始预算表外的维度值 |
| 22 | fsumorgunitid | 预算组织 | int8 | 64 |  | √ | 0 | [预算组织选择 xkbm_orgselect](../xkbm_files/xkbm_orgselect.md) |
| 23 | fdimselecttype | 维度选择方式 | varchar | 10 |  | √ | '10' | 维度选择方式,枚举: 10 :维度值 20 :维度过滤 |
| 24 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 25 | fcurrencyid | 币种 | int8 | 64 |  | √ | 0 | [币种 bd_currency](../base_files/bd_currency.md) |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_xkbm_rptautoschemeentry |  | fentryid |
| 2 | idx_xkbm_rptschemeentry |  | fid |

---

## 单据体-多语言表 t_xkbm_rptautoschemeentry_l

- **表名称：** 单据体-多语言表
- **表名：** t_xkbm_rptautoschemeentry_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fadjustreason | 调整事由 | varchar | 255 |  | √ | ' ' | 调整事由 |
| 2 | fadjustmaindimname | 维度值 | varchar | 2000 |  | √ | ' ' | 维度值 |
| 3 | fmaindim | 主维度 | varchar | 1000 |  | √ | ' ' | 主维度 |
| 4 | feffectdescription | 条件描述 | varchar | 2000 |  | √ | ' ' | 条件描述 |
| 5 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 6 | fpkid | fpkid | varchar | 36 |  | √ | ' ' | pkid |
| 7 | fentryid | fentryid | int8 | 64 |  | √ | 0 |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_xkbm_rptschemeey_l |  | fentryid,flocaleid |
| 2 | pk_t_xkbm_rptautoschemeentry_l |  | fpkid |

---

## 子单据体-子表 t_xkbm_autoschemesubentry

- **表名称：** 子单据体-子表
- **表名：** t_xkbm_autoschemesubentry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fdimeffectjson | 维度过滤json | varchar | 2000 |  | √ | ' ' | 维度过滤json |
| 2 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 3 | fdimeffectsql | 维度过滤sql | varchar | 2000 |  | √ | ' ' | 维度过滤sql |
| 4 | fdetailid | fdetailid | int8 | 64 |  | √ | 0 | id |
| 5 | ffilterkey | 维度范围 | varchar | 2000 |  | √ | ' ' | 维度范围 |
| 6 | ffilterdescription | 描述 | varchar | 2000 |  | √ | ' ' | 描述 |
| 7 | fentryid | fentryid | int8 | 64 |  | √ | 0 |  |
| 8 | fdimension | 报告维度 | int8 | 64 |  | √ | 0 | [维度 xkrpt_dimension](../xkrpt_files/xkrpt_dimension.md) |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fdetailid | fdetailid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_xkbm_autosubentry |  | fentryid |
| 2 | pk_xkbm_autoschemesubentry |  | fdetailid |

---

## 调整表自动创建方案-主表 t_xkbm_rptautoscheme

- **表名称：** 调整表自动创建方案-主表
- **表名：** t_xkbm_rptautoscheme

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fgroupid | 分组 | int8 | 64 |  | √ | 0 | [调整表自动创建方案分组 xkbm_adjustrptschemegroup](../xkbm_files/xkbm_adjustrptschemegroup.md) |
| 3 | frptstartdate | 时间范围：.开始 | timestamp | 0 |  |  | null | 时间范围：.开始 |
| 4 | fscheduletime | 调度时间 | timestamp | 0 |  |  | null | 调度时间 |
| 5 | fschemeid | 预算方案 | int8 | 64 |  | √ | 0 | [预算方案 xkbm_scheme](../xkbm_files/xkbm_scheme.md) |
| 6 | fiscreatelastrpt | 按执行时间创建上期报表 | bpchar | 1 |  | √ | ' ' | 按执行时间创建上期报表 |
| 7 | fiscreatemulrpt | 创建多期报表 | bpchar | 1 |  | √ | ' ' | 创建多期报表 |
| 8 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 9 | fstatus | 数据状态 | bpchar | 1 |  | √ | 'C' | 数据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 10 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 11 | fmasterid | 主数据内码 | int8 | 64 |  | √ | 0 | 主数据内码 |
| 12 | ftimezoneid | ftimezoneid | int8 | 64 |  | √ | 0 |  |
| 13 | fisrecreatereport | 覆盖已存在报表 | bpchar | 1 |  | √ | ' ' | 覆盖已存在报表 |
| 14 | fautosubmitrpt | 报表自动提交审核 | bpchar | 1 |  | √ | ' ' | 报表自动提交审核 |
| 15 | fforbidderid | 禁用人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 16 | fplan | cron表达式 | varchar | 50 |  | √ | ' ' | cron表达式 |
| 17 | fxkbmbusinessservice | 所属应用 | int8 | 64 |  | √ | 0 | [预算业务服务 xkbm_businessservice](../xkbm_files/xkbm_businessservice.md) |
| 18 | fname | 名称 | varchar | 255 |  | √ | ' ' | 名称 |
| 19 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 20 | fissumreport | 周期性汇总表 | bpchar | 1 |  | √ | '0' | 周期性汇总表 |
| 21 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 22 | fenableauto | 启用自动执行 | bpchar | 1 |  | √ | ' ' | 启用自动执行 |
| 23 | fiscreatecurrpt | 按执行时间创建当期报表 | bpchar | 1 |  | √ | ' ' | 按执行时间创建当期报表 |
| 24 | fdescription | 描述 | varchar | 255 |  | √ | ' ' | 描述 |
| 25 | frepeatmode | 重复时间单位 | bpchar | 1 |  | √ | ' ' | 重复时间单位,枚举: d :天 w :星期 m :月 y :年 |
| 26 | fstarttime | 开始时间 | timestamp | 0 |  |  | null | 开始时间 |
| 27 | fisrecalreport | 重算已存在报表 | bpchar | 1 |  | √ | ' ' | 重算已存在报表 |
| 28 | fdeadline | 不截止 | bpchar | 1 |  | √ | ' ' | 不截止 |
| 29 | fcreatenewrpt | 创建最新版本报表 | bpchar | 1 |  | √ | ' ' | 创建最新版本报表 |
| 30 | fenable | 使用状态 | bpchar | 1 |  | √ | '1' | 使用状态,枚举: 0 :禁用 1 :可用 |
| 31 | fnumber | 编码 | varchar | 30 |  | √ | ' ' | 编码 |
| 32 | fdesc | 调度计划示例 | varchar | 2000 |  | √ | ' ' | 调度计划示例 |
| 33 | fendtime | 失效时间 | timestamp | 0 |  |  | null | 失效时间 |
| 34 | fforbiddate | 禁用时间 | timestamp | 0 |  |  | null | 禁用时间 |
| 35 | fcyclenum | 重复周期 | int8 | 64 |  | √ | 1 | 重复周期 |
| 36 | frptcreatetype | 报表创建方式 | varchar | 10 |  | √ | '10' | 报表创建方式 |
| 37 | frptenddate | 时间范围：.结束 | timestamp | 0 |  |  | null | 时间范围：.结束 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_xkbm_rptautoscheme |  | fnumber |
| 2 | pk_t_xkbm_rptautoscheme |  | fid |

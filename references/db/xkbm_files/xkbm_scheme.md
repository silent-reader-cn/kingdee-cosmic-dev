# 预算方案-xkbm_scheme

## 预算方案-多语言表 t_xkbm_scheme_l

- **表名称：** 预算方案-多语言表
- **表名：** t_xkbm_scheme_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fname | 名称 | varchar | 255 |  | √ | ' ' | 名称 |
| 3 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 4 | fpkid | fpkid | varchar | 36 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_xkbm_scheme_l_fid |  | fid,flocaleid |
| 2 | pk_xkbm_scheme_l |  | fpkid |

---

## 方案明细-子表 t_xkbm_schemeentry

- **表名称：** 方案明细-子表
- **表名：** t_xkbm_schemeentry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 3 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 4 | fdistributeid | 关联分发ID | varchar | 50 |  | √ | ' ' | 关联分发ID |
| 5 | fentryeditor | 预算编制主体 | varchar | 50 |  | √ | ' ' | 预算编制主体 |
| 6 | fsampleid | 模板编码 | varchar | 36 |  | √ | ' ' | [预算模板 xkbm_reportsample](../xkbm_files/xkbm_reportsample.md) |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_xkbm_schemeentry_fid |  | fid |
| 2 | pk_xkbm_schemeentry |  | fentryid |

---

## 预算方案-主表 t_xkbm_scheme

- **表名称：** 预算方案-主表
- **表名：** t_xkbm_scheme

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fxkbmbusinessservice | 所属应用 | int8 | 64 |  | √ | 0 | [预算业务服务 xkbm_businessservice](../xkbm_files/xkbm_businessservice.md) |
| 3 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 4 | fname | 名称 | varchar | 255 |  | √ | ' ' | 名称 |
| 5 | fgroupid | 分组 | int8 | 64 |  | √ | 0 | [预算方案分组 xkbm_schemegroup](../xkbm_files/xkbm_schemegroup.md) |
| 6 | fisstartactual | 按启用日期取实际数 | bpchar | 1 |  | √ | '0' | 按启用日期取实际数 |
| 7 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 8 | fbudgetorgid | 预算组织架构 | int8 | 64 |  | √ | 0 | [预算组织架构 xkbm_budgetorg](../xkbm_files/xkbm_budgetorg.md) |
| 9 | factualstartdate | 启用日期 | timestamp | 0 |  |  | null | 启用日期 |
| 10 | fendyear | 结束年度 | varchar | 30 |  | √ | '0' | 结束年度,枚举: |
| 11 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 12 | fstartyear | 开始年度 | varchar | 30 |  | √ | '0' | 开始年度,枚举: |
| 13 | fenddate | 结束日期 | timestamp | 0 |  |  | null | 结束日期 |
| 14 | fstatus | 数据状态 | bpchar | 1 |  | √ | ' ' | 数据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 15 | fcalendarid | 预算日历 | int8 | 64 |  | √ | 0 | [预算日历 xkbm_budgetcalendar](../xkbm_files/xkbm_budgetcalendar.md) |
| 16 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 17 | fmasterid | 主数据内码 | int8 | 64 |  | √ | 0 | 主数据内码 |
| 18 | fratetypeid | 默认汇率表 | int8 | 64 |  | √ | 0 | [汇率表 bd_exratetable](../base_files/bd_exratetable.md) |
| 19 | fstartdate | 开始日期 | timestamp | 0 |  |  | null | 开始日期 |
| 20 | fenable | 使用状态 | bpchar | 1 |  | √ | ' ' | 使用状态,枚举: 0 :禁用 1 :可用 |
| 21 | fnumber | 编码 | varchar | 30 |  | √ | ' ' | 编码 |
| 22 | fforbiddate | 禁用时间 | timestamp | 0 |  |  | null | 禁用时间 |
| 23 | fforbidderid | 禁用人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_xkbm_scheme |  | fid |
| 2 | idx_xkbm_scheme_fenable |  | fenable |
| 3 | idx_xkbm_scheme_number |  | fnumber |

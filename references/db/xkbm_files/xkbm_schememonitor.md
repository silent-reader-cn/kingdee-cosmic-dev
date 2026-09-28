# 预算方案监控-xkbm_schememonitor

## 预算方案监控-主表 t_xkbm_schememonitor

- **表名称：** 预算方案监控-主表
- **表名：** t_xkbm_schememonitor

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fperiodstartdate | 起始日期 | timestamp | 0 |  |  | null | 起始日期 |
| 3 | forgid | 组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 4 | fschemeid | 预算方案 | int8 | 64 |  | √ | 0 | [预算方案 xkbm_scheme](../xkbm_files/xkbm_scheme.md) |
| 5 | forgtype | 预算组织类型 | varchar | 30 |  | √ | ' ' | 预算组织类型,枚举: DEPT :部门 ORG :组织 |
| 6 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 7 | fstatus | 数据状态 | bpchar | 1 |  | √ | ' ' | 数据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 8 | fmasterid | 主数据内码 | int8 | 64 |  | √ | 0 | 主数据内码 |
| 9 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 10 | fcalendarid | 预算日历 | int8 | 64 |  | √ | 0 | [预算日历 xkbm_budgetcalendar](../xkbm_files/xkbm_budgetcalendar.md) |
| 11 | fperiodenddate | 结束日期 | timestamp | 0 |  |  | null | 结束日期 |
| 12 | forgunitid | 预算组织 | int8 | 64 |  | √ | 0 | [预算组织 xkbm_budgetorgunit](../xkbm_files/xkbm_budgetorgunit.md) |
| 13 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 14 | fname | 名称 | varchar | 255 |  | √ | ' ' | 名称 |
| 15 | factivestatus | 分发状态 | bpchar | 1 |  | √ | '0' | 分发状态,枚举: 0 :取消分发 1 :正常分发 |
| 16 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 17 | fdeptorgid | 部门组织ID | int8 | 64 |  | √ | 0 | 部门组织ID |
| 18 | fperiodnumber | 预算日历期间编码 | varchar | 255 |  | √ | ' ' | 预算日历期间编码 |
| 19 | fyearperiod | 年期组合 | int4 | 32 |  | √ | 0 | 年期组合 |
| 20 | fyear | 年度 | int4 | 32 |  | √ | 0 | 年度 |
| 21 | fperiodtype | 周期类型 | bpchar | 1 |  | √ | '0' | 周期类型,枚举: 0 :年 1 :半年 2 :季 3 :月 4 :旬 5 :周 6 :日 |
| 22 | fperiod | 期间 | int4 | 32 |  | √ | 0 | 期间 |
| 23 | fexcutestatus | 执行状态 | bpchar | 1 |  | √ | '1' | 执行状态,枚举: 1 :未执行 2 :部分执行 3 :执行中 4 :部分关闭 5 :已关闭 |
| 24 | fenable | 使用状态 | bpchar | 1 |  | √ | ' ' | 使用状态,枚举: 0 :禁用 1 :可用 |
| 25 | fnumber | 编码 | varchar | 30 |  | √ | ' ' | 编码 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_xkbm_schememonitor |  | fid |
| 2 | idx_xkbm_monitor_factive |  | factivestatus |
| 3 | idx_xkbm_monitor_schemeid |  | fschemeid |
| 4 | idx_xkbm_monitor_period |  | fyear,fperiod,fperiodtype |

---

## 单据体-子表 t_xkbm_schememonitorrpt

- **表名称：** 单据体-子表
- **表名：** t_xkbm_schememonitorrpt

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fvalidity | 有效日期范围 | bpchar | 1 |  | √ | '0' | 有效日期范围,枚举: 0 :否 1 :是 |
| 3 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 4 | fnewsampleid | 分发预算复制模板ID | varchar | 36 |  | √ | ' ' | [预算模板 xkbm_reportsample](../xkbm_files/xkbm_reportsample.md) |
| 5 | factivestatusrpt | 分发状态 | bpchar | 1 |  | √ | '0' | 分发状态,枚举: 0 :取消分发 1 :正常分发 |
| 6 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 7 | fdistributeorgunitid | 编制组织 | int8 | 64 |  | √ | 0 | [预算组织 xkbm_budgetorgunit](../xkbm_files/xkbm_budgetorgunit.md) |
| 8 | fsamplebuildstatus | 编制状态 | bpchar | 1 |  | √ | '1' | 编制状态,枚举: 1 :未编 2 :编制中 3 :完编 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_xkbm_schememonitorrpt |  | fentryid |
| 2 | idx_xkbm_monitorrpt_fid |  | fid |

---

## 预算方案监控-多语言表 t_xkbm_schememonitor_l

- **表名称：** 预算方案监控-多语言表
- **表名：** t_xkbm_schememonitor_l

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
| 1 | pk_xkbm_schememonitor_l |  | fpkid |
| 2 | idx_xkbm_monitor_l_fid |  | fid,flocaleid |

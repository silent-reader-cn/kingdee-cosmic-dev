# 需求计划方案-mds_rplancal

## 需求计划方案-主表 t_mds_rplancal

- **表名称：** 需求计划方案-主表
- **表名：** t_mds_rplancal

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fdeduct_h | 向前冲减天数 | int8 | 64 |  | √ | 0 | 向前冲减天数 |
| 3 | fpredversion | 目标需求计划版本 | int8 | 64 |  | √ | 0 | [版本定义 mds_vrds](../mds_files/mds_vrds.md) |
| 4 | fopenlv | 展开层 | int8 | 64 |  | √ | 0 | 展开层 |
| 5 | forgid | 创建组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 6 | frepeat | 重复运算 | bpchar | 1 |  | √ | '0' | 重复运算 |
| 7 | frunninglog_tag | 运行日志_详情 | text | 0 |  |  | null | 运行日志_详情 |
| 8 | fpredtime | 预约时间 | int8 | 64 |  | √ | 0 | 预约时间 |
| 9 | fdeduct_t | 向后冲减天数 | int8 | 64 |  | √ | 0 | 向后冲减天数 |
| 10 | frunningtype | 运行时间类型 | varchar | 30 |  | √ | ' ' | 运行时间类型,枚举: |
| 11 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 12 | fplanid | 计划号 | varchar | 50 |  | √ | ' ' | 计划号 |
| 13 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 14 | fdaysofmon | 月 | varchar | 100 |  | √ | ' ' | 月 |
| 15 | fsourcetype | 计划来源类型 | varchar | 30 |  | √ | ' ' | 计划来源类型,枚举: mds_vrds :指定预测 mds_corl :需求计划关联关系 mds_setoffsetting :预测冲减定义 |
| 16 | fchangeway | 改写方式 | varchar | 30 |  | √ | ' ' | 改写方式,枚举: 0 :全部覆盖 1 :仅更新增加 |
| 17 | fend | 计划截止时间 | timestamp | 0 |  |  | null | 计划截止时间 |
| 18 | fdummysiteid | 缺配额组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 19 | fbillno | 需求计划方案编码 | varchar | 30 |  | √ | ' ' | 需求计划方案编码 |
| 20 | fstype | 计划来源类型 | varchar | 20 |  | √ | ' ' | 计划来源类型,枚举: 0 :指定需求计划 1 :需求计划关联关系 |
| 21 | fdaysofweek | 周 | varchar | 100 |  | √ | ' ' | 周 |
| 22 | fcalstatus | 使用状态 | varchar | 30 |  | √ | ' ' | 使用状态,枚举: A :禁用 B :可用 |
| 23 | foutlookperiod | 展望期（天） | numeric | 23 | 10 | √ | 0.0000000000 | 展望期（天） |
| 24 | fdatetype | 展望期类型 | varchar | 30 |  | √ | ' ' | 展望期类型,枚举: A :天 |
| 25 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 26 | fbillstatus | 单据状态 | varchar | 30 |  | √ | ' ' | 单据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 27 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 28 | fstart | 计划开始时间 | timestamp | 0 |  |  | null | 计划开始时间 |
| 29 | fjobid | 作业号 | varchar | 50 |  | √ | ' ' | 作业号 |
| 30 | fsourcename | 计划来源 | int8 | 64 |  | √ | 0 | 版本定义 mds_vrds |
| 31 | fauditdate | 审核日期 | timestamp | 0 |  |  | null | 审核日期 |
| 32 | fmod | 计算百分比（%） | numeric | 23 | 10 | √ | 0.0000000000 | 计算百分比（%） |
| 33 | frepeattype | 时间重复类型 | varchar | 30 |  | √ | ' ' | 时间重复类型,枚举: |
| 34 | fplangrp | 计划组 | int8 | 64 |  | √ | 0 | [计划业务组 mpdm_demandgroup](../mpdm_files/mpdm_demandgroup.md) |
| 35 | fsetoffverid | 版本定义 | int8 | 64 |  | √ | 0 | [版本定义 mds_vrds](../mds_files/mds_vrds.md) |
| 36 | ftype | BOM类型 | int8 | 64 |  | √ | 0 | [BOM类型 mpdm_bomtype](../mpdm_files/mpdm_bomtype.md) |
| 37 | fdeduct | 是否冲减 | bpchar | 1 |  | √ | '0' | 是否冲减 |
| 38 | famounttype | 数量类型 | varchar | 30 |  | √ | ' ' | 数量类型,枚举: 0 :初始值 1 :现有值 |
| 39 | fisquota | 需求配额 | bpchar | 1 |  | √ | '0' | 需求配额 |
| 40 | flosedate | 失效时间 | timestamp | 0 |  |  | null | 失效时间 |
| 41 | fauditorid | 审核人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 42 | fdtype | 需求类型 | int8 | 64 |  | √ | 0 | [需求类型 mds_dmtp](../msplan_files/mds_dmtp.md) |
| 43 | fbillstatuscheckbox | 是否需要单据已确认 | bpchar | 1 |  | √ | '0' | 是否需要单据已确认 |
| 44 | frunninglog | 运行日志 | varchar | 500 |  | √ | ' ' | 运行日志 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_mds_rplancal |  | fbillno,forgid |
| 2 | t_mds_rplancal_pkey |  | fid |

---

## 需求计划方案-多语言表 t_mds_rplancal_l

- **表名称：** 需求计划方案-多语言表
- **表名：** t_mds_rplancal_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fname | 需求计划方案名称 | varchar | 100 |  | √ | ' ' | 需求计划方案名称 |
| 3 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 4 | fpkid | fpkid | varchar | 36 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_mds_rplancal_l |  | fpkid |

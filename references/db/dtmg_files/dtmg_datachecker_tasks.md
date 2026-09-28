# 校对任务-dtmg_datachecker_tasks

## 附件-附件表 t_dtmg_dc_billquantattach

- **表名称：** 附件-附件表
- **表名：** t_dtmg_dc_billquantattach

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fbasedataid | fbasedataid | int8 | 64 |  | √ | 0 | [附件字段实体 bd_attachment](../frame_files/bd_attachment.md) |
| 2 | fpkid | fpkid | int8 | 64 |  | √ | 0 | FPKID |
| 3 | fentryid | fentryid | int8 | 64 |  | √ | 0 |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_dtmg_dc_billquantattach |  | fpkid |
| 2 | idx_dtmg_dc_billquantattach_at |  | fentryid,fbasedataid |

---

## Excel校对任务差异记录-子表 t_dtmg_dc_exceltasks

- **表名称：** Excel校对任务差异记录-子表
- **表名：** t_dtmg_dc_exceltasks

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fex_diff_0 | 差异 | varchar | 50 |  | √ | ' ' | 差异 |
| 3 | fex_diff_1 | 差异 | varchar | 50 |  | √ | ' ' | 差异 |
| 4 | fex_diff_2 | 差异 | varchar | 50 |  | √ | ' ' | 差异 |
| 5 | fex_diff_3 | 差异 | varchar | 50 |  | √ | ' ' | 差异 |
| 6 | fex_data_group | 数据存在类型 | varchar | 50 |  | √ | ' ' | 数据存在类型,枚举: A :旗舰存在 B :源系统存在 C :旗舰及源系统都存在 |
| 7 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 8 | fex_target_count_0 | 目标系统（旗舰） | varchar | 50 |  | √ | ' ' | 目标系统（旗舰） |
| 9 | fex_target_count_1 | 目标系统（旗舰） | varchar | 50 |  | √ | ' ' | 目标系统（旗舰） |
| 10 | fex_target_count_2 | 目标系统（旗舰） | varchar | 50 |  | √ | ' ' | 目标系统（旗舰） |
| 11 | fex_target_count_3 | 目标系统（旗舰） | varchar | 50 |  | √ | ' ' | 目标系统（旗舰） |
| 12 | fex_target_count_4 | 目标系统（旗舰） | varchar | 50 |  | √ | ' ' | 目标系统（旗舰） |
| 13 | fex_target_count_5 | 目标系统（旗舰） | varchar | 50 |  | √ | ' ' | 目标系统（旗舰） |
| 14 | fex_target_count_6 | 目标系统（旗舰） | varchar | 50 |  | √ | ' ' | 目标系统（旗舰） |
| 15 | fex_target_count_7 | 目标系统（旗舰） | varchar | 50 |  | √ | ' ' | 目标系统（旗舰） |
| 16 | fex_source_count_6 | 源系统 | varchar | 50 |  | √ | ' ' | 源系统 |
| 17 | fex_source_count_7 | 源系统 | varchar | 50 |  | √ | ' ' | 源系统 |
| 18 | fex_source_count_0 | 源系统 | varchar | 50 |  | √ | ' ' | 源系统 |
| 19 | fpkvalue_3 | 标识3 | varchar | 50 |  | √ | ' ' | 标识3 |
| 20 | fex_source_count_1 | 源系统 | varchar | 50 |  | √ | ' ' | 源系统 |
| 21 | fpkvalue_2 | 标识2 | varchar | 50 |  | √ | ' ' | 标识2 |
| 22 | fex_source_count_2 | 源系统 | varchar | 50 |  | √ | ' ' | 源系统 |
| 23 | fex_diff_4 | 差异 | varchar | 50 |  | √ | ' ' | 差异 |
| 24 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 25 | fpkvalue_1 | 标识1 | varchar | 50 |  | √ | ' ' | 标识1 |
| 26 | fex_source_count_3 | 源系统 | varchar | 50 |  | √ | ' ' | 源系统 |
| 27 | fex_diff_5 | 差异 | varchar | 50 |  | √ | ' ' | 差异 |
| 28 | fpkvalue_0 | 标识0 | varchar | 50 |  | √ | ' ' | 标识0 |
| 29 | fex_source_count_4 | 源系统 | varchar | 50 |  | √ | ' ' | 源系统 |
| 30 | fex_diff_6 | 差异 | varchar | 50 |  | √ | ' ' | 差异 |
| 31 | fex_source_count_5 | 源系统 | varchar | 50 |  | √ | ' ' | 源系统 |
| 32 | fex_diff_7 | 差异 | varchar | 50 |  | √ | ' ' | 差异 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_dtmg_dc_billquanttasks_fk |  | fid |
| 2 | pk_dtmg_dc_exceltasks |  | fentryid |

---

## 校对任务-主表 t_dtmg_dc_tasks

- **表名称：** 校对任务-主表
- **表名：** t_dtmg_dc_tasks

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fcreator | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 3 | fname | 名称 | varchar | 50 |  | √ | ' ' | 名称 |
| 4 | fentryinfo | 校对器配置明细 | varchar | 50 |  | √ | ' ' | 校对器配置明细 |
| 5 | ftasktype | 类型 | varchar | 50 |  | √ | ' ' | 类型,枚举: dtmg_datachecker_excel :Excel数据校对 dtmg_datachecker_billquantity :单据数量校对 |
| 6 | fexcelsourcestartrow | 源excel表头开始行 | int4 | 32 |  | √ | 0 | 源excel表头开始行 |
| 7 | fex_colname_indexes | Excel校对字段名及索引 | varchar | 500 |  | √ | ' ' | Excel校对字段名及索引 |
| 8 | fenddatetime | 执行结束时间 | timestamp | 0 |  |  | null | 执行结束时间 |
| 9 | fentryinfo_tag | 校对器配置明细_详情 | text | 0 |  |  | null | 校对器配置明细_详情 |
| 10 | fzipconfig | Config 配置信息 | varchar | 50 |  | √ | ' ' | Config 配置信息 |
| 11 | fexceltargetendrow | 目标excel表头结束行 | int4 | 32 |  | √ | 0 | 目标excel表头结束行 |
| 12 | fexcelsourceendrow | 目标excel表头结束行 | int4 | 32 |  | √ | 0 | 目标excel表头结束行 |
| 13 | fdcid | 来源校对器 | varchar | 50 |  | √ | ' ' | [校对器基础资料 dtmg_datachecker_basedata](../dtmg_files/dtmg_datachecker_basedata.md) |
| 14 | fbegindatetime | 执行开始时间 | timestamp | 0 |  |  | null | 执行开始时间 |
| 15 | fduration | 用时（秒） | int8 | 64 |  | √ | 0 | 用时（秒） |
| 16 | frunstatus | 运行状态 | varchar | 50 |  | √ | ' ' | 运行状态,枚举: A :待执行 B :执行中 C :已执行 D :已终止 |
| 17 | fzipconfig_tag | Config 配置信息_详情 | text | 0 |  |  | null | Config 配置信息_详情 |
| 18 | fserviceid | fserviceid | varchar | 50 |  | √ | ' ' |  |
| 19 | fexceltargetstartrow | 目标excel表头开始行 | int4 | 32 |  | √ | 0 | 目标excel表头开始行 |
| 20 | fbillno | 编号 | varchar | 30 |  | √ | ' ' | 编号 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_dtmg_dc_tasks |  | fid |

---

## 单据数量校对任务差异记录-子表 t_dtmg_dc_billquanttasks

- **表名称：** 单据数量校对任务差异记录-子表
- **表名：** t_dtmg_dc_billquanttasks

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fbq_different | fbq_different | int4 | 32 |  | √ | 0 |  |
| 3 | fremark | 备注 | varchar | 500 |  | √ | ' ' | 备注 |
| 4 | fbq_isdiff | 是否有差异 | bpchar | 1 |  | √ | '0' | 是否有差异 |
| 5 | fbq_target_diff | 旗舰自建数 | int8 | 64 |  | √ | 0 | 旗舰自建数 |
| 6 | fbq_billcount_diff | 单据总数差异 | int8 | 64 |  | √ | 0 | 单据总数差异 |
| 7 | fconvertcode | 转换关系编码 | varchar | 200 |  | √ | ' ' | 转换关系编码 |
| 8 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 9 | fbq_zipfilename | 校对文件 | varchar | 200 |  | √ | ' ' | 校对文件 |
| 10 | fbq_detail | 差异数据详情 | varchar | 50 |  | √ | ' ' | 差异数据详情 |
| 11 | fbq_target_billcount | 旗舰已有数 | int8 | 64 |  | √ | 0 | 旗舰已有数 |
| 12 | fbq_runstatus | 执行状态 | varchar | 50 |  | √ | ' ' | 执行状态,枚举: A :待执行 B :执行中 C :已执行 D :已终止 |
| 13 | fbq_detail_tag | 差异数据详情_详情 | text | 0 |  |  | null | 差异数据详情_详情 |
| 14 | fbq_source_billcount | 源系统应迁数 | int8 | 64 |  | √ | 0 | 源系统应迁数 |
| 15 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 16 | fobjecttypeid | 业务对象 | varchar | 36 |  | √ | ' ' | [主实体对象 bos_entityobject](../mdl_files/bos_entityobject.md) |
| 17 | fbq_source_diff | 源系统未迁数 | int8 | 64 |  | √ | 0 | 源系统未迁数 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_dtmg_dc_billquanttasks |  | fentryid |
| 2 | idx_dtmg_dc_exceltasks_zipfile |  | fid,fbq_zipfilename |
| 3 | idx_dtmg_dc_exceltasks_fk |  | fid |

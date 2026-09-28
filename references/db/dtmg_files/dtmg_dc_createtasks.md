# 创建校对任务-dtmg_dc_createtasks

## 创建校对任务-主表 t_dtmg_dc_tasks

- **表名称：** 创建校对任务-主表
- **表名：** t_dtmg_dc_tasks

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fcreator | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 3 | fname | 名称 | varchar | 50 |  | √ | ' ' | 名称 |
| 4 | fentryinfo | 校对器配置明细 | varchar | 50 |  | √ | ' ' | 校对器配置明细 |
| 5 | ftasktype | 类型 | varchar | 50 |  | √ | ' ' | 类型,枚举: dtmg_datachecker_excel :Excel数据校对 dtmg_datachecker_billquantity :单据数量校对 |
| 6 | fexcelsourcestartrow | 表头显示第 | int4 | 32 |  | √ | 0 | 表头显示第 |
| 7 | fex_colname_indexes | fex_colname_indexes | varchar | 500 |  | √ | ' ' |  |
| 8 | fenddatetime | 执行结束时间 | timestamp | 0 |  |  | null | 执行结束时间 |
| 9 | fentryinfo_tag | 校对器配置明细_详情 | text | 0 |  |  | null | 校对器配置明细_详情 |
| 10 | fzipconfig | Config 配置信息 | varchar | 50 |  | √ | ' ' | Config 配置信息 |
| 11 | fexceltargetendrow | 表头显示第 | int4 | 32 |  | √ | 0 | 表头显示第 |
| 12 | fexcelsourceendrow | 表头显示第 | int4 | 32 |  | √ | 0 | 表头显示第 |
| 13 | fdcid | 来源校对器 | varchar | 50 |  | √ | ' ' | [校对器基础资料 dtmg_datachecker_basedata](../dtmg_files/dtmg_datachecker_basedata.md) |
| 14 | fbegindatetime | 执行开始时间 | timestamp | 0 |  |  | null | 执行开始时间 |
| 15 | fduration | 用时（秒） | int8 | 64 |  | √ | 0 | 用时（秒） |
| 16 | frunstatus | 运行状态 | varchar | 50 |  | √ | ' ' | 运行状态,枚举: A :待执行 B :执行中 C :已执行 D :已终止 |
| 17 | fzipconfig_tag | Config 配置信息_详情 | text | 0 |  |  | null | Config 配置信息_详情 |
| 18 | fserviceid | 后台服务ID | varchar | 50 |  | √ | ' ' | 后台服务ID |
| 19 | fexceltargetstartrow | 表头显示第 | int4 | 32 |  | √ | 0 | 表头显示第 |
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
| 4 | fbq_isdiff | fbq_isdiff | bpchar | 1 |  | √ | '0' |  |
| 5 | fbq_target_diff | 差异数 | int8 | 64 |  | √ | 0 | 差异数 |
| 6 | fbq_billcount_diff | 单据总数差异 | int8 | 64 |  | √ | 0 | 单据总数差异 |
| 7 | fconvertcode | 转换关系编码 | varchar | 200 |  | √ | ' ' | 转换关系编码 |
| 8 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 9 | fbq_zipfilename | 校对文件 | varchar | 200 |  | √ | ' ' | 校对文件 |
| 10 | fbq_detail | 差异数据详情 | varchar | 50 |  | √ | ' ' | 差异数据详情 |
| 11 | fbq_target_billcount | 单据总数 | int8 | 64 |  | √ | 0 | 单据总数 |
| 12 | fbq_runstatus | 执行状态 | varchar | 50 |  | √ | ' ' | 执行状态,枚举: A :待执行 B :执行中 C :已执行 D :已终止 |
| 13 | fbq_detail_tag | 差异数据详情_详情 | text | 0 |  |  | null | 差异数据详情_详情 |
| 14 | fbq_source_billcount | 单据总数 | int8 | 64 |  | √ | 0 | 单据总数 |
| 15 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 16 | fobjecttypeid | 业务对象 | varchar | 36 |  | √ | ' ' | [主实体对象 bos_entityobject](../mdl_files/bos_entityobject.md) |
| 17 | fbq_source_diff | 差异数 | int8 | 64 |  | √ | 0 | 差异数 |

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

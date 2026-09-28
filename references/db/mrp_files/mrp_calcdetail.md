# MRP计算明细表-mrp_calcdetail

## 单据体-子表 t_mrp_caldetailentry

- **表名称：** 单据体-子表
- **表名：** t_mrp_caldetailentry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fsupplybillno | 供应单据编码 | varchar | 50 |  | √ | ' ' | 供应单据编码 |
| 3 | fexceptionnumber | 例外信息编码 | varchar | 255 |  | √ | ' ' | 例外信息编码 |
| 4 | fconfiguredcode | 配置号 | int8 | 64 |  | √ | 0 | 配置号 bd_configuredcode |
| 5 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 6 | fsupplybilltype | 供应单据实体名称 | varchar | 50 |  | √ | ' ' | 供应单据实体名称 |
| 7 | fbillentryseq | 原需求单据分录行号 | int8 | 64 |  | √ | 0 | 原需求单据分录行号 |
| 8 | fadjustqty | 调整数量 | numeric | 23 | 10 | √ | 0.0000000000 | 调整数量 |
| 9 | fllc | 低位码 | varchar | 255 |  | √ | ' ' | 低位码 |
| 10 | fdemandsourcetype | 需求来源类型 | varchar | 50 |  | √ | ' ' | 需求来源类型 |
| 11 | fadjustsuggest | 调整建议 | varchar | 50 |  | √ | ' ' | 调整建议,枚举: 不调整 :不调整 建议提前 :建议提前 提前占用 :提前占用 建议延后 :建议延后 延后占用 :延后占用 建议取消 :建议取消 |
| 12 | fdemanddate | 需求日期 | timestamp | 0 |  |  | null | 需求日期 |
| 13 | fsrcdemandqty | 原需求数量 | numeric | 23 | 10 | √ | 0.0000000000 | 原需求数量 |
| 14 | freqsourcebillno | 需求来源号 | varchar | 255 |  | √ | ' ' | 需求来源号 |
| 15 | fsupplystorage | 供应货主 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 16 | fbomid | 父项BOMID | varchar | 100 |  | √ | ' ' | 父项BOMID |
| 17 | freqflexmetricval | 需求计划维度 | varchar | 2000 |  | √ | ' ' | 需求计划维度 |
| 18 | fsupmaterial | 供应物料 | int8 | 64 |  | √ | 0 | 物料 bd_material |
| 19 | foriginsupplyqty | 原供应数量 | numeric | 23 | 10 | √ | 0 | 原供应数量 |
| 20 | fdemandbilltype | 需求单据实体名称 | varchar | 50 |  | √ | ' ' | 需求单据实体名称 |
| 21 | fmaterial | 物料 | int8 | 64 |  | √ | 0 | 物料 bd_material |
| 22 | fsexpmsg | 供应例外信息 | varchar | 255 |  | √ | ' ' | 供应例外信息 |
| 23 | ftracknumber | 跟踪号 | int8 | 64 |  | √ | 0 | 跟踪号 bd_tracknumber |
| 24 | fbillno | 需求单据编码 | varchar | 50 |  | √ | ' ' | 需求单据编码 |
| 25 | forigindemanddate | 原始需求日期 | timestamp | 0 |  |  | null | 原始需求日期 |
| 26 | feventid | 计算事件ID | varchar | 50 |  | √ | ' ' | 计算事件ID |
| 27 | fsupflexmetricid | 供应物料维度 | varchar | 2000 |  | √ | ' ' | 供应物料维度 |
| 28 | fmergebillno | 合并后需求单据编码 | varchar | 50 |  | √ | ' ' | 合并后需求单据编码 |
| 29 | fdemandbillf7 | 需求单据实体标识 | varchar | 60 |  | √ | ' ' | 主实体对象 bos_entityobject |
| 30 | freqflexmetricid | 需求物料维度 | varchar | 2000 |  | √ | ' ' | 需求物料维度 |
| 31 | fwarehouseid | 供应仓库 | int8 | 64 |  | √ | 0 | 仓库 bd_warehouse |
| 32 | fsupplyqty | 供应数量 | numeric | 23 | 10 | √ | 0.0000000000 | 供应数量 |
| 33 | fsupplybilltypeid | 供应单据类型 | int8 | 64 |  | √ | 0 | 单据类型 bos_billtype |
| 34 | fsupplybillentryseq | 供应单据分录行号 | int8 | 64 |  | √ | 0 | 供应单据分录行号 |
| 35 | fsupplydetail | 供应明细 | varchar | 255 |  | √ | ' ' | 供应明细 |
| 36 | fcopsupply | 联副产品供应 | bpchar | 1 |  | √ | '0' | 联副产品供应,枚举: 1 :是 0 :否 |
| 37 | fishandle | 处理标识 | bpchar | 1 |  | √ | '0' | 处理标识 |
| 38 | fbillid | 需求单据ID | varchar | 50 |  | √ | ' ' | 需求单据ID |
| 39 | fparentbomid | BOMID | varchar | 100 |  | √ | ' ' | BOMID |
| 40 | fbilldetailid | 需求子单据体分录ID | varchar | 50 |  | √ | ' ' | 需求子单据体分录ID |
| 41 | fsupplybillentryid | 供应分录ID | varchar | 50 |  | √ | ' ' | 供应分录ID |
| 42 | fexception | 例外信息 | varchar | 255 |  | √ | ' ' | 例外信息 |
| 43 | fismerge | 是否合并需求 | bpchar | 1 |  | √ | '0' | 是否合并需求 |
| 44 | fsupplyorgid | 供应组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 45 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 46 | fsuptracknumber | 供应跟踪号 | int8 | 64 |  | √ | 0 | 跟踪号 bd_tracknumber |
| 47 | fsuppriority | 供应优先级 | varchar | 255 |  | √ | ' ' | 供应优先级 |
| 48 | fbomversion | 需求物料版本 | int8 | 64 |  | √ | 0 | 物料版本 bd_bomversion_new |
| 49 | fsupplybilldetailid | 供应子单据体分录ID | varchar | 50 |  | √ | ' ' | 供应子单据体分录ID |
| 50 | fdemandauxpty | 需求物料辅助属性 | int8 | 64 |  | √ | 0 | null 001 |
| 51 | fsexpnumber | 供应例外信息编码 | varchar | 255 |  | √ | ' ' | 供应例外信息编码 |
| 52 | fcomputeid | 运算标识 | int8 | 64 |  | √ | 0 | 运算标识 |
| 53 | fsupplydate | 供应单据日期 | timestamp | 0 |  |  | null | 供应单据日期 |
| 54 | fmergebillentryseq | 合并后需求单据分录序列号 | int8 | 64 |  | √ | 0 | 合并后需求单据分录序列号 |
| 55 | fexception_tag | 例外信息_详情 | text | 0 |  |  | null | 例外信息_详情 |
| 56 | fmergebillid | 合并后需求单据ID | varchar | 50 |  | √ | ' ' | 合并后需求单据ID |
| 57 | freqpriority | 需求优先级 | varchar | 255 |  | √ | ' ' | 需求优先级 |
| 58 | fmergebillentryid | 合并后需求单据分录ID | varchar | 50 |  | √ | ' ' | 合并后需求单据分录ID |
| 59 | fsupplyoperator | 供应计划员 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 60 | fdemandstorage | 需求货主 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 61 | fadjustdate | 调整日期 | timestamp | 0 |  |  | null | 调整日期 |
| 62 | feditdate | 修改日期 | timestamp | 0 |  |  | null | 修改日期 |
| 63 | fsupbomversion | 供应物料版本 | int8 | 64 |  | √ | 0 | 物料版本 bd_bomversion_new |
| 64 | finvpriority | 供应库存优先级 | varchar | 255 |  | √ | ' ' | 供应库存优先级 |
| 65 | fresolverip | 计算节点IP | varchar | 50 |  | √ | ' ' | 计算节点IP |
| 66 | fdynamicscrapformula | 动态损耗计算公式 | varchar | 30 |  | √ | ' ' | 动态损耗计算公式,枚举: A :标准用量/（1-损耗率） B :标准用量*（1+损耗率） |
| 67 | fmaterialattr | 物料属性 | varchar | 50 |  | √ | ' ' | 物料属性,枚举: 10020 :虚拟件 10030 :自制件 10040 :外购件 10050 :外协件 10060 :内协件 10070 :其他 |
| 68 | fsupplantag | 供应计划标识 | varchar | 50 |  | √ | ' ' | 供应计划标识 |
| 69 | fsupplyauxpty | 供应物料辅助属性 | int8 | 64 |  | √ | 0 | null 001 |
| 70 | frequireoperator | 需求计划员 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 71 | fsupplybillid | 供应单据ID | varchar | 50 |  | √ | ' ' | 供应单据ID |
| 72 | frequireorgid | 需求组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 73 | fscrapratio | 损耗率 | numeric | 23 | 10 | √ | 0.0000000000 | 损耗率 |
| 74 | fdynamicscrapratio | 动态损耗率 | numeric | 23 | 10 | √ | 0.0000000000 | 动态损耗率 |
| 75 | fplantag | 需求计划标识 | varchar | 50 |  | √ | ' ' | 需求计划标识 |
| 76 | fsupflexmetricval | 供应计划维度 | varchar | 2000 |  | √ | ' ' | 供应计划维度 |
| 77 | ffixscrap | 固定损耗 | numeric | 23 | 10 | √ | 0.0000000000 | 固定损耗 |
| 78 | fsupplybillf7 | 供应单据实体标识 | varchar | 60 |  | √ | ' ' | 主实体对象 bos_entityobject |
| 79 | flocationid | 供应仓位 | int8 | 64 |  | √ | 0 | 仓位 bd_location |
| 80 | fyieldratio | 成品率 | numeric | 23 | 10 | √ | 0.0000000000 | 成品率 |
| 81 | fbillentryid | 需求分录ID | varchar | 50 |  | √ | ' ' | 需求分录ID |
| 82 | fdemandqty | 需求数量 | numeric | 23 | 10 | √ | 0.0000000000 | 需求数量 |
| 83 | feditreason | 修改原因 | varchar | 255 |  | √ | ' ' | 修改原因 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_mrp_caldetailentry_fid |  | fid |
| 2 | idx_mrp_caldetailentry_req |  | fbillid,fbillentryid |
| 3 | idx_mrp_caldetailentry_sup |  | fsupplybillid,fsupplybillentryid |
| 4 | idx_mrp_caldetailentry_suptrack |  | fsuptracknumber |
| 5 | idx_mrp_caldetailentry_src |  | freqsourcebillno |
| 6 | idx_mrp_caldetailentry_rtype |  | fdemandbillf7 |
| 7 | idx_mrp_caldetailentry_tracknumber |  | ftracknumber |
| 8 | idx_mrp_caldetailentry_stype |  | fsupplybillf7 |
| 9 | idx_mrp_caldetailentry_ma |  | fmaterial |
| 10 | idx_mrp_caldetailentry_adj |  | fadjustsuggest |
| 11 | idx_mrp_caldetailentry_fseq |  | fseq |
| 12 | t_mrp_caldetailentry_pkey |  | fentryid |

---

## MRP计算明细表-主表 t_mrp_calcdetail

- **表名称：** MRP计算明细表-主表
- **表名：** t_mrp_calcdetail

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fplanvalue | 计划方案值 | int8 | 64 |  | √ | 0 | 计划方案值 |
| 3 | feventid | feventid | varchar | 300 |  | √ | ' ' |  |
| 4 | fcreatetime | 创建日期 | timestamp | 0 |  |  | null | 创建日期 |
| 5 | fruntype | 运算类型 | varchar | 30 |  | √ | ' ' | 运算类型,枚举: A :全局计划 B :齐套计划 C :调拨计划 D :齐套二代 E :计划运算向导 |
| 6 | fmrpplan | 计划方案 | int8 | 64 |  | √ | 0 | 计划方案 mrp_planscheme |
| 7 | fcaculatenumber | 运算日志编码 | varchar | 50 |  | √ | ' ' | 运算日志编码 |
| 8 | fplantype | 计划方案编码 | varchar | 50 |  | √ | ' ' | 计划方案编码 |
| 9 | fresolverip | fresolverip | varchar | 50 |  | √ | ' ' |  |
| 10 | fcaculatelog | 运算日志(基础资料) | int8 | 64 |  | √ | 0 | 运算日志 mrp_caculate_log |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_mrp_calde_log |  | fcaculatelog |
| 2 | t_mrp_calcdetail_pkey |  | fid |

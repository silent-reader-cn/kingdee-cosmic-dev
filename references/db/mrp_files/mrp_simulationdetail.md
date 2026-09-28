# 模拟计算明细表-mrp_simulationdetail

## 模拟计算明细表-主表 t_mrp_simulationcalc

- **表名称：** 模拟计算明细表-主表
- **表名：** t_mrp_simulationcalc

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fplanvalue | 计划方案值 | int8 | 64 |  | √ | 0 | 计划方案值 |
| 3 | fcreatetime | 创建日期 | timestamp | 0 |  |  | null | 创建日期 |
| 4 | fruntype | 运算类型 | varchar | 50 |  | √ | ' ' | 运算类型,枚举: A :全局计划 B :齐套计划 C :调拨计划 D :齐套二代 G :模拟计划 |
| 5 | fmrpplan | 计划方案 | int8 | 64 |  | √ | 0 | 计划方案定义(作废) mrp_planprogram |
| 6 | fcaculatenumber | 运算日志编码 | varchar | 50 |  | √ | ' ' | 运算日志编码 |
| 7 | fplantype | 计划方案编码 | varchar | 50 |  | √ | ' ' | 计划方案编码 |
| 8 | fcaculatelog | 运算日志(基础资料) | int8 | 64 |  | √ | 0 | 运算日志 mrp_caculate_log |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_mrp_simulationcalc |  | fid |
| 2 | idx_mrp_simulationcalc |  | fcaculatenumber |

---

## 单据体-子表 t_mrp_simulationcalcentry

- **表名称：** 单据体-子表
- **表名：** t_mrp_simulationcalcentry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fsupplybillno | 供应单据编码 | varchar | 50 |  | √ | ' ' | 供应单据编码 |
| 3 | fexceptionnumber | 例外信息编码 | varchar | 255 |  | √ | ' ' | 例外信息编码 |
| 4 | fwastagerateformula | 损耗率计算公式 | varchar | 50 |  | √ | ' ' | 损耗率计算公式,枚举: |
| 5 | fconfiguredcode | 配置号 | int8 | 64 |  | √ | 0 | 配置号 bd_configuredcode |
| 6 | fentryqtynumerator | 分子 | numeric | 23 | 10 | √ | 0 | 分子 |
| 7 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 8 | fbillentryseq | 原需求单据分录行号 | int4 | 32 |  | √ | 0 | 原需求单据分录行号 |
| 9 | fsupplybilltype | 供应单据类型 | varchar | 50 |  | √ | ' ' | 供应单据类型 |
| 10 | fadjustqty | 调整数量 | numeric | 23 | 10 | √ | 0 | 调整数量 |
| 11 | fllc | 低位码 | varchar | 50 |  | √ | ' ' | 低位码 |
| 12 | fdemandsourcetype | 需求来源类型 | varchar | 50 |  | √ | ' ' | 需求来源类型 |
| 13 | fdemanddate | 需求日期 | timestamp | 0 |  |  | null | 需求日期 |
| 14 | fadjustsuggest | 调整建议 | varchar | 50 |  | √ | ' ' | 调整建议,枚举: 不调整 :不调整 建议提前 :建议提前 提前占用 :提前占用 建议延后 :建议延后 延后占用 :延后占用 建议取消 :建议取消 |
| 15 | fsrcdemandqty | 原需求数量 | numeric | 23 | 10 | √ | 0 | 原需求数量 |
| 16 | freqsourcebillno | 需求来源号 | varchar | 255 |  | √ | ' ' | 需求来源号 |
| 17 | fsupplystorage | 供应货主 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 18 | fbomid | 父项BOMID | varchar | 50 |  | √ | ' ' | 父项BOMID |
| 19 | fentryqtytype | 用量类型 | varchar | 50 |  | √ | ' ' | 用量类型,枚举: |
| 20 | fsupmaterial | 供应物料 | int8 | 64 |  | √ | 0 | 物料 bd_material |
| 21 | foriginsupplyqty | 原供应数量 | numeric | 23 | 10 | √ | 0 | 原供应数量 |
| 22 | fdemandbilltype | 需求单据类型 | varchar | 50 |  | √ | ' ' | 需求单据类型 |
| 23 | fmaterial | 物料 | int8 | 64 |  | √ | 0 | 物料 bd_material |
| 24 | fsexpmsg | 供应例外信息 | varchar | 255 |  | √ | ' ' | 供应例外信息 |
| 25 | ftracknumber | 跟踪号 | int8 | 64 |  | √ | 0 | 跟踪号 bd_tracknumber |
| 26 | fbillno | 需求单据编码 | varchar | 50 |  | √ | ' ' | 需求单据编码 |
| 27 | forigindemanddate | 原始需求日期 | timestamp | 0 |  |  | null | 原始需求日期 |
| 28 | feventid | 计算事件ID | varchar | 50 |  | √ | ' ' | 计算事件ID |
| 29 | fmergebillno | 合并后需求单据编码 | varchar | 50 |  | √ | ' ' | 合并后需求单据编码 |
| 30 | fdemandbillf7 | 需求单据类型F7 | varchar | 36 |  | √ | ' ' | 主实体对象 bos_entityobject |
| 31 | forderdate | 计划准备日期 | timestamp | 0 |  |  | null | 计划准备日期 |
| 32 | fwarehouseid | 供应仓库 | int8 | 64 |  | √ | 0 | 仓库 bd_warehouse |
| 33 | fsupplyqty | 供应数量 | numeric | 23 | 10 | √ | 0 | 供应数量 |
| 34 | fsupplybillentryseq | 供应单据分录行号 | int4 | 32 |  | √ | 0 | 供应单据分录行号 |
| 35 | fsupplydetail | 供应明细 | varchar | 50 |  | √ | ' ' | 供应明细 |
| 36 | fishandle | 处理标识 | bpchar | 1 |  | √ | '0' | 处理标识 |
| 37 | fentryqtydenominator | 分母 | numeric | 23 | 10 | √ | 0 | 分母 |
| 38 | fbillid | 需求单据ID | varchar | 50 |  | √ | ' ' | 需求单据ID |
| 39 | fparentbomid | BOMID | varchar | 50 |  | √ | ' ' | BOMID |
| 40 | fexception | 例外信息 | varchar | 255 |  | √ | ' ' | 例外信息 |
| 41 | fsupplybillentryid | 供应分录ID | varchar | 50 |  | √ | ' ' | 供应分录ID |
| 42 | fismerge | 是否合并需求 | bpchar | 1 |  | √ | '0' | 是否合并需求 |
| 43 | fsupplyorgid | 供应组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 44 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 45 | fsuptracknumber | 供应跟踪号 | int8 | 64 |  | √ | 0 | 跟踪号 bd_tracknumber |
| 46 | fsuppriority | 供应优先级 | varchar | 50 |  | √ | ' ' | 供应优先级 |
| 47 | fbomversion | BOM版本 | int8 | 64 |  | √ | 0 | BOM版本 bd_bomversion |
| 48 | fdemandauxpty | 需求物料辅助属性 | int8 | 64 |  | √ | 0 | null 001 |
| 49 | fsexpnumber | 供应例外信息编码 | varchar | 255 |  | √ | ' ' | 供应例外信息编码 |
| 50 | fsupplydate | 供应单据日期 | timestamp | 0 |  |  | null | 供应单据日期 |
| 51 | fmergebillentryseq | 合并后需求单据分录序列号 | int4 | 32 |  | √ | 0 | 合并后需求单据分录序列号 |
| 52 | fexception_tag | 例外信息_详情 | text | 0 |  |  | null | 例外信息_详情 |
| 53 | fmergebillid | 合并后需求单据ID | varchar | 50 |  | √ | ' ' | 合并后需求单据ID |
| 54 | freqpriority | 需求优先级 | varchar | 50 |  | √ | ' ' | 需求优先级 |
| 55 | fmergebillentryid | 合并后需求单据分录ID | varchar | 50 |  | √ | ' ' | 合并后需求单据分录ID |
| 56 | fsupplyoperator | 供应计划员 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 57 | fdemandstorage | 需求货主 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 58 | fadjustdate | 调整日期 | timestamp | 0 |  |  | null | 调整日期 |
| 59 | feditdate | 修改日期 | timestamp | 0 |  |  | null | 修改日期 |
| 60 | finvpriority | 供应库存优先级 | varchar | 50 |  | √ | ' ' | 供应库存优先级 |
| 61 | fleadtime | 偏置提前期 | int4 | 32 |  | √ | 0 | 偏置提前期 |
| 62 | fresolverip | 计算节点IP | varchar | 50 |  | √ | ' ' | 计算节点IP |
| 63 | fdynamicscrapformula | 动态损耗计算公式 | varchar | 50 |  | √ | ' ' | 动态损耗计算公式,枚举: A :标准用量/（1-损耗率） B :标准用量*（1+损耗率） |
| 64 | fmaterialattr | 物料属性 | varchar | 50 |  | √ | ' ' | 物料属性,枚举: 10020 :虚拟件 10030 :自制件 10040 :外购件 10050 :外协件 10060 :内协件 10070 :其他 |
| 65 | fsupplantag | 供应计划标识 | varchar | 50 |  | √ | ' ' | 供应计划标识 |
| 66 | fsupplyauxpty | 供应物料辅助属性 | int8 | 64 |  | √ | 0 | null 001 |
| 67 | frequireoperator | 需求计划员 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 68 | fsupplybillid | 供应单据ID | varchar | 50 |  | √ | ' ' | 供应单据ID |
| 69 | frequireorgid | 需求组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 70 | fscrapratio | 损耗率 | numeric | 23 | 10 | √ | 0 | 损耗率 |
| 71 | fdynamicscrapratio | 动态损耗率 | numeric | 23 | 10 | √ | 0 | 动态损耗率 |
| 72 | fplantag | 需求计划标识 | varchar | 50 |  | √ | ' ' | 需求计划标识 |
| 73 | ffixscrap | 固定损耗 | numeric | 23 | 10 | √ | 0 | 固定损耗 |
| 74 | fsupplybillf7 | 供应单据类型F7 | varchar | 36 |  | √ | ' ' | 主实体对象 bos_entityobject |
| 75 | flocationid | 供应仓位 | int8 | 64 |  | √ | 0 | 仓位 bd_location |
| 76 | fyieldratio | 成品率 | numeric | 23 | 10 | √ | 0 | 成品率 |
| 77 | fbillentryid | 需求分录ID | varchar | 50 |  | √ | ' ' | 需求分录ID |
| 78 | fdemandqty | 需求数量 | numeric | 23 | 10 | √ | 0 | 需求数量 |
| 79 | feditreason | 修改原因 | varchar | 255 |  | √ | ' ' | 修改原因 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_mrp_simulationcalcentry |  | fentryid |
| 2 | idx_mrp_simulationcalcentry |  | fid,fseq |

# 计划模拟计算明细表-mrp_simcalcdetail

## 单据体-子表 t_mrp_simcalcdetailentry

- **表名称：** 单据体-子表
- **表名：** t_mrp_simcalcdetailentry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fsupplybillno | 供应单据编码 | varchar | 50 |  | √ | ' ' | 供应单据编码 |
| 3 | fexceptionnumber | 例外信息编码 | varchar | 255 |  | √ | ' ' | 例外信息编码 |
| 4 | fconfiguredcode | 配置号 | int8 | 64 |  | √ | 0 | [配置号（废弃） bd_configuredcode](../sbd_files/bd_configuredcode.md) |
| 5 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 6 | fbillentryseq | 原需求单据分录行号 | int4 | 32 |  | √ | 0 | 原需求单据分录行号 |
| 7 | fsupplybilltype | 供应单据实体名称 | varchar | 50 |  | √ | ' ' | 供应单据实体名称 |
| 8 | fadjustqty | 调整数量 | numeric | 23 | 10 | √ | 0 | 调整数量 |
| 9 | fllc | 低位码 | varchar | 50 |  | √ | ' ' | 低位码 |
| 10 | fdemandsourcetype | 需求来源类型 | varchar | 50 |  | √ | ' ' | 需求来源类型 |
| 11 | fdemanddate | 需求日期 | timestamp | 0 |  |  | null | 需求日期 |
| 12 | fadjustsuggest | 调整建议 | varchar | 50 |  | √ | ' ' | 调整建议,枚举: 不调整 :不调整 建议提前 :建议提前 提前占用 :提前占用 建议延后 :建议延后 延后占用 :延后占用 建议取消 :建议取消 |
| 13 | fsrcdemandqty | 原需求数量 | numeric | 23 | 10 | √ | 0 | 原需求数量 |
| 14 | freqsourcebillno | 需求来源号 | varchar | 255 |  | √ | ' ' | 需求来源号 |
| 15 | fsupplystorage | 供应货主 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 16 | fbomid | 父项BOMID | varchar | 50 |  | √ | ' ' | 父项BOMID |
| 17 | freqflexmetricval | 需求计划维度 | varchar | 100 |  | √ | ' ' | 需求计划维度 |
| 18 | fsupmaterial | 供应物料 | int8 | 64 |  | √ | 0 | [物料 bd_material](../basedata_files/bd_material.md) |
| 19 | foriginsupplyqty | 原供应数量 | numeric | 23 | 10 | √ | 0 | 原供应数量 |
| 20 | fdemandbilltype | 需求单据实体名称 | varchar | 50 |  | √ | ' ' | 需求单据实体名称 |
| 21 | fmaterial | 物料 | int8 | 64 |  | √ | 0 | [物料 bd_material](../basedata_files/bd_material.md) |
| 22 | fsexpmsg | 供应例外信息 | varchar | 255 |  | √ | ' ' | 供应例外信息 |
| 23 | ftracknumber | 跟踪号 | int8 | 64 |  | √ | 0 | [跟踪号 bd_tracknumber](../sbd_files/bd_tracknumber.md) |
| 24 | fbillno | 需求单据编码 | varchar | 50 |  | √ | ' ' | 需求单据编码 |
| 25 | forigindemanddate | 原始需求日期 | timestamp | 0 |  |  | null | 原始需求日期 |
| 26 | feventid | 计算事件ID | varchar | 50 |  | √ | ' ' | 计算事件ID |
| 27 | fsupflexmetricid | 供应物料维度 | varchar | 100 |  | √ | ' ' | 供应物料维度 |
| 28 | fmergebillno | 合并后需求单据编码 | varchar | 50 |  | √ | ' ' | 合并后需求单据编码 |
| 29 | fdemandbillf7 | 需求单据实体标识 | varchar | 50 |  | √ | ' ' | [主实体对象 bos_entityobject](../mdl_files/bos_entityobject.md) |
| 30 | freqflexmetricid | 需求物料维度 | varchar | 100 |  | √ | ' ' | 需求物料维度 |
| 31 | fwarehouseid | 供应仓库 | int8 | 64 |  | √ | 0 | [仓库 bd_warehouse](../sbd_files/bd_warehouse.md) |
| 32 | fsupplyqty | 供应数量 | numeric | 23 | 10 | √ | 0 | 供应数量 |
| 33 | fsupplybilltypeid | 供应单据类型 | int8 | 64 |  | √ | 0 | [单据类型 bos_billtype](../cts_files/bos_billtype.md) |
| 34 | fsupplybillentryseq | 供应单据分录行号 | int4 | 32 |  | √ | 0 | 供应单据分录行号 |
| 35 | fsupplydetail | 供应明细 | varchar | 255 |  | √ | ' ' | 供应明细 |
| 36 | fcopsupply | 联副产品供应 | varchar | 30 |  | √ | '0' | 联副产品供应,枚举: 1 :是 0 :否 |
| 37 | fishandle | 处理标识 | bpchar | 1 |  | √ | '0' | 处理标识 |
| 38 | fbillid | 需求单据ID | varchar | 50 |  | √ | ' ' | 需求单据ID |
| 39 | fparentbomid | BOMID | varchar | 50 |  | √ | ' ' | BOMID |
| 40 | fbilldetailid | 需求子单据体分录ID | varchar | 50 |  | √ | ' ' | 需求子单据体分录ID |
| 41 | fexception | 例外信息 | varchar | 255 |  | √ | ' ' | 例外信息 |
| 42 | fsupplybillentryid | 供应分录ID | varchar | 50 |  | √ | ' ' | 供应分录ID |
| 43 | fismerge | 是否合并需求 | bpchar | 1 |  | √ | '0' | 是否合并需求 |
| 44 | fsupplyorgid | 供应组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 45 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 46 | fsuptracknumber | 供应跟踪号 | int8 | 64 |  | √ | 0 | [跟踪号 bd_tracknumber](../sbd_files/bd_tracknumber.md) |
| 47 | flicenseno | 许可证编号 | int8 | 64 |  | √ | 0 | [许可证 bd_licence](../sbd_files/bd_licence.md) |
| 48 | fsuppriority | 供应优先级 | varchar | 50 |  | √ | '0' | 供应优先级 |
| 49 | fbomversion | 需求物料版本 | int8 | 64 |  | √ | 0 | [物料版本 bd_bomversion_new](../basedata_files/bd_bomversion_new.md) |
| 50 | fsupplybilldetailid | 供应子单据体分录ID | varchar | 50 |  | √ | ' ' | 供应子单据体分录ID |
| 51 | fdemandauxpty | 需求物料辅助属性 | int8 | 64 |  | √ | 0 | null 001 |
| 52 | fsexpnumber | 供应例外信息编码 | varchar | 255 |  | √ | ' ' | 供应例外信息编码 |
| 53 | fcomputeid | 运算标识 | int8 | 64 |  | √ | 0 | 运算标识 |
| 54 | fsupplydate | 供应单据日期 | timestamp | 0 |  |  | null | 供应单据日期 |
| 55 | fmergebillentryseq | 合并后需求单据分录序列号 | int4 | 32 |  | √ | 0 | 合并后需求单据分录序列号 |
| 56 | fexception_tag | 例外信息_详情 | text | 0 |  |  | null | 例外信息_详情 |
| 57 | fmergebillid | 合并后需求单据ID | varchar | 50 |  | √ | ' ' | 合并后需求单据ID |
| 58 | freqpriority | 需求优先级 | varchar | 50 |  | √ | '0' | 需求优先级 |
| 59 | fmergebillentryid | 合并后需求单据分录ID | varchar | 50 |  | √ | ' ' | 合并后需求单据分录ID |
| 60 | fsupplyoperator | 供应计划员 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 61 | fdemandstorage | 需求货主 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 62 | fbonded | 保税 | bpchar | 1 |  | √ | '0' | 保税 |
| 63 | fadjustdate | 调整日期 | timestamp | 0 |  |  | null | 调整日期 |
| 64 | feditdate | 有效期至 | timestamp | 0 |  |  | null | 有效期至 |
| 65 | fsupbomversion | 供应物料版本 | int8 | 64 |  | √ | 0 | [物料版本 bd_bomversion_new](../basedata_files/bd_bomversion_new.md) |
| 66 | finvpriority | 供应库存优先级 | varchar | 50 |  | √ | ' ' | 供应库存优先级 |
| 67 | fresolverip | 计算节点IP | varchar | 50 |  | √ | ' ' | 计算节点IP |
| 68 | fdynamicscrapformula | 动态损耗计算公式 | varchar | 30 |  | √ | ' ' | 动态损耗计算公式,枚举: A :标准用量/（1-损耗率） B :标准用量*（1+损耗率） |
| 69 | fmaterialattr | 物料属性 | varchar | 50 |  | √ | ' ' | 物料属性,枚举: 10020 :虚拟件 10030 :自制件 10040 :外购件 10050 :外协件 10060 :内协件 10070 :其他 |
| 70 | fsupplantag | 供应计划标识 | varchar | 50 |  | √ | ' ' | 供应计划标识 |
| 71 | fsupplyauxpty | 供应物料辅助属性 | int8 | 64 |  | √ | 0 | null 001 |
| 72 | frequireoperator | 需求计划员 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 73 | fsupplybillid | 供应单据ID | varchar | 50 |  | √ | ' ' | 供应单据ID |
| 74 | frequireorgid | 需求组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 75 | fscrapratio | 损耗率 | numeric | 23 | 10 | √ | 0 | 损耗率 |
| 76 | fdynamicscrapratio | 动态损耗率 | numeric | 23 | 10 | √ | 0 | 动态损耗率 |
| 77 | fplantag | 需求计划标识 | varchar | 50 |  | √ | ' ' | 需求计划标识 |
| 78 | fsupflexmetricval | 供应计划维度 | varchar | 100 |  | √ | ' ' | 供应计划维度 |
| 79 | ffixscrap | 固定损耗 | numeric | 23 | 10 | √ | 0 | 固定损耗 |
| 80 | fsupplybillf7 | 供应单据实体标识 | varchar | 50 |  | √ | ' ' | [主实体对象 bos_entityobject](../mdl_files/bos_entityobject.md) |
| 81 | flocationid | 供应仓位 | int8 | 64 |  | √ | 0 | [仓位 bd_location](../sbd_files/bd_location.md) |
| 82 | fyieldratio | 成品率 | numeric | 23 | 10 | √ | 0 | 成品率 |
| 83 | fbillentryid | 需求分录ID | varchar | 50 |  | √ | ' ' | 需求分录ID |
| 84 | fdemandqty | 需求数量 | numeric | 23 | 10 | √ | 0 | 需求数量 |
| 85 | feditreason | 修改原因 | varchar | 255 |  | √ | ' ' | 修改原因 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_mrp_simcalcdetailentry_fid |  | fid |
| 2 | pk_mrp_simcalcdetailentry |  | fentryid |

---

## 计划模拟计算明细表-主表 t_mrp_simcalcdetail

- **表名称：** 计划模拟计算明细表-主表
- **表名：** t_mrp_simcalcdetail

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fplanvalue | 计划方案值 | int8 | 64 |  | √ | 0 | 计划方案值 |
| 3 | fcreatetime | 创建日期 | timestamp | 0 |  |  | null | 创建日期 |
| 4 | fruntype | 运算类型 | varchar | 30 |  | √ | ' ' | 运算类型,枚举: A :全局计划 B :齐套计划 C :调拨计划 D :齐套二代 E :计划运算向导 |
| 5 | fmrpplan | 计划方案 | int8 | 64 |  | √ | 0 | [计划方案 mrp_planscheme](../msplan_files/mrp_planscheme.md) |
| 6 | fcaculatenumber | 运算日志编码 | varchar | 50 |  | √ | ' ' | 运算日志编码 |
| 7 | fplantype | 计划方案编码 | varchar | 50 |  | √ | ' ' | 计划方案编码 |
| 8 | fcaculatelog | 运算日志(基础资料) | int8 | 64 |  | √ | 0 | [运算日志 mrp_caculate_log](../msplan_files/mrp_caculate_log.md) |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_mrp_simcalcdetail_clognum |  | fcaculatenumber |
| 2 | pk_mrp_simcalcdetail |  | fid |

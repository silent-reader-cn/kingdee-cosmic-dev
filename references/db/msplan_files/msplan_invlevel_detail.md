# 库存计划计算明细表-msplan_invlevel_detail

## 库存计划计算明细表-主表 t_msplan_invdetail

- **表名称：** 库存计划计算明细表-主表
- **表名：** t_msplan_invdetail

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fplanvalue | 计划方案值 | int8 | 64 |  | √ | 0 | 计划方案值 |
| 3 | feventid | feventid | varchar | 300 |  | √ | ' ' |  |
| 4 | fcreatetime | 创建日期 | timestamp | 0 |  |  | null | 创建日期 |
| 5 | fruntype | 运算类型 | varchar | 30 |  | √ | ' ' | 运算类型,枚举: A :全局计划 B :齐套计划 C :调拨计划 D :齐套二代 |
| 6 | fmrpplan | 计划方案 | int8 | 64 |  | √ | 0 | [计划方案定义(作废) mrp_planprogram](../msplan_files/mrp_planprogram.md) |
| 7 | fcaculatenumber | 运算日志编码 | varchar | 50 |  | √ | '' | 运算日志编码 |
| 8 | fplantype | 计划方案编码 | varchar | 50 |  | √ | ' ' | 计划方案编码 |
| 9 | fresolverip | fresolverip | varchar | 50 |  | √ | ' ' |  |
| 10 | fcaculatelog | 运算日志(基础资料) | int8 | 64 |  | √ | 0 | [运算日志 mrp_caculate_log](../msplan_files/mrp_caculate_log.md) |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_msplan_invdetail |  | fid |
| 2 | idx_msplan_invdetail_log |  | fcaculatelog |

---

## 单据体-子表 t_msplan_invdetailentry

- **表名称：** 单据体-子表
- **表名：** t_msplan_invdetailentry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fsupplybillno | 供应单据编码 | varchar | 50 |  | √ | ' ' | 供应单据编码 |
| 3 | fexceptionnumber | 例外信息编码 | varchar | 255 |  | √ | ' ' | 例外信息编码 |
| 4 | fconfiguredcode | 配置号 | int8 | 64 |  | √ | 0 | [配置号（废弃） bd_configuredcode](../sbd_files/bd_configuredcode.md) |
| 5 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 6 | fsupplybilltype | 供应单据类型 | varchar | 50 |  | √ | ' ' | 供应单据类型 |
| 7 | fbillentryseq | 原需求单据分录行号 | int4 | 32 |  | √ | 0 | 原需求单据分录行号 |
| 8 | fadjustqty | 调整数量 | numeric | 23 | 10 | √ | 0 | 调整数量 |
| 9 | fllc | 低位码 | varchar | 255 |  | √ | ' ' | 低位码 |
| 10 | fdemandsourcetype | 需求来源类型 | varchar | 50 |  | √ | ' ' | 需求来源类型 |
| 11 | fadjustsuggest | 调整建议 | varchar | 50 |  | √ | ' ' | 调整建议,枚举: 不调整 :不调整 建议提前 :建议提前 提前占用 :提前占用 建议延后 :建议延后 延后占用 :延后占用 建议取消 :建议取消 |
| 12 | fdemanddate | 需求日期 | timestamp | 0 |  |  | null | 需求日期 |
| 13 | fsupplystorage | 供应货主 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 14 | fsrcdemandqty | 原需求数量 | numeric | 23 | 10 | √ | 0 | 原需求数量 |
| 15 | freqsourcebillno | 需求来源号 | varchar | 255 |  | √ | ' ' | 需求来源号 |
| 16 | fbomid | 父项BOMID | varchar | 100 |  | √ | ' ' | 父项BOMID |
| 17 | fsupmaterial | 供应物料 | int8 | 64 |  | √ | 0 | [物料 bd_material](../basedata_files/bd_material.md) |
| 18 | foriginsupplyqty | 原供应数量 | numeric | 23 | 10 | √ | 0 | 原供应数量 |
| 19 | fdemandbilltype | 需求单据类型 | varchar | 50 |  | √ | ' ' | 需求单据类型 |
| 20 | fmaterial | 物料 | int8 | 64 |  | √ | 0 | [物料 bd_material](../basedata_files/bd_material.md) |
| 21 | fsexpmsg | 供应例外信息 | varchar | 255 |  | √ | ' ' | 供应例外信息 |
| 22 | ftracknumber | 跟踪号 | int8 | 64 |  | √ | 0 | [跟踪号 bd_tracknumber](../sbd_files/bd_tracknumber.md) |
| 23 | fbillno | 需求单据编码 | varchar | 50 |  | √ | ' ' | 需求单据编码 |
| 24 | forigindemanddate | 原始需求日期 | timestamp | 0 |  |  | null | 原始需求日期 |
| 25 | feventid | 计算事件ID | varchar | 50 |  | √ | ' ' | 计算事件ID |
| 26 | fmergebillno | 合并后需求单据编码 | varchar | 50 |  | √ | ' ' | 合并后需求单据编码 |
| 27 | fdemandbillf7 | 需求单据类型F7 | varchar | 60 |  | √ | ' ' | [主实体对象 bos_entityobject](../mdl_files/bos_entityobject.md) |
| 28 | fwarehouseid | 供应仓库 | int8 | 64 |  | √ | 0 | [仓库 bd_warehouse](../sbd_files/bd_warehouse.md) |
| 29 | fsupplyqty | 供应数量 | numeric | 23 | 10 | √ | 0 | 供应数量 |
| 30 | fsupplybillentryseq | 供应单据分录行号 | int4 | 32 |  | √ | 0 | 供应单据分录行号 |
| 31 | fsupplydetail | 供应明细 | varchar | 255 |  | √ | ' ' | 供应明细 |
| 32 | fishandle | 处理标识 | bpchar | 1 |  | √ | '0' | 处理标识 |
| 33 | fbillid | 需求单据ID | varchar | 50 |  | √ | ' ' | 需求单据ID |
| 34 | fparentbomid | BOMID | varchar | 100 |  | √ | ' ' | BOMID |
| 35 | fsupplybillentryid | 供应分录ID | varchar | 50 |  | √ | ' ' | 供应分录ID |
| 36 | fexception | 例外信息 | varchar | 255 |  | √ | ' ' | 例外信息 |
| 37 | fismerge | 是否合并需求 | bpchar | 1 |  | √ | '0' | 是否合并需求 |
| 38 | fsupplyorgid | 供应组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 39 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 40 | fsuptracknumber | 供应跟踪号 | int8 | 64 |  | √ | 0 | [跟踪号 bd_tracknumber](../sbd_files/bd_tracknumber.md) |
| 41 | fsuppriority | 供应优先级 | varchar | 255 |  | √ | ' ' | 供应优先级 |
| 42 | fbomversion | BOM版本 | int8 | 64 |  | √ | 0 | [BOM版本 bd_bomversion](../basedata_files/bd_bomversion.md) |
| 43 | fdemandauxpty | 需求物料辅助属性 | int8 | 64 |  | √ | 0 | null 001 |
| 44 | fsexpnumber | 供应例外信息编码 | varchar | 255 |  | √ | ' ' | 供应例外信息编码 |
| 45 | fsupplydate | 供应单据日期 | timestamp | 0 |  |  | null | 供应单据日期 |
| 46 | fmergebillentryseq | 合并后需求单据分录序列号 | int8 | 64 |  | √ | 0 | 合并后需求单据分录序列号 |
| 47 | fexception_tag | 例外信息_详情 | text | 0 |  |  | null | 例外信息_详情 |
| 48 | fmergebillid | 合并后需求单据ID | varchar | 50 |  | √ | ' ' | 合并后需求单据ID |
| 49 | freqpriority | 需求优先级 | varchar | 255 |  | √ | ' ' | 需求优先级 |
| 50 | fmergebillentryid | 合并后需求单据分录ID | varchar | 50 |  | √ | ' ' | 合并后需求单据分录ID |
| 51 | fsupplyoperator | 供应计划员 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 52 | fdemandstorage | 需求货主 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 53 | fadjustdate | 调整日期 | timestamp | 0 |  |  | null | 调整日期 |
| 54 | feditdate | 修改日期 | timestamp | 0 |  |  | null | 修改日期 |
| 55 | finvpriority | 供应库存优先级 | varchar | 255 |  | √ | ' ' | 供应库存优先级 |
| 56 | fresolverip | 计算节点IP | varchar | 50 |  | √ | ' ' | 计算节点IP |
| 57 | fdynamicscrapformula | 动态损耗计算公式 | varchar | 30 |  | √ | ' ' | 动态损耗计算公式,枚举: A :标准用量/（1-损耗率） B :标准用量*（1+损耗率） |
| 58 | fmaterialattr | 物料属性 | varchar | 50 |  | √ | ' ' | 物料属性,枚举: 10020 :虚拟件 10030 :自制件 10040 :外购件 10050 :外协件 10060 :内协件 10070 :其他 |
| 59 | fsupplantag | 供应计划标识 | varchar | 50 |  | √ | ' ' | 供应计划标识 |
| 60 | fsupplyauxpty | 供应物料辅助属性 | int8 | 64 |  | √ | 0 | null 001 |
| 61 | frequireoperator | 需求计划员 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 62 | fsupplybillid | 供应单据ID | varchar | 50 |  | √ | ' ' | 供应单据ID |
| 63 | frequireorgid | 需求组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 64 | fscrapratio | 损耗率 | numeric | 23 | 10 | √ | 0 | 损耗率 |
| 65 | fdynamicscrapratio | 动态损耗率 | numeric | 23 | 10 | √ | 0 | 动态损耗率 |
| 66 | fplantag | 需求计划标识 | varchar | 50 |  | √ | ' ' | 需求计划标识 |
| 67 | ffixscrap | 固定损耗 | numeric | 23 | 10 | √ | 0 | 固定损耗 |
| 68 | fsupplybillf7 | 供应单据类型F7 | varchar | 60 |  | √ | ' ' | [主实体对象 bos_entityobject](../mdl_files/bos_entityobject.md) |
| 69 | flocationid | 供应仓位 | int8 | 64 |  | √ | 0 | [仓位 bd_location](../sbd_files/bd_location.md) |
| 70 | fyieldratio | 成品率 | numeric | 23 | 10 | √ | 0 | 成品率 |
| 71 | fbillentryid | 需求分录ID | varchar | 50 |  | √ | ' ' | 需求分录ID |
| 72 | fdemandqty | 需求数量 | numeric | 23 | 10 | √ | 0 | 需求数量 |
| 73 | feditreason | 修改原因 | varchar | 255 |  | √ | ' ' | 修改原因 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_msplan_invdetailentry_fid |  | fid |
| 2 | pk_msplan_invdetailentry |  | fentryid |
| 3 | idx_msplan_invdetailentry_fseq |  | fseq |

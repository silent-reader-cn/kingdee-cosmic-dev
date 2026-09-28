# 模拟计划-mrp_simulation

## 单据体-子表 t_mrp_simulatefieldentry

- **表名称：** 单据体-子表
- **表名：** t_mrp_simulatefieldentry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | ffieldentity | 实体标识 | varchar | 50 |  | √ | ' ' | 实体标识 |
| 3 | ffieldname | 字段名称 | varchar | 50 |  | √ | ' ' | 字段名称 |
| 4 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 5 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 6 | ffieldkey | 字段标识 | varchar | 50 |  | √ | ' ' | 字段标识 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_mrp_simulatefieldentry |  | fentryid |
| 2 | idx_mrp_simulatefieldentry |  | fid,fseq |

---

## 模拟概要-子表 t_mrp_simulationoutline

- **表名称：** 模拟概要-子表
- **表名：** t_mrp_simulationoutline

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | frequiredate | 需求日期 | timestamp | 0 |  |  | null | 需求日期 |
| 3 | foperatorid | 销售员 | int8 | 64 |  | √ | 0 | 供应链业务员 bd_operator |
| 4 | fmaterialid | 物料编码 | int8 | 64 |  | √ | 0 | 物料 bd_material |
| 5 | fauxptyid | 辅助属性 | int8 | 64 |  | √ | 0 | null 001 |
| 6 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 7 | fbillentrykey | 单据分录标识 | varchar | 50 |  | √ | ' ' | 单据分录标识 |
| 8 | fconfiguredcodeid | 配置号 | int8 | 64 |  | √ | 0 | 配置号 bd_configuredcode |
| 9 | fsourcetype | 来源 | bpchar | 1 |  | √ | 'B' | 来源,枚举: A :选单 B :手工 |
| 10 | fwayqty | 可交总量 | numeric | 23 | 10 | √ | 0 | 可交总量 |
| 11 | ftracknumberid | 跟踪号 | int8 | 64 |  | √ | 0 | 跟踪号 bd_tracknumber |
| 12 | frequiretypeid | 需求单据类型 | int8 | 64 |  | √ | 0 | 数据源配置 mrp_resource_dataconfig |
| 13 | fqty | 数量 | numeric | 23 | 10 | √ | 0 | 数量 |
| 14 | fpromisedate | 承诺日期 | timestamp | 0 |  |  | null | 承诺日期 |
| 15 | finvqty | 库存可交数量 | numeric | 23 | 10 | √ | 0 | 库存可交数量 |
| 16 | funitid | 计量单位 | int8 | 64 |  | √ | 0 | 计量单位 bd_measureunits |
| 17 | frequireorgid | 需求组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 18 | fdeliverydate | 最早交货日期 | timestamp | 0 |  |  | null | 最早交货日期 |
| 19 | fbillnumber | 单据编号 | varchar | 50 |  | √ | ' ' | 单据编号 |
| 20 | fbillentryid | 单据分录ID | int8 | 64 |  | √ | 0 | 单据分录ID |
| 21 | fbillid | 单据ID | int8 | 64 |  | √ | 0 | 单据ID |
| 22 | frowno | 行号 | int4 | 32 |  | √ | 0 | 行号 |
| 23 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 24 | fstockorgid | 发货组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 25 | fcustomerid | 客户 | int8 | 64 |  | √ | 0 | 客户 bd_customer |
| 26 | fbilltypeid | 单据类型 | int8 | 64 |  | √ | 0 | 单据类型 bos_billtype |
| 27 | fdemandbillid | fdemandbillid | varchar | 50 |  | √ | ' ' |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_mrp_simulationoutline |  | fentryid |
| 2 | idx_mrp_simulationoutline |  | fid,fseq |

---

## 模拟计划-主表 t_mrp_simulation

- **表名称：** 模拟计划-主表
- **表名：** t_mrp_simulation

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | frunlogid | 计划运算号 | int8 | 64 |  | √ | 0 | 运算日志 mrp_caculate_log |
| 3 | forgid | 计划组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 4 | fremarks | 备注 | varchar | 255 |  | √ | ' ' | 备注 |
| 5 | fclosedate | 关闭时间 | timestamp | 0 |  |  | null | 关闭时间 |
| 6 | fsimulationstatus | 模拟状态 | bpchar | 1 |  | √ | 'A' | 模拟状态,枚举: A :未模拟 B :已模拟 C :已转正 D :已过期 |
| 7 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 8 | fplanid | 模拟方案 | int8 | 64 |  | √ | 0 | 计划方案定义(作废) mrp_planprogram |
| 9 | fisallowdateinpast | 允许计划建议开始日期在过去 | bpchar | 1 |  | √ | '1' | 允许计划建议开始日期在过去 |
| 10 | fenddate | 结束截止日期 | timestamp | 0 |  |  | null | 结束截止日期 |
| 11 | fdataversionid | 数据版本定义 | int8 | 64 |  | √ | 0 | 数据版本 msplan_ds_version |
| 12 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 13 | fisllc | 重算低位码 | bpchar | 1 |  | √ | '0' | 重算低位码 |
| 14 | fbillno | 模拟编号 | varchar | 30 |  | √ | ' ' | 模拟编号 |
| 15 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 16 | fretentiondays | 保留天数 | int4 | 32 |  | √ | 0 | 保留天数 |
| 17 | fsimulationuserid | 模拟人员 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 18 | fbillstatus | 单据状态 | varchar | 50 |  | √ | ' ' | 单据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 19 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 20 | fsimulationdate | 模拟启动时间 | timestamp | 0 |  |  | null | 模拟启动时间 |
| 21 | fauditdate | 审核时间 | timestamp | 0 |  |  | null | 审核时间 |
| 22 | fabctype | ABC分类 | varchar | 50 |  | √ | ' ' | ABC分类,枚举: A :A类 B :B类 C :C类 |
| 23 | fclosestatus | 关闭状态 | bpchar | 1 |  | √ | 'B' | 关闭状态,枚举: A :已关闭 B :未关闭 |
| 24 | fcloseuserid | 关闭人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 25 | fauditorid | 审核人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 26 | fisbomcheck | BOM嵌套检查 | bpchar | 1 |  | √ | '0' | BOM嵌套检查 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_mrp_simulation |  | forgid,fbillno |
| 2 | pk_mrp_simulation |  | fid |

---

## 物料汇总详情-子表 t_mrp_simulationsummary

- **表名称：** 物料汇总详情-子表
- **表名：** t_mrp_simulationsummary

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fplanqty | 数量 | numeric | 23 | 10 | √ | 0 | 数量 |
| 3 | fmaterialid | 物料编码 | int8 | 64 |  | √ | 0 | 物料 bd_material |
| 4 | fauxptyid | 辅助属性 | int8 | 64 |  | √ | 0 | null 001 |
| 5 | freplaceqty | 替代需求 | numeric | 23 | 10 | √ | 0 | 替代需求 |
| 6 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 7 | fconfiguredcodeid | 配置号 | int8 | 64 |  | √ | 0 | 配置号 bd_configuredcode |
| 8 | fplancurrentqty | 本次分配 | numeric | 23 | 10 | √ | 0 | 本次分配 |
| 9 | fadjustsuggest | 调整建议 | varchar | 50 |  | √ | ' ' | 调整建议,枚举: 不调整 :不调整 建议提前 :建议提前 提前占用 :提前占用 建议延后 :建议延后 延后占用 :延后占用 建议取消 :建议取消 |
| 10 | freplacedqty | 被替代 | numeric | 23 | 10 | √ | 0 | 被替代 |
| 11 | ftracknumberid | 跟踪号 | int8 | 64 |  | √ | 0 | 跟踪号 bd_tracknumber |
| 12 | fcanuseqty | 可用量 | numeric | 23 | 10 | √ | 0 | 可用量 |
| 13 | fwaycanqty | 可用量 | numeric | 23 | 10 | √ | 0 | 可用量 |
| 14 | ffinishqty | 期末可用量 | numeric | 23 | 10 | √ | 0 | 期末可用量 |
| 15 | fwaycurrentqty | 本次分配 | numeric | 23 | 10 | √ | 0 | 本次分配 |
| 16 | fmaterialarr | 物料属性 | varchar | 50 |  | √ | ' ' | 物料属性,枚举: 10020 :虚拟件 10030 :自制件 10040 :外购件 10050 :外协件 10060 :内协件 10070 :其他 |
| 17 | finvqty | 即时库存 | numeric | 23 | 10 | √ | 0 | 即时库存 |
| 18 | fbillcount | 单据数 | int4 | 32 |  | √ | 0 | 单据数 |
| 19 | funitid | 计量单位 | int8 | 64 |  | √ | 0 | 计量单位 bd_measureunits |
| 20 | fcurrentqty | 本次分配 | numeric | 23 | 10 | √ | 0 | 本次分配 |
| 21 | fdemandqty | 独立需求 | numeric | 23 | 10 | √ | 0 | 独立需求 |
| 22 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 23 | fsafetyqty | 安全库存 | numeric | 23 | 10 | √ | 0 | 安全库存 |
| 24 | fallqty | 总资源 | numeric | 23 | 10 | √ | 0 | 总资源 |
| 25 | fdependentqty | 相关需求 | numeric | 23 | 10 | √ | 0 | 相关需求 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_mrp_simulationsummary |  | fid,fseq |
| 2 | pk_mrp_simulationsummary |  | fentryid |

---

## 模拟详情-子表 t_mrp_simulationdetail

- **表名称：** 模拟详情-子表
- **表名：** t_mrp_simulationdetail

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | frequireqty | 需求数量 | numeric | 23 | 10 | √ | 0 | 需求数量 |
| 3 | fwastagerateformula | 损耗率计算公式 | varchar | 50 |  | √ | ' ' | 损耗率计算公式,枚举: A :1-变动损耗率 B :1+变动损耗率 |
| 4 | fauxptyid | 辅助属性 | int8 | 64 |  | √ | 0 | null 001 |
| 5 | fentryqtynumerator | 分子 | numeric | 23 | 10 | √ | 0 | 分子 |
| 6 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 7 | freqsourcebillno | 需求来源号 | varchar | 255 |  | √ | ' ' | 需求来源号 |
| 8 | fentryqtytype | 用量类型 | varchar | 50 |  | √ | ' ' | 用量类型,枚举: A :变动 B :固定 C :阶梯 |
| 9 | fparententryid | fparententryid | int8 | 64 |  | √ | 0 | pid |
| 10 | fisreplace | 替代件 | bpchar | 1 |  | √ | '0' | 替代件 |
| 11 | fbillno | 单据编号 | varchar | 50 |  | √ | ' ' | 单据编号 |
| 12 | fisrequire | 独立需求 | bpchar | 1 |  | √ | '0' | 独立需求 |
| 13 | fpromisedate | 承诺日期 | timestamp | 0 |  |  | null | 承诺日期 |
| 14 | fmaterialarr | 物料属性 | varchar | 50 |  | √ | ' ' | 物料属性,枚举: 10020 :虚拟件 10030 :自制件 10040 :外购件 10050 :外协件 10060 :内协件 10070 :其他 |
| 15 | funitid | 计量单位 | int8 | 64 |  | √ | 0 | 计量单位 bd_measureunits |
| 16 | fsupplyqty | 供应数量 | numeric | 23 | 10 | √ | 0 | 供应数量 |
| 17 | fqty20 | 数量20 | numeric | 23 | 10 | √ | 0 | 数量20 |
| 18 | fentryqtydenominator | 分母 | numeric | 23 | 10 | √ | 0 | 分母 |
| 19 | fbillid | 单据ID | varchar | 50 |  | √ | ' ' | 单据ID |
| 20 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 21 | fmaterialid | 物料编码 | int8 | 64 |  | √ | 0 | 物料 bd_material |
| 22 | fqty19 | 数量19 | numeric | 23 | 10 | √ | 0 | 数量19 |
| 23 | fqty16 | 数量16 | numeric | 23 | 10 | √ | 0 | 数量16 |
| 24 | fqty15 | 数量15 | numeric | 23 | 10 | √ | 0 | 数量15 |
| 25 | fqty18 | 数量18 | numeric | 23 | 10 | √ | 0 | 数量18 |
| 26 | fconfiguredcodeid | 配置号 | int8 | 64 |  | √ | 0 | 配置号 bd_configuredcode |
| 27 | fqty17 | 数量17 | numeric | 23 | 10 | √ | 0 | 数量17 |
| 28 | fqty12 | 数量12 | numeric | 23 | 10 | √ | 0 | 数量12 |
| 29 | flongestpath | 最长路径 | bpchar | 1 |  | √ | '0' | 最长路径 |
| 30 | fqty11 | 数量11 | numeric | 23 | 10 | √ | 0 | 数量11 |
| 31 | fqty14 | 数量14 | numeric | 23 | 10 | √ | 0 | 数量14 |
| 32 | fqty13 | 数量13 | numeric | 23 | 10 | √ | 0 | 数量13 |
| 33 | fqty10 | 数量10 | numeric | 23 | 10 | √ | 0 | 数量10 |
| 34 | ftracknumberid | 跟踪号 | int8 | 64 |  | √ | 0 | 跟踪号 bd_tracknumber |
| 35 | fisexception | 存在计划信息 | bpchar | 1 |  | √ | '0' | 存在计划信息 |
| 36 | fbegindate | 建议采购/生产日期 | timestamp | 0 |  |  | null | 建议采购/生产日期 |
| 37 | fdynamicscrapratio | 损耗率 | numeric | 23 | 10 | √ | 0 | 损耗率 |
| 38 | ffinishdate | 建议到货/完工日期 | timestamp | 0 |  |  | null | 建议到货/完工日期 |
| 39 | fqty2 | 数量2 | numeric | 23 | 10 | √ | 0 | 数量2 |
| 40 | flevel | 层级 | int8 | 64 |  | √ | 0 | 层级 |
| 41 | fqty3 | 数量3 | numeric | 23 | 10 | √ | 0 | 数量3 |
| 42 | ffixscrap | 固定损耗 | numeric | 23 | 10 | √ | 0 | 固定损耗 |
| 43 | fqty1 | 数量1 | numeric | 23 | 10 | √ | 0 | 数量1 |
| 44 | fqty6 | 数量6 | numeric | 23 | 10 | √ | 0 | 数量6 |
| 45 | fbillentryid | 单据分录ID | varchar | 50 |  | √ | ' ' | 单据分录ID |
| 46 | fqty7 | 数量7 | numeric | 23 | 10 | √ | 0 | 数量7 |
| 47 | fqty4 | 数量4 | numeric | 23 | 10 | √ | 0 | 数量4 |
| 48 | fqty5 | 数量5 | numeric | 23 | 10 | √ | 0 | 数量5 |
| 49 | fqty8 | 数量8 | numeric | 23 | 10 | √ | 0 | 数量8 |
| 50 | fqty9 | 数量9 | numeric | 23 | 10 | √ | 0 | 数量9 |
| 51 | frowno | 行号 | int4 | 32 |  | √ | 0 | 行号 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_mrp_simulationdetail |  | fentryid |
| 2 | idx_mrp_simulationdetail |  | fid,fseq |

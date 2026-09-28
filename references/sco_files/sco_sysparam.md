# 成本参数基础资料-sco_sysparam

## 成本参数基础资料-主表 t_sco_sysparam

- **表名称：** 成本参数基础资料-主表
- **表名：** t_sco_sysparam

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fbillrange | 参与完工产量归集的单据范围 | varchar | 510 |  | √ | ' ' | 参与完工产量归集的单据范围,枚举: WIPCOMPELETE :完工入库单 WIPCOMPELETEBACK :完工入库退回 PRODUCTCOMPELETE :生产入库单 PRODUCTCOMPELETEBACK :生产入库退回 |
| 3 | fplancollectrange | 参与计划数量归集的单据范围 | varchar | 255 |  | √ | 'PROCESSREPORT,PROCESSADJUST,MFTORDERREPORT ' | 参与计划数量归集的单据范围,枚举: SCGD :生产工单 WWGD :委外工单 WGRK :完工产量归集单 |
| 4 | fwarehousepoint | 仅归集入库点资源 | bpchar | 1 |  | √ | '0' | 仅归集入库点资源 |
| 5 | fassistant | 辅助分配方法 | varchar | 30 |  | √ | 'direct' | 辅助分配方法,枚举: direct :直接分配法 mutual :交互分配法 algebra :代数分配法 |
| 6 | fhourexpense | 工时费用维度 | varchar | 255 |  | √ | ' ' | 工时费用维度,枚举: TRADE :行业 ROLE :角色 RESOURCE :资源 |
| 7 | forgid | 成本核算参数中的核算组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 8 | fmfgfeebilltype | 制造费用归集新增方式 | varchar | 255 |  |  | 'MANUAL' | 制造费用归集新增方式,枚举: SYS :内部系统引入 EXCEL :模板引入 API :API接口 MANUAL :手工录入 |
| 9 | fstartbomrouterule | 启用新BOM设置/新工艺路线设置 | bpchar | 1 |  | √ | '0' | 启用新BOM设置/新工艺路线设置 |
| 10 | fimportperiodscope | 业务单据引入期间范围 | varchar | 68 |  | √ | ' ' | 业务单据引入期间范围 |
| 11 | fcompletetype | 完工产量新增方式 | varchar | 30 |  | √ | ' ' | 完工产量新增方式,枚举: OBJECTRULE :内部系统引入 EXCEL :模板引入 API :API接口 MANUAL :手工录入 |
| 12 | freductstrategy | 差异分摊策略 | varchar | 50 |  | √ | ' ' | 差异分摊策略,枚举: OVERALL_REDUCT :综合分摊 ITEMIZED_REDUCT :分项分摊 |
| 13 | fispreviousoneton | 引入前N月业务单据 | bpchar | 1 |  | √ | '0' | 引入前N月业务单据 |
| 14 | fappnum | 所属应用 | varchar | 10 |  | √ | ' ' | 所属应用,枚举: sca :标准成本 aca :实际成本 |
| 15 | fisautoupdate | 成本更新单据审核后自动进行【更新确认】单据 | bpchar | 1 |  | √ | '0' | 成本更新单据审核后自动进行【更新确认】单据 |
| 16 | fresourcerange | 参与资源耗用量归集的单据范围 | varchar | 255 |  | √ | 'PROCESSREPORT,PROCESSADJUST,MFTORDERREPORT ' | 参与资源耗用量归集的单据范围,枚举: PROCESSREPORT :工序汇报单 PROCESSADJUST :汇报资源调整单 MFTORDERREPORT :工单汇报单 |
| 17 | fisupdatebyperiod | 按期进行成本更新 | bpchar | 1 |  | √ | '0' | 按期进行成本更新 |
| 18 | fnum | 前N月 | int4 | 32 |  | √ | 0 | 前N月 |
| 19 | fmodifydate | 修改日期 | timestamp | 0 |  |  | null | 修改日期 |
| 20 | fcostaccountid | 成本主体 | int8 | 64 |  | √ | 0 | 成本主体 cal_bd_costaccount |
| 21 | fplancollecttype | 计划数量新增方式 | varchar | 80 |  | √ | ' ' | 计划数量新增方式,枚举: OBJECTRULE :内部系统引入 EXCEL :模板引入 API :API接口 MANUAL :手工录入 |
| 22 | ftab | 所属页签 | varchar | 50 |  | √ | ' ' | 所属页签 |
| 23 | fcostcenterid | 成本中心 | int8 | 64 |  | √ | 0 | 成本中心 bos_costcenter |
| 24 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 25 | feffectcontrol | 有效期控制 | varchar | 255 |  | √ | ' ' | 有效期控制,枚举: |
| 26 | fmatcollectrange | 材料耗用归集的单据范围 | varchar | 255 |  | √ | ' ' | 材料耗用归集的单据范围,枚举: PRO_GET :生产领料单 PRO_FALLBACK :生产退料单 PRO_ADD :生产补料单 GET_OUTSTORAGE :领料出库单 |
| 27 | fcostinitdate | 历史数据初始化日期 | timestamp | 0 |  |  | null | 历史数据初始化日期 |
| 28 | fmatcollectway | 材料耗用归集新增方式 | varchar | 50 |  | √ | ' ' | 材料耗用归集新增方式,枚举: INNERSYSIMPORT :内部系统引入 TPLIMPORT :模板引入 APIINTERFACE :API接口 MANUALENTER :手工录入 |
| 29 | factorgid | 归集时间范围核算组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 30 | frestoredimension | 实际成本还原计算维度 | varchar | 50 |  | √ | 'A' | 实际成本还原计算维度,枚举: A :核算组织 B :核算组织+生产组织 |
| 31 | fresourceusetype | 资源耗用量新增方式 | varchar | 50 |  | √ | 'MANUAL' | 资源耗用量新增方式,枚举: OBJECTRULE :内部系统引入 EXCEL :模板引入 API :API接口 MANUAL :手工录入 |
| 32 | fimporttimescope | 业务单据覆盖引入时间范围 | varchar | 80 |  | √ | ' ' | 业务单据覆盖引入时间范围 |
| 33 | faccountorgid | 归集业务范围组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 34 | frestorecalcrange | 实际成本还原计算范围 | varchar | 50 |  | √ | ' ' | 实际成本还原计算范围,枚举: WIPCOM :完工入库单 TRANSDIRBILL :调拨单 PURINBILL :采购入库单 |
| 35 | fisallupdate | 支持全量更新 | bpchar | 1 |  | √ | '0' | 支持全量更新 |
| 36 | foutsourceprice | 产品委外取价配置 | varchar | 50 |  | √ | ' ' | 产品委外取价配置,枚举: OVERALL :综合结转 ITEMIZED :分项结转 |
| 37 | fismergebill | 成本中心内费用合单分配 | bpchar | 1 |  | √ | '0' | 成本中心内费用合单分配 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | index_sco_sysparam_df |  | faccountorgid,fcostcenterid |
| 2 | pk_sco_sysparam |  | fid |

---

## 采购入库取数范围-多选基础资料表 t_sco_sysparamrsrange

- **表名称：** 采购入库取数范围-多选基础资料表
- **表名：** t_sco_sysparamrsrange

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fbasedataid | fbasedataid | int8 | 64 |  | √ | 0 | 成本主体 cal_bd_costaccount |
| 3 | fpkid | fpkid | int8 | 64 |  | √ | 0 | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_sco_sysparamrsrange_fk |  | fid |
| 2 | pk_sco_sysparamrsrange |  | fpkid |

---

## 生产事务类型-多选基础资料表 t_sco_sysparamtranstype

- **表名称：** 生产事务类型-多选基础资料表
- **表名：** t_sco_sysparamtranstype

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fbasedataid | fbasedataid | int8 | 64 |  | √ | 0 | 生产事务类型 mpdm_transactproduct |
| 3 | fpkid | fpkid | int8 | 64 |  | √ | 0 | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_sco_sysparamtranstype |  | fpkid |
| 2 | idx_sco_sysparamtranstype |  | fid |

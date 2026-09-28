# 成本参数基础资料-cad_sysparam

## 生产单据类型-多选基础资料表 t_cad_sysparamtranstype

- **表名称：** 生产单据类型-多选基础资料表
- **表名：** t_cad_sysparamtranstype

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fbasedataid | fbasedataid | int8 | 64 |  | √ | 0 | [单据类型 bos_billtype](../cts_files/bos_billtype.md) |
| 3 | fpkid | fpkid | int8 | 64 |  | √ | 0 | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_cad_sysparamtranstype |  | fpkid |
| 2 | idx_cad_sysparamtranstype |  | fid |

---

## 成本参数基础资料-主表 t_cad_sysparam

- **表名称：** 成本参数基础资料-主表
- **表名：** t_cad_sysparam

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fbillrange | 参与完工产量归集的单据范围 | varchar | 510 |  | √ | ' ' | 参与完工产量归集的单据范围,枚举: WIPCOMPELETE :完工入库单 WIPCOMPELETEBACK :完工入库退回 PRODUCTCOMPELETE :生产入库单 PRODUCTCOMPELETEBACK :生产入库退回 ARMPRODUCTINBILL :重复生产完工入库单 |
| 3 | fplancollectrange | 参与计划数量归集的单据范围 | varchar | 255 |  |  | 'SCGD' | 参与计划数量归集的单据范围,枚举: SCGD :生产工单 WWGD :委外工单 WGRK :完工产量归集单 |
| 4 | fwarehousepoint | 仅归集入库点资源 | bpchar | 1 |  | √ | '0' | 仅归集入库点资源 |
| 5 | fassistant | 辅助分配方法 | varchar | 30 |  | √ | 'direct' | 辅助分配方法,枚举: direct :直接分配法 mutual :交互分配法 algebra :代数分配法 |
| 6 | fhourexpense | 工时费用维度 | varchar | 255 |  | √ | ' ' | 工时费用维度,枚举: TRADE :行业 ROLE :角色 RESOURCE :资源 |
| 7 | forgid | 成本核算参数中的核算组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 8 | fmfgfeebilltype | 制造费用归集新增方式 | varchar | 255 |  |  | 'MANUAL' | 制造费用归集新增方式,枚举: SYS :内部系统引入 EXCEL :模板引入 API :API接口 MANUAL :手工录入 |
| 9 | fcompletetype | 完工产量新增方式 | varchar | 20 |  | √ | ' ' | 完工产量新增方式,枚举: OBJECTRULE :内部系统引入 EXCEL :模板引入 API :API接口 MANUAL :手工录入 |
| 10 | freductstrategy | 差异分摊策略 | varchar | 50 |  | √ | ' ' | 差异分摊策略,枚举: OVERALL_REDUCT :综合分摊 ITEMIZED_REDUCT :分项分摊 |
| 11 | fispreviousoneton | 引入前N月业务单据 | bpchar | 1 |  | √ | '0' | 引入前N月业务单据 |
| 12 | fappnum | 所属应用 | varchar | 100 |  | √ | ' ' | 所属应用,枚举: sca :标准成本 aca :实际成本 |
| 13 | fisautoupdate | 成本更新单据审核后自动进行【更新确认】单据 | bpchar | 1 |  | √ | '0' | 成本更新单据审核后自动进行【更新确认】单据 |
| 14 | fresourcerange | 参与资源耗用量归集的单据范围 | varchar | 100 |  | √ | 'PROCESSREPORT,PROCESSADJUST,MFTORDERREPORT ' | 参与资源耗用量归集的单据范围,枚举: PROCESSREPORT :工序汇报单 PROCESSADJUST :汇报资源调整单 MFTORDERREPORT :工单汇报单 ARMWORKHOURSREPORT :重复生产工时汇报单 |
| 15 | fisupdatebyperiod | 按期进行成本更新 | bpchar | 1 |  | √ | '0' | 按期进行成本更新 |
| 16 | fnum | 前N月 | int4 | 32 |  | √ | 0 | 前N月 |
| 17 | fmodifydate | 修改日期 | timestamp | 0 |  |  | null | 修改日期 |
| 18 | fcostaccountid | 成本主体 | int8 | 64 |  | √ | 0 | [成本主体 cal_bd_costaccount](../cal_files/cal_bd_costaccount.md) |
| 19 | fplancollecttype | 计划数量新增方式 | varchar | 80 |  |  | 'OBJECTRULE' | 计划数量新增方式,枚举: OBJECTRULE :内部系统引入 EXCEL :模板引入 API :API接口 MANUAL :手工录入 |
| 20 | ftab | 所属页签 | varchar | 50 |  | √ | ' ' | 所属页签 |
| 21 | fcostcenterid | 成本中心 | int8 | 64 |  | √ | 0 | [成本中心 bos_costcenter](../basedata_files/bos_costcenter.md) |
| 22 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 23 | feffectcontrol | 有效期控制 | varchar | 255 |  | √ | ' ' | 有效期控制,枚举: |
| 24 | fmatcollectrange | 材料耗用归集的单据范围 | varchar | 255 |  | √ | ' ' | 材料耗用归集的单据范围,枚举: PRO_GET :生产领料单 PRO_FALLBACK :生产退料单 PRO_ADD :生产补料单 GET_OUTSTORAGE :领料出库单 |
| 25 | fcostinitdate | 历史数据初始化日期 | timestamp | 0 |  |  | null | 历史数据初始化日期 |
| 26 | fmatcollectway | 材料耗用归集新增方式 | varchar | 50 |  | √ | ' ' | 材料耗用归集新增方式,枚举: INNERSYSIMPORT :内部系统引入 TPLIMPORT :模板引入 APIINTERFACE :API接口 MANUALENTER :手工录入 |
| 27 | factorgid | 归集时间范围核算组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 28 | frestoredimension | 实际成本还原计算维度 | varchar | 50 |  | √ | 'A' | 实际成本还原计算维度,枚举: A :核算组织 B :核算组织+生产组织 |
| 29 | fresourceusetype | 资源耗用量新增方式 | varchar | 50 |  | √ | 'MANUAL' | 资源耗用量新增方式,枚举: OBJECTRULE :内部系统引入 EXCEL :模板引入 API :API接口 MANUAL :手工录入 |
| 30 | fimporttimescope | 业务单据覆盖引入时间范围 | varchar | 100 |  | √ | ' ' | 业务单据覆盖引入时间范围 |
| 31 | faccountorgid | 归集业务范围组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 32 | frestorecalcrange | 实际成本还原计算范围 | varchar | 50 |  | √ | ' ' | 实际成本还原计算范围,枚举: WIPCOM :完工入库单 TRANSDIRBILL :调拨单 PURINBILL :采购入库单 |
| 33 | fisallupdate | 支持全量更新 | bpchar | 1 |  | √ | '0' | 支持全量更新 |
| 34 | foutsourceprice | 产品委外取价配置 | varchar | 30 |  | √ | 'ITEMIZED' | 产品委外取价配置,枚举: OVERALL :综合结转 ITEMIZED :分项结转 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_sysparam_orgcosta |  | forgid,fcostaccountid |
| 2 | t_cad_sysparam_pkey |  | fid |
| 3 | index_cad_sysparam_df |  | faccountorgid,fcostcenterid |

---

## 采购入库取数范围-多选基础资料表 t_cad_sysparamrsrange

- **表名称：** 采购入库取数范围-多选基础资料表
- **表名：** t_cad_sysparamrsrange

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fbasedataid | fbasedataid | int8 | 64 |  | √ | 0 | [成本主体 cal_bd_costaccount](../cal_files/cal_bd_costaccount.md) |
| 3 | fpkid | fpkid | int8 | 64 |  | √ | 0 | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_cad_sysparamrsrange |  | fpkid |
| 2 | idx_t_cad_sysparamrsrange |  | fid,fbasedataid |

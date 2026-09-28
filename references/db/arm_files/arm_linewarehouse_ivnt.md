# 线边仓库存管理平台-arm_linewarehouse_ivnt

## 物料库存状态-子表 t_arm_mateinvtstatus

- **表名称：** 物料库存状态-子表
- **表名：** t_arm_mateinvtstatus

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | feusablebaseinvt | 预计可用库存基本数量 | numeric | 23 | 10 |  | null | 预计可用库存基本数量 |
| 3 | flocation | 仓位 | int8 | 64 |  |  | null | [仓位 bd_location](../sbd_files/bd_location.md) |
| 4 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 5 | fstrategy | 默认补料策略 | bpchar | 1 |  | √ | 'A' | 默认补料策略,枚举: A :按再订货点补料 B :按需求补料（截至今日） C :按需求补料（截至明日） |
| 6 | fbaseunit | 基本单位 | int8 | 64 |  |  | null | [计量单位 bd_measureunits](../base_files/bd_measureunits.md) |
| 7 | fdefaultoutorg | 默认调出组织 | int8 | 64 |  |  | null | [业务单元 bos_org](../base_files/bos_org.md) |
| 8 | fbonded | 保税 | bpchar | 1 |  | √ | '0' | 保税 |
| 9 | fstatus | 状态 | varchar | 50 |  | √ | ' ' | 状态,枚举: 0 :低于再订货点且低于需求 3 :低于再订货点但高于需求 1 :高于再订货点但低于需求 2 :正常 |
| 10 | ftodayreqbaseqty | 今日订单需求基本数量 | numeric | 23 | 10 |  | null | 今日订单需求基本数量 |
| 11 | freorderpoint | 再订货点 | numeric | 23 | 10 |  | null | 再订货点 |
| 12 | fprocessinventory | 在途库存 | numeric | 23 | 10 |  | null | 在途库存 |
| 13 | fownertype | 货主类型 | varchar | 50 |  | √ | ' ' | 货主类型,枚举: bos_org :业务组织 bd_supplier :供应商 |
| 14 | fmaterial | 物料编码 | int8 | 64 |  |  | null | [物料库存信息 bd_materialinventoryinfo](../sbd_files/bd_materialinventoryinfo.md) |
| 15 | fstardreordernum | 标准订货数量 | numeric | 23 | 10 |  | null | 标准订货数量 |
| 16 | fdefaultoutlocation | 默认调出仓位 | int8 | 64 |  |  | null | [仓位 bd_location](../sbd_files/bd_location.md) |
| 17 | fcompauxpty | 辅助属性 | int8 | 64 |  |  | null | null 001 |
| 18 | festimateusableinvt | 预计可用库存 | numeric | 23 | 10 |  | null | 预计可用库存 |
| 19 | factualreordernum | 实际订货数量 | numeric | 23 | 10 |  | null | 实际订货数量 |
| 20 | fprepamatermode | 默认调拨类型 | varchar | 50 |  | √ | ' ' | 默认调拨类型,枚举: 0 :组织内调拨 1 :跨组织调拨 2 :仓位移动单 3 :VMI组织内调拨 4 :VMI跨组织调拨 |
| 21 | factualbasenum | 实际订货基本数量 | numeric | 23 | 10 | √ | 0 | 实际订货基本数量 |
| 22 | fcompunitid | 库存单位 | int8 | 64 |  |  | null | [计量单位 bd_measureunits](../base_files/bd_measureunits.md) |
| 23 | fmodifierfield | 修改人 | int8 | 64 |  |  | null | [人员 bos_user](../base_files/bos_user.md) |
| 24 | fdefaultoutware | 默认调出仓库 | int8 | 64 |  |  | null | [仓库 bd_warehouse](../sbd_files/bd_warehouse.md) |
| 25 | fcompversion | 物料版本 | int8 | 64 |  |  | null | [物料版本 bd_bomversion_new](../basedata_files/bd_bomversion_new.md) |
| 26 | fwarehouse | 仓库 | int8 | 64 |  |  | null | [仓库 bd_warehouse](../sbd_files/bd_warehouse.md) |
| 27 | fusableinvt | 可用库存 | numeric | 23 | 10 |  | null | 可用库存 |
| 28 | fmaterialmasterid | 物料业务策略主内码 | int8 | 64 |  | √ | 0 | 物料业务策略主内码 |
| 29 | fmodifydatefield | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 30 | ftodayrequiredqty | 今日订单需求数量 | numeric | 23 | 10 |  | null | 今日订单需求数量 |
| 31 | fusableinvtbasenum | 可用库存基本数量 | numeric | 23 | 10 |  | null | 可用库存基本数量 |
| 32 | ffollowrequiredqty | 明日订单需求数量 | numeric | 23 | 10 |  | null | 明日订单需求数量 |
| 33 | fprocessbaseinvt | 在途库存基本数量 | numeric | 23 | 10 |  | null | 在途库存基本数量 |
| 34 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 35 | fforeqbaseqty | 明日订单需求基本数量 | numeric | 23 | 10 |  | null | 明日订单需求基本数量 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_t_arm_mate_invtstatus |  | fid |
| 2 | pk_t_arm_mateinvtstatus |  | fentryid |

---

## 线边仓库存管理平台-主表 t_arm_linewareinventory

- **表名称：** 线边仓库存管理平台-主表
- **表名：** t_arm_linewareinventory

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fmodifierid | 修改人 | int8 | 64 |  |  | null | [人员 bos_user](../base_files/bos_user.md) |
| 3 | fcreatorid | 创建人 | int8 | 64 |  |  | null | [人员 bos_user](../base_files/bos_user.md) |
| 4 | flinestoreid | 线边仓库 | int8 | 64 |  |  | null | [仓库 bd_warehouse](../sbd_files/bd_warehouse.md) |
| 5 | fbillstatus | 单据状态 | varchar | 50 |  | √ | ' ' | 单据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 6 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 7 | forgid | 生产组织 | int8 | 64 |  |  | null | [业务单元 bos_org](../base_files/bos_org.md) |
| 8 | fauditdate | 审核日期 | timestamp | 0 |  |  | null | 审核日期 |
| 9 | fbillno | 单据编号 | varchar | 30 |  | √ | ' ' | 单据编号 |
| 10 | fauditorid | 审核人 | int8 | 64 |  |  | null | [人员 bos_user](../base_files/bos_user.md) |
| 11 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_t_arm_lnwr_ivnt |  | fbillno,fid |
| 2 | pk_t_arm_linewareinventory |  | fid |

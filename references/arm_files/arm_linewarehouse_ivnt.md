# 线边仓库存管理平台-arm_linewarehouse_ivnt

## 物料库存状态-子表 t_arm_mateinvtstatus

- **表名称：** 物料库存状态-子表
- **表名：** t_arm_mateinvtstatus

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | feusablebaseinvt | 预计可用库存基本数量 | numeric | 23 | 10 |  | null | 预计可用库存基本数量 |
| 3 | flocation | 仓位 | int8 | 64 |  |  | null | 仓位 bd_location |
| 4 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 5 | fbaseunit | 基本单位 | int8 | 64 |  |  | null | 计量单位 bd_measureunits |
| 6 | fdefaultoutorg | 默认调出组织 | int8 | 64 |  |  | null | 业务单元 bos_org |
| 7 | fstatus | 状态 | varchar | 50 |  | √ | ' ' | 状态,枚举: 0 :低于再订货点 1 :正常但低于需求数 2 :正常 |
| 8 | ftodayreqbaseqty | 今日订单需求基本数量 | numeric | 23 | 10 |  | null | 今日订单需求基本数量 |
| 9 | freorderpoint | 再订货点 | numeric | 23 | 10 |  | null | 再订货点 |
| 10 | fprocessinventory | 在途库存 | numeric | 23 | 10 |  | null | 在途库存 |
| 11 | fmaterial | 物料编码 | int8 | 64 |  |  | null | 物料库存信息 bd_materialinventoryinfo |
| 12 | fstardreordernum | 标准订货数量 | numeric | 23 | 10 |  | null | 标准订货数量 |
| 13 | fdefaultoutlocation | 默认调出仓位 | int8 | 64 |  |  | null | 仓位 bd_location |
| 14 | fcompauxpty | 辅助属性 | int8 | 64 |  |  | null | null 001 |
| 15 | festimateusableinvt | 预计可用库存 | numeric | 23 | 10 |  | null | 预计可用库存 |
| 16 | factualreordernum | 实际订货数量 | numeric | 23 | 10 |  | null | 实际订货数量 |
| 17 | fprepamatermode | 备料方式 | varchar | 50 |  | √ | ' ' | 备料方式,枚举: 0 :组织内调拨 1 :跨组织调拨 2 :仓位移动单 |
| 18 | factualbasenum | 实际订货基本数量 | numeric | 23 | 10 | √ | 0 | 实际订货基本数量 |
| 19 | fcompunitid | 库存单位 | int8 | 64 |  |  | null | 计量单位 bd_measureunits |
| 20 | fmodifierfield | 修改人 | int8 | 64 |  |  | null | 人员 bos_user |
| 21 | fdefaultoutware | 默认调出仓库 | int8 | 64 |  |  | null | 仓库 bd_warehouse |
| 22 | fcompversion | 物料版本 | int8 | 64 |  |  | null | 物料版本 bd_bomversion_new |
| 23 | fwarehouse | 仓库 | int8 | 64 |  |  | null | 仓库 bd_warehouse |
| 24 | fusableinvt | 可用库存 | numeric | 23 | 10 |  | null | 可用库存 |
| 25 | fmodifydatefield | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 26 | ftodayrequiredqty | 今日订单需求数量 | numeric | 23 | 10 |  | null | 今日订单需求数量 |
| 27 | fusableinvtbasenum | 可用库存基本数量 | numeric | 23 | 10 |  | null | 可用库存基本数量 |
| 28 | ffollowrequiredqty | 明日订单需求数量 | numeric | 23 | 10 |  | null | 明日订单需求数量 |
| 29 | fprocessbaseinvt | 在途库存基本数量 | numeric | 23 | 10 |  | null | 在途库存基本数量 |
| 30 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 31 | fforeqbaseqty | 明日订单需求基本数量 | numeric | 23 | 10 |  | null | 明日订单需求基本数量 |

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
| 2 | fmodifierid | 修改人 | int8 | 64 |  |  | null | 人员 bos_user |
| 3 | fcreatorid | 创建人 | int8 | 64 |  |  | null | 人员 bos_user |
| 4 | flinestoreid | 线边仓库 | int8 | 64 |  |  | null | 仓库 bd_warehouse |
| 5 | fbillstatus | 单据状态 | varchar | 50 |  | √ | ' ' | 单据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 6 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 7 | forgid | 生产组织 | int8 | 64 |  |  | null | 业务单元 bos_org |
| 8 | fauditdate | 审核日期 | timestamp | 0 |  |  | null | 审核日期 |
| 9 | fbillno | 单据编号 | varchar | 30 |  | √ | ' ' | 单据编号 |
| 10 | fauditorid | 审核人 | int8 | 64 |  |  | null | 人员 bos_user |
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

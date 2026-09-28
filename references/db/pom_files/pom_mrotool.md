# 检修工具清单-pom_mrotool

## 检修工具清单-主表 t_pom_mrotool

- **表名称：** 检修工具清单-主表
- **表名：** t_pom_mrotool

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fmodel | fmodel | varchar | 50 |  | √ | ' ' |  |
| 3 | fmaterialid | 产品编码 | int8 | 64 |  | √ | 0 | 物料生产信息 bd_materialmftinfo |
| 4 | forgid | 生产组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 5 | forderid | 检修工单ID | varchar | 50 |  | √ | ' ' | 检修工单ID |
| 6 | forderidnew | 检修工单主id | int8 | 64 |  | √ | 0 | 检修工单主id |
| 7 | fremarks | 备注 | varchar | 255 |  | √ | ' ' | 备注 |
| 8 | fworkcardid | 工卡号 | int8 | 64 |  | √ | 0 | 工卡 mpdm_mrocardroute |
| 9 | forderbizstatus | forderbizstatus | varchar | 50 |  | √ | ' ' |  |
| 10 | forderpickstatus | forderpickstatus | varchar | 50 |  | √ | ' ' |  |
| 11 | forderentryid | 检修工单行号 | int8 | 64 |  | √ | 0 | 检修工单分录F7 pom_mroorder_f7 |
| 12 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 13 | fauxproperty | 辅助属性 | int8 | 64 |  | √ | 0 | null 001 |
| 14 | fcardversion | fcardversion | varchar | 50 |  | √ | ' ' |  |
| 15 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 16 | forderstatus | 检修工单状态 | varchar | 50 |  | √ | ' ' | 检修工单状态 |
| 17 | fordertaskstatus | fordertaskstatus | varchar | 50 |  | √ | ' ' |  |
| 18 | fbaseunitid | 基本单位 | int8 | 64 |  | √ | 0 | 计量单位 bd_measureunits |
| 19 | fbillno | 单据编号 | varchar | 50 |  | √ | ' ' | 单据编号 |
| 20 | ftransactiontypeid | 生产事务类型 | int8 | 64 |  | √ | 0 | 生产事务类型 mpdm_transactproduct |
| 21 | fqty | 数量 | numeric | 23 | 10 | √ | 0 | 数量 |
| 22 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 23 | forderseq | forderseq | varchar | 50 |  | √ | ' ' |  |
| 24 | fcustomer | 客户 | int8 | 64 |  | √ | 0 | 客户 bd_customer |
| 25 | fprojectid | 项目 | int8 | 64 |  | √ | 0 | 项目 pmpd_project |
| 26 | fbillstatus | 单据状态 | varchar | 50 |  | √ | ' ' | 单据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 27 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 28 | funitid | 计量单位 | int8 | 64 |  | √ | 0 | 计量单位 bd_measureunits |
| 29 | fproductmasterid | 产品(主数据) | int8 | 64 |  | √ | 0 | 物料 bd_material |
| 30 | fauditdate | 审核日期 | timestamp | 0 |  |  | null | 审核日期 |
| 31 | fmftdeptorgid | 生产部门 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 32 | forderplanstatus | forderplanstatus | varchar | 50 |  | √ | ' ' |  |
| 33 | forderno | 检修工单编号 | varchar | 50 |  | √ | ' ' | 检修工单编号 |
| 34 | fworkcenter | fworkcenter | varchar | 50 |  | √ | ' ' |  |
| 35 | fsourcebillid | 来源单据id | int8 | 64 |  | √ | 0 | 来源单据id |
| 36 | fbaseqty | 基本数量 | numeric | 23 | 10 | √ | 0 | 基本数量 |
| 37 | fauditorid | 审核人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 38 | fbilltype | 单据类型 | int8 | 64 |  | √ | 0 | 单据类型 bos_billtype |
| 39 | fproductname | fproductname | varchar | 50 |  | √ | ' ' |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_pom_mrotool_forderid |  | forderid |
| 2 | idx_pom_mrotool_forderentryid |  | forderentryid |
| 3 | pk_pom_mrotool |  | fid |
| 4 | idx_pom_mrotool_fsourcebillid |  | fsourcebillid |

---

## 关联子实体-子表 t_pom_mrotoolentry_lk

- **表名称：** 关联子实体-子表
- **表名：** t_pom_mrotoolentry_lk

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fsbillid | 源单内码 | int8 | 64 |  |  | null | 源单内码 |
| 2 | fstableid | 源单主实体编码 | int8 | 64 |  |  | null | 源单主实体编码 |
| 3 | fsid | 源单主实体内码 | int8 | 64 |  |  | null | 源单主实体内码 |
| 4 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 5 | fentryid | fentryid | int8 | 64 |  | √ | null |  |
| 6 | fpkid | fpkid | int8 | 64 |  | √ | null | id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_pom_mrotoolentry_lk |  | fpkid |
| 2 | idx_pom_mrotoolentry_lk_fk |  | fentryid |

---

## 工具明细-子表 t_pom_mrotoolentry

- **表名称：** 工具明细-子表
- **表名：** t_pom_mrotoolentry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | foutqty | 下推工具申请基本数量 | numeric | 23 | 10 | √ | 0 | 下推工具申请基本数量 |
| 3 | ffentryreplacegroup | 替代组 | varchar | 100 |  | √ | ' ' | 替代组 |
| 4 | flocation | 供货仓位 | int8 | 64 |  | √ | 0 | 仓位 bd_location |
| 5 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 6 | fwarehouseid | 供货仓库 | int8 | 64 |  | √ | 0 | 仓库 bd_warehouse |
| 7 | fmaterielmasterid | 工具件号 | int8 | 64 |  | √ | 0 | 物料 bd_material |
| 8 | fsupplierid | 货主 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 9 | fbegintime | 开始使用时间 | timestamp | 0 |  |  | null | 开始使用时间 |
| 10 | fmustselect | 必选 | bpchar | 1 |  | √ | '0' | 必选 |
| 11 | fsupplymode | 货主类型 | varchar | 50 |  | √ | ' ' | 货主类型,枚举: bos_org :业务单元 bd_customer :客户 bd_supplier :供应商 |
| 12 | fentrylevel | 优先级 | int8 | 64 |  | √ | 0 | 优先级 |
| 13 | fisbomextend | 来源于BOM展开 | bpchar | 1 |  | √ | '0' | 来源于BOM展开 |
| 14 | fmaterialunitid | 基本单位 | int8 | 64 |  | √ | 0 | 计量单位 bd_measureunits |
| 15 | factissueqty | 领用基本数量 | numeric | 23 | 10 | √ | 0 | 领用基本数量 |
| 16 | fdemandqty | 需求基本数量 | numeric | 23 | 10 | √ | 0 | 需求基本数量 |
| 17 | fentryremark | 备注 | varchar | 255 |  | √ | ' ' | 备注 |
| 18 | fmeanstype | 工具分类 | int8 | 64 |  | √ | 0 | 树形基础资料模板 mpdm_meanstype |
| 19 | fendtime | 结束使用时间 | timestamp | 0 |  |  | null | 结束使用时间 |
| 20 | fstocksource | 工具来源 | varchar | 50 |  | √ | ' ' | 工具来源,枚举: A :手工新增 B :工卡工具需求 |
| 21 | fsupplyorgid | 供货库存组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 22 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 23 | fusetime | 使用时长(小时) | numeric | 23 | 10 | √ | 0 | 使用时长(小时) |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_mrotoolentry_fmasterid |  | fmaterielmasterid |
| 2 | pk_pom_mrotoolentry |  | fentryid |

---

## 检修工具清单-反写记录表 t_pom_mrotool_wb

- **表名称：** 检修工具清单-反写记录表
- **表名：** t_pom_mrotool_wb

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | null |  |
| 2 | foperate | foperate | varchar | 50 |  | √ | ' ' |  |
| 3 | fruleverid | fruleverid | int8 | 64 |  |  | null |  |
| 4 | fsbillid | fsbillid | int8 | 64 |  |  | null |  |
| 5 | fstableid | fstableid | int8 | 64 |  |  | null |  |
| 6 | fsid | fsid | int8 | 64 |  |  | null |  |
| 7 | fwritevalue | fwritevalue | numeric | 23 | 10 |  | null |  |
| 8 | fseq | fseq | int4 | 32 |  | √ | 0 |  |
| 9 | fentryid | fentryid | int8 | 64 |  | √ | null |  |
| 10 | fruleitemid | fruleitemid | int8 | 64 |  |  | null |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_pom_mrotool_wb_fk |  | fid |
| 2 | pk_pom_mrotool_wb |  | fentryid |

---

## 检修工具清单-关联追踪表 t_pom_mrotool_tc

- **表名称：** 检修工具清单-关联追踪表
- **表名：** t_pom_mrotool_tc

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | null |  |
| 2 | ftbillid | ftbillid | int8 | 64 |  |  | null |  |
| 3 | fttableid | fttableid | int8 | 64 |  |  | null |  |
| 4 | fsbillid | fsbillid | int8 | 64 |  |  | null |  |
| 5 | fstableid | fstableid | int8 | 64 |  |  | null |  |
| 6 | fsid | fsid | int8 | 64 |  |  | null |  |
| 7 | ftid | ftid | int8 | 64 |  |  | null |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_pom_mrotool_tc_tid |  | ftid |
| 2 | pk_pom_mrotool_tc |  | fid |
| 3 | idx_pom_mrotool_tc_tbill |  | ftbillid |

---

## 关联子实体-子表 t_pom_mrotool_lk

- **表名称：** 关联子实体-子表
- **表名：** t_pom_mrotool_lk

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | null |  |
| 2 | fsbillid | 源单内码 | int8 | 64 |  |  | null | 源单内码 |
| 3 | fstableid | 源单主实体编码 | int8 | 64 |  |  | null | 源单主实体编码 |
| 4 | fsid | 源单主实体内码 | int8 | 64 |  |  | null | 源单主实体内码 |
| 5 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 6 | fpkid | fpkid | int8 | 64 |  | √ | null | id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_pom_mrotool_lk_fk |  | fid |
| 2 | pk_pom_mrotool_lk |  | fpkid |

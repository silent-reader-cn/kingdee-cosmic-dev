# 日生产计划待排表定义-mds_dpsarrangeset

## 库存状态-子表 t_mds_dspstockstatus

- **表名称：** 库存状态-子表
- **表名：** t_mds_dspstockstatus

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fstockstatusflag | 参与计算标识 | bpchar | 1 |  | √ | '0' | 参与计算标识 |
| 3 | fstockstatusld | 编码 | int8 | 64 |  | √ | 0 | [库存状态 bd_invstatus](../sbd_files/bd_invstatus.md) |
| 4 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 5 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_mds_dspstockstatus_fid |  | fid |
| 2 | pk_mds_dspstockstatus |  | fentryid |

---

## 发货设置单据体-子表 t_mds_dspdelivery

- **表名称：** 发货设置单据体-子表
- **表名：** t_mds_dspdelivery

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fbiztype | 业务类型 | int8 | 64 |  | √ | 0 | [业务类型 bd_biztype](../sbd_files/bd_biztype.md) |
| 3 | ftranstype | 调拨类型 | varchar | 5 |  | √ | ' ' | 调拨类型,枚举: A :组织内调拨 B :跨组织调拨 |
| 4 | finvscheme | 库存事务 | int8 | 64 |  | √ | 0 | [库存事务 im_invscheme](../im_files/im_invscheme.md) |
| 5 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 6 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 7 | fbilltype | 源单据类型 | varchar | 5 |  | √ | ' ' | 源单据类型,枚举: 0 :销售出库单 1 :其他出库单 2 :领料出库单 3 :分步调出单 4 :直接调拨单 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_mds_dspdelivery_fid |  | fid |
| 2 | pk_mds_dspdelivery |  | fentryid |

---

## 仓库设置单据体-子表 t_mds_dspstockset

- **表名称：** 仓库设置单据体-子表
- **表名：** t_mds_dspstockset

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fstocknumberid | 仓库编码 | int8 | 64 |  | √ | 0 | [仓库 bd_warehouse](../sbd_files/bd_warehouse.md) |
| 3 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 4 | fstockindexld | 仓位 | int8 | 64 |  | √ | 0 | [仓位 bd_location](../sbd_files/bd_location.md) |
| 5 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 6 | fstockorgld | 库存组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_mds_dspstockset_fid |  | fid |
| 2 | pk_mds_dspstockset |  | fentryid |

---

## 日生产计划待排表定义-多语言表 t_mds_dpsvrdsset_l

- **表名称：** 日生产计划待排表定义-多语言表
- **表名：** t_mds_dpsvrdsset_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fname | 名称 | varchar | 100 |  | √ | ' ' | 名称 |
| 3 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 4 | fpkid | fpkid | varchar | 36 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_mds_dpsvrdsset_l |  | fid,flocaleid |
| 2 | pk_t_mds_dpsvrdsset_l |  | fpkid |

---

## 日生产计划待排表定义-使用范围位图表 t_mds_dpsvrdsset_m

- **表名称：** 日生产计划待排表定义-使用范围位图表
- **表名：** t_mds_dpsvrdsset_m

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | forgid | forgid | int8 | 64 |  | √ | null |  |
| 2 | fdata | fdata | bytea | 0 |  | √ | null |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | forgid | forgid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_mds_dpsvrdsset_m |  | forgid |

---

## 日生产计划待排表定义-使用范围表 t_mds_dpsvrdsset_u

- **表名称：** 日生产计划待排表定义-使用范围表
- **表名：** t_mds_dpsvrdsset_u

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fcreateorgid | fcreateorgid | int8 | 64 |  |  | null |  |
| 2 | fdataid | fdataid | int8 | 64 |  | √ | null |  |
| 3 | fuseorgid | fuseorgid | int8 | 64 |  | √ | null |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fdataid | fdataid,fuseorgid |
| 2 | fuseorgid | fdataid,fuseorgid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_t_mds_dpsvrdsset_u_uo |  | fuseorgid |
| 2 | pk_t_mds_dpsvrdsset_u |  | fdataid,fuseorgid |

---

## 工单设置单据体-子表 t_mds_dspworkorder

- **表名称：** 工单设置单据体-子表
- **表名：** t_mds_dspworkorder

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | ftransactproductid | 生产事务类型编码 | int8 | 64 |  | √ | 0 | [生产事务类型 mpdm_transactproduct](../mpdm_files/mpdm_transactproduct.md) |
| 3 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 4 | forderuseorg | 使用组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 5 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_mds_dspworkorder |  | fentryid |
| 2 | idx_mds_dspworkorder_fid |  | fid |

---

## 日生产计划待排表定义-主表 t_mds_dpsvrdsset

- **表名称：** 日生产计划待排表定义-主表
- **表名：** t_mds_dpsvrdsset

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fdpsstatuscheckbox | 日生产计划确认状态 | bpchar | 1 |  | √ | '0' | 日生产计划确认状态 |
| 3 | fproductfamily | 产品族 | bpchar | 1 |  | √ | '0' | 产品族 |
| 4 | fdetailmsg | 详细信息 | varchar | 2000 |  | √ | ' ' | 详细信息 |
| 5 | forgid | 组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 6 | fsopvrds | 预测计划版本 | int8 | 64 |  | √ | 0 | [版本定义 mds_vrds](../mds_files/mds_vrds.md) |
| 7 | fresult | 运行结果 | varchar | 50 |  | √ | ' ' | 运行结果 |
| 8 | fsrccreateorgid | 原创建组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 9 | ftransfer | 实体映射 | int8 | 64 |  | √ | 0 | [实体字段映射 mrp_billfieldtransfer](../msplan_files/mrp_billfieldtransfer.md) |
| 10 | fstockradiogroup | 库存设置单选按钮 | varchar | 5 |  | √ | ' ' | 库存设置单选按钮,枚举: 4 :全部仓库 5 :参与计算仓库 6 :不参与计算仓库 |
| 11 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 12 | fstatus | 数据状态 | varchar | 80 |  | √ | ' ' | 数据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 13 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 14 | fmasterid | 主数据内码 | int8 | 64 |  | √ | 0 | 主数据内码 |
| 15 | fsourcedataid | 原资料id | int8 | 64 |  | √ | 0 | 原资料id |
| 16 | fbitindex | 位图 | int4 | 32 |  | √ | 0 | 位图 |
| 17 | fcytype | 周期类型 | varchar | 30 |  | √ | ' ' | 周期类型,枚举: 1 :周 |
| 18 | fcreateorgid | 创建组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 19 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 20 | fdeliveryradiogroup | 发货设置单选按钮 | varchar | 5 |  | √ | ' ' | 发货设置单选按钮,枚举: 1 :全部参与 2 :参与计算 3 :不参与计算 |
| 21 | fsopstatuscheckbox | 预测计划确认状态 | bpchar | 1 |  | √ | ' ' | 预测计划确认状态 |
| 22 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 23 | fvrds | 日生产计划版本 | int8 | 64 |  | √ | 0 | [版本定义 mds_vrds](../mds_files/mds_vrds.md) |
| 24 | fstarttime | 开始时间 | timestamp | 0 |  |  | null | 开始时间 |
| 25 | fctrlstrategy | 控制策略 | varchar | 80 |  | √ | ' ' | 控制策略,枚举: 2 :分配/局部共享 5 :全局共享 7 :私有 |
| 26 | fweeknum | 期数 | int8 | 64 |  | √ | 0 | 期数 |
| 27 | fenable | 使用状态 | varchar | 80 |  | √ | ' ' | 使用状态,枚举: 0 :禁用 1 :可用 |
| 28 | fnumber | 编码 | varchar | 80 |  | √ | ' ' | 编码 |
| 29 | fendtime | 结束时间 | timestamp | 0 |  |  | null | 结束时间 |
| 30 | fworkorderradiogroup | 工单设置单选按钮组 | varchar | 5 |  | √ | ' ' | 工单设置单选按钮组,枚举: 7 :全部生产事务类型 8 :参与计算生产事物类型 9 :不参与计算生产事物类型 |
| 31 | fisfault | 默认 | bpchar | 1 |  | √ | '0' | 默认 |
| 32 | fsourcebitindex | 原资料位图 | int4 | 32 |  | √ | 0 | 原资料位图 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_mds_dpsvrdsset |  | fid |
| 2 | idx_mds_dpsvrdsset |  | fnumber |
| 3 | idx_t_mds_dpsvrdsset_createorg |  | fcreateorgid |
| 4 | idx_t_mds_dpsvrdsset_master |  | fmasterid |

---

## 库存类型-子表 t_mds_dspstocktype

- **表名称：** 库存类型-子表
- **表名：** t_mds_dspstocktype

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fstocktypeld | 编码 | int8 | 64 |  | √ | 0 | [库存类型 bd_invtype](../sbd_files/bd_invtype.md) |
| 3 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 4 | fstocktypeflag | 参与计算标识 | bpchar | 1 |  | √ | '0' | 参与计算标识 |
| 5 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_mds_dspstocktype |  | fentryid |
| 2 | idx_mds_dspstocktype_fid |  | fid |

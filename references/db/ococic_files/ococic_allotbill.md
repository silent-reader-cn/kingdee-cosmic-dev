# 可销量分配单-ococic_allotbill

## 分配单子单体-子表 t_ococic_allotsubentry

- **表名称：** 分配单子单体-子表
- **表名：** t_ococic_allotsubentry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 2 | fdetailid | fdetailid | int8 | 64 |  | √ | 0 | id |
| 3 | fchannelid | 渠道 | int8 | 64 |  | √ | 0 | [渠道 ocdbd_channel](../ocdbd_files/ocdbd_channel.md) |
| 4 | fentryid | fentryid | int8 | 64 |  | √ | 0 |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fdetailid | fdetailid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_ococic_allotsubentry |  | fdetailid |
| 2 | idx_ococic_allotsubentry_eid |  | fentryid |

---

## 分配单单据体-子表 t_ococic_allotentry

- **表名称：** 分配单单据体-子表
- **表名：** t_ococic_allotentry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fskey | 分配源唯一标识 | varchar | 50 |  | √ | ' ' | 分配源唯一标识 |
| 3 | fpkey | 分配明细唯一标示 | varchar | 50 |  | √ | ' ' | 分配明细唯一标示 |
| 4 | fmaterialid | 物料 | int8 | 64 |  | √ | 0 | [物料 bd_material](../basedata_files/bd_material.md) |
| 5 | fauxptyid | 辅助属性 | int8 | 64 |  | √ | 0 | null 001 |
| 6 | finvbaseqty | 可用基本数量 | numeric | 23 | 10 | √ | 0 | 可用基本数量 |
| 7 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 8 | fckey | 渠道范围标识 | varchar | 50 |  | √ | ' ' | 渠道范围标识 |
| 9 | fwarehouseid | 仓库 | int8 | 64 |  | √ | 0 | [仓库 bd_warehouse](../sbd_files/bd_warehouse.md) |
| 10 | fitemid | 商品 | int8 | 64 |  | √ | 0 | [商品信息 ocdbd_iteminfo](../ocdbd_files/ocdbd_iteminfo.md) |
| 11 | fallottype | 共享/独享 | bpchar | 1 |  | √ | ' ' | 共享/独享,枚举: A :共享 B :独享 |
| 12 | fcalculatetype | 计算方式 | bpchar | 1 |  | √ | ' ' | 计算方式,枚举: A :按比例 B :按数量 |
| 13 | fsumbaseqty | 已分配基本数量 | numeric | 23 | 10 | √ | 0 | 已分配基本数量 |
| 14 | fallotbaseqty | 可分配基本数量 | numeric | 23 | 10 | √ | 0 | 可分配基本数量 |
| 15 | fbaseunitid | 基本单位 | int8 | 64 |  | √ | 0 | [计量单位 bd_measureunits](../base_files/bd_measureunits.md) |
| 16 | fbaseqty | 分配基本数量 | numeric | 23 | 10 | √ | 0 | 分配基本数量 |
| 17 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 18 | fstockorgid | 库存组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 19 | fpercent | 分配比例% | int4 | 32 |  | √ | 0 | 分配比例% |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_ococic_allotentry |  | fentryid |
| 2 | idx_ococic_allotentry_fid |  | fid |

---

## 可销量分配单-主表 t_ococic_allotbill

- **表名称：** 可销量分配单-主表
- **表名：** t_ococic_allotbill

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 3 | fupdatetype | 更新方式 | bpchar | 1 |  | √ | ' ' | 更新方式,枚举: A :累加并新增 B :更新并新增 |
| 4 | fbillstatus | 单据状态 | bpchar | 1 |  | √ | ' ' | 单据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 5 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 6 | forgid | 创建组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 7 | finvalidendtime | 失效时间 | timestamp | 0 |  |  | null | 失效时间 |
| 8 | fauditdate | 审核日期 | timestamp | 0 |  |  | null | 审核日期 |
| 9 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 10 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 11 | finvalidbegintime | 生效时间 | timestamp | 0 |  |  | null | 生效时间 |
| 12 | fbillno | 单据编号 | varchar | 80 |  | √ | ' ' | 单据编号 |
| 13 | fauditorid | 审核人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_ococic_allotbill |  | fid |
| 2 | idx_ococic_allotbill_no |  | fbillno |

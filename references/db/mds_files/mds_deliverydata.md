# 发货记录表-mds_deliverydata

## 发货记录表-主表 t_mds_deliverydata

- **表名称：** 发货记录表-主表
- **表名：** t_mds_deliverydata

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fqty | 数量 | numeric | 23 | 10 | √ | 0 | 数量 |
| 3 | fname | 名称 | varchar | 100 |  | √ | ' ' | 名称 |
| 4 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 5 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 6 | fdeliverydate | 发货日期 | timestamp | 0 |  |  | null | 发货日期 |
| 7 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 8 | fstatus | 数据状态 | varchar | 5 |  | √ | ' ' | 数据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 9 | frundate | 运算时间 | timestamp | 0 |  |  | null | 运算时间 |
| 10 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 11 | fmasterid | 主数据内码 | int8 | 64 |  | √ | 0 | 主数据内码 |
| 12 | fdeliveryquerysetid | 发货查询方案 | int8 | 64 |  | √ | 0 | 发货查询方案 mds_deliveryqueryset |
| 13 | fenable | 使用状态 | varchar | 5 |  | √ | ' ' | 使用状态,枚举: 0 :禁用 1 :可用 |
| 14 | fstockorg | 库存组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 15 | fnumber | 编码 | varchar | 80 |  | √ | ' ' | 编码 |
| 16 | fdeliverytype | 发货类型 | varchar | 5 |  | √ | ' ' | 发货类型,枚举: 0 :销售出库 1 :生产领料 2 :其他出库 3 :直接调拨 4 :分步调拨 |
| 17 | fmateriel | 物料 | int8 | 64 |  | √ | 0 | 物料 bd_material |
| 18 | funit | 计量单位 | int8 | 64 |  | √ | 0 | 计量单位 bd_measureunits |
| 19 | fbilltype | 单据类型 | varchar | 36 |  | √ | ' ' | 主实体对象 bos_entityobject |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_mds_deliverydata |  | fid |
| 2 | idx_mds_deliverydata_m |  | fmateriel |

---

## 发货记录表-多语言表 t_mds_deliverydata_l

- **表名称：** 发货记录表-多语言表
- **表名：** t_mds_deliverydata_l

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
| 1 | idx_mds_deliverydata_l_fid |  | fid,flocaleid |
| 2 | pk_mds_deliverydata_l |  | fpkid |

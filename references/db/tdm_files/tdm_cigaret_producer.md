# 生产企业卷烟销售明细表-tdm_cigaret_producer

## 生产企业卷烟销售明细表-主表 t_tdm_cigaret_producer

- **表名称：** 生产企业卷烟销售明细表-主表
- **表名：** t_tdm_cigaret_producer

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | ftaxperiod | 所属税期 | timestamp | 0 |  |  | null | 所属税期 |
| 3 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 4 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 5 | forgid | 税务组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 6 | ftaxprice | ftaxprice | numeric | 23 | 10 | √ | 0.0000000000 |  |
| 7 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 8 | fbarcode | 卷烟条包装商品条码 | varchar | 50 |  | √ | ' ' | 卷烟条包装商品条码 |
| 9 | fstatus | 数据状态 | varchar | 50 |  | √ | ' ' | 数据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 10 | fsaleprice | 销售价格 | numeric | 23 | 10 | √ | 0.0000000000 | 销售价格 |
| 11 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 12 | fmasterid | 主数据内码 | int8 | 64 |  | √ | 0 | 主数据内码 |
| 13 | fpackagespecification | 烟支包装规格 | varchar | 50 |  | √ | ' ' | 烟支包装规格 |
| 14 | ftype | ftype | varchar | 50 |  | √ | ' ' |  |
| 15 | ftransfertype | 调拨类型 | varchar | 50 |  | √ | ' ' | 调拨类型 |
| 16 | factualsales | factualsales | numeric | 23 | 10 | √ | 0.0000000000 |  |
| 17 | fsalequantity | 销售数量 | numeric | 23 | 10 | √ | 0.0000000000 | 销售数量 |
| 18 | ftaxsales | ftaxsales | numeric | 23 | 10 | √ | 0.0000000000 |  |
| 19 | fbrandspecification | 卷烟牌号规格 | varchar | 50 |  | √ | ' ' | 卷烟牌号规格 |
| 20 | fenable | 使用状态 | varchar | 50 |  | √ | ' ' | 使用状态,枚举: 0 :禁用 1 :可用 |
| 21 | ftransferprice | ftransferprice | numeric | 23 | 10 | √ | 0.0000000000 |  |
| 22 | fnumber | 物料编码 | varchar | 30 |  | √ | ' ' | 物料编码 |
| 23 | fsaletype | 销售类型 | varchar | 50 |  | √ | ' ' | 销售类型,枚举: 1 :正常销售 2 :视同销售 3 :出口 4 :其他 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_tdm_cigaret_producer |  | fid |
| 2 | idx_tdm_cigaret_producer |  | forgid,ftaxperiod |

---

## 生产企业卷烟销售明细表-多语言表 t_tdm_cigaret_producer_l

- **表名称：** 生产企业卷烟销售明细表-多语言表
- **表名：** t_tdm_cigaret_producer_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fname | 物料名称 | varchar | 50 |  | √ | ' ' | 物料名称 |
| 3 | fnote | 备注 | varchar | 250 |  | √ | ' ' | 备注 |
| 4 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 5 | fpkid | fpkid | varchar | 36 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_tdm_cigaret_producer_l_0 |  | fid,flocaleid |
| 2 | pk_tdm_cigaret_producer_l |  | fpkid |

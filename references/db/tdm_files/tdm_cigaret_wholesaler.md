# 批发企业卷烟销售明细表-tdm_cigaret_wholesaler

## 批发企业卷烟销售明细表-主表 t_tdm_cigaret_wholesaler

- **表名称：** 批发企业卷烟销售明细表-主表
- **表名：** t_tdm_cigaret_wholesaler

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | ftaxperiod | 所属税期 | timestamp | 0 |  |  | null | 所属税期 |
| 3 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 4 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 5 | forgid | 税务组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 6 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 7 | fbarcode | 卷烟条包装商品条码 | varchar | 50 |  | √ | ' ' | 卷烟条包装商品条码 |
| 8 | fstatus | 数据状态 | varchar | 50 |  | √ | ' ' | 数据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 9 | fsaleprice | 销售价格 | numeric | 23 | 10 | √ | 0.0000000000 | 销售价格 |
| 10 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 11 | fmasterid | 主数据内码 | int8 | 64 |  | √ | 0 | 主数据内码 |
| 12 | fcigaretcategory | 卷烟类别 | varchar | 50 |  | √ | ' ' | 卷烟类别,枚举: 1 :一类卷烟 2 :二类卷烟 3 :三类卷烟 4 :四类卷烟 5 :五类卷烟 |
| 13 | fsalequantity | 销售数量 | numeric | 23 | 10 | √ | 0.0000000000 | 销售数量 |
| 14 | fsales | 销售额 | numeric | 23 | 10 | √ | 0.0000000000 | 销售额 |
| 15 | fbrandspecification | 卷烟牌号规格 | varchar | 50 |  | √ | ' ' | 卷烟牌号规格 |
| 16 | fenable | 使用状态 | varchar | 50 |  | √ | ' ' | 使用状态,枚举: 0 :禁用 1 :可用 |
| 17 | fcigarettype | 卷烟类型 | varchar | 50 |  | √ | ' ' | 卷烟类型,枚举: 1 :国产卷烟 2 :进口卷烟 3 :罚没卷烟 4 :其他 |
| 18 | fnumber | 物料编码 | varchar | 30 |  | √ | ' ' | 物料编码 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_tdm_cigaret_wholesaler |  | forgid,ftaxperiod |
| 2 | pk_tdm_cigaret_wholesaler |  | fid |

---

## 批发企业卷烟销售明细表-多语言表 t_tdm_cigaret_wholesaler_l

- **表名称：** 批发企业卷烟销售明细表-多语言表
- **表名：** t_tdm_cigaret_wholesaler_l

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
| 1 | idx_tdm_cigaret_wholesaler_l_0 |  | fid,flocaleid |
| 2 | pk_tdm_cigaret_wholesaler_l |  | fpkid |

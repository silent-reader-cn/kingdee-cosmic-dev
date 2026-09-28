# 物料标准价目表-scax_matstdprices

## 成本子要素信息-子表 t_scax_matstdpricedetail

- **表名称：** 成本子要素信息-子表
- **表名：** t_scax_matstdpricedetail

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fsubelement | 成本子要素 | int8 | 64 |  | √ | 0 | 成本子要素 cad_subelement |
| 2 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 3 | fmaterial | 物料 | int8 | 64 |  | √ | 0 | 物料 bd_material |
| 4 | fdetailid | fdetailid | int8 | 64 |  | √ | 0 | id |
| 5 | felement | 成本要素 | int8 | 64 |  | √ | 0 | 成本要素 cad_element |
| 6 | fentryid | fentryid | int8 | 64 |  | √ | 0 |  |
| 7 | fprice | 标准单价 | numeric | 23 | 10 | √ | 0 | 标准单价 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fdetailid | fdetailid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_scax_matstdpricedetail |  | fentryid |
| 2 | pk_scax_matstdpricedetail |  | fdetailid |

---

## 物料信息-子表 t_scax_matstdpriceentry

- **表名称：** 物料信息-子表
- **表名：** t_scax_matstdpriceentry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fsrcbillnumber | 价格来源单据编码 | varchar | 255 |  | √ | ' ' | 价格来源单据编码 |
| 3 | fsrcbillid | 价格来源单据id | int8 | 64 |  | √ | 0 | 价格来源单据id |
| 4 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 5 | fdatasrc | 价格来源 | varchar | 10 |  | √ | 'manual' | 价格来源,枚举: manual :手工新增 costupdate :成本更新 order :采购订单 purchase :采购价目表 |
| 6 | fmaterial | 物料编码 | int8 | 64 |  | √ | 0 | 物料 bd_material |
| 7 | famount | 标准金额 | numeric | 23 | 10 | √ | 0 | 标准金额 |
| 8 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 9 | ftracknumber | 跟踪号 | int8 | 64 |  | √ | 0 | 跟踪号 bd_tracknumber |
| 10 | fsrcbillentryid | 价格来源单据分录id | int8 | 64 |  | √ | 0 | 价格来源单据分录id |
| 11 | fsrcbillentryseq | 价格来源单据分录行号 | int8 | 64 |  | √ | 0 | 价格来源单据分录行号 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_scax_matstdpriceentry |  | fentryid |
| 2 | idx_scax_matstdpriceentry |  | fid |

---

## 物料标准价目表-多语言表 t_scax_matstdprices_l

- **表名称：** 物料标准价目表-多语言表
- **表名：** t_scax_matstdprices_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fremark | 备注 | varchar | 255 |  | √ | ' ' | 备注 |
| 3 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 4 | fpkid | fpkid | varchar | 36 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_scax_matstdprices_l |  | fid,flocaleid |
| 2 | pk_scax_matstdprices_l |  | fpkid |

---

## 物料标准价目表-主表 t_scax_matstdprices

- **表名称：** 物料标准价目表-主表
- **表名：** t_scax_matstdprices

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 3 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 4 | fcosttypeid | 标准成本方案 | int8 | 64 |  | √ | 0 | 标准成本方案 cad_costtype |
| 5 | fbillstatus | 单据状态 | bpchar | 1 |  | √ | ' ' | 单据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 6 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 7 | fdatasrc | 数据来源 | varchar | 10 |  | √ | ' ' | 数据来源,枚举: manual :手工新增 purprice :采购取价 |
| 8 | fauditdate | 审核时间 | timestamp | 0 |  |  | null | 审核时间 |
| 9 | fcurrencyid | 币别 | int8 | 64 |  | √ | 0 | 币种 bd_currency |
| 10 | fbillno | 单据编号 | varchar | 80 |  | √ | ' ' | 单据编号 |
| 11 | fauditorid | 审核人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 12 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_scax_matstdprices_number |  | fbillno |
| 2 | pk_scax_matstdprices |  | fid |
| 3 | idx_scax_matstdprices |  | fcosttypeid |

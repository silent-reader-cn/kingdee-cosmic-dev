# 税收分类编码映射-ar_goodslinktaxtype

## 税收分类编码映射-多语言表 t_ar_goodslinktaxtype_l

- **表名称：** 税收分类编码映射-多语言表
- **表名：** t_ar_goodslinktaxtype_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fname | 名称 | varchar | 80 |  | √ | ' ' | 名称 |
| 3 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 4 | fpkid | fpkid | varchar | 18 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | t_ar_goodslinktaxtype_l_pkey |  | fpkid |
| 2 | idx_ar_gltt_fid |  | flocaleid,fid |

---

## 税收分类编码映射-主表 t_ar_goodslinktaxtype

- **表名称：** 税收分类编码映射-主表
- **表名：** t_ar_goodslinktaxtype

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fexpenseitemid | 费用项目 | int8 | 64 |  | √ | 0 | 费用项目 er_expenseitemedit |
| 3 | fremark | 描述 | varchar | 255 |  | √ | ' ' | 描述 |
| 4 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 5 | fname | fname | varchar | 100 |  | √ | ' ' |  |
| 6 | ftaxrate | 税率(%) | numeric | 23 | 10 | √ | 0.0000000000 | 税率(%) |
| 7 | fmaterialid | 物料 | int8 | 64 |  | √ | 0 | 物料 bd_material |
| 8 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 9 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 10 | fistax | 是否含税 | bpchar | 1 |  | √ | '0' | 是否含税 |
| 11 | fvatspecialmanagement | 增值税特殊管理 | varchar | 50 |  | √ | ' ' | 增值税特殊管理,枚举: "" :非零税率 1 :免税 2 :不征税 3 :普通零税率 |
| 12 | ftaxsupertypename | 税收分类大类 | varchar | 50 |  | √ | ' ' | 税收分类大类 |
| 13 | fstatus | 数据状态 | varchar | 5 |  | √ | ' ' | 数据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 14 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 15 | fspectype | 开票规格型号 | varchar | 50 |  | √ | ' ' | 开票规格型号 |
| 16 | fmasterid | 主数据内码 | int8 | 64 |  | √ | 0 | 主数据内码 |
| 17 | ftaxsupertypenum | 税收分类编码 | varchar | 80 |  | √ | ' ' | 税收分类编码 er_taxclasscode |
| 18 | ftaxrateid | 税率 | int8 | 64 |  | √ | 0 | 税率 bd_taxrate |
| 19 | fenable | 使用状态 | varchar | 30 |  | √ | ' ' | 使用状态,枚举: 0 :禁用 1 :启用 |
| 20 | fnumber | 编码 | varchar | 80 |  | √ | ' ' | 编码 |
| 21 | fmeasureunitid | 计量单位 | int8 | 64 |  | √ | 0 | 计量单位 bd_measureunits |
| 22 | finvname | 开票名称 | varchar | 255 |  | √ | ' ' | 开票名称 |
| 23 | fcustomerid | 客户 | int8 | 64 |  | √ | 0 | 客户 bd_customer |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_ar_fnumber |  | fnumber |
| 2 | t_ar_goodslinktaxtype_pkey |  | fid |

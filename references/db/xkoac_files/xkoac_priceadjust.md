# 结算定价调整表-xkoac_priceadjust

## 单据体-子表 t_xkoac_priceadjustentry

- **表名称：** 单据体-子表
- **表名：** t_xkoac_priceadjustentry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fremark | 备注 | varchar | 255 |  | √ | ' ' | 备注 |
| 2 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 3 | fupdatedtime | 更新日期 | timestamp | 0 |  |  | null | 更新日期 |
| 4 | fadjustratio | 调整比率值（%） | numeric | 23 | 10 | √ | 0 | 调整比率值（%） |
| 5 | fmaterialid | 物料编码 | int8 | 64 |  | √ | 0 | [物料 bd_material](../basedata_files/bd_material.md) |
| 6 | fmaterialgroupid | 物料分类 | int8 | 64 |  | √ | 0 | [物料分类 bd_materialgroup](../basedata_files/bd_materialgroup.md) |
| 7 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 8 | fadjusttype | 调整类型 | varchar | 50 |  | √ | ' ' | 调整类型,枚举: 1 :折扣 2 :加成 3 :固定 4 :自定义 |
| 9 | fexpiredate | 失效日期 | timestamp | 0 |  |  | null | 失效日期 |
| 10 | fformula | 调整后单价计算公式 | varchar | 255 |  | √ | ' ' | 调整后单价计算公式 |
| 11 | feffectivedate | 生效日期 | timestamp | 0 |  |  | null | 生效日期 |
| 12 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 13 | ffixvalue | 调整固定值 | numeric | 23 | 10 | √ | 0 | 调整固定值 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_xkoac_priceadjustentry_fk |  | fid |
| 2 | pk_xkoac_priceadjustentry |  | fentryid |

---

## 卖方经营单元-多选基础资料表 t_xkoac_priceadj_seller

- **表名称：** 卖方经营单元-多选基础资料表
- **表名：** t_xkoac_priceadj_seller

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fbasedataid | fbasedataid | int8 | 64 |  | √ | 0 | [经营单元 xkoac_unit](../basedata_files/xkoac_unit.md) |
| 3 | fpkid | fpkid | int8 | 64 |  | √ | 0 | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_xkoac_priceadj_seller |  | fpkid |
| 2 | idx_xkoac_priceadj_seller_fk |  | fid |

---

## 适用经营账簿-多选基础资料表 t_xkoac_priceadjust_book

- **表名称：** 适用经营账簿-多选基础资料表
- **表名：** t_xkoac_priceadjust_book

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fbasedataid | fbasedataid | int8 | 64 |  | √ | 0 | [经营账簿 xkoac_operatingbook](../xkoac_files/xkoac_operatingbook.md) |
| 3 | fpkid | fpkid | int8 | 64 |  | √ | 0 | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_xkoac_priceadjust_book |  | fpkid |
| 2 | idx_xkoac_priceadjust_book_fk |  | fid |

---

## 买方经营单元-多选基础资料表 t_xkoac_priceadjust_buyer

- **表名称：** 买方经营单元-多选基础资料表
- **表名：** t_xkoac_priceadjust_buyer

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fbasedataid | fbasedataid | int8 | 64 |  | √ | 0 | [经营单元 xkoac_unit](../basedata_files/xkoac_unit.md) |
| 3 | fpkid | fpkid | int8 | 64 |  | √ | 0 | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_xkoac_priceadjust_buyer |  | fpkid |
| 2 | idx_xkoac_priceadjust_buyer_fk |  | fid |

---

## 结算定价调整表-多语言表 t_xkoac_priceadjust_l

- **表名称：** 结算定价调整表-多语言表
- **表名：** t_xkoac_priceadjust_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fname | 名称 | varchar | 255 |  | √ | ' ' | 名称 |
| 3 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 4 | fpkid | fpkid | varchar | 36 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_xkoac_priceadjust_l_0 |  | fid,flocaleid |
| 2 | pk_xkoac_priceadjust_l |  | fpkid |

---

## 结算定价调整表-主表 t_xkoac_priceadjust

- **表名称：** 结算定价调整表-主表
- **表名：** t_xkoac_priceadjust

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fadjuststrategy | 调整策略 | bpchar | 1 |  | √ | ' ' | 调整策略,枚举: 1 :双边调整 2 :单边调整 3 :通用调整 |
| 2 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 3 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 4 | fname | 名称 | varchar | 255 |  | √ | ' ' | 名称 |
| 5 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 6 | fdisablerid | 禁用人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 7 | faudittime | 审核日期 | timestamp | 0 |  |  | null | 审核日期 |
| 8 | fdisabletime | 禁用日期 | timestamp | 0 |  |  | null | 禁用日期 |
| 9 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 10 | fadjustobject | 调整对象 | bpchar | 1 |  | √ | ' ' | 调整对象,枚举: 1 :物料 2 :物料分类 |
| 11 | fstatus | 数据状态 | bpchar | 1 |  | √ | 'A' | 数据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 12 | fbasecurrencyid | 本位币 | int8 | 64 |  | √ | 0 | [币种 bd_currency](../base_files/bd_currency.md) |
| 13 | fmasterid | 主数据内码 | int8 | 64 |  | √ | 0 | 主数据内码 |
| 14 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 15 | fenable | 使用状态 | bpchar | 1 |  | √ | '1' | 使用状态,枚举: 0 :禁用 1 :可用 |
| 16 | fnumber | 编码 | varchar | 255 |  | √ | ' ' | 编码 |
| 17 | fauditorid | 审核人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_xkoac_priceadjust |  | fid |
| 2 | idx_xkoac_priceadjust_m0 |  | fnumber |

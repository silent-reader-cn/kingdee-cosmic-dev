# 经营单元内部结算单-xkoac_instatement

## 分录-子表 t_xkoac_instatemententry

- **表名称：** 分录-子表
- **表名：** t_xkoac_instatemententry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fitem_expense | 金额 | numeric | 23 | 10 | √ | 0 | 金额 |
| 3 | fcostid | 费用项目 | int8 | 64 |  | √ | 0 | [费用项目 er_expenseitemedit](../basedata_files/er_expenseitemedit.md) |
| 4 | fcost_quantity | fcost_quantity | int8 | 64 |  | √ | 0 |  |
| 5 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 6 | fcost_expense | fcost_expense | numeric | 23 | 10 | √ | 0 |  |
| 7 | fnote | 备注 | varchar | 255 |  |  | ' ' | 备注 |
| 8 | fitem_quantity | 数量 | numeric | 23 | 10 | √ | 0 | 数量 |
| 9 | funitfield | 计量单位 | int8 | 64 |  | √ | 0 | [计量单位 bd_measureunits](../base_files/bd_measureunits.md) |
| 10 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 11 | fprice | 单价 | numeric | 23 | 10 |  | null | 单价 |
| 12 | fitemid | 物料 | int8 | 64 |  | √ | 0 | [物料 bd_material](../basedata_files/bd_material.md) |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_xkoac_instatemententry |  | fentryid |
| 2 | idx_xkoac_instatemententry |  | fid |

---

## 分录-多语言表 t_xkoac_instatemententry_l

- **表名称：** 分录-多语言表
- **表名：** t_xkoac_instatemententry_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fnote | 备注 | varchar | 255 |  | √ | ' ' | 备注 |
| 2 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 3 | fpkid | fpkid | varchar | 36 |  | √ | ' ' | pkid |
| 4 | fentryid | fentryid | int8 | 64 |  | √ | 0 |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_xkoac_instatemententry_l |  | fpkid |
| 2 | idx_xkoac_instatemententry_l |  | fentryid,flocaleid |

---

## 经营单元内部结算单-主表 t_xkoac_instatement

- **表名称：** 经营单元内部结算单-主表
- **表名：** t_xkoac_instatement

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | forgstructureid | 组织架构版本 | int8 | 64 |  | √ | 0 | [经营组织架构版本 xkoac_orgsystem](../xkoac_files/xkoac_orgsystem.md) |
| 3 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 4 | fcustomerapart | 买方经营单元 | int8 | 64 |  | √ | 0 | [经营单元 xkoac_unit](../basedata_files/xkoac_unit.md) |
| 5 | fbillstatus | 单据状态 | bpchar | 1 |  |  | 'A' | 单据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 6 | fcreatetime | 创建日期 | timestamp | 0 |  |  | null | 创建日期 |
| 7 | forgid | 创建组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 8 | fauditdate | 审核日期 | timestamp | 0 |  |  | null | 审核日期 |
| 9 | faccountbookid | 经营账簿 | int8 | 64 |  | √ | 0 | [经营账簿 xkoac_operatingbook](../xkoac_files/xkoac_operatingbook.md) |
| 10 | fmodifytime | 修改日期 | timestamp | 0 |  |  | null | 修改日期 |
| 11 | fbasecurrency | 币别 | int8 | 64 |  | √ | 0 | [币种 bd_currency](../base_files/bd_currency.md) |
| 12 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 13 | fdate | 业务日期 | timestamp | 0 |  |  | null | 业务日期 |
| 14 | fpaymenttype | 结算类型 | bpchar | 1 |  | √ | '2' | 结算类型,枚举: 1 :服务 2 :物料 |
| 15 | fbillno | 单据编号 | varchar | 30 |  | √ | ' ' | 单据编号 |
| 16 | fauditorid | 审核人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 17 | fsupplierapart | 卖方经营单元 | int8 | 64 |  | √ | 0 | [经营单元 xkoac_unit](../basedata_files/xkoac_unit.md) |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_xkoac_instatement |  | fbillno |
| 2 | pk_t_xkoac_instatement |  | fid |

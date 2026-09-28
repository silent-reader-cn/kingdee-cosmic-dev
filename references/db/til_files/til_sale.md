# 视同销售-til_sale

## 视同销售-主表 t_til_sale

- **表名称：** 视同销售-主表
- **表名：** t_til_sale

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | ftaxamount | 税额 | numeric | 23 | 10 | √ | 0.0000000000 | 税额 |
| 3 | fisgeneratevoucher | 是否生成凭证 | varchar | 50 |  | √ | ' ' | 是否生成凭证,枚举: 1 :是 0 :否 |
| 4 | fbillstatus | 单据状态 | varchar | 30 |  | √ | ' ' | 单据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 5 | fcreatedatefield | 创建日期 | timestamp | 0 |  |  | null | 创建日期 |
| 6 | famount | 视同销售收入 | numeric | 23 | 10 | √ | 0.0000000000 | 视同销售收入 |
| 7 | fauditdate | 审核日期 | timestamp | 0 |  |  | null | 审核日期 |
| 8 | fmodifierfield | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 9 | forg | 税务组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 10 | ftaxcategory | 税率 | int8 | 64 |  | √ | 0 | [税率 bd_taxrate](../basedata_files/bd_taxrate.md) |
| 11 | fcreaterfield | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 12 | fmodifydatefield | 修改日期 | timestamp | 0 |  |  | null | 修改日期 |
| 13 | fsecendtype | 自产/外购 | varchar | 50 |  | √ | ' ' | 自产/外购,枚举: 1 :自产 2 :外购 3 :不适用 |
| 14 | fdatasource | 数据来源 | varchar | 50 |  | √ | ' ' | 数据来源,枚举: 1 :手工新增 2 :模板导入 |
| 15 | fcurrencyfield | 币别 | int8 | 64 |  | √ | 0 | [币种 bd_currency](../base_files/bd_currency.md) |
| 16 | fpostdate | 记账日期 | timestamp | 0 |  |  | null | 记账日期 |
| 17 | fsaletype | 视同销售类型 | varchar | 50 |  | √ | ' ' | 视同销售类型,枚举: 1 :集体福利 2 :个人消费 3 :无偿赠送 4 :无偿应税服务 5 :分配 6 :投资 7 :非应税项目 8 :跨县市移送 9 :无偿转让不动产 10 :无偿转让无形资产 11 :交付他人代销 12 :代销货物 13 :其他 |
| 18 | fbillno | 业务编号 | varchar | 50 |  | √ | ' ' | 业务编号 |
| 19 | fcode | 业务编码 | varchar | 50 |  | √ | ' ' | 业务编码 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_til_sale |  | fid |
| 2 | idx_til_sale |  | forg |

---

## 视同销售-多语言表 t_til_sale_l

- **表名称：** 视同销售-多语言表
- **表名：** t_til_sale_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fremark | 备注 | varchar | 100 |  | √ | ' ' | 备注 |
| 3 | fname | 业务名称 | varchar | 50 |  | √ | ' ' | 业务名称 |
| 4 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 5 | fpkid | fpkid | varchar | 36 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_til_sale_l_0 |  | fid,flocaleid |
| 2 | pk_til_sale_l |  | fpkid |

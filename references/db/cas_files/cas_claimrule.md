# 通知认领规则-cas_claimrule

## 适用组织-子表 t_cas_recpayrule_uorg

- **表名称：** 适用组织-子表
- **表名：** t_cas_recpayrule_uorg

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fuorgid | 组织名称 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 3 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 4 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_cas_recpayrule_uorg |  | fuorgid |
| 2 | t_cas_recpayrule_uorg_pkey |  | fentryid |

---

## 规则设置-子表 t_cas_recpayrule_e

- **表名称：** 规则设置-子表
- **表名：** t_cas_recpayrule_e

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fispushandsave | fispushandsave | varchar | 128 |  | √ | '1' |  |
| 3 | fdatafilter | 数据过滤条件 | text | 0 |  |  | null | 数据过滤条件 |
| 4 | fpayerbasetype | 付款人基础类型 | varchar | 30 |  | √ | ' ' | 付款人基础类型,枚举: bd_customer :客户 bd_supplier :供应商 bos_org :业务单元 bos_user :职员 cas_othercontactunit :其他 |
| 5 | frecerbasetype | 收款人基础类型 | varchar | 50 |  | √ | ' ' | 收款人基础类型,枚举: bd_customer :客户 bd_supplier :供应商 bos_org :业务单元 bos_user :职员 other :其他往来单位 |
| 6 | frecerid | 收款人基础资料 | int8 | 64 |  | √ | 0 | 客户 bd_customer |
| 7 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 8 | fdatafilterdesc | 适用条件 | varchar | 1024 |  | √ | ' ' | 适用条件 |
| 9 | fpayeetypeid | 收款人类型下拉 | varchar | 100 |  | √ | ' ' | 收款人类型下拉,枚举: bos_org :公司 bd_supplier :供应商 bd_customer :客户 bos_user :职员 cas_othercontactunit :其他 |
| 10 | fpayer | 付款人存 | varchar | 50 |  | √ | ' ' | 付款人存 |
| 11 | freceivingtypeid | 收款用途基础资料 | int8 | 64 |  | √ | 0 | [收款用途 cas_receivingbilltype](../cas_files/cas_receivingbilltype.md) |
| 12 | frecbilltype | 收款单单据类型基础资料 | int8 | 64 |  | √ | 0 | [单据类型 bos_billtype](../cts_files/bos_billtype.md) |
| 13 | fehandlebill | 入账单据 | varchar | 100 |  | √ | ' ' | 入账单据,枚举: recvbill :收款处理 paybill :付款处理 upbill :上划处理 downbill :下拨处理 |
| 14 | frecer | 收款人存 | varchar | 100 |  | √ | ' ' | 收款人存 |
| 15 | fpaybilltype | 付款单单据类型基础资料 | int8 | 64 |  | √ | 0 | [单据类型 bos_billtype](../cts_files/bos_billtype.md) |
| 16 | fsettlementtype | 结算方式基础资料 | int8 | 64 |  | √ | 0 | [结算方式 bd_settlementtype](../basedata_files/bd_settlementtype.md) |
| 17 | fpayerid | 付款人基础资料 | int8 | 64 |  | √ | 0 | 客户 bd_customer |
| 18 | fremark | 摘要 | varchar | 255 |  | √ | ' ' | 摘要 |
| 19 | fcontactunittype | 往来单位类型基础资料 | varchar | 36 |  | √ | ' ' | 往来单位类型基础资料,枚举: bd_supplier :供应商 bd_customer :客户 bos_user :人员 bos_org :业务单元 cas_othercontactunit :其他往来单位 other :其他 |
| 20 | fbizbillstatu | fbizbillstatu | bpchar | 1 |  | √ | '0' |  |
| 21 | ffundflowitemid | 资金用途基础资料 | int8 | 64 |  | √ | 0 | [资金用途 cas_fundflowitem](../cas_files/cas_fundflowitem.md) |
| 22 | fpayertypeid | 付款人类型下拉 | varchar | 100 |  | √ | ' ' | 付款人类型下拉,枚举: bd_customer :客户 bd_supplier :供应商 bos_org :公司 bos_user :职员 cas_othercontactunit :其他往来单位 |
| 23 | fdatafilter_tag | 数据过滤条件_详情 | text | 0 |  |  | null | 数据过滤条件_详情 |
| 24 | fsavenotifi | 大文本 | text | 0 |  |  | null | 大文本 |
| 25 | fnotifische | 通知方案 | varchar | 1024 |  | √ | ' ' | 通知方案 |
| 26 | fsavenotifi_tag | 大文本_详情 | text | 0 |  |  | null | 大文本_详情 |
| 27 | frulesname | 规则项名称 | varchar | 100 |  | √ | ' ' | 规则项名称 |
| 28 | fhandlescheme | 处理方案 | varchar | 30 |  | √ | ' ' | 处理方案,枚举: rule :按规则生成 recv :收款认领 ticket :票据认领 |
| 29 | fpaymenttypeid | 付款用途基础资料 | int8 | 64 |  | √ | 0 | [付款用途 cas_paymentbilltype](../cas_files/cas_paymentbilltype.md) |
| 30 | fcontactunit | 往来单位基础资料 | int8 | 64 |  | √ | 0 | 供应商 bd_supplier |
| 31 | fsettleorgid | 结算组织基础资料 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 32 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | t_cas_recpayrule_e_pkey |  | fentryid |
| 2 | idx_cas_recpayrule_e |  | frulesname |

---

## 通知认领规则-主表 t_cas_recpayrule

- **表名称：** 通知认领规则-主表
- **表名：** t_cas_recpayrule

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fcreateorgid | fcreateorgid | int8 | 64 |  | √ | 0 |  |
| 3 | fremark | 备注 | varchar | 512 |  | √ | ' ' | 备注 |
| 4 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 5 | fname | fname | varchar | 100 |  | √ | ' ' |  |
| 6 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 7 | fbizbillstatu | fbizbillstatu | bpchar | 1 |  | √ | '0' |  |
| 8 | forgid | 组织(历史数据) | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 9 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 10 | fctrlstrategy | fctrlstrategy | varchar | 30 |  | √ | ' ' |  |
| 11 | fstatus | 数据状态 | varchar | 30 |  | √ | ' ' | 数据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 12 | fbiztype | 业务类型 | varchar | 100 |  | √ | ' ' | 业务类型,枚举: rec :收款 pay :付款 recticket :票据 electicket :收票(电票) |
| 13 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 14 | fmasterid | 主数据内码 | int8 | 64 |  | √ | 0 | 主数据内码 |
| 15 | fissystem | 系统预置 | bpchar | 1 |  | √ | '0' | 系统预置 |
| 16 | fenable | 使用状态 | varchar | 5 |  | √ | ' ' | 使用状态,枚举: 0 :禁用 1 :可用 |
| 17 | fnumber | 规则编码 | varchar | 80 |  | √ | ' ' | 规则编码 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_cas_recpayrule |  | forgid |
| 2 | pk_t_cas_recpayrule |  | fid |

---

## 通知认领规则-多语言表 t_cas_recpayrule_l

- **表名称：** 通知认领规则-多语言表
- **表名：** t_cas_recpayrule_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fname | 方案名称 | varchar | 100 |  | √ | ' ' | 方案名称 |
| 3 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 4 | fpkid | fpkid | varchar | 18 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | t_cas_recpayrule_l_pkey |  | fpkid |
| 2 | idx_t_cas_recpayrule_l |  | fname |

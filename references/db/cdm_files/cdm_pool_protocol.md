# 银行票据池协议-cdm_pool_protocol

## 银行票据池协议-多语言表 t_cdm_poolprotocol_l

- **表名称：** 银行票据池协议-多语言表
- **表名：** t_cdm_poolprotocol_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fname | 票据池名称 | varchar | 255 |  | √ | ' ' | 票据池名称 |
| 3 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 4 | fpkid | fpkid | varchar | 30 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_cdm_poolprotocol_l |  | fpkid |
| 2 | idx_cdm_poolprotocol_l_fid |  | fid |

---

## 银行票据池协议-主表 t_cdm_poolprotocol

- **表名称：** 银行票据池协议-主表
- **表名：** t_cdm_poolprotocol

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fopenuser | 反关闭操作人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 3 | forgid | 签约组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 4 | fclosedate | 关闭操作时间 | timestamp | 0 |  |  | null | 关闭操作时间 |
| 5 | famount | 总授信额度 | numeric | 23 | 10 | √ | 0 | 总授信额度 |
| 6 | fcloseuser | 关闭操作人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 7 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 8 | fstatus | 单据状态 | varchar | 50 |  | √ | ' ' | 单据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 9 | fenddate | 票据池结束日期 | timestamp | 0 |  |  | null | 票据池结束日期 |
| 10 | fexpireset | 票据到期时间 | varchar | 50 |  | √ | ' ' | 票据到期时间,枚举: 0 :所有 1 :1个月 |
| 11 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 12 | fmasterid | 主数据内码 | int8 | 64 |  | √ | 0 | 主数据内码 |
| 13 | fname | 票据池名称 | varchar | 50 |  | √ | ' ' | 票据池名称 |
| 14 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 15 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 16 | fcurrency | 币种 | int8 | 64 |  | √ | 0 | [币种 bd_currency](../base_files/bd_currency.md) |
| 17 | facceportname | 承兑人 | varchar | 255 |  | √ | ' ' | 承兑人 |
| 18 | fbank | 合作银行 | int8 | 64 |  | √ | 0 | [金融机构 bd_finorginfo](../basedata_files/bd_finorginfo.md) |
| 19 | fopendate | 反关闭操作时间 | timestamp | 0 |  |  | null | 反关闭操作时间 |
| 20 | fauditdate | 审核时间 | timestamp | 0 |  |  | null | 审核时间 |
| 21 | fsignaccount | 签约账户 | int8 | 64 |  | √ | 0 | [银行账户 bd_accountbanks](../basedata_files/bd_accountbanks.md) |
| 22 | fconvertratio | 额度折算比例（%） | numeric | 23 | 10 | √ | 0 | 额度折算比例（%） |
| 23 | fstartdate | 票据池开始日期 | timestamp | 0 |  |  | null | 票据池开始日期 |
| 24 | fbizdate | 签约日期 | timestamp | 0 |  |  | null | 签约日期 |
| 25 | fdepositaccount | 保证金账户 | int8 | 64 |  | √ | 0 | [银行账户 bd_accountbanks](../basedata_files/bd_accountbanks.md) |
| 26 | fenable | 票据池状态 | varchar | 50 |  | √ | ' ' | 票据池状态,枚举: 0 :已关闭 1 :已启用 |
| 27 | fnumber | 编码 | varchar | 50 |  | √ | ' ' | 编码 |
| 28 | fauditorid | 审核人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 29 | fcontraceno | 合同编号 | varchar | 255 |  | √ | ' ' | 合同编号 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_cdm_poolprotocol |  | fid |

---

## 单据体-子表 t_cdm_poolprotocol_entry

- **表名称：** 单据体-子表
- **表名：** t_cdm_poolprotocol_entry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | flimitamount | 限定金额 | numeric | 23 | 10 | √ | 0 | 限定金额 |
| 3 | fshareorg | 组织编码 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 4 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 5 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 6 | fislimit | 是否限定额度 | bpchar | 1 |  | √ | '0' | 是否限定额度 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_cdm_pool_entry_fid |  | fid |
| 2 | pk_t_cdm_poolprotocol_entry |  | fentryid |

# 变更申请-am_changeapply

## 变更申请-多语言表 t_am_changeapply_l

- **表名称：** 变更申请-多语言表
- **表名：** t_am_changeapply_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fclosereason | fclosereason | varchar | 255 |  | √ | ' ' |  |
| 3 | flocaleid | flocaleid | varchar | 30 |  | √ | ' ' | localeid |
| 4 | fdescription | fdescription | varchar | 255 |  | √ | ' ' |  |
| 5 | fpkid | fpkid | varchar | 30 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_am_changeapply_l |  | fpkid |
| 2 | t_am_changeapply_l_fid |  | fid,flocaleid |

---

## 变更申请-主表 t_am_changeapply

- **表名称：** 变更申请-主表
- **表名：** t_am_changeapply

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 3 | fbillstatus | 单据状态 | varchar | 80 |  | √ | ' ' | 单据状态,枚举: A :暂存 B :已提交 C :已审核 H :变更处理中 E :退单 |
| 4 | fapplydate | 申请日期 | timestamp | 0 |  |  | null | 申请日期 |
| 5 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 6 | fauditdate | 审核日期 | timestamp | 0 |  |  | null | 审核日期 |
| 7 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 8 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 9 | fapplyuserid | 申请人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 10 | fbillno | 单据编号 | varchar | 80 |  | √ | ' ' | 单据编号 |
| 11 | fauditorid | 审核人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 12 | faccountbankid | 银行账号 | int8 | 64 |  | √ | 0 | [银行账户 bd_accountbanks](../basedata_files/bd_accountbanks.md) |
| 13 | fcompanyid | 资金组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_am_changeapply |  | fid |
| 2 | idx_t_am_changeapply_num |  | fbillno |

---

## 单据体-子表 t_am_changeapply_entry

- **表名称：** 单据体-子表
- **表名：** t_am_changeapply_entry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fchangefieldname | 变更属性名称 | varchar | 255 |  | √ | ' ' | 变更属性名称 |
| 3 | fbeforechangename | 变更前 | varchar | 255 |  | √ | ' ' | 变更前 |
| 4 | fbasedataid | 多类别基础资料 | varchar | 255 |  | √ | ' ' | 业务单元 bos_org |
| 5 | fafterchangename | 变更后 | varchar | 255 |  | √ | ' ' | 变更后 |
| 6 | fbeforechange | 变更前 | varchar | 255 |  | √ | ' ' | 变更前 |
| 7 | fbasedatatype | 基础资料类型 | varchar | 255 |  | √ | ' ' | 基础资料类型,枚举: bos_org :业务单元 bd_finorginfo :金融机构 bd_acctpurpose :账户用途 bos_user :人员 bd_currency :币别 am_strategy :账户管理策略 bd_bankcgsetting :银行类别 |
| 8 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 9 | freason | 变更原因 | varchar | 255 |  | √ | ' ' | 变更原因 |
| 10 | fchangefield | 变更属性 | varchar | 50 |  | √ | ' ' | 变更属性,枚举: |
| 11 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 12 | fafterchange | 变更后 | varchar | 255 |  | √ | ' ' | 变更后 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_am_changeapply_entry |  | fentryid |
| 2 | idx_t_am_changeapply_entry_fid |  | fid |

---

## 币别-多选基础资料表 t_am_changeapply_cur

- **表名称：** 币别-多选基础资料表
- **表名：** t_am_changeapply_cur

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fbasedataid | fbasedataid | int8 | 64 |  | √ | 0 | [币种 bd_currency](../base_files/bd_currency.md) |
| 2 | fpkid | fpkid | int8 | 64 |  | √ | 0 | pkid |
| 3 | fentryid | fentryid | int8 | 64 |  | √ | 0 |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_t_am_changeapply_cur |  | fentryid |
| 2 | pk_t_am_changeapply_cur |  | fpkid |

---

## 限定结算方式-多选基础资料表 t_am_changeapply_st

- **表名称：** 限定结算方式-多选基础资料表
- **表名：** t_am_changeapply_st

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fbasedataid | fbasedataid | int8 | 64 |  | √ | 0 | [结算方式 bd_settlementtype](../basedata_files/bd_settlementtype.md) |
| 2 | fpkid | fpkid | int8 | 64 |  | √ | 0 | pkid |
| 3 | fentryid | fentryid | int8 | 64 |  | √ | 0 |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_t_am_changeapply_st |  | fentryid |
| 2 | pk_t_am_changeapply_st |  | fpkid |

---

## 单据体-子表 t_am_changeapply_entry2

- **表名称：** 单据体-子表
- **表名：** t_am_changeapply_entry2

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | feremark | feremark | varchar | 255 |  | √ | ' ' |  |
| 3 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 4 | feaccountbankid | 银行账号 | int8 | 64 |  | √ | 0 | [银行账户 bd_accountbanks](../basedata_files/bd_accountbanks.md) |
| 5 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_t_am_changeapply_ent2_fid |  | fid |
| 2 | pk_t_am_changeapply_entry2 |  | fentryid |

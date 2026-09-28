# 企享云多账号-tsate_qxy_account

## 企享云多账号-主表 t_tsate_qxy_account

- **表名称：** 企享云多账号-主表
- **表名：** t_tsate_qxy_account

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 3 | fgryhm | 个人用户名 | varchar | 50 |  | √ | ' ' | 个人用户名 |
| 4 | fbillstatus | 单据状态 | varchar | 50 |  | √ | ' ' | 单据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 5 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 6 | faggorgid | 企业id | varchar | 50 |  | √ | ' ' | 企业id |
| 7 | fauditdate | 审核日期 | timestamp | 0 |  |  | null | 审核日期 |
| 8 | fisspecial | 是否特定主体 | varchar | 50 |  | √ | ' ' | 是否特定主体,枚举: 本主体 :0 特定主体 :1 |
| 9 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 10 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 11 | fdeclareconfigid | 税局登录配置id | varchar | 50 |  | √ | ' ' | 税局登录配置id |
| 12 | fbillno | 单据编号 | varchar | 50 |  | √ | ' ' | 单据编号 |
| 13 | fauditorid | 审核人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 14 | faccountid | 账户id | varchar | 50 |  | √ | ' ' | 账户id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_tsate_qxy_account |  | fid |
| 2 | idx_tsate_qxy_account_1 |  | faggorgid |

---

## 单据体-子表 t_tsate_qxy_account_e

- **表名称：** 单据体-子表
- **表名：** t_tsate_qxy_account_e

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fmodifydatefield | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 3 | fbindproduct | 产品列表 | varchar | 50 |  | √ | ' ' | 产品列表,枚举: 0002 :归集（将要弃用，历史用户沿用） 0009 :发票归集（企业版 0017 :发票归集（代账版） 0003 :认证 0004 :数电开票 0024 :小企业申报 0020 :小企业申报(含归集) 0022 :大企业申报 0018 :数电票版式文件下载(代账版) 0005 :数电票版式文件下载(企业版) |
| 4 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 5 | fbindstatus | 绑定状态 | varchar | 50 |  | √ | ' ' | 绑定状态,枚举: 0 :未绑定 1 :已绑定 |
| 6 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 7 | fmodifierfield | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_tsate_qxy_account_e1 |  | fid |
| 2 | pk_tsate_qxy_account_e |  | fentryid |

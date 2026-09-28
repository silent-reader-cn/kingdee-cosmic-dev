# 开票抬头管理-bdm_inv_issue_title

## 开票抬头管理-主表 t_bdm_inv_issue_title

- **表名称：** 开票抬头管理-主表
- **表名：** t_bdm_inv_issue_title

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fbuyertype | 购方类型 | varchar | 30 |  | √ | ' ' | 购方类型,枚举: 1 :企业 2 :个人 |
| 3 | fmobilephone | 联系手机 | varchar | 11 |  | √ | ' ' | 联系手机 |
| 4 | fcompanycode | 组织机构代码 | varchar | 100 |  | √ | ' ' | 组织机构代码 |
| 5 | fcreatetime | 创建日期 | timestamp | 0 |  |  | null | 创建日期 |
| 6 | femail | 公司邮箱 | varchar | 100 |  | √ | ' ' | 公司邮箱 |
| 7 | fcontacts | 联系人 | varchar | 20 |  | √ | ' ' | 联系人 |
| 8 | fepname | 购方名称 | varchar | 100 |  | √ | ' ' | 购方名称 |
| 9 | forg | 关联组织信息 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 10 | fepinfo | 当前用户所属企业 | int8 | 64 |  | √ | 0 | 企业基础信息 bdm_enterprise_baseinfo |
| 11 | fmodifytime | 修改日期 | timestamp | 0 |  |  | null | 修改日期 |
| 12 | fstatus | 启用/禁用 | varchar | 30 |  | √ | ' ' | 启用/禁用,枚举: 1 :启用 0 :禁用 |
| 13 | fidcode | 身份证号码 | varchar | 20 |  | √ | ' ' | 身份证号码 |
| 14 | ftaxno | 企业税号 | varchar | 20 |  | √ | ' ' | 企业税号 |
| 15 | faddr | 地址及电话 | varchar | 100 |  | √ | ' ' | 地址及电话 |
| 16 | fopeningbank | 开户银行及账号 | varchar | 100 |  | √ | ' ' | 开户银行及账号 |
| 17 | fcode | 购方编号 | varchar | 32 |  | √ | ' ' | 购方编号 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_bdm_inv_issue_title |  | fid |
| 2 | idx_bdm_inv_issue_title |  | fcode |

---

## 客户信息单据体-子表 t_bdm_issue_title_cust

- **表名称：** 客户信息单据体-子表
- **表名：** t_bdm_issue_title_cust

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fcustomertaxno | 客户税号 | varchar | 50 |  | √ | ' ' | 客户税号 |
| 3 | fcustomer | 客户 | int8 | 64 |  | √ | 0 | 客户 bd_customer |
| 4 | fcustomername | 客户名称 | varchar | 100 |  | √ | ' ' | 客户名称 |
| 5 | fcustomerno | 客户编码 | varchar | 50 |  | √ | ' ' | 客户编码 |
| 6 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 7 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_bdm_issue_title_cust |  | fentryid |
| 2 | idx_bdm_issue_title_cust |  | fid |

---

## 开户行单据体-子表 t_bdm_issue_title_items

- **表名称：** 开户行单据体-子表
- **表名：** t_bdm_issue_title_items

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fotherid | otherId | varchar | 50 |  | √ | ' ' | otherId |
| 3 | fmobilephone | 联系手机 | varchar | 40 |  | √ | ' ' | 联系手机 |
| 4 | femail | 公司邮箱 | varchar | 100 |  | √ | ' ' | 公司邮箱 |
| 5 | fpriority | 优先级 | int8 | 64 |  | √ | 0 | 优先级 |
| 6 | fcontacts | 联系人 | varchar | 20 |  | √ | ' ' | 联系人 |
| 7 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 8 | ffilter_tag | 过滤条件_详情 | text | 0 |  |  | null | 过滤条件_详情 |
| 9 | ffilter | 过滤条件 | varchar | 255 |  | √ | ' ' | 过滤条件 |
| 10 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 11 | faddr | 地址及电话 | varchar | 100 |  | √ | ' ' | 地址及电话 |
| 12 | fopeningbank | 开户银行及账号 | varchar | 100 |  | √ | ' ' | 开户银行及账号 |
| 13 | fisdefault | 是否默认 | varchar | 10 |  | √ | ' ' | 是否默认 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_bdm_issue_title_items |  | fid |
| 2 | pk_t_bdm_issue_title_items |  | fentryid |

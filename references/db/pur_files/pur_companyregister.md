# 企业注册电子签章-pur_companyregister

## 分录-子表 t_pur_crentry

- **表名称：** 分录-子表
- **表名：** t_pur_crentry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | null |  |
| 2 | fphone | 手机号 | varchar | 30 |  |  | null | 手机号 |
| 3 | fseq | 分录行号 | int8 | 64 |  |  | null | 分录行号 |
| 4 | fpuserid | 签章人 | int8 | 64 |  |  | null | [人员 bos_user](../base_files/bos_user.md) |
| 5 | fentryid | fentryid | int8 | 64 |  | √ | null | id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | t_pur_crentry_pkey |  | fentryid |
| 2 | idx_pur_crentry_fpuserid_fseq |  | fpuserid,fseq |

---

## 企业注册电子签章-主表 t_pur_companyregister

- **表名称：** 企业注册电子签章-主表
- **表名：** t_pur_companyregister

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | null | id |
| 2 | fmaster | 法人 | varchar | 50 |  |  | null | 法人 |
| 3 | fstatus | 状态 | bpchar | 1 |  |  | ' ' | 状态,枚举: A :未注册 B :已注册 C :禁用 |
| 4 | fcreatorid | 创建人 | int8 | 64 |  |  | null | [人员 bos_user](../base_files/bos_user.md) |
| 5 | forgcode | 组织机构代码 | varchar | 50 |  |  | null | 组织机构代码 |
| 6 | fcreatetime | 创建日期 | timestamp | 0 |  |  | null | 创建日期 |
| 7 | ficcode | 公司登记号 | varchar | 50 |  |  | null | 公司登记号 |
| 8 | fidentity | 法人身份证号 | varchar | 30 |  |  | null | 法人身份证号 |
| 9 | ftaxcode | 纳税识别号 | varchar | 50 |  |  | null | 纳税识别号 |
| 10 | fmobile | 法人手机号 | varchar | 30 |  |  | null | 法人手机号 |
| 11 | feuser | feuser | varchar | 80 |  |  | null |  |
| 12 | fcompanyid | 公司 | int8 | 64 |  |  | null | [业务单元 bos_org](../base_files/bos_org.md) |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | t_pur_companyregister_pkey |  | fid |
| 2 | idx_pur_companyreg_fcompanyid |  | fcompanyid |

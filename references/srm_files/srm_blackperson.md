# 人员黑名单-srm_blackperson

## 人员黑名单-主表 t_pur_black_person

- **表名称：** 人员黑名单-主表
- **表名：** t_pur_black_person

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fremark | 事件详述 | varchar | 2000 |  | √ | ' ' | 事件详述 |
| 3 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 4 | fname | 人员姓名 | varchar | 50 |  | √ | ' ' | 人员姓名 |
| 5 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 6 | forgid | 采购方 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 7 | fsourceid | 源单ID | int8 | 64 |  | √ | 0 | 源单ID |
| 8 | fsourcename | fsourcename | varchar | 100 |  | √ | ' ' |  |
| 9 | fisblacklist | 加入黑名单 | bpchar | 1 |  | √ | ' ' | 加入黑名单 |
| 10 | flastupdateuserid | 修改人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 11 | fdescription | 事件简述 | varchar | 100 |  | √ | ' ' | 事件简述 |
| 12 | fauditdate | 审核时间 | timestamp | 0 |  |  | null | 审核时间 |
| 13 | fauditopinion | 审批意见 | varchar | 255 |  | √ | ' ' | 审批意见 |
| 14 | fsupplierid | 注册供应商 | int8 | 64 |  | √ | 0 | 供应商 srm_supplier |
| 15 | flastupdatetime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 16 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 17 | fauditstatus | 审批状态 | bpchar | 1 |  | √ | ' ' | 审批状态,枚举: A :拟定 B :提交审批 C :审批通过 D :审批驳回 |
| 18 | fstatus | 数据状态 | bpchar | 1 |  | √ | ' ' | 数据状态,枚举: A :保存 B :已提交 C :已审核 |
| 19 | fbiztype | 业务类型 | bpchar | 1 |  | √ | ' ' | 业务类型,枚举: A :人员黑名单 |
| 20 | fmasterid | 主数据内码 | int8 | 64 |  | √ | 0 | 主数据内码 |
| 21 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 22 | fenable | 使用状态 | bpchar | 1 |  | √ | ' ' | 使用状态,枚举: 0 :禁用 1 :可用 |
| 23 | fnumber | 身份证号码 | varchar | 30 |  | √ | ' ' | 身份证号码 |
| 24 | fauditorid | 审核人 | int8 | 64 |  | √ | 0 | 人员 bos_user |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | t_pur_black_person_pkey |  | fid |
| 2 | idx_pur_black_person_number |  | fnumber |

---

## 人员黑名单-多语言表 t_pur_black_person_l

- **表名称：** 人员黑名单-多语言表
- **表名：** t_pur_black_person_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fname | 人员姓名 | varchar | 50 |  | √ | ' ' | 人员姓名 |
| 3 | fsourcename | 来源名称 | varchar | 100 |  | √ | ' ' | 来源名称 |
| 4 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 5 | fpkid | fpkid | varchar | 36 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_pur_black_person_l_fid |  | fid,flocaleid |
| 2 | t_pur_black_person_l_pkey |  | fpkid |

---

## 企业分录-子表 t_pur_black_person_e

- **表名称：** 企业分录-子表
- **表名：** t_pur_black_person_e

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fbdsupplier_eid | 系统内供应商 | int8 | 64 |  | √ | 0 | 供应商 bd_supplier |
| 3 | fblacklistdeadline_e | 黑名单有效期 | timestamp | 0 |  |  | null | 黑名单有效期 |
| 4 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 5 | fnote | 备注 | varchar | 255 |  | √ | ' ' | 备注 |
| 6 | fisblacklist | 加入黑名单 | bpchar | 1 |  | √ | ' ' | 加入黑名单 |
| 7 | fename | 企业名称 | varchar | 100 |  | √ | ' ' | 企业名称 |
| 8 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 9 | fenumber | 统一社会信用代码 | varchar | 60 |  | √ | ' ' | 统一社会信用代码 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | t_pur_black_person_e_pkey |  | fentryid |
| 2 | idx_pur_black_person_e_fid |  | fid,fseq |

---

## 人员分录-子表 t_pur_black_person_p

- **表名称：** 人员分录-子表
- **表名：** t_pur_black_person_p

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 3 | fpnumber | 身份证号码 | varchar | 20 |  | √ | ' ' | 身份证号码 |
| 4 | fpname | 人员姓名 | varchar | 50 |  | √ | ' ' | 人员姓名 |
| 5 | fnote | 备注 | varchar | 255 |  | √ | ' ' | 备注 |
| 6 | fisblacklist | 加入黑名单 | bpchar | 1 |  | √ | ' ' | 加入黑名单 |
| 7 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_pur_black_person_p_fid |  | fid,fseq |
| 2 | t_pur_black_person_p_pkey |  | fentryid |

# 人员黑名单-srm_blackperson

## 人员黑名单-主表 t_pur_black_person

- **表名称：** 人员黑名单-主表
- **表名：** t_pur_black_person

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | forgid | 采购方 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 3 | fsourceid | 源单ID | int8 | 64 |  | √ | 0 | 源单ID |
| 4 | fisblacklist | 加入黑名单 | bpchar | 1 |  | √ | ' ' | 加入黑名单 |
| 5 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 6 | fauditstatus | 黑名单状态 | bpchar | 1 |  | √ | ' ' | 黑名单状态,枚举: A :拟定 B :提交审批 C :已生效 D :审批驳回 E :已解除 |
| 7 | fstatus | 数据状态 | bpchar | 1 |  | √ | ' ' | 数据状态,枚举: A :保存 B :已提交 C :已审核 |
| 8 | fbiztype | 业务类型 | bpchar | 1 |  | √ | ' ' | 业务类型,枚举: A :人员黑名单 |
| 9 | fmasterid | 主数据内码 | int8 | 64 |  | √ | 0 | 主数据内码 |
| 10 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 11 | freleaseremark | 解除说明 | varchar | 2000 |  | √ | ' ' | 解除说明 |
| 12 | fremark | 事件详述 | varchar | 2000 |  | √ | ' ' | 事件详述 |
| 13 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 14 | fname | 人员姓名 | varchar | 50 |  | √ | ' ' | 人员姓名 |
| 15 | fphone | 手机号 | varchar | 30 |  | √ | ' ' | 手机号 |
| 16 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 17 | femail | 邮箱 | varchar | 100 |  | √ | ' ' | 邮箱 |
| 18 | fsourcename | fsourcename | varchar | 100 |  | √ | ' ' |  |
| 19 | fblacktype | 操作类型 | bpchar | 1 |  | √ | '1' | 操作类型,枚举: 1 :加入黑名单 2 :解除黑名单 |
| 20 | flastupdateuserid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 21 | fdescription | 事件简述 | varchar | 100 |  | √ | ' ' | 事件简述 |
| 22 | fauditdate | 审核时间 | timestamp | 0 |  |  | null | 审核时间 |
| 23 | fauditopinion | 审批意见 | varchar | 255 |  | √ | ' ' | 审批意见 |
| 24 | fsupplierid | 注册供应商 | int8 | 64 |  | √ | 0 | [供应商 srm_supplier](../srm_files/srm_supplier.md) |
| 25 | flastupdatetime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 26 | fsourceblackbillid | 源黑名单id | varchar | 50 |  | √ | ' ' | 源黑名单id |
| 27 | fenable | 使用状态 | bpchar | 1 |  | √ | ' ' | 使用状态,枚举: 0 :禁用 1 :可用 |
| 28 | fnumber | 身份证号码 | varchar | 30 |  | √ | ' ' | 身份证号码 |
| 29 | fauditorid | 审核人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |

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
| 2 | fbdsupplier_eid | 系统内供应商 | int8 | 64 |  | √ | 0 | [供应商 bd_supplier](../basedata_files/bd_supplier.md) |
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
| 2 | fpphone | 手机号 | varchar | 30 |  | √ | ' ' | 手机号 |
| 3 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 4 | fpnumber | 身份证号码 | varchar | 20 |  | √ | ' ' | 身份证号码 |
| 5 | fpname | 人员姓名 | varchar | 50 |  | √ | ' ' | 人员姓名 |
| 6 | fnote | 备注 | varchar | 255 |  | √ | ' ' | 备注 |
| 7 | fisblacklist | 加入黑名单 | bpchar | 1 |  | √ | ' ' | 加入黑名单 |
| 8 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 9 | fpemail | 邮箱 | varchar | 100 |  | √ | ' ' | 邮箱 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_pur_black_person_p_fid |  | fid,fseq |
| 2 | t_pur_black_person_p_pkey |  | fentryid |

---

## 关联子实体-子表 t_pur_black_person_lk

- **表名称：** 关联子实体-子表
- **表名：** t_pur_black_person_lk

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | null |  |
| 2 | fsbillid | 源单内码 | int8 | 64 |  |  | null | 源单内码 |
| 3 | fstableid | 源单主实体编码 | int8 | 64 |  |  | null | 源单主实体编码 |
| 4 | fsid | 源单主实体内码 | int8 | 64 |  |  | null | 源单主实体内码 |
| 5 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 6 | fpkid | fpkid | int8 | 64 |  | √ | null | id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_pur_black_person_lk_fk |  | fid |
| 2 | pk_pur_black_person_lk |  | fpkid |

# 合同主体-conm_contparties

## 合同主体-多语言表 t_conm_contparties_l

- **表名称：** 合同主体-多语言表
- **表名：** t_conm_contparties_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fdepositbank | 开户行 | varchar | 255 |  | √ | ' ' | 开户行 |
| 3 | fname | 名称 | varchar | 255 |  | √ | ' ' | 名称 |
| 4 | ffirmaddress | 住所 | varchar | 255 |  | √ | ' ' | 住所 |
| 5 | ffirmname | 公司名称 | varchar | 255 |  | √ | ' ' | 公司名称 |
| 6 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 7 | fpkid | fpkid | varchar | 36 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_conm_contparties_l_fid |  | fid,flocaleid |
| 2 | t_conm_contparties_l_pkey |  | fpkid |

---

## 合同主体-主表 t_conm_contparties

- **表名称：** 合同主体-主表
- **表名：** t_conm_contparties

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | faddress | 联系地址 | varchar | 512 |  |  | null | 联系地址 |
| 3 | forgid | 业务组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 4 | fcontacts | 联系人 | varchar | 60 |  | √ | ' ' | 联系人 |
| 5 | fbankaccount | 银行账户 | varchar | 255 |  | √ | ' ' | 银行账户 |
| 6 | ffirmphone | 电话 | varchar | 255 |  | √ | ' ' | 电话 |
| 7 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 8 | festablishmentdate | 成立日期 | timestamp | 0 |  |  | null | 成立日期 |
| 9 | fstatus | 数据状态 | varchar | 5 |  | √ | ' ' | 数据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 10 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 11 | fmasterid | 主数据内码 | int8 | 64 |  | √ | 0 | 主数据内码 |
| 12 | frepresentativeorgid | 法人组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 13 | fpostcode | 邮编 | varchar | 100 |  | √ | ' ' | 邮编 |
| 14 | funiformsocialcreditcode | 统一社会信用代码 | varchar | 255 |  | √ | ' ' | 统一社会信用代码 |
| 15 | fname | 名称 | varchar | 255 |  | √ | ' ' | 名称 |
| 16 | fphone | 联系电话 | varchar | 255 |  |  | null | 联系电话 |
| 17 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 18 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 19 | femail | femail | varchar | 100 |  | √ | ' ' |  |
| 20 | fauditdate | 审核时间 | timestamp | 0 |  |  | null | 审核时间 |
| 21 | frepresentative | 法定代表人 | varchar | 255 |  |  | null | 法定代表人 |
| 22 | fenable | 使用状态 | varchar | 5 |  | √ | ' ' | 使用状态,枚举: 0 :禁用 1 :可用 |
| 23 | fnumber | 编码 | varchar | 80 |  | √ | ' ' | 编码 |
| 24 | ftaxregnum | 纳税人识别号 | varchar | 255 |  | √ | ' ' | 纳税人识别号 |
| 25 | fisdefault | 是否默认 | bpchar | 1 |  | √ | '0' | 是否默认 |
| 26 | fauditorid | 审核人 | int8 | 64 |  | √ | 0 | 人员 bos_user |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | t_conm_contparties_pkey |  | fid |
| 2 | idx_conm_contparties_num |  | fnumber |

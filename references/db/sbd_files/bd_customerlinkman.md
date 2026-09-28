# 客户联系人-bd_customerlinkman

## 客户联系人-主表 t_bd_customerlinkman

- **表名称：** 客户联系人-主表
- **表名：** t_bd_customerlinkman

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | 客户内码 | int8 | 64 |  |  | null | 客户内码 |
| 2 | fphone | 固定电话 | varchar | 255 |  | √ | ' ' | 固定电话 |
| 3 | faddress | 地址(已废弃) | varchar | 100 |  |  | null | 地址(已废弃) |
| 4 | fgivenname | fgivenname | varchar | 150 |  | √ | ' ' |  |
| 5 | fgender | 性别(已废弃) | varchar | 50 |  |  | null | 性别(已废弃) |
| 6 | femail | 邮箱 | varchar | 255 |  | √ | ' ' | 邮箱 |
| 7 | fdept | fdept | varchar | 80 |  | √ | ' ' |  |
| 8 | fseq | fseq | int8 | 64 |  |  | null |  |
| 9 | fassociatedaddress | 联系人关联地址f7 | int8 | 64 |  | √ | 0 | [地址 bd_address](../basedata_files/bd_address.md) |
| 10 | faddresspurpose | faddresspurpose | int8 | 64 |  | √ | 0 |  |
| 11 | fmobile | 手机(已废弃) | varchar | 40 |  |  | null | 手机(已废弃) |
| 12 | frole | frole | varchar | 30 |  | √ | ' ' |  |
| 13 | fmiddlename | fmiddlename | varchar | 150 |  | √ | ' ' |  |
| 14 | fpostalcode | 邮政编码(已废弃) | varchar | 10 |  |  | null | 邮政编码(已废弃) |
| 15 | ffamilyname | ffamilyname | varchar | 150 |  | √ | ' ' |  |
| 16 | finvalid | 失效 | bpchar | 1 |  | √ | '0' | 失效 |
| 17 | ffax | 传真 | varchar | 40 |  |  | null | 传真 |
| 18 | fcontactperson | fcontactperson | varchar | 255 |  | √ | ' ' |  |
| 19 | fentryid | fentryid | int8 | 64 |  | √ | null | id |
| 20 | falias | falias | varchar | 150 |  | √ | ' ' |  |
| 21 | fisdefault | 默认 | bpchar | 1 |  |  | null | 默认 |
| 22 | fcontactpersonpost | fcontactpersonpost | varchar | 60 |  | √ | ' ' |  |
| 23 | fcellphone | 移动电话 | varchar | 50 |  | √ | ' ' | 移动电话 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | t_bd_customerlinkman_pkey |  | fentryid |
| 2 | idx_bd_custlinkman_cust |  | fid |

---

## 客户联系人-多语言表 t_bd_customerlinkman_l

- **表名称：** 客户联系人-多语言表
- **表名：** t_bd_customerlinkman_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fdept | 部门 | varchar | 80 |  |  | null | 部门 |
| 2 | fcontactperson | 名称 | varchar | 255 |  | √ | ' ' | 名称 |
| 3 | flocaleid | flocaleid | varchar | 10 |  |  | null | localeid |
| 4 | fpkid | fpkid | varchar | 36 |  | √ | null | pkid |
| 5 | fentryid | fentryid | int8 | 64 |  |  | null |  |
| 6 | fcontactpersonpost | 职务 | varchar | 60 |  |  | null | 职务 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | t_bd_customerlinkman_l_pkey |  | fpkid |
| 2 | idx_bd_custlinkman_l_entry |  | fentryid,flocaleid |
